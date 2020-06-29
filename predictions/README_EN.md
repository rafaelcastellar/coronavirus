# **Predictions**
For experience, I'm running simple predictions over the cases and deaths per day. As they are time-series, I'm using [Facebook Prophet](https://facebook.github.io/prophet/docs/quick_start.html) that is also designed for this kind of prediction in a very simpler way. It works well for most of the time; sometimes there is a huge leap and it takes more time and more data to be understood.

These predictions were made with Covid19 pandemic data from **2020-04-29**.

As there are many states to have their data predicted in a row, I selected a few of them plus São Paulo to be predicted:
['PI', 'CE', 'AM', 'RJ', 'SP', 'PR'].
***Tip**: you can set yourself at the *[prediction.ipynb](../prediction.ipynb)* notebook which states you prefer to predict*


## The prediction
As Facebook Prophet predicts time-series data and it is running the prediction over cases per day and deaths per day. After that, I compute theirs cumulatives.It is predicting for the next 10 days.
By the end, a CSV file containing all the predicted data is generated.

#### The São Paulo's last 5 days and next predicted 10 days
*predicted? = True* means the line is a prediction; *=False* means they are real numbers.
|    | state   | ds                  |   case_day |   death_day |   cases |   deaths | predicted?   |
|---:|:--------|:--------------------|-----------:|------------:|--------:|---------:|:-------------|
| 59 | SP      | 2020-04-25 00:00:00 |       2178 |         155 |   20004 |     1667 | False        |
| 60 | SP      | 2020-04-26 00:00:00 |        711 |          33 |   20715 |     1700 | False        |
| 61 | SP      | 2020-04-27 00:00:00 |        981 |         125 |   21696 |     1825 | False        |
| 62 | SP      | 2020-04-28 00:00:00 |       2345 |         224 |   24041 |     2049 | False        |
| 63 | SP      | 2020-04-29 00:00:00 |       2117 |         198 |   26158 |     2247 | False        |
| 64 | SP      | 2020-04-30 00:00:00 |       1111 |         118 |   27269 |     2365 | True         |
| 65 | SP      | 2020-05-01 00:00:00 |       1227 |         111 |   28496 |     2476 | True         |
| 66 | SP      | 2020-05-02 00:00:00 |       1246 |         108 |   29742 |     2584 | True         |
| 67 | SP      | 2020-05-03 00:00:00 |        997 |          88 |   30739 |     2672 | True         |
| 68 | SP      | 2020-05-04 00:00:00 |        998 |          99 |   31737 |     2771 | True         |
| 69 | SP      | 2020-05-05 00:00:00 |       1383 |         127 |   33120 |     2898 | True         |
| 70 | SP      | 2020-05-06 00:00:00 |       1481 |         124 |   34601 |     3022 | True         |
| 71 | SP      | 2020-05-07 00:00:00 |       1269 |         133 |   35870 |     3155 | True         |
| 72 | SP      | 2020-05-08 00:00:00 |       1385 |         126 |   37255 |     3281 | True         |
| 73 | SP      | 2020-05-09 00:00:00 |       1404 |         123 |   38659 |     3404 | True         |

 #### The predicted São Paulo's cumulative curves
![](brazil_predictions.png)

Facebook's Prophet automatically generates charts about the behaviour of the analysed and predicted data. That has a good visual information. Here are for the São Paulo's prediction:
### Cases
![](brazil_prophet_cases.png)

 ### Deaths
![](brazil_prophet_deaths.png)
#### Finally, the predictions for selected states for:
**Tomorrow**
|    | state   | ds                  |   case_day |   death_day |   cases |   deaths | predicted?   |
|---:|:--------|:--------------------|-----------:|------------:|--------:|---------:|:-------------|
| 41 | PI      | 2020-04-30 00:00:00 |         27 |           0 |     481 |       24 | True         |
| 44 | CE      | 2020-04-30 00:00:00 |        469 |          29 |    7736 |      470 | True         |
| 46 | AM      | 2020-04-30 00:00:00 |        296 |          24 |    5097 |      404 | True         |
| 56 | RJ      | 2020-04-30 00:00:00 |        450 |          42 |    9319 |      836 | True         |
| 64 | SP      | 2020-04-30 00:00:00 |       1111 |         118 |   27269 |     2365 | True         |
| 49 | PR      | 2020-04-30 00:00:00 |         53 |           4 |    1401 |       86 | True         |

 **The day after tomorrow** 
|    | state   | ds                  |   case_day |   death_day |   cases |   deaths | predicted?   |
|---:|:--------|:--------------------|-----------:|------------:|--------:|---------:|:-------------|
| 42 | PI      | 2020-05-01 00:00:00 |         33 |           1 |     514 |       25 | True         |
| 45 | CE      | 2020-05-01 00:00:00 |        387 |          26 |    8123 |      496 | True         |
| 47 | AM      | 2020-05-01 00:00:00 |        265 |          24 |    5362 |      428 | True         |
| 57 | RJ      | 2020-05-01 00:00:00 |        403 |          42 |    9722 |      878 | True         |
| 65 | SP      | 2020-05-01 00:00:00 |       1227 |         111 |   28496 |     2476 | True         |
| 50 | PR      | 2020-05-01 00:00:00 |         53 |           4 |    1454 |       90 | True         |