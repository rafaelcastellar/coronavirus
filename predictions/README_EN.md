# **Predictions**
For experience, I'm running simple predictions over the cases and deaths per day. As they are time-series, I'm using [Facebook Prophet](https://facebook.github.io/prophet/docs/quick_start.html) that is also designed for this kind of prediction in a very simpler way. It works well for most of the time; sometimes there is a huge leap and it takes more time and more data to be understood.

These predictions were made with Covid19 pandemic data from **2020-12-04**.

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
| 49 | SP      | 2020-04-15 00:00:00 |       1672 |          83 |   11043 |      778 | False        |
| 50 | SP      | 2020-04-16 00:00:00 |        525 |          75 |   11568 |      853 | False        |
| 51 | SP      | 2020-04-17 00:00:00 |       1273 |          75 |   12841 |      928 | False        |
| 52 | SP      | 2020-04-18 00:00:00 |       1053 |          63 |   13894 |      991 | False        |
| 53 | SP      | 2020-04-19 00:00:00 |        373 |          24 |   14267 |     1015 | False        |
| 54 | SP      | 2020-12-05 00:00:00 |        455 |          34 |   14722 |     1049 | True         |
| 55 | SP      | 2020-12-06 00:00:00 |        327 |          24 |   15049 |     1073 | True         |
| 56 | SP      | 2020-12-07 00:00:00 |        174 |          18 |   15223 |     1091 | True         |
| 57 | SP      | 2020-12-08 00:00:00 |        463 |          34 |   15686 |     1125 | True         |
| 58 | SP      | 2020-12-09 00:00:00 |        461 |          30 |   16147 |     1155 | True         |
| 59 | SP      | 2020-12-10 00:00:00 |        229 |          24 |   16376 |     1179 | True         |
| 60 | SP      | 2020-12-11 00:00:00 |        363 |          27 |   16739 |     1206 | True         |
| 61 | SP      | 2020-12-12 00:00:00 |        458 |          34 |   17197 |     1240 | True         |
| 62 | SP      | 2020-12-13 00:00:00 |        330 |          24 |   17527 |     1264 | True         |
| 63 | SP      | 2020-12-14 00:00:00 |        177 |          18 |   17704 |     1282 | True         |

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
| 31 | PI      | 2020-12-05 00:00:00 |          4 |           0 |     149 |       10 | True         |
| 34 | CE      | 2020-12-05 00:00:00 |        158 |           9 |    3410 |      195 | True         |
| 43 | MG      | 2020-12-05 00:00:00 |         24 |           1 |    1178 |       40 | True         |
| 46 | RJ      | 2020-12-05 00:00:00 |        132 |          11 |    4897 |      413 | True         |
| 54 | SP      | 2020-12-05 00:00:00 |        455 |          34 |   14722 |     1049 | True         |
| 39 | PR      | 2020-12-05 00:00:00 |         65 |           3 |    1052 |       51 | True         |

 **The day after tomorrow** 
|    | state   | ds                  |   case_day |   death_day |   cases |   deaths | predicted?   |
|---:|:--------|:--------------------|-----------:|------------:|--------:|---------:|:-------------|
| 32 | PI      | 2020-12-06 00:00:00 |          6 |           0 |     155 |       10 | True         |
| 35 | CE      | 2020-12-06 00:00:00 |        135 |           7 |    3545 |      202 | True         |
| 44 | MG      | 2020-12-06 00:00:00 |         39 |           0 |    1217 |       40 | True         |
| 47 | RJ      | 2020-12-06 00:00:00 |        127 |           8 |    5024 |      421 | True         |
| 55 | SP      | 2020-12-06 00:00:00 |        327 |          24 |   15049 |     1073 | True         |
| 40 | PR      | 2020-12-06 00:00:00 |         41 |           3 |    1093 |       54 | True         |