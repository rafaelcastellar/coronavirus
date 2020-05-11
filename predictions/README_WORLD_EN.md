# **Predictions**
For experience, I'm running simple predictions over the cases and deaths per day. As they are time-series, I'm using [Facebook Prophet](https://facebook.github.io/prophet/docs/quick_start.html) that is also designed for this kind of prediction in a very simpler way. It works well for most of the time; sometimes there is a huge leap and it takes more time and more data to be understood.

These predictions were made with Covid19 pandemic data from **2020-05-10**.

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
| 70 | Brazil    | 2020-05-06 00:00:00 |      11156 |         650 |  126611 |     8588 | False        |
| 71 | Brazil    | 2020-05-07 00:00:00 |       9162 |         602 |  135773 |     9190 | False        |
| 72 | Brazil    | 2020-05-08 00:00:00 |      11121 |         827 |  146894 |    10017 | False        |
| 73 | Brazil    | 2020-05-09 00:00:00 |       9167 |         639 |  156061 |    10656 | False        |
| 74 | Brazil    | 2020-05-10 00:00:00 |       6638 |         467 |  162699 |    11123 | False        |
| 75 | Brazil    | 2020-05-11 00:00:00 |       8399 |         539 |  171098 |    11662 | True         |
| 76 | Brazil    | 2020-05-12 00:00:00 |       8941 |         607 |  180039 |    12269 | True         |
| 77 | Brazil    | 2020-05-13 00:00:00 |       9765 |         622 |  189804 |    12891 | True         |
| 78 | Brazil    | 2020-05-14 00:00:00 |       9894 |         658 |  199698 |    13549 | True         |
| 79 | Brazil    | 2020-05-15 00:00:00 |      10013 |         669 |  209711 |    14218 | True         |
| 80 | Brazil    | 2020-05-16 00:00:00 |      10038 |         654 |  219749 |    14872 | True         |
| 81 | Brazil    | 2020-05-17 00:00:00 |       9706 |         618 |  229455 |    15490 | True         |
| 82 | Brazil    | 2020-05-18 00:00:00 |      10241 |         647 |  239696 |    16137 | True         |
| 83 | Brazil    | 2020-05-19 00:00:00 |      10783 |         715 |  250479 |    16852 | True         |
| 84 | Brazil    | 2020-05-20 00:00:00 |      11607 |         730 |  262086 |    17582 | True         |

 #### The predicted Brazil's cumulative curves
![](brazil_predictions.png)

Facebook's Prophet automatically generates charts about the behaviour of the analysed and predicted data. That has a good visual information. Here are for the Brazil's prediction:
### Cases
![](brazil_prophet_cases.png)

 ### Deaths
![](brazil_prophet_deaths.png)
#### Finally, the predictions for selected countries for:
**Tomorrow**
|     | country        | ds                  |   case_day |   death_day |   cases |   deaths | predicted?   |
|----:|:---------------|:--------------------|-----------:|------------:|--------:|---------:|:-------------|
|  75 | Brazil         | 2020-05-11 00:00:00 |       8399 |         539 |  171098 |    11662 | True         |
| 101 | Italy          | 2020-05-11 00:00:00 |       3556 |         581 |  222626 |    31141 | True         |
| 101 | United Kingdom | 2020-05-11 00:00:00 |       5719 |         726 |  226168 |    32656 | True         |
| 100 | Spain          | 2020-05-11 00:00:00 |       4228 |         543 |  238603 |    27164 | True         |
| 110 | US             | 2020-05-11 00:00:00 |      32430 |        2056 | 1361690 |    81582 | True         |
|  97 | Belgium        | 2020-05-11 00:00:00 |        852 |         205 |   53933 |     8861 | True         |
| 108 | France         | 2020-05-11 00:00:00 |       3525 |         580 |  181649 |    26963 | True         |

 **The day after tomorrow** 
|     | country        | ds                  |   case_day |   death_day |   cases |   deaths | predicted?   |
|----:|:---------------|:--------------------|-----------:|------------:|--------:|---------:|:-------------|
|  76 | Brazil         | 2020-05-12 00:00:00 |       8941 |         607 |  180039 |    12269 | True         |
| 102 | Italy          | 2020-05-12 00:00:00 |       3555 |         610 |  226181 |    31751 | True         |
| 102 | United Kingdom | 2020-05-12 00:00:00 |       5822 |         899 |  231990 |    33555 | True         |
| 101 | Spain          | 2020-05-12 00:00:00 |       4263 |         522 |  242866 |    27686 | True         |
| 111 | US             | 2020-05-12 00:00:00 |      33445 |        2343 | 1395135 |    83925 | True         |
|  98 | Belgium        | 2020-05-12 00:00:00 |        813 |         234 |   54746 |     9095 | True         |
| 109 | France         | 2020-05-12 00:00:00 |       3693 |         633 |  185342 |    27596 | True         |