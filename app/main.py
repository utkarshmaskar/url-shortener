from fastapi import FastAPI
from app.config import settings


app=FastAPI(
    title=settings.app_name,
    description="A production-grade URL shortener app",
    version="0.1.0"

)



@app.get("/")
def checkhealth():
    return{
        "message":"Health ok",
        'app-name':settings.app_name
    }
