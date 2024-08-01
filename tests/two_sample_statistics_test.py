from hypothesis_testing_tool.compute_stats.two_sample_statistics import TwoSampleTest


def test_two_sample_t_test_returns_correct_t_statistic_and_p_value_for_alternative_of_two_sided_and_equal_variance():
    group_a = [1, 2, 5, 8, 10]
    group_b = [e * 2 for e in group_a]
    t_test = TwoSampleTest(group_a, group_b).t_test_results
    print(t_test.pvalue)
    assert round(t_test.pvalue, 3) == 0.212
    assert round(t_test.statistic, 3) == -1.356
    assert round(t_test.df) == 8.0


def test_two_sample_t_test_returns_correct_t_statistic_and_p_value_for_alternative_of_two_sided_and_unequal_variance():
    group_a = [1, 2, 5, 8, 10]
    group_b = [e * 2 for e in group_a]
    t_test = TwoSampleTest(group_a, group_b, equal_var=False).t_test_results
    print(t_test.pvalue)
    assert round(t_test.pvalue, 3) == 0.225
    assert round(t_test.statistic, 3) == -1.356
    assert round(t_test.df, 3) == 5.882


def test_two_sample_t_test_returns_correct_t_statistic_and_p_value_for_alternative_of_greater_and_equal_variance():
    group_a = [1, 2, 5, 8, 10]
    group_b = [e * 2 for e in group_a]
    t_test = TwoSampleTest(group_a, group_b, alternative="greater").t_test_results
    print(t_test.pvalue)
    assert round(t_test.pvalue, 3) == 0.894
    assert round(t_test.statistic, 3) == -1.356
    assert round(t_test.df) == 8.0


def test_two_sample_t_test_returns_correct_t_statistic_and_p_value_for_alternative_of_greater_and_unequal_variance():
    group_a = [1, 2, 5, 8, 10]
    group_b = [e * 2 for e in group_a]
    t_test = TwoSampleTest(group_a, group_b, equal_var=False, alternative="greater").t_test_results
    print(t_test.pvalue)
    assert round(t_test.pvalue, 3) == 0.888
    assert round(t_test.statistic, 3) == -1.356
    assert round(t_test.df, 3) == 5.882


def test_two_sample_t_test_returns_correct_t_statistic_and_p_value_for_alternative_of_less_and_equal_variance():
    group_a = [1, 2, 5, 8, 10]
    group_b = [e * 2 for e in group_a]
    t_test = TwoSampleTest(group_a, group_b, alternative="less").t_test_results
    print(t_test.pvalue)
    assert round(t_test.pvalue, 3) == 0.106
    assert round(t_test.statistic, 3) == -1.356
    assert round(t_test.df) == 8.0


def test_two_sample_t_test_returns_correct_t_statistic_and_p_value_for_alternative_of_less_and_unequal_variance():
    group_a = [1, 2, 5, 8, 10]
    group_b = [e * 2 for e in group_a]
    t_test = TwoSampleTest(group_a, group_b, equal_var=False, alternative="less").t_test_results
    print(t_test.pvalue)
    assert round(t_test.pvalue, 3) == 0.112
    assert round(t_test.statistic, 3) == -1.356
    assert round(t_test.df, 3) == 5.882
