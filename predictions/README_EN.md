# **Predictions**
For experience, I'm running simple predictions over the cases and deaths per day. As they are time-series, I'm using [Facebook Prophet](https://facebook.github.io/prophet/docs/quick_start.html) that is also designed for this kind of prediction in a very simpler way. It works well for most of the time; sometimes there is a huge leap and it takes more time and more data to be understood.

These predictions were made with Covid19 pandemic data from **2020-04-25**.

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
| 55 | SP      | 2020-04-21 00:00:00 |        805 |          56 |   15385 |     1093 | False        |
| 56 | SP      | 2020-04-22 00:00:00 |        529 |          41 |   15914 |     1134 | False        |
| 57 | SP      | 2020-04-23 00:00:00 |        826 |         211 |   16740 |     1345 | False        |
| 58 | SP      | 2020-04-24 00:00:00 |       1086 |         167 |   17826 |     1512 | False        |
| 59 | SP      | 2020-04-25 00:00:00 |       2178 |         155 |   20004 |     1667 | False        |
| 60 | SP      | 2020-04-26 00:00:00 |        744 |          66 |   20748 |     1733 | True         |
| 61 | SP      | 2020-04-27 00:00:00 |        711 |          67 |   21459 |     1800 | True         |
| 62 | SP      | 2020-04-28 00:00:00 |        974 |          86 |   22433 |     1886 | True         |
| 63 | SP      | 2020-04-29 00:00:00 |       1112 |          86 |   23545 |     1972 | True         |
| 64 | SP      | 2020-04-30 00:00:00 |        988 |         105 |   24533 |     2077 | True         |
| 65 | SP      | 2020-05-01 00:00:00 |       1104 |          99 |   25637 |     2176 | True         |
| 66 | SP      | 2020-05-02 00:00:00 |       1123 |          95 |   26760 |     2271 | True         |
| 67 | SP      | 2020-05-03 00:00:00 |        877 |          79 |   27637 |     2350 | True         |
| 68 | SP      | 2020-05-04 00:00:00 |        845 |          80 |   28482 |     2430 | True         |
| 69 | SP      | 2020-05-05 00:00:00 |       1108 |          98 |   29590 |     2528 | True         |

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
| 37 | PI      | 2020-04-26 00:00:00 |         21 |           0 |     318 |       17 | True         |
| 40 | CE      | 2020-04-26 00:00:00 |        299 |          17 |    5720 |      327 | True         |
| 49 | MG      | 2020-04-26 00:00:00 |         78 |           2 |    1559 |       60 | True         |
| 52 | RJ      | 2020-04-26 00:00:00 |        324 |          29 |    7152 |      644 | True         |
| 60 | SP      | 2020-04-26 00:00:00 |        744 |          66 |   20748 |     1733 | True         |
| 45 | PR      | 2020-04-26 00:00:00 |         49 |           3 |    1189 |       72 | True         |

 **The day after tomorrow** 
|    | state   | ds                  |   case_day |   death_day |   cases |   deaths | predicted?   |
|---:|:--------|:--------------------|-----------:|------------:|--------:|---------:|:-------------|
| 38 | PI      | 2020-04-27 00:00:00 |         20 |           1 |     338 |       18 | True         |
| 41 | CE      | 2020-04-27 00:00:00 |        326 |          19 |    6046 |      346 | True         |
| 50 | MG      | 2020-04-27 00:00:00 |         61 |           3 |    1620 |       63 | True         |
| 53 | RJ      | 2020-04-27 00:00:00 |        318 |          30 |    7470 |      674 | True         |
| 61 | SP      | 2020-04-27 00:00:00 |        711 |          67 |   21459 |     1800 | True         |
| 46 | PR      | 2020-04-27 00:00:00 |         33 |           3 |    1222 |       75 | True         |