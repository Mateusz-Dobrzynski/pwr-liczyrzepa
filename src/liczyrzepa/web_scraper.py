import requests
from bs4 import BeautifulSoup
from lxml import etree


class WebScraper:
    def __init__(self) -> None:
        pass

    def scrape_text_content(self, url, xpath) -> str:
        HEADERS = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36",
            "Accept-Language": "en-US, en;q=0.5",
        }
        webpage = requests.get(url, headers=HEADERS)
        soup = BeautifulSoup(webpage.content, "html.parser")
        dom = etree.HTML(str(soup), parser=None)
        element = dom.xpath(xpath)
        if isinstance(element, list):
            text = element[0].text
        else:
            text = element.text
        return self._remove_xa0_from(text)

    def _remove_xa0_from(self, text: str) -> str:
        return text.replace("\xa0", " ")
