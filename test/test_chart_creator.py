from liczyrzepa.chart_creator import ChartCreator
from .price_history_factory import PriceHistoryFactory


class TestChartCreator:
    def test_saving_chart_to_file(self):
        history = PriceHistoryFactory().n_records_with_random_values(200)
        ChartCreator(history).save_chart_as_image("test/charts/test_chart.png")
