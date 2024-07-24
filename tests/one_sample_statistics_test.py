from hypothesis_testing_tool.one_sample_statistics import (
    OneSampleHypothesisTesting,
)
import pytest


def test_one_sample_t_test_returns_correct_t_statistic_and_p_value_for_alternative_of_two_sided():

    t_test = OneSampleHypothesisTesting(data=[1, 2, 5, 8, 10], population_mean=3.5).t_test_results

    assert round(t_test.pvalue, 3) == 0.378
    assert round(t_test.statistic, 3) == 0.991


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
