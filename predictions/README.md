# **Predictions**
For experience, I'm running simple predictions over the cases and deaths per day. As they are time-series, I'm using [Facebook Prophet](https://facebook.github.io/prophet/docs/quick_start.html) that is also designed for this kind of prediction in a very simpler way. It works well for most of the time; sometimes there is a huge leap and it takes sometime more data to be understood.

These predictions were made with Covid19 pandemic data from **2020-04-14**.

As there are many countries to have their data predicted in a row, I selected a few of them plus Brazil to be predicted:
['Brazil', 'Italy', 'United Kingdom', 'Spain', 'US', 'Belgium', 'France'].
***Tip**: you can set yourself at the *[prediction.ipynb](../prediction.ipynb)* notebook which countries you prefer to predict*


## The prediction
As Facebook Prophet predicts time-series data and it is running the prediction over cases per day and deaths per day. After that, I compute theirs cumulatives.It is predicting for the next 10 days.
By the end, a CSV file containing all the predicted data is generated.

#### The Brazil's last 5 days and predicted next 10 days
*predicted? = True* means the line is a prediction; *=False* means they are real numbers.
|    | country   | ds                  |   case_day |   death_day |   cases |   deaths | predicted?   |
|---:|:----------|:--------------------|-----------:|------------:|--------:|---------:|:-------------|
| 44 | Brazil    | 2020-04-10 00:00:00 |       1546 |         107 |   19638 |     1057 | False        |
| 45 | Brazil    | 2020-04-11 00:00:00 |       1089 |          67 |   20727 |     1124 | False        |
| 46 | Brazil    | 2020-04-12 00:00:00 |       1465 |          99 |   22192 |     1223 | False        |
| 47 | Brazil    | 2020-04-13 00:00:00 |       1238 |         105 |   23430 |     1328 | False        |
| 48 | Brazil    | 2020-04-14 00:00:00 |       1832 |         204 |   25262 |     1532 | False        |
| 49 | Brazil    | 2020-04-15 00:00:00 |       1609 |         101 |   26871 |     1633 | True         |
| 50 | Brazil    | 2020-04-16 00:00:00 |       1638 |         108 |   28509 |     1741 | True         |
| 51 | Brazil    | 2020-04-17 00:00:00 |       1559 |          98 |   30068 |     1839 | True         |
| 52 | Brazil    | 2020-04-18 00:00:00 |       1536 |         100 |   31604 |     1939 | True         |
| 53 | Brazil    | 2020-04-19 00:00:00 |       1539 |          99 |   33143 |     2038 | True         |
| 54 | Brazil    | 2020-04-20 00:00:00 |       1522 |         105 |   34665 |     2143 | True         |
| 55 | Brazil    | 2020-04-21 00:00:00 |       1848 |         129 |   36513 |     2272 | True         |
| 56 | Brazil    | 2020-04-22 00:00:00 |       1882 |         120 |   38395 |     2392 | True         |
| 57 | Brazil    | 2020-04-23 00:00:00 |       1911 |         127 |   40306 |     2519 | True         |
| 58 | Brazil    | 2020-04-24 00:00:00 |       1832 |         116 |   42138 |     2635 | True         |

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
| 49 | Brazil         | 2020-04-15 00:00:00 |       1609 |         101 |   26871 |     1633 | True         |
| 75 | Italy          | 2020-04-15 00:00:00 |       5461 |         751 |  167949 |    21818 | True         |
| 75 | United Kingdom | 2020-04-15 00:00:00 |       6175 |         961 |  101020 |    13090 | True         |
| 74 | Spain          | 2020-04-15 00:00:00 |       6956 |         745 |  179497 |    18801 | True         |
| 84 | US             | 2020-04-15 00:00:00 |      35850 |        2154 |  641043 |    27911 | True         |
| 71 | Belgium        | 2020-04-15 00:00:00 |       1345 |         306 |   32464 |     4463 | True         |
| 82 | France         | 2020-04-15 00:00:00 |       4552 |         756 |  135913 |    16504 | True         |

 **The day after tomorrow** 
|    | country        | ds                  |   case_day |   death_day |   cases |   deaths | predicted?   |
|---:|:---------------|:--------------------|-----------:|------------:|--------:|---------:|:-------------|
| 50 | Brazil         | 2020-04-16 00:00:00 |       1638 |         108 |   28509 |     1741 | True         |
| 76 | Italy          | 2020-04-16 00:00:00 |       5491 |         741 |  173440 |    22559 | True         |
| 76 | United Kingdom | 2020-04-16 00:00:00 |       6170 |         991 |  107190 |    14081 | True         |
| 75 | Spain          | 2020-04-16 00:00:00 |       6796 |         738 |  186293 |    19539 | True         |
| 85 | US             | 2020-04-16 00:00:00 |      37799 |        2233 |  678842 |    30144 | True         |
| 72 | Belgium        | 2020-04-16 00:00:00 |       1473 |         326 |   33937 |     4789 | True         |
| 83 | France         | 2020-04-16 00:00:00 |       4472 |         934 |  140385 |    17438 | True         |