# **Predictions**
For experience, I'm running simple predictions over the cases and deaths per day. As they are time-series, I'm using [Facebook Prophet](https://facebook.github.io/prophet/docs/quick_start.html) that is also designed for this kind of prediction in a very simpler way. It works well for most of the time; sometimes there is a huge leap and it takes more time and more data to be understood.

These predictions were made with Covid19 pandemic data from **2020-06-13**.

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
| 104 | Brazil    | 2020-06-09 00:00:00 |      32091 |        1272 |  739503 |    38406 | False        |
| 105 | Brazil    | 2020-06-10 00:00:00 |      32913 |        1274 |  772416 |    39680 | False        |
| 106 | Brazil    | 2020-06-11 00:00:00 |      30412 |        1239 |  802828 |    40919 | False        |
| 107 | Brazil    | 2020-06-12 00:00:00 |      25982 |         909 |  828810 |    41828 | False        |
| 108 | Brazil    | 2020-06-13 00:00:00 |      21704 |         892 |  850514 |    42720 | False        |
| 109 | Brazil    | 2020-06-14 00:00:00 |      26722 |        1020 |  877236 |    43740 | True         |
| 110 | Brazil    | 2020-06-15 00:00:00 |      26788 |        1088 |  904024 |    44828 | True         |
| 111 | Brazil    | 2020-06-16 00:00:00 |      30118 |        1276 |  934142 |    46104 | True         |
| 112 | Brazil    | 2020-06-17 00:00:00 |      31573 |        1277 |  965715 |    47381 | True         |
| 113 | Brazil    | 2020-06-18 00:00:00 |      32151 |        1329 |  997866 |    48710 | True         |
| 114 | Brazil    | 2020-06-19 00:00:00 |      32525 |        1285 | 1030391 |    49995 | True         |
| 115 | Brazil    | 2020-06-20 00:00:00 |      32059 |        1237 | 1062450 |    51232 | True         |
| 116 | Brazil    | 2020-06-21 00:00:00 |      30317 |        1132 | 1092767 |    52364 | True         |
| 117 | Brazil    | 2020-06-22 00:00:00 |      30383 |        1201 | 1123150 |    53565 | True         |
| 118 | Brazil    | 2020-06-23 00:00:00 |      33713 |        1388 | 1156863 |    54953 | True         |

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
| 109 | Brazil         | 2020-06-14 00:00:00 |      26722 |        1020 |  877236 |    43740 | True         |
| 135 | Italy          | 2020-06-14 00:00:00 |       -439 |         -43 |  236212 |    34258 | True         |
| 135 | United Kingdom | 2020-06-14 00:00:00 |       1488 |         163 |  297731 |    41910 | True         |
| 134 | Spain          | 2020-06-14 00:00:00 |       1235 |         -92 |  245203 |    27044 | True         |
| 144 | US             | 2020-06-14 00:00:00 |      23707 |         999 | 2098233 |   116435 | True         |
| 131 | Belgium        | 2020-06-14 00:00:00 |        -10 |         -15 |   59908 |     9635 | True         |
| 142 | France         | 2020-06-14 00:00:00 |       1014 |         -44 |  197471 |    29357 | True         |

 **The day after tomorrow** 
|     | country        | ds                  |   case_day |   death_day |   cases |   deaths | predicted?   |
|----:|:---------------|:--------------------|-----------:|------------:|--------:|---------:|:-------------|
| 110 | Brazil         | 2020-06-15 00:00:00 |      26788 |        1088 |  904024 |    44828 | True         |
| 136 | Italy          | 2020-06-15 00:00:00 |       -814 |         -36 |  235398 |    34222 | True         |
| 136 | United Kingdom | 2020-06-15 00:00:00 |       1090 |         181 |  298821 |    42091 | True         |
| 135 | Spain          | 2020-06-15 00:00:00 |        742 |        -190 |  245945 |    26854 | True         |
| 145 | US             | 2020-06-15 00:00:00 |      23215 |        1074 | 2121448 |   117509 | True         |
| 132 | Belgium        | 2020-06-15 00:00:00 |       -146 |         -25 |   59762 |     9610 | True         |
| 143 | France         | 2020-06-15 00:00:00 |        296 |          -7 |  197767 |    29350 | True         |