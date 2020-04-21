# **Predictions**
For experience, I'm running simple predictions over the cases and deaths per day. As they are time-series, I'm using [Facebook Prophet](https://facebook.github.io/prophet/docs/quick_start.html) that is also designed for this kind of prediction in a very simpler way. It works well for most of the time; sometimes there is a huge leap and it takes more time and more data to be understood.

These predictions were made with Covid19 pandemic data from **2020-04-20**.

As there are many countries to have their data predicted in a row, I selected a few of them plus Brazil to be predicted:
['Brazil', 'Italy', 'United Kingdom', 'Spain', 'US', 'Belgium', 'France'].
***Tip**: you can set yourself at the *[prediction.ipynb](../prediction.ipynb)* notebook which countries you prefer to predict*


## The prediction
As Facebook Prophet predicts time-series data and it is running the prediction over cases per day and deaths per day. After that, I compute theirs cumulatives.It is predicting for the next 10 days.
By the end, a CSV file containing all the predicted data is generated.

#### The Brazil's last 5 days and next predicted 10 days
*predicted? = True* means the line is a prediction; *=False* means they are real numbers.
|    | country   | ds                  |   case_day |   death_day |   cases |   deaths | predicted?   |
|---:|:----------|:--------------------|-----------:|------------:|--------:|---------:|:-------------|
| 50 | Brazil    | 2020-04-16 00:00:00 |       2105 |         188 |   30425 |     1924 | False        |
| 51 | Brazil    | 2020-04-17 00:00:00 |       3257 |         217 |   33682 |     2141 | False        |
| 52 | Brazil    | 2020-04-18 00:00:00 |       2976 |         213 |   36658 |     2354 | False        |
| 53 | Brazil    | 2020-04-19 00:00:00 |       1996 |         108 |   38654 |     2462 | False        |
| 54 | Brazil    | 2020-04-20 00:00:00 |       2089 |         125 |   40743 |     2587 | False        |
| 55 | Brazil    | 2020-04-21 00:00:00 |       2468 |         172 |   43211 |     2759 | True         |
| 56 | Brazil    | 2020-04-22 00:00:00 |       2708 |         178 |   45919 |     2937 | True         |
| 57 | Brazil    | 2020-04-23 00:00:00 |       2634 |         183 |   48553 |     3120 | True         |
| 58 | Brazil    | 2020-04-24 00:00:00 |       2728 |         179 |   51281 |     3299 | True         |
| 59 | Brazil    | 2020-04-25 00:00:00 |       2692 |         182 |   53973 |     3481 | True         |
| 60 | Brazil    | 2020-04-26 00:00:00 |       2592 |         170 |   56565 |     3651 | True         |
| 61 | Brazil    | 2020-04-27 00:00:00 |       2608 |         178 |   59173 |     3829 | True         |
| 62 | Brazil    | 2020-04-28 00:00:00 |       2960 |         206 |   62133 |     4035 | True         |
| 63 | Brazil    | 2020-04-29 00:00:00 |       3200 |         212 |   65333 |     4247 | True         |
| 64 | Brazil    | 2020-04-30 00:00:00 |       3126 |         217 |   68459 |     4464 | True         |

 #### The predicted Brazil's cumulative curves
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
| 55 | Brazil         | 2020-04-21 00:00:00 |       2468 |         172 |   43211 |     2759 | True         |
| 81 | Italy          | 2020-04-21 00:00:00 |       4943 |         771 |  186171 |    24885 | True         |
| 81 | United Kingdom | 2020-04-21 00:00:00 |       6172 |         885 |  132028 |    17435 | True         |
| 80 | Spain          | 2020-04-21 00:00:00 |       6226 |         686 |  206436 |    21538 | True         |
| 90 | US             | 2020-04-21 00:00:00 |      36162 |        2625 |  820488 |    44719 | True         |
| 77 | Belgium        | 2020-04-21 00:00:00 |       1443 |         338 |   41426 |     6166 | True         |
| 88 | France         | 2020-04-21 00:00:00 |       5356 |         886 |  161836 |    21178 | True         |

 **The day after tomorrow** 
|    | country        | ds                  |   case_day |   death_day |   cases |   deaths | predicted?   |
|---:|:---------------|:--------------------|-----------:|------------:|--------:|---------:|:-------------|
| 56 | Brazil         | 2020-04-22 00:00:00 |       2708 |         178 |   45919 |     2937 | True         |
| 82 | Italy          | 2020-04-22 00:00:00 |       5248 |         762 |  191419 |    25647 | True         |
| 82 | United Kingdom | 2020-04-22 00:00:00 |       6515 |         923 |  138543 |    18358 | True         |
| 81 | Spain          | 2020-04-22 00:00:00 |       7054 |         761 |  213490 |    22299 | True         |
| 91 | US             | 2020-04-22 00:00:00 |      36937 |        2691 |  857425 |    47410 | True         |
| 78 | Belgium        | 2020-04-22 00:00:00 |       1657 |         323 |   43083 |     6489 | True         |
| 89 | France         | 2020-04-22 00:00:00 |       4976 |         907 |  166812 |    22085 | True         |