from .scrapper import Scrapper
from typing import List, Optional
from fastapi import FastAPI
from pydantic import BaseModel

class Request(BaseModel):
    url: str

app = FastAPI()

s = Scrapper()

@app.get('/')
def ping():
    return 'price history scrapper'

@app.post('/shopee/item')
def scrap_shopee(req: Request):
    result = s.shopee(req.url, 'item')
    return result

@app.post('/shopee/shop')
def scrap_shopee(req: Request):
    result = s.shopee(req.url, 'shop')
    return result

@app.on_event("shutdown")
def shutdown():
    s.shutdown()
