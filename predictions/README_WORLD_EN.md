# **Predictions**
For experience, I'm running simple predictions over the cases and deaths per day. As they are time-series, I'm using [Facebook Prophet](https://facebook.github.io/prophet/docs/quick_start.html) that is also designed for this kind of prediction in a very simpler way. It works well for most of the time; sometimes there is a huge leap and it takes more time and more data to be understood.

These predictions were made with Covid19 pandemic data from **2020-05-19**.

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
| 79 | Brazil    | 2020-05-15 00:00:00 |      17126 |         963 |  220291 |    14962 | False        |
| 80 | Brazil    | 2020-05-16 00:00:00 |      13220 |         700 |  233511 |    15662 | False        |
| 81 | Brazil    | 2020-05-17 00:00:00 |       7569 |         456 |  241080 |    16118 | False        |
| 82 | Brazil    | 2020-05-18 00:00:00 |      14288 |         735 |  255368 |    16853 | False        |
| 83 | Brazil    | 2020-05-19 00:00:00 |      16517 |        1130 |  271885 |    17983 | False        |
| 84 | Brazil    | 2020-05-20 00:00:00 |      13549 |         838 |  285434 |    18821 | True         |
| 85 | Brazil    | 2020-05-21 00:00:00 |      13814 |         872 |  299248 |    19693 | True         |
| 86 | Brazil    | 2020-05-22 00:00:00 |      14320 |         903 |  313568 |    20596 | True         |
| 87 | Brazil    | 2020-05-23 00:00:00 |      14072 |         869 |  327640 |    21465 | True         |
| 88 | Brazil    | 2020-05-24 00:00:00 |      13352 |         819 |  340992 |    22284 | True         |
| 89 | Brazil    | 2020-05-25 00:00:00 |      14315 |         871 |  355307 |    23155 | True         |
| 90 | Brazil    | 2020-05-26 00:00:00 |      15142 |         987 |  370449 |    24142 | True         |
| 91 | Brazil    | 2020-05-27 00:00:00 |      15917 |         976 |  386366 |    25118 | True         |
| 92 | Brazil    | 2020-05-28 00:00:00 |      16183 |        1010 |  402549 |    26128 | True         |
| 93 | Brazil    | 2020-05-29 00:00:00 |      16688 |        1040 |  419237 |    27168 | True         |

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
|  84 | Brazil         | 2020-05-20 00:00:00 |      13549 |         838 |  285434 |    18821 | True         |
| 110 | Italy          | 2020-05-20 00:00:00 |       2939 |         494 |  229638 |    32663 | True         |
| 110 | United Kingdom | 2020-05-20 00:00:00 |       5354 |         816 |  255492 |    36238 | True         |
| 109 | Spain          | 2020-05-20 00:00:00 |       3948 |         524 |  246010 |    28302 | True         |
| 119 | US             | 2020-05-20 00:00:00 |      32283 |        2220 | 1560851 |    94141 | True         |
| 106 | Belgium        | 2020-05-20 00:00:00 |        515 |         202 |   56306 |     9310 | True         |
| 117 | France         | 2020-05-20 00:00:00 |        599 |         535 |  181647 |    28560 | True         |

 **The day after tomorrow** 
|     | country        | ds                  |   case_day |   death_day |   cases |   deaths | predicted?   |
|----:|:---------------|:--------------------|-----------:|------------:|--------:|---------:|:-------------|
|  85 | Brazil         | 2020-05-21 00:00:00 |      13814 |         872 |  299248 |    19693 | True         |
| 111 | Italy          | 2020-05-21 00:00:00 |       2976 |         481 |  232614 |    33144 | True         |
| 111 | United Kingdom | 2020-05-21 00:00:00 |       5387 |         804 |  260879 |    37042 | True         |
| 110 | Spain          | 2020-05-21 00:00:00 |       3924 |         505 |  249934 |    28807 | True         |
| 120 | US             | 2020-05-21 00:00:00 |      34207 |        2174 | 1595058 |    96315 | True         |
| 107 | Belgium        | 2020-05-21 00:00:00 |        534 |         193 |   56840 |     9503 | True         |
| 118 | France         | 2020-05-21 00:00:00 |       1387 |         562 |  183034 |    29122 | True         |