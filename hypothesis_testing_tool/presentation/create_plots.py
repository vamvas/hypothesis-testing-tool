import matplotlib.pyplot as plt


class OneSampleCIPlot:

    def __init__(self, ci_dict, **kwargs):
        self.ci_dict: dict = ci_dict
        self.width: int = kwargs.get("width", 10)
        self.height: int = kwargs.get("height", 5)
        self.fig = None
        self.ax = None

    def __enter__(self):
        self.fig, self.ax = self.__create_plot(self.width, self.height)
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        plt.close(self.fig)
        self.fig = None
        self.ax = None

    def __create_plot(self, width, height):
        fig, ax = plt.subplots(1, 1, figsize=(width, height))

        ax.plot([self.ci_dict["lower_bound"], self.ci_dict["upper_bound"]], [0, 0], color="gray", linewidth=1)
        ax.plot(self.ci_dict["lower_bound"], 0, marker="o", color="orange", markersize=6, label="95% CI Lower Bound")
        ax.plot(self.ci_dict["point_estimate"], 0, marker="o", color="black", markersize=6, label="Observed Point Estimate")
        ax.plot(self.ci_dict["upper_bound"], 0, marker="o", color="#05c9de", markersize=6, label="95% CI Upper Bound")

        ax.set_yticks([])
        ax.set_xlabel("Values")
        ax.set_title("95% Confidence Interval (CI) for the Mean of One Sample")

        ax.axvline(x=self.ci_dict["null_population_mean"], color="red", linestyle="--", linewidth=2, label="Null Population Mean")

        ax.legend(loc="upper right", frameon=True)

        return fig, ax

    def show_plot(self):
        plt.show()

    def save_plot(self, path_to_save_plot: str):
        self.fig.savefig(path_to_save_plot)
