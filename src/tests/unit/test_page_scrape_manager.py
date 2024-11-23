from app.controller.scrapper.page_scrape_manager import PageScrapeManager


class TestPageScraperManager:
    def test__extract_product_names(self, scraper: PageScrapeManager):
        product_names = scraper._extract_product_names()

        assert product_names == ["Product 1", "Product 2"]


    def test__extract_product_prices(self, scraper: PageScrapeManager):
        product_prices = scraper._extract_product_prices()

        assert product_prices == [("100.0", "90.0"), ("200.0", "180.0")]


    def test_extract_data(self, scraper: PageScrapeManager):
        scraped_data = scraper.extract_data()

        assert len(scraped_data.products) == 2
        assert scraped_data.products[0].name == "Product 1"
        assert scraped_data.products[0].price == "90.0"
        assert scraped_data.products[0].promo_price == "100.0"
        assert scraped_data.products[1].name == "Product 2"
        assert scraped_data.products[1].price == "180.0"
        assert scraped_data.products[1].promo_price == "200.0"