from datetime import date
from decimal import Decimal
from typing import List, Optional

from sqlalchemy import DECIMAL, Date, ForeignKey, ForeignKeyConstraint, Index, Integer, String
from sqlalchemy.orm import Mapped, DeclarativeBase, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class DimCity(Base):
    __tablename__ = 'dim_city'

    city_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    city_name: Mapped[Optional[str]] = mapped_column(String(45))

    fact_sales: Mapped[List['FactSales']] = relationship('FactSales', back_populates='city')


class DimOffice(Base):
    __tablename__ = 'dim_office'

    office_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    office_city: Mapped[Optional[str]] = mapped_column(String(45))

    fact_sales: Mapped[List['FactSales']] = relationship('FactSales', back_populates='office')


class DimProductLine(Base):
    __tablename__ = 'dim_product_line'

    product_line_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    product_line: Mapped[Optional[str]] = mapped_column(String(45))

    dim_product: Mapped[List['DimProduct']] = relationship('DimProduct', uselist=True, back_populates='product_line')
    fact_sales: Mapped[List['FactSales']] = relationship('FactSales', back_populates='product_line')


class DimSalesRep(Base):
    __tablename__ = 'dim_sales_rep'

    sales_rep_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    sales_rep_name: Mapped[Optional[str]] = mapped_column(String(45))

    fact_sales: Mapped[List['FactSales']] = relationship('FactSales', back_populates='sales_rep')


class DimProduct(Base):
    __tablename__ = 'dim_product'
    __table_args__ = (
        ForeignKeyConstraint(['product_line_id'], ['dim_product_line.product_line_id'], ondelete='RESTRICT', onupdate='RESTRICT', name='fk_product_line'),
        Index('fk_product_line_idx', 'product_line_id'),
    )

    product_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    product_name: Mapped[Optional[str]] = mapped_column(String(45))
    product_line_id: Mapped[int] = mapped_column(Integer)

    product_line: Mapped[Optional['DimProductLine']] = relationship('DimProductLine', back_populates='dim_product')
    fact_sales: Mapped[List['FactSales']] = relationship('FactSales', back_populates='product')


class FactSales(Base):
    __tablename__ = 'fact_sales'
    __table_args__ = (
        Index('to_office_idx', 'office_id'),
        Index('to_city_idx', 'city_id'),
        Index('to_sales_rep_idx', 'sales_rep_id'),
        Index('to_produc_idx', 'product_id', 'product_line_id'),
        Index('to_product_line_idx', 'product_line_id'),
    )

    order_id: Mapped[str] = mapped_column(String(15), primary_key=True)
    order_date: Mapped[date] = mapped_column(Date, nullable=False)
    city_id: Mapped[int] = mapped_column(Integer, ForeignKey('dim_city.city_id'), nullable=False)
    office_id: Mapped[int] = mapped_column(Integer, ForeignKey('dim_office.office_id'), nullable=False)
    sales_rep_id: Mapped[int] = mapped_column(Integer, ForeignKey('dim_sales_rep.sales_rep_id'), nullable=False)
    product_id: Mapped[int] = mapped_column(Integer, ForeignKey('dim_product.product_id'), primary_key=True)
    product_line_id: Mapped[int] = mapped_column(Integer, ForeignKey('dim_product_line.product_line_id'), nullable=False)
    revenue: Mapped[Decimal] = mapped_column(DECIMAL(10, 2), nullable=False)
    quantity: Mapped[int] = mapped_column(Integer, nullable=False)

    city: Mapped['DimCity'] = relationship('DimCity', back_populates='fact_sales')
    office: Mapped['DimOffice'] = relationship('DimOffice', back_populates='fact_sales')
    sales_rep: Mapped['DimSalesRep'] = relationship('DimSalesRep', back_populates='fact_sales')
    product: Mapped['DimProduct'] = relationship('DimProduct', back_populates='fact_sales')
    product_line: Mapped['DimProductLine'] = relationship('DimProductLine', back_populates='fact_sales')
