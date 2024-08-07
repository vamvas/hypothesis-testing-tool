from hypothesis_testing_tool.compute_stats.one_sample_statistics import OneSampleTest
import pytest


def test_one_sample_t_test_returns_correct_t_statistic_and_p_value_for_alternative_of_two_sided():

    t_test = OneSampleTest(data=[1, 2, 5, 8, 10], null_population_mean=3.5).t_test_results

    assert round(t_test.pvalue, 3) == 0.378
    assert round(t_test.statistic, 3) == 0.991


def test_one_sample_t_test_returns_correct_t_statistic_and_p_value_for_alternative_of_lower():

    t_test = OneSampleTest(data=[1, 2, 5, 8, 10], null_population_mean=3.5, alternative="less").t_test_results

    assert round(t_test.pvalue, 3) == 0.811
    assert round(t_test.statistic, 3) == 0.991


def test_one_sample_t_test_returns_correct_t_statistic_and_p_value_for_alternative_of_higher():

    t_test = OneSampleTest(data=[1, 2, 5, 8, 10], null_population_mean=3.5, alternative="greater").t_test_results

    assert round(t_test.pvalue, 3) == 0.189
    assert round(t_test.statistic, 3) == 0.991


def test_one_sample_confidence_interval_has_correct_lower_and_upper_bound():

    confidence_interval = OneSampleTest(data=[1, 2, 5, 8, 10], null_population_mean=3.5).calculate_ci()

    assert round(confidence_interval["lower_bound"], 3) == 0.439
    assert round(confidence_interval["point_estimate"], 3) == 5.2
    assert round(confidence_interval["upper_bound"], 3) == 9.961


def test_one_sample_confidence_interval_has_correct_lower_and_upper_bound_for_alpha_different_than_default():

    confidence_interval = OneSampleTest(data=[1, 2, 5, 8, 10], null_population_mean=3.5).calculate_ci(alpha=0.01)

    assert round(confidence_interval["lower_bound"], 3) == -2.694
    assert round(confidence_interval["point_estimate"], 3) == 5.2
    assert round(confidence_interval["upper_bound"], 3) == 13.094


@pytest.mark.parametrize("input_data", [([]), [5]])
def test_one_sample_t_test_raises_error_when_input_has_less_than_two_elements(
    input_data,
):
    with pytest.raises(
        Exception,
        match="Input data must have at least two data points",
    ):
        OneSampleTest(input_data, null_population_mean=3.5)


def test_one_sample_t_test_raises_error_when_input_has_identical_elements():
    with pytest.raises(
        Exception,
        match="Input data must not have identical elements",
    ):
        input_data = [1] * 10
        OneSampleTest(input_data, null_population_mean=3.5)
