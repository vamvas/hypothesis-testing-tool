from hypothesis_testing_tool.compute_stats.two_sample_statistics import (
    TwoSampleHypothesisTesting,
)


def test_two_sample_t_test_returns_correct_t_statistic_and_p_value_for_alternative_of_two_sided_and_equal_variance():
    group_a = [1, 2, 5, 8, 10]
    group_b = [e * 2 for e in group_a]
    t_test = TwoSampleHypothesisTesting(group_a, group_b).t_test_results
    print(t_test.pvalue)
    assert round(t_test.pvalue, 3) == 0.212
    assert round(t_test.statistic, 3) == -1.356
    assert round(t_test.df) == 8.0


def test_two_sample_t_test_returns_correct_t_statistic_and_p_value_for_alternative_of_two_sided_and_unequal_variance():
    group_a = [1, 2, 5, 8, 10]
    group_b = [e * 2 for e in group_a]
    t_test = TwoSampleHypothesisTesting(group_a, group_b, equal_var=False).t_test_results
    print(t_test.pvalue)
    assert round(t_test.pvalue, 3) == 0.225
    assert round(t_test.statistic, 3) == -1.356
    assert round(t_test.df, 3) == 5.882
