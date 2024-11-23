from typing import Optional
from bs4 import BeautifulSoup, Tag

from app.controller.schemas.schemas import ScrapedProductsData, Product
from app.config.scraping_config import SCRAPING_CONFIG


class PageScrapeManager:
    def __init__(self, url: str, html_format: str):
        self.product_name_selector = SCRAPING_CONFIG["selectors"]["product_name"]
        self.prices_selector = SCRAPING_CONFIG["selectors"]["price_container"]
        self.prices_id = SCRAPING_CONFIG["selectors"]["prices_id"]
        self.page_soup: BeautifulSoup = BeautifulSoup(html_format, "html.parser")
        self.url = url
        
    def _extract_product_names(self) -> list[str]:
        return [
            name.text.strip() 
            for name in self.page_soup.find_all(class_=self.product_name_selector, limit=15)
        ]
        
    def _extract_product_prices(self) -> list[tuple[Optional[float], float]]:
        def extract_price(price_element: Tag) -> str:
            return price_element.text.replace("\xa0", " ")
        
        def process_price_block(price_container: Tag) -> tuple[Optional[str], str]:
            price_elements = price_container.find_all(id=self.prices_id)
            regular_price = extract_price(price_elements[0]) if len(price_elements) > 1 else None
            promotional_price = extract_price(price_elements[-1])
            return (regular_price, promotional_price)

        price_containers = self.page_soup.find_all(
            class_=self.prices_selector, limit=15
        )
        
        return [process_price_block(price_container) for price_container in price_containers]
        
    def extract_data(self) -> ScrapedProductsData:
        product_prices = self._extract_product_prices()
        product_names = self._extract_product_names()
        
        products = [
            Product(name=name, promo_price=promo_price, price=price)
            for name, (promo_price, price) in zip(product_names, product_prices)
        ]

        return ScrapedProductsData(url=self.url, products=products)