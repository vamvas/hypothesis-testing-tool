from hypothesis_testing_tool.one_sample_statistics import (
    OneSampleHypothesisTesting,
)
import pytest


def test_one_sample_t_test_returns_correct_t_statistic_and_p_value_when_input_has_length_of_two():

    p_value = OneSampleHypothesisTesting(data=[1, 2], population_mean=3.5).calculate_pvalue()

    assert round(p_value, 3) == 0.156


def test_one_sample_t_test_returns_correct_p_value_when_input_has_length_higher_than_two():

    p_value = OneSampleHypothesisTesting(data=[1, 2, 5, 8, 10], population_mean=3.5).calculate_pvalue()

    assert round(p_value, 3) == 0.378


def test_one_sample_t_test_returns_correct_t_statistic_when_input_has_length_higher_than_two():

    t_statistic = OneSampleHypothesisTesting(data=[1, 2, 5, 8, 10], population_mean=3.5).calculate_t_statistic()

    assert round(t_statistic, 3) == 0.991


@pytest.mark.parametrize("input_data", [([]), [5]])
def test_one_sample_t_test_raises_error_when_input_has_less_than_two_elements(
    input_data,
):
    with pytest.raises(
        Exception,
        match="Input data must have at least two data points",
    ):
        OneSampleHypothesisTesting(input_data, population_mean=3.5)


def test_one_sample_t_test_raises_error_when_input_has_identical_elements():
    with pytest.raises(
        Exception,
        match="Input data must not have identical elements",
    ):
        input_data = [1] * 10
        OneSampleHypothesisTesting(input_data, population_mean=3.5)
