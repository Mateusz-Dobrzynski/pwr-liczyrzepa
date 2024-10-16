from datetime import datetime


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

    def __init__(self) -> None:
        pass

    def to_json(self) -> dict:
        serialized_price_records = []
        for record in self.records:
            serialized_price_records.append(record.to_json())

        return {
            "url": self.url,
            "unit": self.unit,
            "name": self.name,
            "records": serialized_price_records,
        }
