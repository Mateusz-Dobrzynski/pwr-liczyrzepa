from liczyrzepa.web_scraper import WebScraper


class TestWebScraper:
    def test_black_mock_discount_scraping(self):
        assert (
            WebScraper()._scrape_text_content(
                r"https://blackmonk.pl/munchkin/1110-munchkin-legendy.html",
                r"//span[@class='product-price' and @itemprop='price']",
            )
            == "119,90 zł"
        )

    def test_normal_black_monk_scraping(self):
        assert (
            WebScraper()._scrape_text_content(
                r"https://blackmonk.pl/zew-cthulhu/1982-ksiega-straznika-limitowana-edycja-jubileuszowa-pdf.html",
                r"//span[@class='product-price' and @itemprop='price']",
            )
            == "249,90 zł"
        )

    def test_value_parsing(self):
        scraper = WebScraper()
        assert scraper._parse("249 zł") == 249
        assert scraper._parse("2138.19") == 2138.19
        assert scraper._parse("15,5") == 15.5
        assert scraper._parse("150 000") == 150000
        assert scraper._parse("$5.50") == 5.5
        assert scraper._parse("250 000 zł") == 250000
