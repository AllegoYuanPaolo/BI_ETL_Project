from fastapi import APIRouter
from core import showData

router = APIRouter(
    prefix="/sales",
    tags=["Sales Data"]
)


@router.get('/cities')
def cities(): 
    return showData.city_revenue()

@router.get('/offices')
def offices():
    return showData.office_revenue()

@router.get('/products')
def products():
    return showData.product_revenue()

@router.get('/employee')
def employee():
    return showData.employee_revenue()

@router.get('/product_line')
def product_line():
    return showData.productline_revenue()