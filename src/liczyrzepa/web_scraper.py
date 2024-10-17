import requests
from bs4 import BeautifulSoup
from lxml import etree

import re


class WebScraper:
    def __init__(self) -> None:
        pass

    def get_current_value(self, url: str, xpath: str) -> float:
        text_content = self._scrape_text_content(url, xpath)
        return self._parse(text_content)

    def _parse(self, text_content: str) -> float:
        parsed_value_pattern = re.compile(r"\D*([\d ]+[,.]?\d*)")
        match = re.search(parsed_value_pattern, text_content)
        if not match:
            raise Exception()
        value = match.group(1)
        if "," in value:
            value = value.replace(",", ".")
        if " " in value:
            value = value.replace(" ", "")
        return float(value)

    def _scrape_text_content(self, url: str, xpath: str) -> str:
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
