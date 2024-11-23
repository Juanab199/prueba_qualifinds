import os
from fastapi import HTTPException
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from app.config.scraping_config import SCRAPING_CONFIG


class SeleniumManager:
    def __init__(self) -> None:
        self._driver: webdriver = self._initialize_chrome_driver()

    def _initialize_chrome_driver(self) -> webdriver:
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--disable-dev-shm-usage")

        if os.getenv("USE_SELENIUM_REMOTE", "false").lower() == "true":
            self.driver = webdriver.Remote( 
                command_executor=SCRAPING_CONFIG["selenium_host"],
                options=chrome_options,
            )
        else:
            self.driver = webdriver.Chrome(options=chrome_options)

    def get_html_struct_page(self, url: str) -> str:
        try:
            self.driver.get(url)
            self.driver.maximize_window()

            for i in range(100):
                self.driver.execute_script(f"window.scrollTo(0, document.body.scrollHeight/{100-i});")

            html = self.driver.page_source
        
            return html
        
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    def close(self) -> None:
        if hasattr(self, 'driver'):
            self.driver.quit()
        