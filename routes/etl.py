from etl import main
from fastapi import APIRouter

router = APIRouter(
    prefix='/etl',
    tags=['ETL Functions']
)

@router.get('/refresh')
def refresh():
    try:
        main.run_etl()
        return {"message": "OK"}
    except Exception as err:
        return {
                    "message": "ERROR",
                    "ERROR": err
                }
    
    