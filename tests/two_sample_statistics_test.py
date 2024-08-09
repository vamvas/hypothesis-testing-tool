from hypothesis_testing_tool.compute_stats.two_sample_statistics import TwoSampleTest
import pytest
import random


@pytest.fixture(autouse=True)
def mock_data_for_two_samples():
    random.seed(42)
    group_a = [random.gauss(mu=1, sigma=1) for _ in range(50)]
    group_b = [random.gauss(mu=2, sigma=1) for _ in range(50)]

    return group_a, group_b


def test_two_sample_t_test_returns_correct_t_statistic_and_p_value_for_alternative_of_two_sided_and_equal_variance(mock_data_for_two_samples):

    group_a, group_b = mock_data_for_two_samples
    t_test = TwoSampleTest(group_a, group_b).t_test_results

    assert round(t_test.pvalue, 3) == 0.000
    assert round(t_test.statistic, 3) == -7.016
    assert t_test.df == 98.0


def test_two_sample_t_test_returns_correct_t_statistic_and_p_value_for_alternative_of_two_sided_and_unequal_variance(mock_data_for_two_samples):

    group_a, group_b = mock_data_for_two_samples
    t_test = TwoSampleTest(group_a, group_b, equal_var=False).t_test_results

    assert round(t_test.pvalue, 3) == 0.000
    assert round(t_test.statistic, 3) == -7.016
    assert round(t_test.df, 3) == 95.507


def test_two_sample_t_test_returns_correct_t_statistic_and_p_value_for_alternative_of_greater_and_equal_variance(mock_data_for_two_samples):

    group_a, group_b = mock_data_for_two_samples
    t_test = TwoSampleTest(group_a, group_b, alternative="greater").t_test_results

    assert round(t_test.pvalue, 3) == 1.000
    assert round(t_test.statistic, 3) == -7.016
    assert t_test.df == 98.0


def test_two_sample_t_test_returns_correct_t_statistic_and_p_value_for_alternative_of_greater_and_unequal_variance(mock_data_for_two_samples):

    group_a, group_b = mock_data_for_two_samples
    t_test = TwoSampleTest(group_a, group_b, equal_var=False, alternative="greater").t_test_results

    assert round(t_test.pvalue, 3) == 1.000
    assert round(t_test.statistic, 3) == -7.016
    assert round(t_test.df, 3) == 95.507


def test_two_sample_t_test_returns_correct_t_statistic_and_p_value_for_alternative_of_less_and_equal_variance(mock_data_for_two_samples):

    group_a, group_b = mock_data_for_two_samples
    t_test = TwoSampleTest(group_a, group_b, alternative="less").t_test_results

    assert round(t_test.pvalue, 3) == 0.000
    assert round(t_test.statistic, 3) == -7.016
    assert t_test.df == 98.0


def test_two_sample_t_test_returns_correct_t_statistic_and_p_value_for_alternative_of_less_and_unequal_variance(mock_data_for_two_samples):

    group_a, group_b = mock_data_for_two_samples
    t_test = TwoSampleTest(group_a, group_b, equal_var=False, alternative="less").t_test_results

    assert round(t_test.pvalue, 3) == 0.000
    assert round(t_test.statistic, 3) == -7.016
    assert round(t_test.df, 3) == 95.507


def test_bootstrap_method_returns_correct_output(mock_data_for_two_samples):

    group_a, group_b = mock_data_for_two_samples
    boostrap_result = TwoSampleTest(group_a, group_b).get_bootstrap_sampling_distribution_of_means(iterations=5)

    assert [round(x, 3) for x in boostrap_result] == [-1.169, -1.301, -1.451, -1.372, -1.106]
