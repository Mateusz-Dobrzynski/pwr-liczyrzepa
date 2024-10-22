from datetime import datetime


class PriceRecord:
    value: float
    time: datetime

    def __init__(
        self, timestamp: float | int | None = None, value: float | int | None = None
    ) -> None:
        if isinstance(timestamp, float) or isinstance(timestamp, int):
            self.time = datetime.fromtimestamp(timestamp)
        if isinstance(value, float) or isinstance(value, int):
            self.value = value  # type: ignore

    def to_json(self) -> dict:
        return {"timestamp": self.time.timestamp(), "value": self.value}
