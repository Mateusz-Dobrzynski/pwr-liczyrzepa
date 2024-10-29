from price_record import PriceRecord
import pytest
from datetime import datetime


class TestPriceRecord:
    def test_should_raise_exception_when_getting_nonexistent_attributes(self):
        with pytest.raises(AttributeError):
            record = PriceRecord()
            test_value = record.value

        with pytest.raises(AttributeError):
            record = PriceRecord()
            test_value = record.time

    def test_manual_fields_initialization(self):
        # GIVEN
        test_value = 25
        test_timestamp = 50
        record = PriceRecord()

        # WHEN
        record.value = test_value
        record.time = datetime.fromtimestamp(test_timestamp)

        # THEN
        assert record.value == test_value
        assert record.time.timestamp() == test_timestamp

    def test_initialization_via_constructor(self):
        # GIVEN
        test_value = 25
        test_timestamp = 50

        # WHEN
        record = PriceRecord(timestamp=test_timestamp, value=test_value)

        # THEN
        assert record.value == test_value
        assert record.time.timestamp() == test_timestamp

    def test_post_initialization_modification(self):
        # GIVEN
        initial_value = 25
        initial_timestamp = 50
        modified_value = 15
        modified_timestamp = 17
        record = PriceRecord(timestamp=initial_timestamp, value=initial_value)

        # WHEN
        record.value = modified_value
        record.time = datetime.fromtimestamp(modified_timestamp)

        # THEN
        assert record.value == modified_value
        assert record.time.timestamp() == modified_timestamp
