# **Predictions**
For experience, I'm running simple predictions over the cases and deaths per day. As they are time-series, I'm using [Facebook Prophet](https://facebook.github.io/prophet/docs/quick_start.html) that is also designed for this kind of prediction in a very simpler way. It works well for most of the time; sometimes there is a huge leap and it takes more time and more data to be understood.

These predictions were made with Covid19 pandemic data from **2020-06-09**.

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
| 100 | Brazil    | 2020-06-05 00:00:00 |      30830 |        1005 |  645771 |    35026 | False        |
| 101 | Brazil    | 2020-06-06 00:00:00 |      27075 |         904 |  672846 |    35930 | False        |
| 102 | Brazil    | 2020-06-07 00:00:00 |      18912 |         525 |  691758 |    36455 | False        |
| 103 | Brazil    | 2020-06-08 00:00:00 |      15654 |         679 |  707412 |    37134 | False        |
| 104 | Brazil    | 2020-06-09 00:00:00 |      32091 |        1272 |  739503 |    38406 | False        |
| 105 | Brazil    | 2020-06-10 00:00:00 |      28156 |        1188 |  767659 |    39594 | True         |
| 106 | Brazil    | 2020-06-11 00:00:00 |      28955 |        1247 |  796614 |    40841 | True         |
| 107 | Brazil    | 2020-06-12 00:00:00 |      29662 |        1223 |  826276 |    42064 | True         |
| 108 | Brazil    | 2020-06-13 00:00:00 |      29472 |        1174 |  855748 |    43238 | True         |
| 109 | Brazil    | 2020-06-14 00:00:00 |      27297 |        1054 |  883045 |    44292 | True         |
| 110 | Brazil    | 2020-06-15 00:00:00 |      27375 |        1124 |  910420 |    45416 | True         |
| 111 | Brazil    | 2020-06-16 00:00:00 |      30719 |        1313 |  941139 |    46729 | True         |
| 112 | Brazil    | 2020-06-17 00:00:00 |      31902 |        1308 |  973041 |    48037 | True         |
| 113 | Brazil    | 2020-06-18 00:00:00 |      32700 |        1367 | 1005741 |    49404 | True         |
| 114 | Brazil    | 2020-06-19 00:00:00 |      33407 |        1343 | 1039148 |    50747 | True         |

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
| 105 | Brazil         | 2020-06-10 00:00:00 |      28156 |        1188 |  767659 |    39594 | True         |
| 131 | Italy          | 2020-06-10 00:00:00 |       -391 |           2 |  235170 |    34045 | True         |
| 131 | United Kingdom | 2020-06-10 00:00:00 |       1761 |         382 |  292757 |    41350 | True         |
| 130 | Spain          | 2020-06-10 00:00:00 |       1992 |         -13 |  244321 |    27123 | True         |
| 140 | US             | 2020-06-10 00:00:00 |      25194 |        1778 | 1998424 |   113472 | True         |
| 127 | Belgium        | 2020-06-10 00:00:00 |         -3 |          24 |   59434 |     9643 | True         |
| 138 | France         | 2020-06-10 00:00:00 |       -114 |          78 |  194120 |    29377 | True         |

 **The day after tomorrow** 
|     | country        | ds                  |   case_day |   death_day |   cases |   deaths | predicted?   |
|----:|:---------------|:--------------------|-----------:|------------:|--------:|---------:|:-------------|
| 106 | Brazil         | 2020-06-11 00:00:00 |      28955 |        1247 |  796614 |    40841 | True         |
| 132 | Italy          | 2020-06-11 00:00:00 |       -289 |         -10 |  234881 |    34035 | True         |
| 132 | United Kingdom | 2020-06-11 00:00:00 |       1855 |         351 |  294612 |    41701 | True         |
| 131 | Spain          | 2020-06-11 00:00:00 |       2055 |         -42 |  246376 |    27081 | True         |
| 141 | US             | 2020-06-11 00:00:00 |      27041 |        1707 | 2025465 |   115179 | True         |
| 128 | Belgium        | 2020-06-11 00:00:00 |         18 |          14 |   59452 |     9657 | True         |
| 139 | France         | 2020-06-11 00:00:00 |        440 |          89 |  194560 |    29466 | True         |