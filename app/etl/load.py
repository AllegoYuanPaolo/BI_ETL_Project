from typing import Dict, Iterable, List, Optional

from sqlalchemy import text

from etl import ext_trans as src
from models import dest_models as dst
from utils.dbOps import get_db_connection
from utils.logger import get_logger

log = get_logger(__name__)


def _clear_tables(conn):
    log.info("Clearing all destination tables...")
    conn.execute(text("SET FOREIGN_KEY_CHECKS = 0;"))
    tables = [
        'fact_sales', 'dim_product', 'dim_product_line',
        'dim_sales_rep', 'dim_office', 'dim_city',
    ]
    for table in tables:
        conn.execute(text(f"DELETE FROM {table}"))
    conn.execute(text("SET FOREIGN_KEY_CHECKS = 1;"))
    log.info("All tables cleared.")


def _unique(values: Iterable[str]) -> List[str]:
    seen: set[str] = set()
    result: list[str] = []
    for v in values:
        if v not in seen:
            seen.add(v)
            result.append(v)
    return result


def _load_dim_city(conn, data: List[dict]) -> Dict[str, int]:
    cities = _unique(row['city_name'] for row in data if row['city_name'])
    lookup: Dict[str, int] = {}
    for name in cities:
        row = dst.DimCity(city_name=name)
        conn.add(row)
        conn.flush()
        lookup[name] = row.city_id
    log.info(f"Loaded {len(cities)} cities.")
    return lookup


def _load_dim_office(conn, data: List[dict]) -> Dict[str, int]:
    offices = _unique(row['office_city'] for row in data if row['office_city'])
    lookup: Dict[str, int] = {}
    for city in offices:
        row = dst.DimOffice(office_city=city)
        conn.add(row)
        conn.flush()
        lookup[city] = row.office_id
    log.info(f"Loaded {len(offices)} offices.")
    return lookup


def _load_dim_sales_rep(conn, data: List[dict]) -> Dict[str, int]:
    reps = _unique(row['sales_rep_name'] for row in data if row['sales_rep_name'])
    lookup: Dict[str, int] = {}
    for name in reps:
        row = dst.DimSalesRep(sales_rep_name=name)
        conn.add(row)
        conn.flush()
        lookup[name] = row.sales_rep_id
    log.info(f"Loaded {len(reps)} sales reps.")
    return lookup


def _load_dim_product_line(conn, data: List[dict]) -> Dict[str, int]:
    lines = _unique(row['product_line'] for row in data if row['product_line'])
    lookup: Dict[str, int] = {}
    for name in lines:
        row = dst.DimProductLine(product_line=name)
        conn.add(row)
        conn.flush()
        lookup[name] = row.product_line_id
    log.info(f"Loaded {len(lines)} product lines.")
    return lookup


def _load_dim_product(conn, data: List[dict], pl_lookup: Dict[str, int]) -> Dict[str, int]:
    products = _unique(row['product_name'] for row in data if row['product_name'])
    product_to_pl = {r['product_name']: r['product_line'] for r in data}
    lookup: Dict[str, int] = {}
    for name in products:
        pl_name = product_to_pl.get(name)
        pl_id = pl_lookup.get(pl_name) if pl_name else None
        if pl_id is None:
            log.warning(f"Product '{name}' has no matching product_line, skipping.")
            continue
        row = dst.DimProduct(product_name=name, product_line_id=pl_id)
        conn.add(row)
        conn.flush()
        lookup[name] = row.product_id
    log.info(f"Loaded {len(lookup)} products.")
    return lookup


def _load_fact_sales(
    conn,
    data: List[dict],
    city_lookup: Dict[str, int],
    office_lookup: Dict[str, int],
    rep_lookup: Dict[str, int],
    product_lookup: Dict[str, int],
    pl_lookup: Dict[str, int],
):
    count = 0
    for row in data:
        city_id = city_lookup.get(row['city_name'])
        office_id = office_lookup.get(row['office_city'])
        rep_id = rep_lookup.get(row['sales_rep_name'])
        prod_id = product_lookup.get(row['product_name'])
        pl_id = pl_lookup.get(row['product_line'])

        missing = []
        if city_id is None: missing.append('city')
        if office_id is None: missing.append('office')
        if rep_id is None: missing.append('sales_rep')
        if prod_id is None: missing.append('product')
        if pl_id is None: missing.append('product_line')
        if missing:
            log.warning(f"Skipping order {row['order_id']}: missing lookups for {', '.join(missing)}")
            continue

        fact = dst.FactSales(
            order_id=row['order_id'],
            order_date=row['order_date'],
            city_id=city_id,
            office_id=office_id,
            sales_rep_id=rep_id,
            product_id=prod_id,
            product_line_id=pl_id,
            revenue=row['revenue'],
            quantity=row['quantity'],
        )
        conn.add(fact)
        count += 1

    conn.flush()
    log.info(f"Loaded {count} fact rows.")


def load_data():
    conn = get_db_connection('orderStatistics')
    try:
        data = src.get_sales_data()
        if not data:
            log.warning("No data extracted, nothing to load.")
            return

        _clear_tables(conn)

        city_lookup = _load_dim_city(conn, data)
        office_lookup = _load_dim_office(conn, data)
        rep_lookup = _load_dim_sales_rep(conn, data)
        pl_lookup = _load_dim_product_line(conn, data)
        product_lookup = _load_dim_product(conn, data, pl_lookup)

        _load_fact_sales(conn, data, city_lookup, office_lookup, rep_lookup, product_lookup, pl_lookup)

        conn.commit()
        log.info("Data load complete.")
    except Exception as e:
        conn.rollback()
        log.error(f"Load failed: {e}")
        raise
    finally:
        conn.close()


if __name__ == "__main__":
    load_data()
