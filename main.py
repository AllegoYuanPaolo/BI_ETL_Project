from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware
import uvicorn 

from routes import sales
from routes import etl
app = FastAPI()
# Change the origins (IP Addresses) to the IP of the frontend running server 
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],

    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

# 
app.include_router(sales.router)
app.include_router(etl.router)


@app.get('/test')
def test():
    return {"message": "yahallo from the backend! q(≧▽≦q)"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=5010, reload=True)
    ...