from datetime import datetime
from liczyrzepa.price_history import PriceHistory
from liczyrzepa.price_record import PriceRecord
from random import random


class PriceHistoryFactory:
    def n_records_with_random_values(self, records: int) -> PriceHistory:
        history = PriceHistory()
        for i in range(records):
            record = PriceRecord(datetime.timestamp(datetime.now()), random())
            history.records.append(record)
        return history

    def from_values_array(self, array: list[float]) -> PriceHistory:
        history = PriceHistory()
        for value in array:
            record = PriceRecord(datetime.timestamp(datetime.now()), value)
            history.records.append(record)
        return history

    def from_timestamps_array(self, array: list[float]) -> PriceHistory:
        history = PriceHistory()
        for timestamp in array:
            record = PriceRecord(timestamp, random())
            history.records.append(record)
        return history
