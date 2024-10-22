from .price_history_factory import PriceHistoryFactory
from datetime import datetime


class TestPriceHistoryFactory:
    def test_creation_with_random_values(self):
        records = PriceHistoryFactory().n_records_with_random_values(15).records
        assert len(records) == 15

    def test_creating_from_values_array(self):
        records = PriceHistoryFactory().from_values_array([15.5, 2137, 115]).records

        assert len(records) == 3
        assert records[0].value == 15.5
        assert records[1].value == 2137
        assert records[2].value == 115

    def test_creating_from_timestamps_array(self):
        records = (
            PriceHistoryFactory().from_timestamps_array([2137420, 222, 777]).records
        )

        assert len(records) == 3
        assert datetime.timestamp(records[0].time) == 2137420
        assert datetime.timestamp(records[1].time) == 222
        assert datetime.timestamp(records[2].time) == 777
