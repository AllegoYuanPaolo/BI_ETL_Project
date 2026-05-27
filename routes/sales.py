from fastapi import APIRouter
from core import showData
from schemas import APIContracts as api

router = APIRouter(
    prefix="/sales",
    tags=["Sales Data"]
)


@router.get('/cities', response_model=list[api.CityRevenue])
def cities(): 
    return showData.city_revenue()

@router.get('/offices', response_model=list[api.OfficeRevenue])
def offices():
    return showData.office_revenue()

@router.get('/products', response_model=list[api.ProductRevenue])
def products():
    return showData.product_revenue()

@router.get('/employee', response_model=list[api.EmployeeRevenue])
def employee():
    return showData.employee_revenue()

@router.get('/product_line', response_model=list[api.ProductLineRevenue])
def product_line():
    return showData.productline_revenue()