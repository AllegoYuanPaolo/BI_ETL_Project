'''
API Contracts for validation and type handling
'''

from pydantic import BaseModel, computed_field, Field

def desc(description: str):
    return Field(description=description)

class CityRevenue(BaseModel):
    city: str = desc("Name of the city")
    total_revenue: float
    total_orders: int

    @computed_field
    @property
    def aov(self)->float:
        return round(self.total_revenue / self.total_orders, 2) if self.total_orders > 0 else 0
    

class ProductRevenue(BaseModel):
    product: str = desc("Product Name")
    total_revenue: float
    total_orders: int

    @computed_field
    @property
    def aov(self)->float:
        return round(self.total_revenue / self.total_orders, 2) if self.total_orders > 0 else 0

class OfficeRevenue(BaseModel):
    office_city: str
    total_revenue: float
    total_orders: int

    @computed_field
    @property
    def aov(self)->float:
        return round(self.total_revenue / self.total_orders, 2) if self.total_orders > 0 else 0
    
class EmployeeRevenue(BaseModel):
    employee_number: int
    employee_name: str
    total_revenue: float
    total_orders: int
    office_city: str

    @computed_field
    @property
    def aov(self)->float:
        return round(self.total_revenue / self.total_orders, 2) if self.total_orders > 0 else 0
    
class ProductLineRevenue(BaseModel):
    product_line: str
    description: str
    total_revenue: float
    total_orders: int

    @computed_field
    @property
    def aov(self)->float:
        return round(self.total_revenue / self.total_orders, 2) if self.total_orders > 0 else 0
    