from hypothesis_testing_tool.presentation.create_plots import create_one_sample_hypothesis_plot
import pytest
import matplotlib

matplotlib.use("Agg")


@pytest.fixture
def ci_dict():
    return {"lower_bound": 0, "point_estimate": 5, "upper_bound": 9, "null_population_mean": 3}


def test_create_one_sample_hypothesis_plot_saves_file_as_png_at_path(ci_dict, tmp_path):

    create_one_sample_hypothesis_plot(tmp_path / "one_sample_plot.png", ci_dict)

    assert (tmp_path / "one_sample_plot.png").exists()


def test_create_one_sample_hypothesis_plot_returns_correct_fig_object_based_on_input(ci_dict, tmp_path):

    fig, ax = create_one_sample_hypothesis_plot(tmp_path / "one_sample_plot.png", ci_dict, width=10, height=5)

    assert fig.get_size_inches().tolist() == [10, 5]
    assert len(fig.get_axes()) == 1


def test_create_one_sample_hypothesis_plot_returns_correct_axes_object_based_on_input(ci_dict, tmp_path):

    fig, ax = create_one_sample_hypothesis_plot(tmp_path / "one_sample_plot.png", ci_dict)
    lines = ax.get_lines()
    horizontal_line = lines[0]
    lower_bound_circle = lines[1]
    point_estimate_circle = lines[2]
    upper_bound_circle = lines[3]
    vertical_null_population_line = lines[-1]
    legend = ax.get_legend()

    assert len(lines) == 5  # Three points, one vertical line, one horizontal_line

    assert horizontal_line.get_color() == "gray"
    assert horizontal_line.get_linewidth() == 1
    assert horizontal_line.get_xdata().tolist() == [ci_dict["lower_bound"], ci_dict["upper_bound"]]
    assert horizontal_line.get_ydata().tolist() == [0, 0]

    assert lower_bound_circle.get_marker() == "o"
    assert lower_bound_circle.get_color() == "orange"
    assert lower_bound_circle.get_markersize() == 6
    assert lower_bound_circle.get_label() == "95% CI Lower Bound"
    assert lower_bound_circle.get_xdata().tolist() == [ci_dict["lower_bound"]]
    assert lower_bound_circle.get_ydata().tolist() == [0]

    assert point_estimate_circle.get_marker() == "o"
    assert point_estimate_circle.get_color() == "black"
    assert point_estimate_circle.get_markersize() == 6
    assert point_estimate_circle.get_label() == "Observed Point Estimate"
    assert point_estimate_circle.get_xdata().tolist() == [ci_dict["point_estimate"]]
    assert point_estimate_circle.get_ydata().tolist() == [0]

    assert upper_bound_circle.get_marker() == "o"
    assert upper_bound_circle.get_color() == "#05c9de"
    assert upper_bound_circle.get_markersize() == 6
    assert upper_bound_circle.get_label() == "95% CI Upper Bound"
    assert upper_bound_circle.get_xdata().tolist() == [ci_dict["upper_bound"]]
    assert upper_bound_circle.get_ydata().tolist() == [0]

    assert vertical_null_population_line.get_color() == "red"
    assert vertical_null_population_line.get_linestyle() == "--"
    assert vertical_null_population_line.get_linewidth() == 2
    assert vertical_null_population_line.get_label() == "Null Population Mean"
    assert vertical_null_population_line.get_xdata() == [3, 3]

    assert ax.get_title() == "95% Confidence Interval (CI) for the Mean of One Sample"
    assert ax.get_xlabel() == "Values"

    assert legend is not None
