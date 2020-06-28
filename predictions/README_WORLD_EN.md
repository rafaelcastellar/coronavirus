# **Predictions**
For experience, I'm running simple predictions over the cases and deaths per day. As they are time-series, I'm using [Facebook Prophet](https://facebook.github.io/prophet/docs/quick_start.html) that is also designed for this kind of prediction in a very simpler way. It works well for most of the time; sometimes there is a huge leap and it takes more time and more data to be understood.

These predictions were made with Covid19 pandemic data from **2020-06-27**.

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
| 118 | Brazil    | 2020-06-23 00:00:00 |      39436 |        1374 | 1145906 |    52645 | False        |
| 119 | Brazil    | 2020-06-24 00:00:00 |      42725 |        1185 | 1188631 |    53830 | False        |
| 120 | Brazil    | 2020-06-25 00:00:00 |      39483 |        1141 | 1228114 |    54971 | False        |
| 121 | Brazil    | 2020-06-26 00:00:00 |      46860 |         990 | 1274974 |    55961 | False        |
| 122 | Brazil    | 2020-06-27 00:00:00 |      38693 |        1109 | 1313667 |    57070 | False        |
| 123 | Brazil    | 2020-06-28 00:00:00 |      33008 |        1028 | 1346675 |    58098 | True         |
| 124 | Brazil    | 2020-06-29 00:00:00 |      33710 |        1091 | 1380385 |    59189 | True         |
| 125 | Brazil    | 2020-06-30 00:00:00 |      38466 |        1333 | 1418851 |    60522 | True         |
| 126 | Brazil    | 2020-07-01 00:00:00 |      39822 |        1323 | 1458673 |    61845 | True         |
| 127 | Brazil    | 2020-07-02 00:00:00 |      39631 |        1362 | 1498304 |    63207 | True         |
| 128 | Brazil    | 2020-07-03 00:00:00 |      42165 |        1310 | 1540469 |    64517 | True         |
| 129 | Brazil    | 2020-07-04 00:00:00 |      40168 |        1261 | 1580637 |    65778 | True         |
| 130 | Brazil    | 2020-07-05 00:00:00 |      36708 |        1115 | 1617345 |    66893 | True         |
| 131 | Brazil    | 2020-07-06 00:00:00 |      37410 |        1178 | 1654755 |    68071 | True         |
| 132 | Brazil    | 2020-07-07 00:00:00 |      42166 |        1420 | 1696921 |    69491 | True         |

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
| 123 | Brazil         | 2020-06-28 00:00:00 |      33008 |        1028 | 1346675 |    58098 | True         |
| 149 | Italy          | 2020-06-28 00:00:00 |       -624 |        -109 |  239640 |    34607 | True         |
| 149 | United Kingdom | 2020-06-28 00:00:00 |        682 |           0 |  312824 |    43598 | True         |
| 148 | Spain          | 2020-06-28 00:00:00 |       -429 |         -68 |  248403 |    28273 | True         |
| 158 | US             | 2020-06-28 00:00:00 |      27897 |         583 | 2538048 |   126122 | True         |
| 145 | Belgium        | 2020-06-28 00:00:00 |        -92 |         -24 |   61117 |     9708 | True         |
| 156 | France         | 2020-06-28 00:00:00 |        423 |         -72 |  202607 |    29709 | True         |

 **The day after tomorrow** 
|     | country        | ds                  |   case_day |   death_day |   cases |   deaths | predicted?   |
|----:|:---------------|:--------------------|-----------:|------------:|--------:|---------:|:-------------|
| 124 | Brazil         | 2020-06-29 00:00:00 |      33710 |        1091 | 1380385 |    59189 | True         |
| 150 | Italy          | 2020-06-29 00:00:00 |       -963 |        -102 |  238677 |    34505 | True         |
| 150 | United Kingdom | 2020-06-29 00:00:00 |        282 |          13 |  313106 |    43611 | True         |
| 149 | Spain          | 2020-06-29 00:00:00 |       -918 |        -154 |  247485 |    28119 | True         |
| 159 | US             | 2020-06-29 00:00:00 |      27734 |         655 | 2565782 |   126777 | True         |
| 146 | Belgium        | 2020-06-29 00:00:00 |       -214 |         -32 |   60903 |     9676 | True         |
| 157 | France         | 2020-06-29 00:00:00 |       -242 |         -35 |  202365 |    29674 | True         |