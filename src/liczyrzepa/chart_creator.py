import matplotlib.pyplot as plt
from price_history import PriceHistory


class ChartCreator:
    def __init__(self, history: PriceHistory) -> None:
        self.history = history
        times = history.get_times()
        values = history.get_values()
        fig, ax = plt.subplots(figsize=(16, 9))
        ax.grid(visible=True, which="both")
        plt.plot(
            times,
            values,
            linestyle="-",
            url=history.url,
            markersize=10,
            marker="o",
            label="Date",
        )
        self.set_chart_text()

    def set_chart_text(self):
        history = self.history
        fontdict = fontdict = {
            "rotation": "horizontal",
            "fontsize": "xx-large",
            "fontweight": 700,
        }
        plt.title(history.name, fontdict=fontdict)
        plt.xlabel("Date", fontdict=fontdict)
        plt.ylabel(
            f"{history.unit} ",
            fontdict=fontdict,
        )

    def show_interactive_chart(self):
        plt.show()

    def save_chart_as_image(self, path):
        plt.savefig(path)
        plt.close()
