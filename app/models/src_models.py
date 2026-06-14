from typing import List, Optional
from sqlalchemy import String, Integer, DECIMAL, Date, ForeignKey, Text, SmallInteger
from sqlalchemy.orm import Mapped, mapped_column, relationship, DeclarativeBase
from sqlalchemy.dialects.mysql import MEDIUMTEXT, MEDIUMBLOB

class Base(DeclarativeBase):
    pass


class Office(Base):
    __tablename__ = "offices"
    
    officeCode: Mapped[str] = mapped_column(String(10), primary_key=True)
    city: Mapped[str] = mapped_column(String(50), nullable=False)
    phone: Mapped[str] = mapped_column(String(50), nullable=False)
    addressLine1: Mapped[str] = mapped_column(String(50), nullable=False)
    addressLine2: Mapped[Optional[str]] = mapped_column(String(50))
    state: Mapped[Optional[str]] = mapped_column(String(50))
    country: Mapped[str] = mapped_column(String(50), nullable=False)
    postalCode: Mapped[str] = mapped_column(String(15), nullable=False)
    territory: Mapped[str] = mapped_column(String(10), nullable=False)

    employees: Mapped[List["Employee"]] = relationship("Employee", back_populates="office")



class Employee(Base):
    __tablename__ = "employees"
    
    employeeNumber: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=False)
    lastName: Mapped[str] = mapped_column(String(50), nullable=False)
    firstName: Mapped[str] = mapped_column(String(50), nullable=False)
    extension: Mapped[str] = mapped_column(String(10), nullable=False)
    email: Mapped[str] = mapped_column(String(100), nullable=False)
    officeCode: Mapped[str] = mapped_column(String(10), ForeignKey("offices.officeCode"), nullable=False)
    reportsTo: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("employees.employeeNumber"))
    jobTitle: Mapped[str] = mapped_column(String(50), nullable=False)

    office: Mapped["Office"] = relationship("Office", back_populates="employees")
    manager: Mapped[Optional["Employee"]] = relationship("Employee", remote_side=[employeeNumber], back_populates="subordinates")
    subordinates: Mapped[List["Employee"]] = relationship("Employee", back_populates="manager")
    customers: Mapped[List["Customer"]] = relationship("Customer", back_populates="sales_rep")



class Customer(Base):
    __tablename__ = "customers"
    
    customerNumber: Mapped[str] = mapped_column(String(15), primary_key=True)
    customerName: Mapped[str] = mapped_column(String(50), nullable=False)
    contactLastName: Mapped[Optional[str]] = mapped_column(String(50))
    contactFirstName: Mapped[Optional[str]] = mapped_column(String(50))
    phone: Mapped[Optional[str]] = mapped_column(String(50))
    addressLine1: Mapped[Optional[str]] = mapped_column(String(50))
    addressLine2: Mapped[Optional[str]] = mapped_column(String(50))
    city: Mapped[Optional[str]] = mapped_column(String(50))
    state: Mapped[Optional[str]] = mapped_column(String(50))
    postalCode: Mapped[Optional[str]] = mapped_column(String(15))
    country: Mapped[Optional[str]] = mapped_column(String(50))
    salesRepEmployeeNumber: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("employees.employeeNumber"))
    creditLimit: Mapped[Optional[float]] = mapped_column(DECIMAL(10, 2))

    sales_rep: Mapped[Optional["Employee"]] = relationship("Employee", back_populates="customers")
    orders: Mapped[List["Order"]] = relationship("Order", back_populates="customer")
    payments: Mapped[List["Payment"]] = relationship("Payment", back_populates="customer")



class ProductLine(Base):
    __tablename__ = "productlines"
    
    productLine: Mapped[str] = mapped_column(String(50), primary_key=True)
    textDescription: Mapped[Optional[str]] = mapped_column(String(4000))
    htmlDescription: Mapped[Optional[str]] = mapped_column(MEDIUMTEXT)
    image: Mapped[Optional[bytes]] = mapped_column(MEDIUMBLOB)

    products: Mapped[List["Product"]] = relationship("Product", back_populates="line_details")



class Product(Base):
    __tablename__ = "products"
    
    productCode: Mapped[str] = mapped_column(String(15), primary_key=True)
    productName: Mapped[str] = mapped_column(String(70), nullable=False)
    productLine: Mapped[str] = mapped_column(String(50), ForeignKey("productlines.productLine"), nullable=False)
    productScale: Mapped[Optional[str]] = mapped_column(String(10))
    productVendor: Mapped[Optional[str]] = mapped_column(String(50))
    productDescription: Mapped[Optional[str]] = mapped_column(Text)
    quantityInStock: Mapped[Optional[int]] = mapped_column(Integer)
    buyPrice: Mapped[Optional[float]] = mapped_column(DECIMAL(10, 2))
    MSRP: Mapped[Optional[float]] = mapped_column(DECIMAL(10, 2))

    line_details: Mapped["ProductLine"] = relationship("ProductLine", back_populates="products")
    order_details: Mapped[List["OrderDetail"]] = relationship("OrderDetail", back_populates="product")



class Order(Base):
    __tablename__ = "orders"
    
    orderNumber: Mapped[str] = mapped_column(String(15), primary_key=True)
    orderDate: Mapped[Optional[Date]] = mapped_column(Date)
    requiredDate: Mapped[Optional[Date]] = mapped_column(Date)
    shippedDate: Mapped[Optional[Date]] = mapped_column(Date)
    status: Mapped[Optional[str]] = mapped_column(String(15))
    comments: Mapped[Optional[str]] = mapped_column(Text)
    customerNumber: Mapped[str] = mapped_column(String(15), ForeignKey("customers.customerNumber"), nullable=False)
    total_Price: Mapped[Optional[float]] = mapped_column(DECIMAL(10, 2))

    customer: Mapped["Customer"] = relationship("Customer", back_populates="orders")
    details: Mapped[List["OrderDetail"]] = relationship("OrderDetail", back_populates="order")



class OrderDetail(Base):
    __tablename__ = "orderdetails"
    
    orderNumber: Mapped[str] = mapped_column(String(15), ForeignKey("orders.orderNumber"), primary_key=True)
    productCode: Mapped[str] = mapped_column(String(15), ForeignKey("products.productCode"), primary_key=True)
    quantityOrdered: Mapped[int] = mapped_column(Integer, nullable=False)
    priceEach: Mapped[float] = mapped_column(DECIMAL(10, 2), nullable=False)
    orderLineNumber: Mapped[int] = mapped_column(SmallInteger, nullable=False)

    order: Mapped["Order"] = relationship("Order", back_populates="details")
    product: Mapped["Product"] = relationship("Product", back_populates="order_details")



class Payment(Base):
    __tablename__ = "payments"
    
    customerNumber: Mapped[str] = mapped_column(String(15), ForeignKey("customers.customerNumber"), primary_key=True)
    checkNumber: Mapped[str] = mapped_column(String(50), primary_key=True)
    paymentDate: Mapped[Date] = mapped_column(Date, nullable=False)
    amount: Mapped[float] = mapped_column(DECIMAL(10, 2), nullable=False)

    customer: Mapped["Customer"] = relationship("Customer", back_populates="payments")
