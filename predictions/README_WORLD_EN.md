# **Predictions**
For experience, I'm running simple predictions over the cases and deaths per day. As they are time-series, I'm using [Facebook Prophet](https://facebook.github.io/prophet/docs/quick_start.html) that is also designed for this kind of prediction in a very simpler way. It works well for most of the time; sometimes there is a huge leap and it takes more time and more data to be understood.

These predictions were made with Covid19 pandemic data from **2020-06-02**.

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
|  93 | Brazil    | 2020-05-29 00:00:00 |      26928 |        1124 |  465166 |    27878 | False        |
|  94 | Brazil    | 2020-05-30 00:00:00 |      33274 |         956 |  498440 |    28834 | False        |
|  95 | Brazil    | 2020-05-31 00:00:00 |      16409 |         480 |  514849 |    29314 | False        |
|  96 | Brazil    | 2020-06-01 00:00:00 |      11598 |         623 |  526447 |    29937 | False        |
|  97 | Brazil    | 2020-06-02 00:00:00 |      28936 |        1262 |  555383 |    31199 | False        |
|  98 | Brazil    | 2020-06-03 00:00:00 |      23418 |        1086 |  578801 |    32285 | True         |
|  99 | Brazil    | 2020-06-04 00:00:00 |      24081 |        1140 |  602882 |    33425 | True         |
| 100 | Brazil    | 2020-06-05 00:00:00 |      24820 |        1149 |  627702 |    34574 | True         |
| 101 | Brazil    | 2020-06-06 00:00:00 |      24849 |        1104 |  652551 |    35678 | True         |
| 102 | Brazil    | 2020-06-07 00:00:00 |      23073 |        1004 |  675624 |    36682 | True         |
| 103 | Brazil    | 2020-06-08 00:00:00 |      23369 |        1068 |  698993 |    37750 | True         |
| 104 | Brazil    | 2020-06-09 00:00:00 |      25758 |        1228 |  724751 |    38978 | True         |
| 105 | Brazil    | 2020-06-10 00:00:00 |      26885 |        1212 |  751636 |    40190 | True         |
| 106 | Brazil    | 2020-06-11 00:00:00 |      27549 |        1267 |  779185 |    41457 | True         |
| 107 | Brazil    | 2020-06-12 00:00:00 |      28288 |        1275 |  807473 |    42732 | True         |

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
|  98 | Brazil         | 2020-06-03 00:00:00 |      23418 |        1086 |  578801 |    32285 | True         |
| 124 | Italy          | 2020-06-03 00:00:00 |       -132 |          64 |  233383 |    33594 | True         |
| 124 | United Kingdom | 2020-06-03 00:00:00 |       2568 |         701 |  282375 |    40153 | True         |
| 123 | Spain          | 2020-06-03 00:00:00 |       2505 |          43 |  242800 |    27170 | True         |
| 133 | US             | 2020-06-03 00:00:00 |      30638 |        2034 | 1862459 |   108214 | True         |
| 120 | Belgium        | 2020-06-03 00:00:00 |         92 |          66 |   58707 |     9571 | True         |
| 131 | France         | 2020-06-03 00:00:00 |       -227 |         178 |  189071 |    29121 | True         |

 **The day after tomorrow** 
|     | country        | ds                  |   case_day |   death_day |   cases |   deaths | predicted?   |
|----:|:---------------|:--------------------|-----------:|------------:|--------:|---------:|:-------------|
|  99 | Brazil         | 2020-06-04 00:00:00 |      24081 |        1140 |  602882 |    33425 | True         |
| 125 | Italy          | 2020-06-04 00:00:00 |        -21 |          51 |  233362 |    33645 | True         |
| 125 | United Kingdom | 2020-06-04 00:00:00 |       2682 |         687 |  285057 |    40840 | True         |
| 124 | Spain          | 2020-06-04 00:00:00 |       2578 |          12 |  245378 |    27182 | True         |
| 134 | US             | 2020-06-04 00:00:00 |      32660 |        1960 | 1895119 |   110174 | True         |
| 121 | Belgium        | 2020-06-04 00:00:00 |        114 |          54 |   58821 |     9625 | True         |
| 132 | France         | 2020-06-04 00:00:00 |        622 |         193 |  189693 |    29314 | True         |