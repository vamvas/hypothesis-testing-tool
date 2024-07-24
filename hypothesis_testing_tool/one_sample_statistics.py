from scipy.stats import ttest_1samp


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

        self.t_test_results = ttest_1samp(
            a=data,
            popmean=population_mean,
            alternative=alternative,
        )
