from scipy import stats
import numpy as np
from typing import List


class TwoSampleTest:
    def __init__(self, group_a: list, group_b: list, alternative: str = "two-sided", equal_var=True):
        self.group_a = group_a
        self.group_b = group_b
        self.alternative = alternative
        self.t_test_results = stats.ttest_ind(
            a=self.group_a,
            b=self.group_b,
            equal_var=equal_var,
            alternative=alternative,
        )

    def shapiro_wilk_pvalue(self) -> float:
        data = self.get_bootstrap_sampling_distribution_of_means()
        shapiro_test = stats.shapiro(data)

        return shapiro_test.pvalue

    def get_bootstrap_sampling_distribution_of_means(self, iterations=1000) -> List[float]:
        np.random.seed(42)
        mean_differences = []
        size_a = len(self.group_a)
        size_b = len(self.group_b)

        for _ in range(iterations):
            sample_a = np.random.choice(self.group_a, size=size_a, replace=True)
            sample_b = np.random.choice(self.group_b, size=size_b, replace=True)
            mean_diff = np.mean(sample_a) - np.mean(sample_b)
            mean_differences.append(mean_diff)

        return [float(x) for x in mean_differences]
