# **Predictions**
For experience, I'm running simple predictions over the cases and deaths per day. As they are time-series, I'm using [Facebook Prophet](https://facebook.github.io/prophet/docs/quick_start.html) that is also designed for this kind of prediction in a very simpler way. It works well for most of the time; sometimes there is a huge leap and it takes sometime more data to be understood.

These predictions were made with Covid19 pandemic data from **2020-04-11**.

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
| 41 | Brazil    | 2020-04-07 00:00:00 |       1873 |         122 |   14034 |      686 | False        |
| 42 | Brazil    | 2020-04-08 00:00:00 |       2136 |         133 |   16170 |      819 | False        |
| 43 | Brazil    | 2020-04-09 00:00:00 |       1922 |         131 |   18092 |      950 | False        |
| 44 | Brazil    | 2020-04-10 00:00:00 |       1546 |         107 |   19638 |     1057 | False        |
| 45 | Brazil    | 2020-04-11 00:00:00 |       1089 |          67 |   20727 |     1124 | False        |
| 46 | Brazil    | 2020-04-12 00:00:00 |       1199 |          68 |   21926 |     1192 | True         |
| 47 | Brazil    | 2020-04-13 00:00:00 |       1217 |          74 |   23143 |     1266 | True         |
| 48 | Brazil    | 2020-04-14 00:00:00 |       1498 |          85 |   24641 |     1351 | True         |
| 49 | Brazil    | 2020-04-15 00:00:00 |       1571 |          90 |   26212 |     1441 | True         |
| 50 | Brazil    | 2020-04-16 00:00:00 |       1599 |          97 |   27811 |     1538 | True         |
| 51 | Brazil    | 2020-04-17 00:00:00 |       1520 |          86 |   29331 |     1624 | True         |
| 52 | Brazil    | 2020-04-18 00:00:00 |       1497 |          88 |   30828 |     1712 | True         |
| 53 | Brazil    | 2020-04-19 00:00:00 |       1463 |          84 |   32291 |     1796 | True         |
| 54 | Brazil    | 2020-04-20 00:00:00 |       1481 |          89 |   33772 |     1885 | True         |
| 55 | Brazil    | 2020-04-21 00:00:00 |       1762 |         101 |   35534 |     1986 | True         |

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
| 46 | Brazil         | 2020-04-12 00:00:00 |       1199 |          68 |   21926 |     1192 | True         |
| 72 | Italy          | 2020-04-12 00:00:00 |       5674 |         756 |  157945 |    20224 | True         |
| 72 | United Kingdom | 2020-04-12 00:00:00 |       5955 |         949 |   85829 |    10841 | True         |
| 71 | Spain          | 2020-04-12 00:00:00 |       6427 |         715 |  169454 |    17321 | True         |
| 81 | US             | 2020-04-12 00:00:00 |      37563 |        1993 |  563959 |    22456 | True         |
| 81 | China          | 2020-04-12 00:00:00 |       -569 |          -5 |   82445 |     3338 | True         |
| 79 | France         | 2020-04-12 00:00:00 |       5301 |         844 |  136028 |    14695 | True         |

 **The day after tomorrow** 
|    | country        | ds                  |   case_day |   death_day |   cases |   deaths | predicted?   |
|---:|:---------------|:--------------------|-----------:|------------:|--------:|---------:|:-------------|
| 47 | Brazil         | 2020-04-13 00:00:00 |       1217 |          74 |   23143 |     1266 | True         |
| 73 | Italy          | 2020-04-13 00:00:00 |       5380 |         764 |  163325 |    20988 | True         |
| 73 | United Kingdom | 2020-04-13 00:00:00 |       5975 |         966 |   91804 |    11807 | True         |
| 72 | Spain          | 2020-04-13 00:00:00 |       6872 |         735 |  176326 |    18056 | True         |
| 82 | US             | 2020-04-13 00:00:00 |      38950 |        2068 |  602909 |    24524 | True         |
| 82 | China          | 2020-04-13 00:00:00 |       -795 |           4 |   81650 |     3342 | True         |
| 80 | France         | 2020-04-13 00:00:00 |       6093 |         913 |  142121 |    15608 | True         |