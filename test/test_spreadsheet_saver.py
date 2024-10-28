from liczyrzepa.spreadsheet_saver import SpreadsheetSaver
from .price_history_factory import PriceHistoryFactory
import pandas as pd
import os
from datetime import datetime


class TestSpreadsheetSaver:

    def test_saving_to_path(self):
        # GIVEN
        test_history = PriceHistoryFactory().n_records_with_random_values(10)
        saver = SpreadsheetSaver()
        save_path = f"{os.getcwd()}/test_sheet.ods"

        # WHEN
        saver.save_history_to_file(test_history, save_path)

        # THEN
        frame = pd.read_excel(save_path)
        assert frame.shape == (10, 2)

    def test_values_integrity(self):
        # GIVEN
        values_array = [10, 15, 20, 25, 15.5]
        test_history = PriceHistoryFactory().from_values_array(values_array)
        saver = SpreadsheetSaver()
        save_path = f"{os.getcwd()}/test_sheet.ods"

        # WHEN
        saver.save_history_to_file(test_history, save_path)

        # THEN
        frame = pd.read_excel(save_path)
        for i in range(len(frame.index)):
            current_row = frame.loc[frame.index[i]]
            assert current_row["value"] == values_array[i]

    def test_times_integrity(self):
        # GIVEN
        timestamps_array = [10, 15, 20, 21.37, 25]
        test_history = PriceHistoryFactory().from_timestamps_array(timestamps_array)
        saver = SpreadsheetSaver()
        save_path = f"{os.getcwd()}/test_sheet.ods"

        # WHEN
        saver.save_history_to_file(test_history, save_path)

        # THEN
        frame = pd.read_excel(save_path)
        for i in range(len(frame.index)):
            current_row = frame.loc[frame.index[i]]
            assert current_row[frame.columns[0]] == datetime.fromtimestamp(
                timestamps_array[i]
            )
