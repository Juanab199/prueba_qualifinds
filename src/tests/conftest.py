import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient

from app.controller.scrapper.page_scrape_manager import PageScrapeManager


@pytest.fixture
def app() -> FastAPI:
    from app.main import app as fastapi_app

    yield fastapi_app
@pytest.fixture

def client(app) -> TestClient:
    with TestClient(app) as client:
        return client
    
@pytest.fixture
def scraper():
    html_format = """
    <html>
        <body>
            <div class="vtex-product-summary-2-x-brandName">Product 1</div>
            <div class="vtex-product-summary-2-x-brandName">Product 2</div>
            <div class="vtex-flex-layout-0-x-flexRowContent--selling-price">
                <div id="items-price">100.0</div>
                <div id="items-price">90.0</div>
            </div>
            <div class="vtex-flex-layout-0-x-flexRowContent--selling-price">
                <div id="items-price">200.0</div>
                <div id="items-price">180.0</div>
            </div>
        </body>
    </html>
    """
    
    return PageScrapeManager(url="www.ejemplo.com", html_format=html_format.replace("\n",""))