# **Predictions**
For experience, I'm running simple predictions over the cases and deaths per day. As they are time-series, I'm using [Facebook Prophet](https://facebook.github.io/prophet/docs/quick_start.html) that is also designed for this kind of prediction in a very simpler way. It works well for most of the time; sometimes there is a huge leap and it takes sometime more data to be understood.

These predictions were made with Covid19 pandemic data from **2020-04-13**.

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
| 43 | Brazil    | 2020-04-09 00:00:00 |       1922 |         131 |   18092 |      950 | False        |
| 44 | Brazil    | 2020-04-10 00:00:00 |       1546 |         107 |   19638 |     1057 | False        |
| 45 | Brazil    | 2020-04-11 00:00:00 |       1089 |          67 |   20727 |     1124 | False        |
| 46 | Brazil    | 2020-04-12 00:00:00 |       1465 |          99 |   22192 |     1223 | False        |
| 47 | Brazil    | 2020-04-13 00:00:00 |       1238 |         105 |   23430 |     1328 | False        |
| 48 | Brazil    | 2020-04-14 00:00:00 |       1513 |          88 |   24943 |     1416 | True         |
| 49 | Brazil    | 2020-04-15 00:00:00 |       1588 |          94 |   26531 |     1510 | True         |
| 50 | Brazil    | 2020-04-16 00:00:00 |       1617 |         101 |   28148 |     1611 | True         |
| 51 | Brazil    | 2020-04-17 00:00:00 |       1537 |          90 |   29685 |     1701 | True         |
| 52 | Brazil    | 2020-04-18 00:00:00 |       1515 |          92 |   31200 |     1793 | True         |
| 53 | Brazil    | 2020-04-19 00:00:00 |       1518 |          92 |   32718 |     1885 | True         |
| 54 | Brazil    | 2020-04-20 00:00:00 |       1501 |          98 |   34219 |     1983 | True         |
| 55 | Brazil    | 2020-04-21 00:00:00 |       1781 |         105 |   36000 |     2088 | True         |
| 56 | Brazil    | 2020-04-22 00:00:00 |       1856 |         111 |   37856 |     2199 | True         |
| 57 | Brazil    | 2020-04-23 00:00:00 |       1885 |         118 |   39741 |     2317 | True         |

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
| 48 | Brazil         | 2020-04-14 00:00:00 |       1513 |          88 |   24943 |     1416 | True         |
| 74 | Italy          | 2020-04-14 00:00:00 |       5178 |         764 |  164694 |    21229 | True         |
| 74 | United Kingdom | 2020-04-14 00:00:00 |       5769 |         505 |   95339 |    11852 | True         |
| 73 | Spain          | 2020-04-14 00:00:00 |       6469 |         715 |  176568 |    18471 | True         |
| 83 | US             | 2020-04-14 00:00:00 |      42180 |        2061 |  724799 |    25590 | True         |
| 83 | China          | 2020-04-14 00:00:00 |       -526 |           1 |   82687 |     3346 | True         |
| 81 | France         | 2020-04-14 00:00:00 |       6471 |         884 |  144346 |    15870 | True         |

 **The day after tomorrow** 
|    | country        | ds                  |   case_day |   death_day |   cases |   deaths | predicted?   |
|---:|:---------------|:--------------------|-----------:|------------:|--------:|---------:|:-------------|
| 49 | Brazil         | 2020-04-15 00:00:00 |       1588 |          94 |   26531 |     1510 | True         |
| 75 | Italy          | 2020-04-15 00:00:00 |       5544 |         757 |  170238 |    21986 | True         |
| 75 | United Kingdom | 2020-04-15 00:00:00 |       6235 |         536 |  101574 |    12388 | True         |
| 74 | Spain          | 2020-04-15 00:00:00 |       7114 |         763 |  183682 |    19234 | True         |
| 84 | US             | 2020-04-15 00:00:00 |      43616 |        2130 |  768415 |    27720 | True         |
| 84 | China          | 2020-04-15 00:00:00 |      -1146 |         -18 |   81541 |     3328 | True         |
| 82 | France         | 2020-04-15 00:00:00 |       5676 |         817 |  150022 |    16687 | True         |