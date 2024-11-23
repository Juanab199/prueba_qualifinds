import logging
from fastapi import APIRouter

from app.controller.schemas.schemas import InpuntData
from app.controller.schemas.schemas import ScrapedProductsData
from fastapi import HTTPException
from app.controller.scrapper.selenium_manager import SeleniumManager
from app.controller.scrapper.page_scrape_manager import PageScrapeManager


selenium_driver = None

task_router = APIRouter(prefix="/api")

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@task_router.on_event("startup")
def startup_event():
    global selenium_driver
    selenium_driver = SeleniumManager()

@task_router.on_event("shutdown")
def shutdown_event():
    if selenium_driver:
        selenium_driver.close()

@task_router.post(
    path="/scrape_data",
    status_code=200
)
async def scrape_data(input_data: InpuntData):
    html_struct = selenium_driver.get_html_struct_page(url=input_data.url)
    
    scrape_manager = PageScrapeManager(input_data.url,html_struct)
    scraped_data = scrape_manager.extract_data()
    
    return scraped_data

