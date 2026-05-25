from typing import List

from sqlalchemy import Column, DECIMAL, ForeignKeyConstraint, Index, Integer, String
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.orm import Mapped, DeclarativeBase, mapped_column, relationship
from sqlalchemy.orm.base import Mapped

class Base(DeclarativeBase):
    pass


class DimEmployeeRevenue(Base):
    __tablename__ = 'dim_employee_revenue'

    employee_number = mapped_column(INTEGER, primary_key=True)
    employee_name = mapped_column(String(100), nullable=False)
    office_city = mapped_column(String(50), nullable=False)

    fact_employee_revenue: Mapped[List['FactEmployeeRevenue']] = relationship('FactEmployeeRevenue', uselist=True, back_populates='dim_employee_revenue')


class DimOfficeSales(Base):
    __tablename__ = 'dim_office_sales'

    office_code = mapped_column(String(10), primary_key=True)
    office_city = mapped_column(String(50), nullable=False)
    sales_rep_employee_number = mapped_column(INTEGER, nullable=False)

    fact_office_sales: Mapped[List['FactOfficeSales']] = relationship('FactOfficeSales', uselist=True, back_populates='dim_office_sales')


class DimProductLineRevenue(Base):
    __tablename__ = 'dim_product_line_revenue'

    product_line = mapped_column(String(50), primary_key=True)
    product_line_description = mapped_column(String(4000), nullable=False)

    fact_product_line_revenue: Mapped[List['FactProductLineRevenue']] = relationship('FactProductLineRevenue', uselist=True, back_populates='dim_product_line_revenue')


class DimProductSales(Base):
    __tablename__ = 'dim_product_sales'

    product_code = mapped_column(String(15), primary_key=True)
    product_name = mapped_column(String(70), nullable=False)

    fact_product_sales: Mapped[List['FactProductSales']] = relationship('FactProductSales', uselist=True, back_populates='dim_product_sales')


class DimSales(Base):
    __tablename__ = 'dim_sales'

    location_id = mapped_column(Integer, primary_key=True)
    customer_city = mapped_column(String(50), nullable=False)

    fact_sales: Mapped[List['FactSales']] = relationship('FactSales', uselist=True, back_populates='location')


class FactEmployeeRevenue(Base):
    __tablename__ = 'fact_employee_revenue'
    __table_args__ = (
        ForeignKeyConstraint(['employee_number'], ['dim_employee_revenue.employee_number'], name='fk_fact_employee_number'),
        Index('fk_fact_employee_number', 'employee_number')
    )

    employee_revenue_id = mapped_column(Integer, primary_key=True)
    employee_number = mapped_column(INTEGER, nullable=False)
    office_code = mapped_column(String(10), nullable=False)
    total_revenue = mapped_column(DECIMAL(10, 2), nullable=False)
    total_orders = mapped_column(Integer, nullable=False)

    dim_employee_revenue: Mapped['DimEmployeeRevenue'] = relationship('DimEmployeeRevenue', back_populates='fact_employee_revenue')


class FactOfficeSales(Base):
    __tablename__ = 'fact_office_sales'
    __table_args__ = (
        ForeignKeyConstraint(['office_code'], ['dim_office_sales.office_code'], name='fk_fact_office_code'),
        Index('fk_fact_office_code', 'office_code')
    )

    office_sales_id = mapped_column(Integer, primary_key=True)
    office_code = mapped_column(String(10), nullable=False)
    sales_rep_employee_number = mapped_column(INTEGER, nullable=False)
    total_revenue = mapped_column(DECIMAL(10, 2), nullable=False)
    total_orders = mapped_column(Integer, nullable=False)

    dim_office_sales: Mapped['DimOfficeSales'] = relationship('DimOfficeSales', back_populates='fact_office_sales')


class FactProductLineRevenue(Base):
    __tablename__ = 'fact_product_line_revenue'
    __table_args__ = (
        ForeignKeyConstraint(['product_line'], ['dim_product_line_revenue.product_line'], name='fk_fact_product_line'),
        Index('fk_fact_product_line', 'product_line')
    )

    product_line_revenue_id = mapped_column(Integer, primary_key=True)
    product_line = mapped_column(String(50), nullable=False)
    total_revenue = mapped_column(DECIMAL(10, 2), nullable=False)
    total_orders = mapped_column(Integer, nullable=False)

    dim_product_line_revenue: Mapped['DimProductLineRevenue'] = relationship('DimProductLineRevenue', back_populates='fact_product_line_revenue')


class FactProductSales(Base):
    __tablename__ = 'fact_product_sales'
    __table_args__ = (
        ForeignKeyConstraint(['product_code'], ['dim_product_sales.product_code'], name='fk_fact_product_code'),
        Index('fk_fact_product_code', 'product_code')
    )

    product_sales_id = mapped_column(Integer, primary_key=True)
    product_code = mapped_column(String(15), nullable=False)
    total_revenue = mapped_column(DECIMAL(10, 2), nullable=False)
    total_orders = mapped_column(Integer, nullable=False)

    dim_product_sales: Mapped['DimProductSales'] = relationship('DimProductSales', back_populates='fact_product_sales')


class FactSales(Base):
    __tablename__ = 'fact_sales'
    __table_args__ = (
        ForeignKeyConstraint(['location_id'], ['dim_sales.location_id'], name='fk_fact_sales_location'),
        Index('fk_fact_sales_location', 'location_id')
    )

    sales_id = mapped_column(Integer, primary_key=True)
    location_id = mapped_column(Integer, nullable=False)
    total_revenue = mapped_column(DECIMAL(10, 2), nullable=False)
    total_orders = mapped_column(Integer, nullable=False)

    location: Mapped['DimSales'] = relationship('DimSales', back_populates='fact_sales')
