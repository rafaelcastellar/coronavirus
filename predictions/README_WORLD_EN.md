# **Predictions**
For experience, I'm running simple predictions over the cases and deaths per day. As they are time-series, I'm using [Facebook Prophet](https://facebook.github.io/prophet/docs/quick_start.html) that is also designed for this kind of prediction in a very simpler way. It works well for most of the time; sometimes there is a huge leap and it takes more time and more data to be understood.

These predictions were made with Covid19 pandemic data from **2020-05-17**.

As there are many countries to have their data predicted in a row, I selected a few of them plus Brazil to be predicted:
['Brazil', 'Italy', 'United Kingdom', 'Spain', 'US', 'Belgium', 'France'].
***Tip**: you can set yourself at the *[prediction.ipynb](../prediction.ipynb)* notebook which countries you prefer to predict*


## The prediction
As Facebook Prophet predicts time-series data and it is running the prediction over cases per day and deaths per day. After that, I compute theirs cumulatives.It is predicting for the next 10 days.
By the end, a CSV file containing all the predicted data is generated.

#### The Brazil's last 5 days and next predicted 10 days
*predicted? = True* means the line is a prediction; *=False* means they are real numbers.
|    | country   | ds                  |   case_day |   death_day |   cases |   deaths | predicted?   |
|---:|:----------|:--------------------|-----------:|------------:|--------:|---------:|:-------------|
| 77 | Brazil    | 2020-05-13 00:00:00 |      11923 |         779 |  190137 |    13240 | False        |
| 78 | Brazil    | 2020-05-14 00:00:00 |      13028 |         759 |  203165 |    13999 | False        |
| 79 | Brazil    | 2020-05-15 00:00:00 |      17126 |         963 |  220291 |    14962 | False        |
| 80 | Brazil    | 2020-05-16 00:00:00 |      13220 |         700 |  233511 |    15662 | False        |
| 81 | Brazil    | 2020-05-17 00:00:00 |       7569 |         456 |  241080 |    16118 | False        |
| 82 | Brazil    | 2020-05-18 00:00:00 |      10976 |         697 |  252056 |    16815 | True         |
| 83 | Brazil    | 2020-05-19 00:00:00 |      11647 |         787 |  263703 |    17602 | True         |
| 84 | Brazil    | 2020-05-20 00:00:00 |      12730 |         799 |  276433 |    18401 | True         |
| 85 | Brazil    | 2020-05-21 00:00:00 |      12972 |         832 |  289405 |    19233 | True         |
| 86 | Brazil    | 2020-05-22 00:00:00 |      13455 |         861 |  302860 |    20094 | True         |
| 87 | Brazil    | 2020-05-23 00:00:00 |      13168 |         826 |  316028 |    20920 | True         |
| 88 | Brazil    | 2020-05-24 00:00:00 |      12409 |         775 |  328437 |    21695 | True         |
| 89 | Brazil    | 2020-05-25 00:00:00 |      13070 |         822 |  341507 |    22517 | True         |
| 90 | Brazil    | 2020-05-26 00:00:00 |      13742 |         912 |  355249 |    23429 | True         |
| 91 | Brazil    | 2020-05-27 00:00:00 |      14825 |         924 |  370074 |    24353 | True         |

 #### The predicted Brazil's cumulative curves
![](brazil_predictions.png)

Facebook's Prophet automatically generates charts about the behaviour of the analysed and predicted data. That has a good visual information. Here are for the Brazil's prediction:
### Cases
![](brazil_prophet_cases.png)

 ### Deaths
![](brazil_prophet_deaths.png)
#### Finally, the predictions for selected countries for:
**Tomorrow**
|     | country        | ds                  |   case_day |   death_day |   cases |   deaths | predicted?   |
|----:|:---------------|:--------------------|-----------:|------------:|--------:|---------:|:-------------|
|  82 | Brazil         | 2020-05-18 00:00:00 |      10976 |         697 |  252056 |    16815 | True         |
| 108 | Italy          | 2020-05-18 00:00:00 |       3019 |         289 |  228454 |    32197 | True         |
| 108 | United Kingdom | 2020-05-18 00:00:00 |       5368 |         672 |  250363 |    35388 | True         |
| 107 | Spain          | 2020-05-18 00:00:00 |       3801 |         473 |  244524 |    28036 | True         |
| 117 | US             | 2020-05-18 00:00:00 |      30943 |        1945 | 1517700 |    91507 | True         |
| 104 | Belgium        | 2020-05-18 00:00:00 |        839 |         177 |   56119 |     9229 | True         |
| 115 | France         | 2020-05-18 00:00:00 |       2039 |         520 |  181847 |    28631 | True         |

 **The day after tomorrow** 
|     | country        | ds                  |   case_day |   death_day |   cases |   deaths | predicted?   |
|----:|:---------------|:--------------------|-----------:|------------:|--------:|---------:|:-------------|
|  83 | Brazil         | 2020-05-19 00:00:00 |      11647 |         787 |  263703 |    17602 | True         |
| 109 | Italy          | 2020-05-19 00:00:00 |       3056 |         308 |  231510 |    32505 | True         |
| 109 | United Kingdom | 2020-05-19 00:00:00 |       5423 |         861 |  255786 |    36249 | True         |
| 108 | Spain          | 2020-05-19 00:00:00 |       3662 |         457 |  248186 |    28493 | True         |
| 118 | US             | 2020-05-19 00:00:00 |      32025 |        2244 | 1549725 |    93751 | True         |
| 105 | Belgium        | 2020-05-19 00:00:00 |        792 |         203 |   56911 |     9432 | True         |
| 116 | France         | 2020-05-19 00:00:00 |       2176 |         573 |  184023 |    29204 | True         |