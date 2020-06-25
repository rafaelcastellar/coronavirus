# **Predictions**
For experience, I'm running simple predictions over the cases and deaths per day. As they are time-series, I'm using [Facebook Prophet](https://facebook.github.io/prophet/docs/quick_start.html) that is also designed for this kind of prediction in a very simpler way. It works well for most of the time; sometimes there is a huge leap and it takes more time and more data to be understood.

These predictions were made with Covid19 pandemic data from **2020-06-24**.

As there are many countries to have their data predicted in a row, I selected a few of them plus Brazil to be predicted:
['Brazil', 'Italy', 'United Kingdom', 'Spain', 'US', 'Belgium', 'France'].
***Tip**: you can set yourself at the *[prediction.ipynb](../prediction.ipynb)* notebook which countries you prefer to predict*


## The prediction
As Facebook Prophet predicts time-series data and it is running the prediction over cases per day and deaths per day. After that, I compute theirs cumulatives.It is predicting for the next 10 days.
By the end, a CSV file containing all the predicted data is generated.

#### The Brazil's last 5 days and next predicted 10 days
*predicted? = True* means the line is a prediction; *=False* means they are real numbers.
|     | country   | ds                  |   case_day |   death_day |   cases |   deaths | predicted?   |
|----:|:----------|:--------------------|-----------:|------------:|--------:|---------:|:-------------|
| 115 | Brazil    | 2020-06-20 00:00:00 |      34666 |        1022 | 1067579 |    49976 | False        |
| 116 | Brazil    | 2020-06-21 00:00:00 |      15762 |         615 | 1083341 |    50591 | False        |
| 117 | Brazil    | 2020-06-22 00:00:00 |      23129 |         680 | 1106470 |    51271 | False        |
| 118 | Brazil    | 2020-06-23 00:00:00 |      39436 |        1374 | 1145906 |    52645 | False        |
| 119 | Brazil    | 2020-06-24 00:00:00 |      42725 |        1185 | 1188631 |    53830 | False        |
| 120 | Brazil    | 2020-06-25 00:00:00 |      34966 |        1303 | 1223597 |    55133 | True         |
| 121 | Brazil    | 2020-06-26 00:00:00 |      37189 |        1257 | 1260786 |    56390 | True         |
| 122 | Brazil    | 2020-06-27 00:00:00 |      35564 |        1198 | 1296350 |    57588 | True         |
| 123 | Brazil    | 2020-06-28 00:00:00 |      32246 |        1049 | 1328596 |    58637 | True         |
| 124 | Brazil    | 2020-06-29 00:00:00 |      32939 |        1112 | 1361535 |    59749 | True         |
| 125 | Brazil    | 2020-06-30 00:00:00 |      37657 |        1354 | 1399192 |    61103 | True         |
| 126 | Brazil    | 2020-07-01 00:00:00 |      38967 |        1345 | 1438159 |    62448 | True         |
| 127 | Brazil    | 2020-07-02 00:00:00 |      38528 |        1393 | 1476687 |    63841 | True         |
| 128 | Brazil    | 2020-07-03 00:00:00 |      40751 |        1347 | 1517438 |    65188 | True         |
| 129 | Brazil    | 2020-07-04 00:00:00 |      39125 |        1288 | 1556563 |    66476 | True         |

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
| 120 | Brazil         | 2020-06-25 00:00:00 |      34966 |        1303 | 1223597 |    55133 | True         |
| 146 | Italy          | 2020-06-25 00:00:00 |       -451 |         -58 |  239087 |    34586 | True         |
| 146 | United Kingdom | 2020-06-25 00:00:00 |        739 |         159 |  309491 |    43324 | True         |
| 145 | Spain          | 2020-06-25 00:00:00 |        -70 |         -24 |  247379 |    28303 | True         |
| 155 | US             | 2020-06-25 00:00:00 |      29181 |         942 | 2410550 |   122921 | True         |
| 142 | Belgium        | 2020-06-25 00:00:00 |        -87 |         -10 |   60920 |     9716 | True         |
| 153 | France         | 2020-06-25 00:00:00 |        219 |          11 |  200815 |    29745 | True         |

 **The day after tomorrow** 
|     | country        | ds                  |   case_day |   death_day |   cases |   deaths | predicted?   |
|----:|:---------------|:--------------------|-----------:|------------:|--------:|---------:|:-------------|
| 121 | Brazil         | 2020-06-26 00:00:00 |      37189 |        1257 | 1260786 |    56390 | True         |
| 147 | Italy          | 2020-06-26 00:00:00 |       -516 |         -45 |  238571 |    34541 | True         |
| 147 | United Kingdom | 2020-06-26 00:00:00 |       1142 |         190 |  310633 |    43514 | True         |
| 146 | Spain          | 2020-06-26 00:00:00 |       -319 |          44 |  247060 |    28347 | True         |
| 156 | US             | 2020-06-26 00:00:00 |      29781 |         869 | 2440331 |   123790 | True         |
| 143 | Belgium        | 2020-06-26 00:00:00 |        -59 |          -8 |   60861 |     9708 | True         |
| 154 | France         | 2020-06-26 00:00:00 |       -147 |         -17 |  200668 |    29728 | True         |