from liczyrzepa.web_scraper import WebScraper


class TestWebScraper:
    def test_black_mock_discount_scraping(self):
        assert (
            WebScraper().scrape_text_content(
                r"https://blackmonk.pl/munchkin/1110-munchkin-legendy.html",
                r"//span[@class='product-price' and @itemprop='price']",
            )
            == "119,90 zł"
        )

    def test_normal_black_monk_scraping(self):
        assert (
            WebScraper().scrape_text_content(
                r"https://blackmonk.pl/zew-cthulhu/1982-ksiega-straznika-limitowana-edycja-jubileuszowa-pdf.html",
                r"//span[@class='product-price' and @itemprop='price']",
            )
            == "249,90 zł"
        )
