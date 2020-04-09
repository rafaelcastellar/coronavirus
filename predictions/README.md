# **Predictions**
For experience, I'm running simple predictions over the cases and deaths per day. As they are time-series, I'm using [Facebook Prophet](https://facebook.github.io/prophet/docs/quick_start.html) that is also designed for this kind of prediction in a very simpler way. It works well for most of the time; sometimes there is a huge leap and it takes sometime more data to be understood.

These predictions were made with Covid19 pandemic data from **2020-04-08**.

As there are many countries to have their data predicted in a row, I selected a few of them plus Brazil to be predicted:
['Brazil', 'Italy', 'United Kingdom', 'Spain', 'US', 'China', 'France'].
***Tip**: you can set yourself at the *[prediction.ipynb](../prediction.ipynb)* notebook which countries you prefer to predict*


## The prediction
As Facebook Prophet predicts time-series data and it is running the prediction over cases per day and deaths per day. After that, I compute theirs cumulatives.It is predicting for the next 10 days.
By the end, a CSV file containing all the predicted data is generated.

#### The Brazil's prediction for the next 10 days
|    | country   | ds                  |   case_day |   death_day |   cases |   deaths | predicted?   |
|---:|:----------|:--------------------|-----------:|------------:|--------:|---------:|:-------------|
| 43 | Brazil    | 2020-04-09 00:00:00 |       1170 |          65 |   17340 |      884 | True         |
| 44 | Brazil    | 2020-04-10 00:00:00 |       1141 |          57 |   18481 |      941 | True         |
| 45 | Brazil    | 2020-04-11 00:00:00 |       1190 |          66 |   19671 |     1007 | True         |
| 46 | Brazil    | 2020-04-12 00:00:00 |       1131 |          61 |   20802 |     1068 | True         |
| 47 | Brazil    | 2020-04-13 00:00:00 |       1149 |          66 |   21951 |     1134 | True         |
| 48 | Brazil    | 2020-04-14 00:00:00 |       1430 |          77 |   23381 |     1211 | True         |
| 49 | Brazil    | 2020-04-15 00:00:00 |       1493 |          82 |   24874 |     1293 | True         |
| 50 | Brazil    | 2020-04-16 00:00:00 |       1414 |          79 |   26288 |     1372 | True         |
| 51 | Brazil    | 2020-04-17 00:00:00 |       1385 |          71 |   27673 |     1443 | True         |
| 52 | Brazil    | 2020-04-18 00:00:00 |       1434 |          80 |   29107 |     1523 | True         |

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
| 43 | Brazil         | 2020-04-09 00:00:00 |       1170 |          65 |   17340 |      884 | True         |
| 69 | Italy          | 2020-04-09 00:00:00 |       5354 |         702 |  144776 |    18371 | True         |
| 69 | United Kingdom | 2020-04-09 00:00:00 |       5058 |         705 |   66532 |     7816 | True         |
| 68 | Spain          | 2020-04-09 00:00:00 |       6735 |         687 |  154955 |    15479 | True         |
| 78 | US             | 2020-04-09 00:00:00 |      36974 |        1631 |  466026 |    16326 | True         |
| 78 | China          | 2020-04-09 00:00:00 |        317 |           8 |   83126 |     3345 | True         |
| 76 | France         | 2020-04-09 00:00:00 |       5566 |         859 |  119525 |    11746 | True         |

 **The day after tomorrow** 
|    | country        | ds                  |   case_day |   death_day |   cases |   deaths | predicted?   |
|---:|:---------------|:--------------------|-----------:|------------:|--------:|---------:|:-------------|
| 44 | Brazil         | 2020-04-10 00:00:00 |       1141 |          57 |   18481 |      941 | True         |
| 70 | Italy          | 2020-04-10 00:00:00 |       6063 |         816 |  150839 |    19187 | True         |
| 70 | United Kingdom | 2020-04-10 00:00:00 |       5467 |         745 |   71999 |     8561 | True         |
| 69 | Spain          | 2020-04-10 00:00:00 |       6770 |         691 |  161725 |    16170 | True         |
| 79 | US             | 2020-04-10 00:00:00 |      38138 |        1706 |  504164 |    18032 | True         |
| 79 | China          | 2020-04-10 00:00:00 |       -460 |          -8 |   82666 |     3337 | True         |
| 77 | France         | 2020-04-10 00:00:00 |       6214 |         864 |  125739 |    12610 | True         |