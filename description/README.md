```python
import sys
import os
sys.path.append(os.path.abspath(os.path.join('..')))
```

<br>
<br>

# Description

<span style="color: #00BFC4;">**A package to run hypothesis testing for one and two samples.**</span>

<br>

## One Sample Hypothesis Testing


```python
from hypothesis_testing_tool.compute_stats.one_sample_statistics import OneSampleTest
```

<br>

<span style="color: #00BFC4;">**Let's see an example of how you can use the `OneSampleTest` class.**</span>



```python
import random

# Set the seed for reproducibility
seed_value = 42
random.seed(seed_value)

random_sample = [random.gauss(mu = 5, sigma = 1) for _ in range(1000)]
```


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

<span style="color: #00BFC4;">**The default is with alternative = "two-sided", but that can change to a one tail test.**</span>


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

<span style="color: #00BFC4;">**You can also compute the confidence interval (default = 95%) for the mean, using the `calculate_ci` method.**</span>

<span style="color: #00BFC4;">**The `calculate_ci` method takes an optional argument `alpha` to adjust to 99% CI (alpha = 0.01) or any other.**</span>



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

<span style="color: #00BFC4;">**Finally, you can create a plot with the CI and save it to a local path.**</span>


```python
from hypothesis_testing_tool.presentation.create_plots import create_one_sample_hypothesis_plot

```


```python
create_one_sample_hypothesis_plot(
    path_to_save_plot = "artifacts/one_sample_plot.png",
    ci_dict = confidence_interval,
    width = 10,
    height = 5
)
```




    (<Figure size 1000x500 with 1 Axes>,
     <Axes: title={'center': '95% Confidence Interval (CI) for the Mean of One Sample'}, xlabel='Values'>)



<img src="https://raw.githubusercontent.com/vamvas/hypothesis-testing-tool/master/description/artifacts/one_sample_plot.png" >

**In the plot above the 95% confidence interval includes 3.5, so we do not reject the null hypothesis.**
