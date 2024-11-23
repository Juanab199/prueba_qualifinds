import re
from typing import Optional
from pydantic import BaseModel, field_validator

from app.controller.common.exeptions import AbsentInputUrl


class InpuntData(BaseModel):
    url: str
    
    @field_validator("url")
    def if_url_is_none(cls, url: str):
        url_regex = re.compile(r'^(https?://)?(www\.)?([a-zA-Z0-9-]+\.)+[a-zA-Z]{2,6}(/[\w\-._~:/?#[\]@!$&\'()*+,;%=]*)?$')
        if not url_regex.match(url):
            raise ValueError('Invalid URL format')
        return url
    
    
class Product(BaseModel):
    name: str
    price: Optional[str]
    promo_price: Optional[str]


class ScrapedProductsData(BaseModel):
    url: str
    products: list[Product]