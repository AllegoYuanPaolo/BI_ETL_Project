from datetime import date
from typing import Optional

from fastapi import APIRouter, Query

from core import showData
from schemas import APIContracts as api

router = APIRouter(
    prefix="/sales",
    tags=["Sales Data"]
)


@router.get('/cities', response_model=list[api.CityRevenue])
def cities(
    start_date: Optional[date] = Query(None, description="Start date (YYYY-MM-DD)"),
    end_date: Optional[date] = Query(None, description="End date (YYYY-MM-DD)"),
    year: Optional[int] = Query(None, description="Filter by year"),
    quarter: Optional[int] = Query(None, ge=1, le=4, description="Filter by quarter (1-4)"),
    half: Optional[int] = Query(None, ge=1, le=2, description="Filter by half (1=H1, 2=H2)"),
    city: Optional[str] = Query(None, description="Filter by city name"),
):
    return showData.city_revenue(
        start_date=start_date, end_date=end_date,
        year=year, quarter=quarter, half=half,
        city=city,
    )


@router.get('/offices', response_model=list[api.OfficeRevenue])
def offices(
    start_date: Optional[date] = Query(None, description="Start date (YYYY-MM-DD)"),
    end_date: Optional[date] = Query(None, description="End date (YYYY-MM-DD)"),
    year: Optional[int] = Query(None, description="Filter by year"),
    quarter: Optional[int] = Query(None, ge=1, le=4, description="Filter by quarter (1-4)"),
    half: Optional[int] = Query(None, ge=1, le=2, description="Filter by half (1=H1, 2=H2)"),
    city: Optional[str] = Query(None, description="Filter by city name"),
    office_city: Optional[str] = Query(None, description="Filter by office city"),
):
    return showData.office_revenue(
        start_date=start_date, end_date=end_date,
        year=year, quarter=quarter, half=half,
        city=city, office_city=office_city,
    )


@router.get('/products', response_model=list[api.ProductRevenue])
def products(
    start_date: Optional[date] = Query(None, description="Start date (YYYY-MM-DD)"),
    end_date: Optional[date] = Query(None, description="End date (YYYY-MM-DD)"),
    year: Optional[int] = Query(None, description="Filter by year"),
    quarter: Optional[int] = Query(None, ge=1, le=4, description="Filter by quarter (1-4)"),
    half: Optional[int] = Query(None, ge=1, le=2, description="Filter by half (1=H1, 2=H2)"),
):
    return showData.product_revenue(
        start_date=start_date, end_date=end_date,
        year=year, quarter=quarter, half=half,
    )


@router.get('/employee', response_model=list[api.EmployeeRevenue])
def employee(
    start_date: Optional[date] = Query(None, description="Start date (YYYY-MM-DD)"),
    end_date: Optional[date] = Query(None, description="End date (YYYY-MM-DD)"),
    year: Optional[int] = Query(None, description="Filter by year"),
    quarter: Optional[int] = Query(None, ge=1, le=4, description="Filter by quarter (1-4)"),
    half: Optional[int] = Query(None, ge=1, le=2, description="Filter by half (1=H1, 2=H2)"),
    city: Optional[str] = Query(None, description="Filter by office city"),
    office_city: Optional[str] = Query(None, description="Filter by office city"),
):
    return showData.employee_revenue(
        start_date=start_date, end_date=end_date,
        year=year, quarter=quarter, half=half,
        city=city, office_city=office_city,
    )


@router.get('/product_line', response_model=list[api.ProductLineRevenue])
def product_line(
    start_date: Optional[date] = Query(None, description="Start date (YYYY-MM-DD)"),
    end_date: Optional[date] = Query(None, description="End date (YYYY-MM-DD)"),
    year: Optional[int] = Query(None, description="Filter by year"),
    quarter: Optional[int] = Query(None, ge=1, le=4, description="Filter by quarter (1-4)"),
    half: Optional[int] = Query(None, ge=1, le=2, description="Filter by half (1=H1, 2=H2)"),
):
    return showData.productline_revenue(
        start_date=start_date, end_date=end_date,
        year=year, quarter=quarter, half=half,
    )
