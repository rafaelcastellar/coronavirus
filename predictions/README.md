# **Predictions**
For experience, I'm running simple predictions over the cases and deaths per day. As they are time-series, I'm using [Facebook Prophet](https://facebook.github.io/prophet/docs/quick_start.html) that is also designed for this kind of prediction in a very simpler way. It works well for most of the time; sometimes there is a huge leap and it takes sometime more data to be understood.

These predictions were made with Covid19 pandemic data from **2020-04-07**.

As there are many countries to have their data predicted in a row, I selected a few of them plus Brazil to be predicted:
['Brazil', 'Italy', 'United Kingdom', 'Spain', 'US', 'China', 'France'].
***Tip**: you can set yourself at the *[prediction.ipynb](../prediction.ipynb)* notebook which countries you prefer to predict*


## The prediction
As Facebook Prophet predicts time-series data and it is running the prediction over cases per day and deaths per day. After that, I compute theirs cumulatives.It is predicting for the next 10 days.
By the end, a CSV file containing all the predicted data is generated.

#### The Brazil's prediction for the next 10 days
|    | country   | ds                  |   case_day |   death_day |   cases |   deaths | predicted?   |
|---:|:----------|:--------------------|-----------:|------------:|--------:|---------:|:-------------|
| 42 | Brazil    | 2020-04-08 00:00:00 |       1013 |          50 |   15047 |      736 | True         |
| 43 | Brazil    | 2020-04-09 00:00:00 |       1082 |          59 |   16129 |      795 | True         |
| 44 | Brazil    | 2020-04-10 00:00:00 |       1053 |          51 |   17182 |      846 | True         |
| 45 | Brazil    | 2020-04-11 00:00:00 |       1102 |          60 |   18284 |      906 | True         |
| 46 | Brazil    | 2020-04-12 00:00:00 |       1043 |          54 |   19327 |      960 | True         |
| 47 | Brazil    | 2020-04-13 00:00:00 |       1061 |          60 |   20388 |     1020 | True         |
| 48 | Brazil    | 2020-04-14 00:00:00 |       1342 |          71 |   21730 |     1091 | True         |
| 49 | Brazil    | 2020-04-15 00:00:00 |       1232 |          62 |   22962 |     1153 | True         |
| 50 | Brazil    | 2020-04-16 00:00:00 |       1301 |          71 |   24263 |     1224 | True         |
| 51 | Brazil    | 2020-04-17 00:00:00 |       1272 |          63 |   25535 |     1287 | True         |

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
| 42 | Brazil         | 2020-04-08 00:00:00 |       1013 |          50 |   15047 |      736 | True         |
| 68 | Italy          | 2020-04-08 00:00:00 |       5421 |         729 |  141007 |    17856 | True         |
| 68 | United Kingdom | 2020-04-08 00:00:00 |       4814 |         302 |   60763 |     6473 | True         |
| 67 | Spain          | 2020-04-08 00:00:00 |       7786 |         683 |  149728 |    14728 | True         |
| 77 | US             | 2020-04-08 00:00:00 |      34827 |        1510 |  431050 |    14232 | True         |
| 77 | China          | 2020-04-08 00:00:00 |      -1142 |         -12 |   81576 |     3323 | True         |
| 75 | France         | 2020-04-08 00:00:00 |       5938 |         777 |  116003 |    11120 | True         |

 **The day after tomorrow** 
|    | country        | ds                  |   case_day |   death_day |   cases |   deaths | predicted?   |
|---:|:---------------|:--------------------|-----------:|------------:|--------:|---------:|:-------------|
| 43 | Brazil         | 2020-04-09 00:00:00 |       1082 |          59 |   16129 |      795 | True         |
| 69 | Italy          | 2020-04-09 00:00:00 |       5414 |         710 |  146421 |    18566 | True         |
| 69 | United Kingdom | 2020-04-09 00:00:00 |       4934 |         316 |   65697 |     6789 | True         |
| 68 | Spain          | 2020-04-09 00:00:00 |       7810 |         685 |  157538 |    15413 | True         |
| 78 | US             | 2020-04-09 00:00:00 |      37344 |        1615 |  468394 |    15847 | True         |
| 78 | China          | 2020-04-09 00:00:00 |        252 |           8 |   81828 |     3331 | True         |
| 76 | France         | 2020-04-09 00:00:00 |       5830 |         904 |  121833 |    12024 | True         |