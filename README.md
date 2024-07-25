# Description

A package to run hypothesis testing for one and two samples.

<br>

## One Sample Hypothesis Testing

    from hypothesis_testing_tool.compute_stats.one_sample_statistics import OneSampleHypothesisTesting

Let's see an example of how you can use the `OneSampleHypothesisTesting` class.

        data = [1, 2, 5, 8, 10]
        null_population_mean = 3.5

        t_test = OneSampleHypothesisTesting(
                        data = [1, 2, 5, 8, 10],
                        null_population_mean = 3.5
                ).t_test_results

From the t_test you can extract the p-value and t-statistic.

        t_test.pvalue
        t_test.statistic

The default is with alternative = "two-sided", but that can change to a one tail test.

        OneSampleHypothesisTesting(
                data = [1, 2, 5, 8, 10],
                null_population_mean = 3.5,
                alternative = "less"
                )

        OneSampleHypothesisTesting(
                data = [1, 2, 5, 8, 10],
                null_population_mean = 3.5,
                alternative = "greater"
                )

You can also compute the confidence interval (default = 95%) for the mean, using the `calculate_ci` method.

The `calculate_ci` method takes an optional argument `alpha` to adjust to 99% CI (alpha = 0.01) or any other.

        confidence_interval = OneSampleHypothesisTesting(
                        data = [1, 2, 5, 8, 10],
                        null_population_mean = 3.5
                ).calculate_ci()

Finally, you can create a plot with the CI and save it to a local path.

        from hypothesis_testing_tool.presentation.create_plots import create_one_sample_hypothesis_plot

        ci_dict = OneSampleHypothesisTesting(
                        data = [1, 2, 5, 8, 10],
                        null_population_mean = 3.5
                ).calculate_ci()

        create_one_sample_hypothesis_plot(path_to_save_plot = "one_sample_plot.png", ci_dict)
