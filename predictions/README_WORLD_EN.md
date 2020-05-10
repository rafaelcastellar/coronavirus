# **Predictions**
For experience, I'm running simple predictions over the cases and deaths per day. As they are time-series, I'm using [Facebook Prophet](https://facebook.github.io/prophet/docs/quick_start.html) that is also designed for this kind of prediction in a very simpler way. It works well for most of the time; sometimes there is a huge leap and it takes more time and more data to be understood.

These predictions were made with Covid19 pandemic data from **2020-05-09**.

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
| 69 | Brazil    | 2020-05-05 00:00:00 |       6835 |         571 |  115455 |     7938 | False        |
| 70 | Brazil    | 2020-05-06 00:00:00 |      11156 |         650 |  126611 |     8588 | False        |
| 71 | Brazil    | 2020-05-07 00:00:00 |       9162 |         602 |  135773 |     9190 | False        |
| 72 | Brazil    | 2020-05-08 00:00:00 |      11121 |         827 |  146894 |    10017 | False        |
| 73 | Brazil    | 2020-05-09 00:00:00 |       9167 |         639 |  156061 |    10656 | False        |
| 74 | Brazil    | 2020-05-10 00:00:00 |       8329 |         518 |  164390 |    11174 | True         |
| 75 | Brazil    | 2020-05-11 00:00:00 |       8744 |         542 |  173134 |    11716 | True         |
| 76 | Brazil    | 2020-05-12 00:00:00 |       9298 |         611 |  182432 |    12327 | True         |
| 77 | Brazil    | 2020-05-13 00:00:00 |      10133 |         626 |  192565 |    12953 | True         |
| 78 | Brazil    | 2020-05-14 00:00:00 |      10283 |         662 |  202848 |    13615 | True         |
| 79 | Brazil    | 2020-05-15 00:00:00 |      10423 |         674 |  213271 |    14289 | True         |
| 80 | Brazil    | 2020-05-16 00:00:00 |      10469 |         657 |  223740 |    14946 | True         |
| 81 | Brazil    | 2020-05-17 00:00:00 |      10312 |         627 |  234052 |    15573 | True         |
| 82 | Brazil    | 2020-05-18 00:00:00 |      10726 |         651 |  244778 |    16224 | True         |
| 83 | Brazil    | 2020-05-19 00:00:00 |      11281 |         720 |  256059 |    16944 | True         |

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
|  74 | Brazil         | 2020-05-10 00:00:00 |       8329 |         518 |  164390 |    11174 | True         |
| 100 | Italy          | 2020-05-10 00:00:00 |       3918 |         571 |  222186 |    30966 | True         |
| 100 | United Kingdom | 2020-05-10 00:00:00 |       6085 |         732 |  222610 |    32394 | True         |
|  99 | Spain          | 2020-05-10 00:00:00 |       4492 |         566 |  237943 |    27044 | True         |
| 109 | US             | 2020-05-10 00:00:00 |      33260 |        2044 | 1342810 |    80839 | True         |
|  96 | Belgium        | 2020-05-10 00:00:00 |       1277 |         214 |   53873 |     8795 | True         |
| 107 | France         | 2020-05-10 00:00:00 |       4634 |         508 |  182446 |    26821 | True         |

 **The day after tomorrow** 
|     | country        | ds                  |   case_day |   death_day |   cases |   deaths | predicted?   |
|----:|:---------------|:--------------------|-----------:|------------:|--------:|---------:|:-------------|
|  75 | Brazil         | 2020-05-11 00:00:00 |       8744 |         542 |  173134 |    11716 | True         |
| 101 | Italy          | 2020-05-11 00:00:00 |       3536 |         595 |  225722 |    31561 | True         |
| 101 | United Kingdom | 2020-05-11 00:00:00 |       5822 |         743 |  228432 |    33137 | True         |
| 100 | Spain          | 2020-05-11 00:00:00 |       4369 |         579 |  242312 |    27623 | True         |
| 110 | US             | 2020-05-11 00:00:00 |      32848 |        2106 | 1375658 |    82945 | True         |
|  97 | Belgium        | 2020-05-11 00:00:00 |       1136 |         209 |   55009 |     9004 | True         |
| 108 | France         | 2020-05-11 00:00:00 |       3685 |         580 |  186131 |    27401 | True         |