from typing import List, Optional

from sqlalchemy import Column, DECIMAL, Date, ForeignKeyConstraint, Index, SmallInteger, String, Text
from sqlalchemy.dialects.mysql import INTEGER, MEDIUMBLOB, MEDIUMTEXT
from sqlalchemy.orm import Mapped, declarative_base, mapped_column, relationship
from sqlalchemy.orm.base import Mapped

Base = declarative_base()


class Offices(Base):
    __tablename__ = 'offices'

    officeCode = mapped_column(String(10), primary_key=True)
    city = mapped_column(String(50), nullable=False)
    phone = mapped_column(String(50), nullable=False)
    addressLine1 = mapped_column(String(50), nullable=False)
    country = mapped_column(String(50), nullable=False)
    postalCode = mapped_column(String(15), nullable=False)
    territory = mapped_column(String(10), nullable=False)
    addressLine2 = mapped_column(String(50))
    state = mapped_column(String(50))

    employees: Mapped[List['Employees']] = relationship('Employees', uselist=True, back_populates='offices')


class Productlines(Base):
    __tablename__ = 'productlines'

    productLine = mapped_column(String(50), primary_key=True)
    textDescription = mapped_column(String(4000))
    htmlDescription = mapped_column(MEDIUMTEXT)
    image = mapped_column(MEDIUMBLOB)

    products: Mapped[List['Products']] = relationship('Products', uselist=True, back_populates='productlines')


class Employees(Base):
    __tablename__ = 'employees'
    __table_args__ = (
        ForeignKeyConstraint(['officeCode'], ['offices.officeCode'], name='employees_ibfk_2'),
        ForeignKeyConstraint(['reportsTo'], ['employees.employeeNumber'], name='employees_ibfk_1'),
        Index('officeCode', 'officeCode'),
        Index('reportsTo', 'reportsTo')
    )

    employeeNumber = mapped_column(INTEGER, primary_key=True)
    lastName = mapped_column(String(50), nullable=False)
    firstName = mapped_column(String(50), nullable=False)
    extension = mapped_column(String(10), nullable=False)
    email = mapped_column(String(100), nullable=False)
    officeCode = mapped_column(String(10), nullable=False)
    jobTitle = mapped_column(String(50), nullable=False)
    reportsTo = mapped_column(INTEGER)

    offices: Mapped['Offices'] = relationship('Offices', back_populates='employees')
    employees: Mapped[Optional['Employees']] = relationship('Employees', remote_side=[employeeNumber], back_populates='employees_reverse')
    employees_reverse: Mapped[List['Employees']] = relationship('Employees', uselist=True, remote_side=[reportsTo], back_populates='employees')
    customers: Mapped[List['Customers']] = relationship('Customers', uselist=True, back_populates='employees')


class Products(Base):
    __tablename__ = 'products'
    __table_args__ = (
        ForeignKeyConstraint(['productLine'], ['productlines.productLine'], name='products_ibfk_1'),
        Index('productLine', 'productLine')
    )

    productCode = mapped_column(String(15), primary_key=True)
    productName = mapped_column(String(70), nullable=False)
    productLine = mapped_column(String(50), nullable=False)
    productScale = mapped_column(String(10))
    productVendor = mapped_column(String(50))
    productDescription = mapped_column(Text)
    quantityInStock = mapped_column(INTEGER)
    buyPrice = mapped_column(DECIMAL(10, 2))
    MSRP = mapped_column(DECIMAL(10, 2))

    productlines: Mapped['Productlines'] = relationship('Productlines', back_populates='products')
    orderdetails: Mapped[List['Orderdetails']] = relationship('Orderdetails', uselist=True, back_populates='products')


class Customers(Base):
    __tablename__ = 'customers'
    __table_args__ = (
        ForeignKeyConstraint(['salesRepEmployeeNumber'], ['employees.employeeNumber'], name='fk_employee'),
        Index('fk_employee', 'salesRepEmployeeNumber')
    )

    customerNumber = mapped_column(String(15), primary_key=True)
    customerName = mapped_column(String(50), nullable=False)
    contactLastName = mapped_column(String(50))
    contactFirstName = mapped_column(String(50))
    phone = mapped_column(String(50))
    addressLine1 = mapped_column(String(50))
    addressLine2 = mapped_column(String(50))
    city = mapped_column(String(50))
    state = mapped_column(String(50))
    postalCode = mapped_column(String(15))
    country = mapped_column(String(50))
    salesRepEmployeeNumber = mapped_column(INTEGER)
    creditLimit = mapped_column(DECIMAL(10, 2))

    employees: Mapped[Optional['Employees']] = relationship('Employees', back_populates='customers')
    orders: Mapped[List['Orders']] = relationship('Orders', uselist=True, back_populates='customers')
    payments: Mapped[List['Payments']] = relationship('Payments', uselist=True, back_populates='customers')


class Orders(Base):
    __tablename__ = 'orders'
    __table_args__ = (
        ForeignKeyConstraint(['customerNumber'], ['customers.customerNumber'], name='orders_ibfk_1'),
        Index('customerNumber', 'customerNumber')
    )

    orderNumber = mapped_column(String(15), primary_key=True)
    customerNumber = mapped_column(String(15), nullable=False)
    orderDate = mapped_column(Date)
    requiredDate = mapped_column(Date)
    shippedDate = mapped_column(Date)
    status = mapped_column(String(15))
    comments = mapped_column(Text)
    total_Price = mapped_column(DECIMAL(10, 2))

    customers: Mapped['Customers'] = relationship('Customers', back_populates='orders')
    orderdetails: Mapped[List['Orderdetails']] = relationship('Orderdetails', uselist=True, back_populates='orders')


class Payments(Base):
    __tablename__ = 'payments'
    __table_args__ = (
        ForeignKeyConstraint(['customerNumber'], ['customers.customerNumber'], name='payments_ibfk_1'),
    )

    customerNumber = mapped_column(String(15), primary_key=True, nullable=False)
    checkNumber = mapped_column(String(50), primary_key=True, nullable=False)
    paymentDate = mapped_column(Date, nullable=False)
    amount = mapped_column(DECIMAL(10, 2), nullable=False)

    customers: Mapped['Customers'] = relationship('Customers', back_populates='payments')


class Orderdetails(Base):
    __tablename__ = 'orderdetails'
    __table_args__ = (
        ForeignKeyConstraint(['orderNumber'], ['orders.orderNumber'], name='orderdetails_ibfk_1'),
        ForeignKeyConstraint(['productCode'], ['products.productCode'], name='orderdetails_ibfk_2'),
        Index('productCode', 'productCode')
    )

    orderNumber = mapped_column(String(15), primary_key=True, nullable=False)
    productCode = mapped_column(String(15), primary_key=True, nullable=False)
    quantityOrdered = mapped_column(INTEGER, nullable=False)
    priceEach = mapped_column(DECIMAL(10, 2), nullable=False)
    orderLineNumber = mapped_column(SmallInteger, nullable=False)

    orders: Mapped['Orders'] = relationship('Orders', back_populates='orderdetails')
    products: Mapped['Products'] = relationship('Products', back_populates='orderdetails')
