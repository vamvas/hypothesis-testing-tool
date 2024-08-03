# A package for conducting one sample and two sample hypothesis testing.

**One Sample Mean**
- p-values (two tailed and one-tailed)
- confidence intervals (with plots for visualising results)

**Two Sample Means**
- p-values (two tailed and one-tailed)

<br>

# **One Sample Hypothesis Testing**


```python
from hypothesis_testing_tool.compute_stats.one_sample_statistics import OneSampleTest
```

<br>

**First let's load some simulated data**


```python
import random

# Set the seed for reproducibility
seed_value = 42
random.seed(seed_value)

random_sample = [random.gauss(mu = 5, sigma = 1) for _ in range(1000)]
```

<br>

**Let's see an example of how you can use the `OneSampleTest` class.**



```python
t_test = OneSampleTest(
        data = random_sample,
        null_population_mean = 3.5
        ).t_test_results

print(f"p-value: {t_test.pvalue:.2f}")
print(f"t-statistic: {t_test.statistic:.2f}")
```

    p-value: 0.00
    t-statistic: 45.96


<br>

**The default is with alternative = "two-sided", but that can change to a one tail test.**


```python
t_test_less = OneSampleTest(
        data = random_sample,
        null_population_mean = 3.5,
        alternative = "less"
        ).t_test_results

print(f"p-value: {t_test_less.pvalue:.2f}")
print(f"t-statistic: {t_test_less.statistic:.2f}")
```

    p-value: 1.00
    t-statistic: 45.96



```python
t_test_greater = OneSampleTest(
        data = random_sample,
        null_population_mean = 3.5,
        alternative = "greater"
        ).t_test_results

print(f"p-value: {t_test_greater.pvalue:.2f}")
print(f"t-statistic: {t_test_greater.statistic:.2f}")
```

    p-value: 0.00
    t-statistic: 45.96


<br>

**You can also compute the confidence interval (default = 95%) for the mean, using the `calculate_ci` method.**

**The `calculate_ci` method takes an optional argument `alpha` to adjust to 99% CI (alpha = 0.01) or any other.**


```python
confidence_interval = OneSampleTest(
        data = random_sample,
        null_population_mean = 3.5
        ).calculate_ci()
confidence_interval
```




    {'lower_bound': 4.918459428969473,
     'point_estimate': 4.9817306915192265,
     'upper_bound': 5.04500195406898,
     'null_population_mean': 3.5}



<br>

**Finally, you can create a plot with the CI and save it to a local path.**

The code should be run using a context manager (`with`) to ensure that the plot closes after execution.


```python
from hypothesis_testing_tool.presentation.create_plots import OneSampleCIPlot

```


```python
with OneSampleCIPlot(confidence_interval, width = 8, height = 4) as plot_instance:
        plot_instance.save_plot("artifacts/one_sample_plot.png")
        plot_instance.show_plot()

```

<img src="https://raw.githubusercontent.com/vamvas/hypothesis-testing-tool/master/description/artifacts/one_sample_plot.png" >

**In the plot above the 95% confidence interval includes 3.5, so we do not reject the null hypothesis.**

<br>

# **Two Sample Hypothesis Testing**


```python
from hypothesis_testing_tool.compute_stats.two_sample_statistics import TwoSampleTest
```


```python
import random

# Set the seed for reproducibility
seed_value = 42
random.seed(seed_value)

data_a = [random.gauss(mu = 5, sigma = 1) for _ in range(1000)]
data_b = [random.gauss(mu = 6, sigma = 1) for _ in range(1000)]
```

<br>

**For the two sample hypothesis test, a user must specify if the variances in the two groups are equal (default) or not**
- If `eqaul_var = True`, the Independent two-sample t-test is executed
- If `eqaul_var = False`, the Welch t-test is executed


```python
t_test = TwoSampleTest(
        group_a = data_a,
        group_b = data_b
        ).t_test_results

print(f"p-value: {t_test.pvalue:.2f}")
print(f"t-statistic: {t_test.statistic:.2f}")
```

    p-value: 0.00
    t-statistic: -22.23



```python
t_test = TwoSampleTest(
        group_a = data_a,
        group_b = data_b,
        equal_var=False
        ).t_test_results

print(f"p-value: {t_test.pvalue:.2f}")
print(f"t-statistic: {t_test.statistic:.2f}")
```

    p-value: 0.00
    t-statistic: -22.23


<br>

**The default is with alternative = "two-sided", but that can change to a one tail test.**


```python
t_test = TwoSampleTest(
        group_a = data_a,
        group_b = data_b,
        alternative = "greater"
        ).t_test_results

print(f"p-value: {t_test.pvalue:.2f}")
print(f"t-statistic: {t_test.statistic:.2f}")
```

    p-value: 1.00
    t-statistic: -22.23
