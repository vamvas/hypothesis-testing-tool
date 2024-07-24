from scipy import stats
import numpy as np


class OneSampleHypothesisTesting:
    def __init__(
        self,
        data: list,
        population_mean: float,
        alternative: str = "two-sided",
    ):

        if len(data) < 2:
            raise Exception("Input data must have at least two data points")

        elif len(set(data)) == 1:
            raise Exception("Input data must not have identical elements")

        self.data = data

        self.t_test_results = stats.ttest_1samp(
            a=self.data,
            popmean=population_mean,
            alternative=alternative,
        )

    def calculate_ci(self, alpha=0.05) -> tuple:
        sample_mean = np.mean(self.data)
        standard_error = np.std(self.data) / len(self.data)
        margin_of_error = stats.t.ppf((1 + (1 - alpha)) / 2, len(self.data) - 1) * standard_error

        lower_bound = sample_mean - margin_of_error
        upper_bound = sample_mean + margin_of_error

        return (lower_bound, upper_bound)
