from liczyrzepa.price_tracker import PriceTracker
from datetime import datetime

from liczyrzepa.types import PriceHistory, PriceRecord


class TestPriceTracker:
    def test_price_history_parsing(self):
        price_tracker = PriceTracker("test/data/test_price_history.json")
        price_history = price_tracker.price_history
        record = price_history.records[0]

        assert price_history.name == "test"
        assert price_history.unit == "zł"
        assert price_history.xpath == "//div[@class='test']"
        assert price_history.url == "https://test.com"
        assert record.value == 2137
        assert record.time == datetime.fromtimestamp(2137)

    def test_adding_records_to_history(self):
        # GIVEN
        price_tracker = PriceTracker("test/data/test_price_history.json")
        record = PriceRecord(timestamp=115, value=225)

        # WHEN
        price_tracker.add_price_record_to_history(record)

        # THEN
        price_history = price_tracker.price_history
        assert price_history.records[-1].time == datetime.fromtimestamp(115)
        assert price_history.records[-1].value == 225

    def test_history_saving(self):
        # GIVEN
        price_tracker = PriceTracker("test/data/test_price_history.json")
        new_record = PriceRecord(2138, 2138)
        modified_history_path = "test/data/modified_price_history.json"

        # WHEN
        price_tracker.add_price_record_to_history(new_record)
        price_tracker.save_to_file(modified_history_path)
        modified_history = PriceTracker(modified_history_path).price_history

        # THEN
        assert modified_history.records[-1].value == new_record.value
        assert modified_history.records[-1].time == new_record.time
