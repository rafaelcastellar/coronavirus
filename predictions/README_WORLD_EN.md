# **Predictions**
For experience, I'm running simple predictions over the cases and deaths per day. As they are time-series, I'm using [Facebook Prophet](https://facebook.github.io/prophet/docs/quick_start.html) that is also designed for this kind of prediction in a very simpler way. It works well for most of the time; sometimes there is a huge leap and it takes more time and more data to be understood.

These predictions were made with Covid19 pandemic data from **2020-06-14**.

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
| 105 | Brazil    | 2020-06-10 00:00:00 |      32913 |        1274 |  772416 |    39680 | False        |
| 106 | Brazil    | 2020-06-11 00:00:00 |      30412 |        1239 |  802828 |    40919 | False        |
| 107 | Brazil    | 2020-06-12 00:00:00 |      25982 |         909 |  828810 |    41828 | False        |
| 108 | Brazil    | 2020-06-13 00:00:00 |      21704 |         892 |  850514 |    42720 | False        |
| 109 | Brazil    | 2020-06-14 00:00:00 |      17110 |         612 |  867624 |    43332 | False        |
| 110 | Brazil    | 2020-06-15 00:00:00 |      25852 |        1056 |  893476 |    44388 | True         |
| 111 | Brazil    | 2020-06-16 00:00:00 |      29162 |        1242 |  922638 |    45630 | True         |
| 112 | Brazil    | 2020-06-17 00:00:00 |      30597 |        1243 |  953235 |    46873 | True         |
| 113 | Brazil    | 2020-06-18 00:00:00 |      31149 |        1294 |  984384 |    48167 | True         |
| 114 | Brazil    | 2020-06-19 00:00:00 |      31497 |        1250 | 1015881 |    49417 | True         |
| 115 | Brazil    | 2020-06-20 00:00:00 |      31012 |        1201 | 1046893 |    50618 | True         |
| 116 | Brazil    | 2020-06-21 00:00:00 |      28639 |        1070 | 1075532 |    51688 | True         |
| 117 | Brazil    | 2020-06-22 00:00:00 |      29217 |        1162 | 1104749 |    52850 | True         |
| 118 | Brazil    | 2020-06-23 00:00:00 |      32526 |        1348 | 1137275 |    54198 | True         |
| 119 | Brazil    | 2020-06-24 00:00:00 |      33962 |        1349 | 1171237 |    55547 | True         |

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
| 110 | Brazil         | 2020-06-15 00:00:00 |      25852 |        1056 |  893476 |    44388 | True         |
| 136 | Italy          | 2020-06-15 00:00:00 |       -759 |         -30 |  236230 |    34315 | True         |
| 136 | United Kingdom | 2020-06-15 00:00:00 |       1001 |         185 |  298758 |    41968 | True         |
| 135 | Spain          | 2020-06-15 00:00:00 |       -909 |        -176 |  243382 |    26960 | True         |
| 145 | US             | 2020-06-15 00:00:00 |      22568 |        1172 | 2116626 |   116904 | True         |
| 132 | Belgium        | 2020-06-15 00:00:00 |       -115 |         -19 |   59914 |     9636 | True         |
| 143 | France         | 2020-06-15 00:00:00 |         -8 |          18 |  196856 |    29428 | True         |

 **The day after tomorrow** 
|     | country        | ds                  |   case_day |   death_day |   cases |   deaths | predicted?   |
|----:|:---------------|:--------------------|-----------:|------------:|--------:|---------:|:-------------|
| 111 | Brazil         | 2020-06-16 00:00:00 |      29162 |        1242 |  922638 |    45630 | True         |
| 137 | Italy          | 2020-06-16 00:00:00 |       -760 |         -16 |  235470 |    34299 | True         |
| 137 | United Kingdom | 2020-06-16 00:00:00 |       1102 |         346 |  299860 |    42314 | True         |
| 136 | Spain          | 2020-06-16 00:00:00 |       -535 |         -86 |  242847 |    26874 | True         |
| 146 | US             | 2020-06-16 00:00:00 |      23146 |        1474 | 2139772 |   118378 | True         |
| 133 | Belgium        | 2020-06-16 00:00:00 |       -169 |          -1 |   59745 |     9635 | True         |
| 144 | France         | 2020-06-16 00:00:00 |         54 |          41 |  196910 |    29469 | True         |