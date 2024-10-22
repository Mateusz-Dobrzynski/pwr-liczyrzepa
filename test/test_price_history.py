from datetime import datetime

from src.liczyrzepa.price_history import PriceHistory
from src.liczyrzepa.price_record import PriceRecord
from test.price_history_factory import PriceHistoryFactory


class TestPriceHistory:
    def test_price_history_parsing(self):
        price_history = PriceHistory("test/data/test_price_history.json")
        record = price_history.records[0]

        assert price_history.name == "test"
        assert price_history.unit == "zł"
        assert price_history.xpath == "//div[@class='test']"
        assert price_history.url == "https://test.com"
        assert record.value == 2137
        assert record.time == datetime.fromtimestamp(2137)

    def test_history_saving(self):
        # GIVEN
        price_history = PriceHistory("test/data/test_price_history.json")
        new_record = PriceRecord(2138, 2138)
        modified_history_path = "test/data/modified_price_history.json"

        # WHEN
        price_history.records.append(new_record)
        price_history.save_to_file(modified_history_path)
        modified_history = PriceHistory(modified_history_path)

        # THEN
        assert modified_history.records[-1].value == new_record.value
        assert modified_history.records[-1].time == new_record.time

    def test_price_record_creation(self):
        # GIVEN
        price_history = PriceHistory("test/data/empty_black_monk_munchkin_legends.json")

        # WHEN
        price_history.create_new_price_record()

        # THEN
        assert len(price_history.records)

    def test_times_array_creation(self):
        # GIVEN
        timestamps_input = [15, 20, 25.5]
        history = PriceHistoryFactory().from_timestamps_array(timestamps_input)

        # WHEN
        timestamps_output = history.get_times()

        # THEN
        assert len(timestamps_input) == len(timestamps_output)
        for i in range(len(timestamps_input)):
            assert timestamps_input[i] == datetime.timestamp(timestamps_output[i])

    def test_values_array_creation(self):
        # GIVEN
        values_input = [15, 20, 25.5]
        history = PriceHistoryFactory().from_values_array(values_input)

        # WHEN
        values_output = history.get_values()

        # THEN
        assert len(values_output) == len(values_output)
        for i in range(len(values_output)):
            assert values_output[i] == values_output[i]
