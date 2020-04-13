# **Predictions**
For experience, I'm running simple predictions over the cases and deaths per day. As they are time-series, I'm using [Facebook Prophet](https://facebook.github.io/prophet/docs/quick_start.html) that is also designed for this kind of prediction in a very simpler way. It works well for most of the time; sometimes there is a huge leap and it takes sometime more data to be understood.

These predictions were made with Covid19 pandemic data from **2020-04-12**.

As there are many countries to have their data predicted in a row, I selected a few of them plus Brazil to be predicted:
['Brazil', 'Italy', 'United Kingdom', 'Spain', 'US', 'China', 'France'].
***Tip**: you can set yourself at the *[prediction.ipynb](../prediction.ipynb)* notebook which countries you prefer to predict*


## The prediction
As Facebook Prophet predicts time-series data and it is running the prediction over cases per day and deaths per day. After that, I compute theirs cumulatives.It is predicting for the next 10 days.
By the end, a CSV file containing all the predicted data is generated.

#### The Brazil's last 5 days and predicted next 10 days
*predicted? = True* means the line is a prediction; *=False* means they are real numbers.
|    | country   | ds                  |   case_day |   death_day |   cases |   deaths | predicted?   |
|---:|:----------|:--------------------|-----------:|------------:|--------:|---------:|:-------------|
| 42 | Brazil    | 2020-04-08 00:00:00 |       2136 |         133 |   16170 |      819 | False        |
| 43 | Brazil    | 2020-04-09 00:00:00 |       1922 |         131 |   18092 |      950 | False        |
| 44 | Brazil    | 2020-04-10 00:00:00 |       1546 |         107 |   19638 |     1057 | False        |
| 45 | Brazil    | 2020-04-11 00:00:00 |       1089 |          67 |   20727 |     1124 | False        |
| 46 | Brazil    | 2020-04-12 00:00:00 |       1465 |          99 |   22192 |     1223 | False        |
| 47 | Brazil    | 2020-04-13 00:00:00 |       1232 |          75 |   23424 |     1298 | True         |
| 48 | Brazil    | 2020-04-14 00:00:00 |       1513 |          87 |   24937 |     1385 | True         |
| 49 | Brazil    | 2020-04-15 00:00:00 |       1588 |          92 |   26525 |     1477 | True         |
| 50 | Brazil    | 2020-04-16 00:00:00 |       1616 |          99 |   28141 |     1576 | True         |
| 51 | Brazil    | 2020-04-17 00:00:00 |       1537 |          88 |   29678 |     1664 | True         |
| 52 | Brazil    | 2020-04-18 00:00:00 |       1514 |          90 |   31192 |     1754 | True         |
| 53 | Brazil    | 2020-04-19 00:00:00 |       1517 |          90 |   32709 |     1844 | True         |
| 54 | Brazil    | 2020-04-20 00:00:00 |       1500 |          92 |   34209 |     1936 | True         |
| 55 | Brazil    | 2020-04-21 00:00:00 |       1781 |         103 |   35990 |     2039 | True         |
| 56 | Brazil    | 2020-04-22 00:00:00 |       1856 |         108 |   37846 |     2147 | True         |

 #### The predicted Brazil's cumulative curves
The prediction are over the daily data, so, here they were cumulated and plotted with the actual data:
![](brazil_predictions.png)

Facebook's Prophet automatically generates charts about the behaviour of the analysed and predicted data. That has a good visual information. Here are for the Brazil's prediction:
### Cases
![](brazil_prophet_cases.png)

 ### Deaths
![](brazil_prophet_deaths.png)
#### Finally, the predictions for selected countries for:
**Tomorrow**
|    | country        | ds                  |   case_day |   death_day |   cases |   deaths | predicted?   |
|---:|:---------------|:--------------------|-----------:|------------:|--------:|---------:|:-------------|
| 47 | Brazil         | 2020-04-13 00:00:00 |       1232 |          75 |   23424 |     1298 | True         |
| 73 | Italy          | 2020-04-13 00:00:00 |       5320 |         750 |  161683 |    20649 | True         |
| 73 | United Kingdom | 2020-04-13 00:00:00 |       5862 |         904 |   91068 |    11533 | True         |
| 72 | Spain          | 2020-04-13 00:00:00 |       6751 |         730 |  173582 |    17939 | True         |
| 82 | US             | 2020-04-13 00:00:00 |      37260 |        2011 |  592573 |    24031 | True         |
| 82 | China          | 2020-04-13 00:00:00 |       -759 |           4 |   82375 |     3347 | True         |
| 80 | France         | 2020-04-13 00:00:00 |       5863 |         843 |  139533 |    15255 | True         |

 **The day after tomorrow** 
|    | country        | ds                  |   case_day |   death_day |   cases |   deaths | predicted?   |
|---:|:---------------|:--------------------|-----------:|------------:|--------:|---------:|:-------------|
| 48 | Brazil         | 2020-04-14 00:00:00 |       1513 |          87 |   24937 |     1385 | True         |
| 74 | Italy          | 2020-04-14 00:00:00 |       5272 |         771 |  166955 |    21420 | True         |
| 74 | United Kingdom | 2020-04-14 00:00:00 |       6056 |         986 |   97124 |    12519 | True         |
| 73 | Spain          | 2020-04-14 00:00:00 |       6615 |         724 |  180197 |    18663 | True         |
| 83 | US             | 2020-04-14 00:00:00 |      38555 |        2187 |  631128 |    26218 | True         |
| 83 | China          | 2020-04-14 00:00:00 |       -547 |           1 |   81828 |     3348 | True         |
| 81 | France         | 2020-04-14 00:00:00 |       6538 |         919 |  146071 |    16174 | True         |