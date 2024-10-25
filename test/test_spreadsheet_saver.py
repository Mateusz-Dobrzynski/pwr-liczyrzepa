from liczyrzepa.spreadsheet_saver import SpreadsheetSaver
from .price_history_factory import PriceHistoryFactory
import pandas as pd
import os


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
