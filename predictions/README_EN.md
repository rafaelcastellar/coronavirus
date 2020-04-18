# **Predictions**
For experience, I'm running simple predictions over the cases and deaths per day. As they are time-series, I'm using [Facebook Prophet](https://facebook.github.io/prophet/docs/quick_start.html) that is also designed for this kind of prediction in a very simpler way. It works well for most of the time; sometimes there is a huge leap and it takes more time and more data to be understood.

These predictions were made with Covid19 pandemic data from **2020-04-17**.

As there are many states to have their data predicted in a row, I selected a few of them plus São Paulo to be predicted:
['PI', 'CE', 'MG', 'RJ', 'SP', 'PR'].
***Tip**: you can set yourself at the *[prediction.ipynb](../prediction.ipynb)* notebook which states you prefer to predict*


## The prediction
As Facebook Prophet predicts time-series data and it is running the prediction over cases per day and deaths per day. After that, I compute theirs cumulatives.It is predicting for the next 10 days.
By the end, a CSV file containing all the predicted data is generated.

#### The São Paulo's last 5 days and next predicted 10 days
*predicted? = True* means the line is a prediction; *=False* means they are real numbers.
|    | state   | ds                  |   case_day |   death_day |   cases |   deaths | predicted?   |
|---:|:--------|:--------------------|-----------:|------------:|--------:|---------:|:-------------|
| 47 | SP      | 2020-04-13 00:00:00 |        140 |          20 |    8895 |      608 | False        |
| 48 | SP      | 2020-04-14 00:00:00 |        476 |          87 |    9371 |      695 | False        |
| 49 | SP      | 2020-04-15 00:00:00 |       1672 |          83 |   11043 |      778 | False        |
| 50 | SP      | 2020-04-16 00:00:00 |        525 |          75 |   11568 |      853 | False        |
| 51 | SP      | 2020-04-17 00:00:00 |       1273 |          75 |   12841 |      928 | False        |
| 52 | SP      | 2020-04-18 00:00:00 |        609 |          48 |   13450 |      976 | True         |
| 53 | SP      | 2020-04-19 00:00:00 |        595 |          46 |   14045 |     1022 | True         |
| 54 | SP      | 2020-04-20 00:00:00 |        566 |          47 |   14611 |     1069 | True         |
| 55 | SP      | 2020-04-21 00:00:00 |        797 |          63 |   15408 |     1132 | True         |
| 56 | SP      | 2020-04-22 00:00:00 |        979 |          64 |   16387 |     1196 | True         |
| 57 | SP      | 2020-04-23 00:00:00 |        803 |          63 |   17190 |     1259 | True         |
| 58 | SP      | 2020-04-24 00:00:00 |        900 |          62 |   18090 |     1321 | True         |
| 59 | SP      | 2020-04-25 00:00:00 |        730 |          58 |   18820 |     1379 | True         |
| 60 | SP      | 2020-04-26 00:00:00 |        716 |          55 |   19536 |     1434 | True         |
| 61 | SP      | 2020-04-27 00:00:00 |        687 |          56 |   20223 |     1490 | True         |

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
| 29 | PI      | 2020-04-18 00:00:00 |          6 |           0 |     108 |        8 | True         |
| 32 | CE      | 2020-04-18 00:00:00 |        175 |          11 |    2859 |      160 | True         |
| 41 | MG      | 2020-04-18 00:00:00 |         51 |           1 |    1072 |       36 | True         |
| 44 | RJ      | 2020-04-18 00:00:00 |        249 |          21 |    4598 |      362 | True         |
| 52 | SP      | 2020-04-18 00:00:00 |        609 |          48 |   13450 |      976 | True         |
| 37 | PR      | 2020-04-18 00:00:00 |         58 |           2 |     932 |       44 | True         |

 **The day after tomorrow** 
|    | state   | ds                  |   case_day |   death_day |   cases |   deaths | predicted?   |
|---:|:--------|:--------------------|-----------:|------------:|--------:|---------:|:-------------|
| 30 | PI      | 2020-04-19 00:00:00 |          7 |           0 |     115 |        8 | True         |
| 33 | CE      | 2020-04-19 00:00:00 |        178 |          11 |    3037 |      171 | True         |
| 42 | MG      | 2020-04-19 00:00:00 |         68 |           2 |    1140 |       38 | True         |
| 45 | RJ      | 2020-04-19 00:00:00 |        267 |          21 |    4865 |      383 | True         |
| 53 | SP      | 2020-04-19 00:00:00 |        595 |          46 |   14045 |     1022 | True         |
| 38 | PR      | 2020-04-19 00:00:00 |         53 |           3 |     985 |       47 | True         |