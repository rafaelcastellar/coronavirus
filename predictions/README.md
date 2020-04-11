# **Predictions**
For experience, I'm running simple predictions over the cases and deaths per day. As they are time-series, I'm using [Facebook Prophet](https://facebook.github.io/prophet/docs/quick_start.html) that is also designed for this kind of prediction in a very simpler way. It works well for most of the time; sometimes there is a huge leap and it takes sometime more data to be understood.

These predictions were made with Covid19 pandemic data from **2020-04-10**.

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
| 40 | Brazil    | 2020-04-06 00:00:00 |       1031 |          78 |   12161 |      564 | False        |
| 41 | Brazil    | 2020-04-07 00:00:00 |       1873 |         122 |   14034 |      686 | False        |
| 42 | Brazil    | 2020-04-08 00:00:00 |       2136 |         133 |   16170 |      819 | False        |
| 43 | Brazil    | 2020-04-09 00:00:00 |       1922 |         131 |   18092 |      950 | False        |
| 44 | Brazil    | 2020-04-10 00:00:00 |       1546 |         107 |   19638 |     1057 | False        |
| 45 | Brazil    | 2020-04-11 00:00:00 |       1269 |          74 |   20907 |     1131 | True         |
| 46 | Brazil    | 2020-04-12 00:00:00 |       1210 |          69 |   22117 |     1200 | True         |
| 47 | Brazil    | 2020-04-13 00:00:00 |       1228 |          74 |   23345 |     1274 | True         |
| 48 | Brazil    | 2020-04-14 00:00:00 |       1509 |          85 |   24854 |     1359 | True         |
| 49 | Brazil    | 2020-04-15 00:00:00 |       1583 |          91 |   26437 |     1450 | True         |
| 50 | Brazil    | 2020-04-16 00:00:00 |       1612 |          98 |   28049 |     1548 | True         |
| 51 | Brazil    | 2020-04-17 00:00:00 |       1533 |          87 |   29582 |     1635 | True         |
| 52 | Brazil    | 2020-04-18 00:00:00 |       1536 |          90 |   31118 |     1725 | True         |
| 53 | Brazil    | 2020-04-19 00:00:00 |       1477 |          85 |   32595 |     1810 | True         |
| 54 | Brazil    | 2020-04-20 00:00:00 |       1495 |          90 |   34090 |     1900 | True         |

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
| 45 | Brazil         | 2020-04-11 00:00:00 |       1269 |          74 |   20907 |     1131 | True         |
| 71 | Italy          | 2020-04-11 00:00:00 |       5880 |         778 |  153457 |    19627 | True         |
| 71 | United Kingdom | 2020-04-11 00:00:00 |       5669 |         914 |   80274 |     9888 | True         |
| 70 | Spain          | 2020-04-11 00:00:00 |       6843 |         849 |  165116 |    16930 | True         |
| 80 | US             | 2020-04-11 00:00:00 |      38445 |        2039 |  534980 |    20625 | True         |
| 80 | China          | 2020-04-11 00:00:00 |       -777 |          11 |   82164 |     3351 | True         |
| 78 | France         | 2020-04-11 00:00:00 |       8099 |         942 |  134030 |    14157 | True         |

 **The day after tomorrow** 
|    | country        | ds                  |   case_day |   death_day |   cases |   deaths | predicted?   |
|---:|:---------------|:--------------------|-----------:|------------:|--------:|---------:|:-------------|
| 46 | Brazil         | 2020-04-12 00:00:00 |       1210 |          69 |   22117 |     1200 | True         |
| 72 | Italy          | 2020-04-12 00:00:00 |       5727 |         764 |  159184 |    20391 | True         |
| 72 | United Kingdom | 2020-04-12 00:00:00 |       5956 |         933 |   86230 |    10821 | True         |
| 71 | Spain          | 2020-04-12 00:00:00 |       6508 |         860 |  171624 |    17790 | True         |
| 81 | US             | 2020-04-12 00:00:00 |      39076 |        2122 |  574056 |    22747 | True         |
| 81 | China          | 2020-04-12 00:00:00 |       -596 |          -5 |   81568 |     3346 | True         |
| 79 | France         | 2020-04-12 00:00:00 |       5831 |         913 |  139861 |    15070 | True         |