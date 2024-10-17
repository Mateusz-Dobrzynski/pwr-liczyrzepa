from datetime import datetime
import json

from liczyrzepa.web_scraper import WebScraper


class PriceRecord:
    value: float
    time: datetime

    def __init__(
        self, timestamp: float | int | None = None, value: float | int | None = None
    ) -> None:
        if isinstance(timestamp, float) or isinstance(timestamp, int):
            self.time = datetime.fromtimestamp(timestamp)
        if isinstance(value, float) or isinstance(timestamp, int):
            self.value = value  # type: ignore

    def to_json(self) -> dict:
        return {"timestamp": self.time.timestamp(), "value": self.value}


class PriceHistory:
    url: str
    unit: str
    name: str
    records: list[PriceRecord]
    xpath: str

    def __init__(self, path: str) -> None:
        try:
            raw_price_history = self._read_json(path)

            self.name = raw_price_history["name"]
            self.url = raw_price_history["url"]
            self.unit = raw_price_history["unit"]
            self.records = self._parse_raw_price_records(raw_price_history["records"])
            self.xpath = raw_price_history["xpath"]
        except:
            raise Exception(f"Failed to read price history from {path}")

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

    def _get_current_price_record(self) -> PriceRecord:
        value = WebScraper().get_current_value(self.url, self.xpath)
        current_timestamp = datetime.timestamp(datetime.now())
        return PriceRecord(current_timestamp, value)

    def append_price_record(self, record: PriceRecord) -> None:
        self.records.append(record)

    def save_to_file(self, history_file_path):
        file = open(history_file_path, "w", encoding="utf-8")
        file.write(json.dumps(self._to_json()))

    def _to_json(self) -> dict:
        serialized_price_records = []
        for record in self.records:
            serialized_price_records.append(record.to_json())

        return {
            "url": self.url,
            "unit": self.unit,
            "name": self.name,
            "records": serialized_price_records,
            "xpath": self.xpath,
        }
