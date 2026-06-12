from datetime import date
from typing import Optional

from sqlalchemy import extract, func, select, desc

from models import dest_models as dst
from schemas import APIContracts as contract
from utils import dbOps


_stats = dbOps.get_session_factory('orderStatistics')


def _exec(stmt):
    session = _stats()
    try:
        return session.execute(stmt).all()
    finally:
        session.close()


# ── filter helper ────────────────────────────────────────────────────────────

def _apply_date_filters(stmt, model, *,
                        start_date: Optional[date] = None,
                        end_date: Optional[date] = None,
                        year: Optional[int] = None,
                        quarter: Optional[int] = None,
                        half: Optional[int] = None):
    if start_date:
        stmt = stmt.where(model.order_date >= start_date)
    if end_date:
        stmt = stmt.where(model.order_date <= end_date)
    if year is not None:
        stmt = stmt.where(extract('year', model.order_date) == year)
    if quarter is not None:
        stmt = stmt.where(extract('quarter', model.order_date) == quarter)
    if half is not None:
        stmt = stmt.where(extract('month', model.order_date).between((half - 1) * 6 + 1, half * 6))
    return stmt


# ── query functions ──────────────────────────────────────────────────────────

def city_revenue(start_date: Optional[date] = None,
                 end_date: Optional[date] = None,
                 year: Optional[int] = None,
                 quarter: Optional[int] = None,
                 half: Optional[int] = None,
                 city: Optional[str] = None) -> list[contract.CityRevenue]:
    stmt = (
        select(
            dst.DimCity.city_name,
            func.sum(dst.FactSales.revenue).label("total_revenue"),
            func.count(dst.FactSales.order_id).label("total_orders"),
        )
        .join(dst.FactSales, dst.DimCity.city_id == dst.FactSales.city_id)
    )
    stmt = _apply_date_filters(stmt, dst.FactSales,
                                start_date=start_date, end_date=end_date,
                                year=year, quarter=quarter, half=half)
    if city:
        stmt = stmt.where(dst.DimCity.city_name == city)
    stmt = stmt.group_by(dst.DimCity.city_name).order_by(desc("total_revenue"))

    return [
        contract.CityRevenue(city=r.city_name, total_revenue=float(r.total_revenue), total_orders=int(r.total_orders))
        for r in _exec(stmt)
    ]


def product_revenue(start_date: Optional[date] = None,
                    end_date: Optional[date] = None,
                    year: Optional[int] = None,
                    quarter: Optional[int] = None,
                    half: Optional[int] = None) -> list[contract.ProductRevenue]:
    stmt = (
        select(
            dst.DimProduct.product_name,
            func.sum(dst.FactSales.revenue).label("total_revenue"),
            func.count(dst.FactSales.order_id).label("total_orders"),
        )
        .join(dst.FactSales, dst.DimProduct.product_id == dst.FactSales.product_id)
    )
    stmt = _apply_date_filters(stmt, dst.FactSales,
                                start_date=start_date, end_date=end_date,
                                year=year, quarter=quarter, half=half)
    stmt = stmt.group_by(dst.DimProduct.product_name).order_by(desc("total_revenue"))

    return [
        contract.ProductRevenue(product=r.product_name, total_revenue=float(r.total_revenue), total_orders=int(r.total_orders))
        for r in _exec(stmt)
    ]


def office_revenue(start_date: Optional[date] = None,
                   end_date: Optional[date] = None,
                   year: Optional[int] = None,
                   quarter: Optional[int] = None,
                   half: Optional[int] = None,
                   city: Optional[str] = None,
                   office_city: Optional[str] = None) -> list[contract.OfficeRevenue]:
    stmt = (
        select(
            dst.DimOffice.office_city,
            func.sum(dst.FactSales.revenue).label("total_revenue"),
            func.count(dst.FactSales.order_id).label("total_orders"),
        )
        .join(dst.FactSales, dst.DimOffice.office_id == dst.FactSales.office_id)
    )
    stmt = _apply_date_filters(stmt, dst.FactSales,
                                start_date=start_date, end_date=end_date,
                                year=year, quarter=quarter, half=half)
    if city:
        stmt = stmt.where(dst.DimOffice.office_city == city)
    if office_city:
        stmt = stmt.where(dst.DimOffice.office_city == office_city)
    stmt = stmt.group_by(dst.DimOffice.office_city).order_by(desc("total_revenue"))

    return [
        contract.OfficeRevenue(office_city=r.office_city, total_revenue=float(r.total_revenue), total_orders=int(r.total_orders))
        for r in _exec(stmt)
    ]


def employee_revenue(start_date: Optional[date] = None,
                     end_date: Optional[date] = None,
                     year: Optional[int] = None,
                     quarter: Optional[int] = None,
                     half: Optional[int] = None,
                     city: Optional[str] = None,
                     office_city: Optional[str] = None) -> list[contract.EmployeeRevenue]:
    stmt = (
        select(
            dst.DimSalesRep.sales_rep_id,
            dst.DimSalesRep.sales_rep_name,
            func.sum(dst.FactSales.revenue).label("total_revenue"),
            func.count(dst.FactSales.order_id).label("total_orders"),
            dst.DimOffice.office_city,
        )
        .join(dst.FactSales, dst.DimSalesRep.sales_rep_id == dst.FactSales.sales_rep_id)
        .join(dst.DimOffice, dst.DimOffice.office_id == dst.FactSales.office_id)
    )
    stmt = _apply_date_filters(stmt, dst.FactSales,
                                start_date=start_date, end_date=end_date,
                                year=year, quarter=quarter, half=half)
    if city:
        stmt = stmt.where(dst.DimOffice.office_city == city)
    if office_city:
        stmt = stmt.where(dst.DimOffice.office_city == office_city)
    stmt = stmt.group_by(dst.DimSalesRep.sales_rep_id).order_by(desc("total_revenue"))

    return [
        contract.EmployeeRevenue(
            employee_number=int(r.sales_rep_id),
            employee_name=r.sales_rep_name,
            total_revenue=float(r.total_revenue),
            total_orders=int(r.total_orders),
            office_city=r.office_city,
        )
        for r in _exec(stmt)
    ]


def productline_revenue(start_date: Optional[date] = None,
                        end_date: Optional[date] = None,
                        year: Optional[int] = None,
                        quarter: Optional[int] = None,
                        half: Optional[int] = None) -> list[contract.ProductLineRevenue]:
    stmt = (
        select(
            dst.DimProductLine.product_line,
            dst.DimProductLine.product_line,
            func.sum(dst.FactSales.revenue).label("total_revenue"),
            func.count(dst.FactSales.order_id).label("total_orders"),
        )
        .join(dst.FactSales, dst.DimProductLine.product_line_id == dst.FactSales.product_line_id)
    )
    stmt = _apply_date_filters(stmt, dst.FactSales,
                                start_date=start_date, end_date=end_date,
                                year=year, quarter=quarter, half=half)
    stmt = stmt.group_by(dst.DimProductLine.product_line).order_by(desc("total_revenue"))

    return [
        contract.ProductLineRevenue(
            product_line=r.product_line,
            description="",
            total_revenue=float(r.total_revenue),
            total_orders=int(r.total_orders),
        )
        for r in _exec(stmt)
    ]


if __name__ == "__main__":
    for c in city_revenue():
        print(c.model_dump())
