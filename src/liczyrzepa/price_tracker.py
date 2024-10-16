import json

from liczyrzepa.types import PriceHistory, PriceRecord
from datetime import datetime

from liczyrzepa.web_scraper import WebScraper


class PriceTracker:
    def __init__(self, history_file_path: str) -> None:
        self.price_history = self._read_price_history_from(history_file_path)
        pass

    def _read_price_history_from(self, path: str) -> PriceHistory:
        try:
            json_file = self._read_json(path)
            history = self._parse_price_history_from(json_file)
            return history
        except:
            raise Exception(f"Failed to read price history from {path}")

    def _parse_price_history_from(self, raw_price_history: dict) -> PriceHistory:
        price_history = PriceHistory()
        price_history.name = raw_price_history["name"]
        price_history.url = raw_price_history["url"]
        price_history.unit = raw_price_history["unit"]
        price_history.records = self._parse_raw_price_records(
            raw_price_history["records"]
        )
        price_history.xpath = raw_price_history["xpath"]
        return price_history

    def _parse_raw_price_records(self, raw_records: list[dict]) -> list[PriceRecord]:
        parsed_records = []

        for record in raw_records:
            parsed_record = PriceRecord()
            parsed_record.time = datetime.fromtimestamp(record["timestamp"])
            parsed_record.value = record["value"]
            parsed_records.append(parsed_record)

        return parsed_records

    def _read_json(self, file_path: str) -> dict:
        file = open(file_path, "r", encoding="utf-8")
        json_file = json.load(file)
        file.close()
        return json_file

    def get_current_price_record(self):
        history = self.price_history
        url = history.url
        xpath = history.xpath
        value = WebScraper().get_current_value(url, xpath)
        current_timestamp = datetime.timestamp(datetime.now())
        record = PriceRecord(current_timestamp, value)
        self.add_price_record_to_history(record)

    def add_price_record_to_history(self, record: PriceRecord) -> None:
        self.price_history.records.append(record)

    def save_to_file(self, history_file_path):
        file = open(history_file_path, "w", encoding="utf-8")
        file.write(json.dumps(self.price_history.to_json()))
