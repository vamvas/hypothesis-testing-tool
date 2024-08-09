from hypothesis_testing_tool.compute_stats.one_sample_statistics import OneSampleTest
import pytest


def test_one_sample_t_test_returns_correct_t_statistic_and_p_value_for_alternative_of_two_sided():

    t_test = OneSampleTest(data=[1, 2, 5, 8, 10], null_population_mean=3.5).t_test_results

    assert t_test.pvalue == pytest.approx(0.3775, abs=1e-4)
    assert t_test.statistic == pytest.approx(0.9914, abs=1e-4)


def test_one_sample_t_test_returns_correct_t_statistic_and_p_value_for_alternative_of_lower():

    t_test = OneSampleTest(data=[1, 2, 5, 8, 10], null_population_mean=3.5, alternative="less").t_test_results

    assert t_test.pvalue == pytest.approx(0.8112, abs=1e-4)
    assert t_test.statistic == pytest.approx(0.9914, abs=1e-4)


def test_one_sample_t_test_returns_correct_t_statistic_and_p_value_for_alternative_of_higher():

    t_test = OneSampleTest(data=[1, 2, 5, 8, 10], null_population_mean=3.5, alternative="greater").t_test_results

    assert t_test.pvalue == pytest.approx(0.1887, abs=1e-4)
    assert t_test.statistic == pytest.approx(0.9914, abs=1e-4)


def test_one_sample_confidence_interval_has_correct_lower_and_upper_bound():

    confidence_interval = OneSampleTest(data=[1, 2, 5, 8, 10], null_population_mean=3.5).calculate_ci()

    assert confidence_interval["lower_bound"] == pytest.approx(0.4393, abs=1e-4)
    assert confidence_interval["point_estimate"] == 5.2
    assert confidence_interval["upper_bound"] == pytest.approx(9.9606, abs=1e-4)


def test_one_sample_confidence_interval_has_correct_lower_and_upper_bound_for_alpha_different_than_default():

    confidence_interval = OneSampleTest(data=[1, 2, 5, 8, 10], null_population_mean=3.5).calculate_ci(alpha=0.01)

    assert confidence_interval["lower_bound"] == pytest.approx(-2.6943, abs=1e-4)
    assert confidence_interval["point_estimate"] == 5.2
    assert confidence_interval["upper_bound"] == pytest.approx(13.0943, abs=1e-4)


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
