# **Predictions**
For experience, I'm running simple predictions over the cases and deaths per day. As they are time-series, I'm using [Facebook Prophet](https://facebook.github.io/prophet/docs/quick_start.html) that is also designed for this kind of prediction in a very simpler way. It works well for most of the time; sometimes there is a huge leap and it takes more time and more data to be understood.

These predictions were made with Covid19 pandemic data from **2020-06-20**.

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
| 111 | Brazil    | 2020-06-16 00:00:00 |      34918 |        1282 |  923189 |    45241 | False        |
| 112 | Brazil    | 2020-06-17 00:00:00 |      32188 |        1269 |  955377 |    46510 | False        |
| 113 | Brazil    | 2020-06-18 00:00:00 |      22765 |        1238 |  978142 |    47748 | False        |
| 114 | Brazil    | 2020-06-19 00:00:00 |      54771 |        1206 | 1032913 |    48954 | False        |
| 115 | Brazil    | 2020-06-20 00:00:00 |          0 |        1022 | 1032913 |    49976 | False        |
| 116 | Brazil    | 2020-06-21 00:00:00 |      26733 |        1026 | 1059646 |    51002 | True         |
| 117 | Brazil    | 2020-06-22 00:00:00 |      26944 |        1090 | 1086590 |    52092 | True         |
| 118 | Brazil    | 2020-06-23 00:00:00 |      30934 |        1305 | 1117524 |    53397 | True         |
| 119 | Brazil    | 2020-06-24 00:00:00 |      32066 |        1306 | 1149590 |    54703 | True         |
| 120 | Brazil    | 2020-06-25 00:00:00 |      31985 |        1351 | 1181575 |    56054 | True         |
| 121 | Brazil    | 2020-06-26 00:00:00 |      34157 |        1306 | 1215732 |    57360 | True         |
| 122 | Brazil    | 2020-06-27 00:00:00 |      30413 |        1248 | 1246145 |    58608 | True         |
| 123 | Brazil    | 2020-06-28 00:00:00 |      29676 |        1124 | 1275821 |    59732 | True         |
| 124 | Brazil    | 2020-06-29 00:00:00 |      29886 |        1187 | 1305707 |    60919 | True         |
| 125 | Brazil    | 2020-06-30 00:00:00 |      33877 |        1402 | 1339584 |    62321 | True         |

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
| 116 | Brazil         | 2020-06-21 00:00:00 |      26733 |        1026 | 1059646 |    51002 | True         |
| 142 | Italy          | 2020-06-21 00:00:00 |       -509 |         -67 |  237894 |    34543 | True         |
| 142 | United Kingdom | 2020-06-21 00:00:00 |       1037 |          82 |  306032 |    42756 | True         |
| 141 | Spain          | 2020-06-21 00:00:00 |        711 |         -29 |  247012 |    28293 | True         |
| 151 | US             | 2020-06-21 00:00:00 |      24258 |         661 | 2279377 |   120380 | True         |
| 138 | Belgium        | 2020-06-21 00:00:00 |        -60 |         -24 |   60490 |     9672 | True         |
| 149 | France         | 2020-06-21 00:00:00 |        557 |         -70 |  199992 |    29566 | True         |

 **The day after tomorrow** 
|     | country        | ds                  |   case_day |   death_day |   cases |   deaths | predicted?   |
|----:|:---------------|:--------------------|-----------:|------------:|--------:|---------:|:-------------|
| 117 | Brazil         | 2020-06-22 00:00:00 |      26944 |        1090 | 1086590 |    52092 | True         |
| 143 | Italy          | 2020-06-22 00:00:00 |       -864 |         -60 |  237030 |    34483 | True         |
| 143 | United Kingdom | 2020-06-22 00:00:00 |        618 |          99 |  306650 |    42855 | True         |
| 142 | Spain          | 2020-06-22 00:00:00 |        233 |        -120 |  247245 |    28173 | True         |
| 152 | US             | 2020-06-22 00:00:00 |      23832 |         729 | 2303209 |   121109 | True         |
| 139 | Belgium        | 2020-06-22 00:00:00 |       -190 |         -33 |   60300 |     9639 | True         |
| 150 | France         | 2020-06-22 00:00:00 |        -92 |         -33 |  199900 |    29533 | True         |