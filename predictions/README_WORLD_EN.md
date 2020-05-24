# **Predictions**
For experience, I'm running simple predictions over the cases and deaths per day. As they are time-series, I'm using [Facebook Prophet](https://facebook.github.io/prophet/docs/quick_start.html) that is also designed for this kind of prediction in a very simpler way. It works well for most of the time; sometimes there is a huge leap and it takes more time and more data to be understood.

These predictions were made with Covid19 pandemic data from **2020-05-23**.

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
| 83 | Brazil    | 2020-05-19 00:00:00 |      16517 |        1130 |  271885 |    17983 | False        |
| 84 | Brazil    | 2020-05-20 00:00:00 |      19694 |         876 |  291579 |    18859 | False        |
| 85 | Brazil    | 2020-05-21 00:00:00 |      18508 |        1188 |  310087 |    20047 | False        |
| 86 | Brazil    | 2020-05-22 00:00:00 |      20803 |        1001 |  330890 |    21048 | False        |
| 87 | Brazil    | 2020-05-23 00:00:00 |      16508 |         965 |  347398 |    22013 | False        |
| 88 | Brazil    | 2020-05-24 00:00:00 |      15670 |         872 |  363068 |    22885 | True         |
| 89 | Brazil    | 2020-05-25 00:00:00 |      16739 |         926 |  379807 |    23811 | True         |
| 90 | Brazil    | 2020-05-26 00:00:00 |      17673 |        1045 |  397480 |    24856 | True         |
| 91 | Brazil    | 2020-05-27 00:00:00 |      19031 |        1038 |  416511 |    25894 | True         |
| 92 | Brazil    | 2020-05-28 00:00:00 |      19280 |        1095 |  435791 |    26989 | True         |
| 93 | Brazil    | 2020-05-29 00:00:00 |      20017 |        1109 |  455808 |    28098 | True         |
| 94 | Brazil    | 2020-05-30 00:00:00 |      19549 |        1077 |  475357 |    29175 | True         |
| 95 | Brazil    | 2020-05-31 00:00:00 |      18902 |        1026 |  494259 |    30201 | True         |
| 96 | Brazil    | 2020-06-01 00:00:00 |      19972 |        1080 |  514231 |    31281 | True         |
| 97 | Brazil    | 2020-06-02 00:00:00 |      20906 |        1199 |  535137 |    32480 | True         |

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
|  88 | Brazil         | 2020-05-24 00:00:00 |      15670 |         872 |  363068 |    22885 | True         |
| 114 | Italy          | 2020-05-24 00:00:00 |       2672 |         132 |  231999 |    32867 | True         |
| 114 | United Kingdom | 2020-05-24 00:00:00 |       4840 |         612 |  263759 |    37369 | True         |
| 113 | Spain          | 2020-05-24 00:00:00 |       3044 |         427 |  248359 |    29105 | True         |
| 123 | US             | 2020-05-24 00:00:00 |      31442 |        1771 | 1654054 |    98858 | True         |
| 110 | Belgium        | 2020-05-24 00:00:00 |        411 |         145 |   57221 |     9382 | True         |
| 121 | France         | 2020-05-24 00:00:00 |       1589 |         365 |  183740 |    28583 | True         |

 **The day after tomorrow** 
|     | country        | ds                  |   case_day |   death_day |   cases |   deaths | predicted?   |
|----:|:---------------|:--------------------|-----------:|------------:|--------:|---------:|:-------------|
|  89 | Brazil         | 2020-05-25 00:00:00 |      16739 |         926 |  379807 |    23811 | True         |
| 115 | Italy          | 2020-05-25 00:00:00 |       2324 |         139 |  234323 |    33006 | True         |
| 115 | United Kingdom | 2020-05-25 00:00:00 |       4521 |         617 |  268280 |    37986 | True         |
| 114 | Spain          | 2020-05-25 00:00:00 |       3137 |         445 |  251496 |    29550 | True         |
| 124 | US             | 2020-05-25 00:00:00 |      31243 |        1852 | 1685297 |   100710 | True         |
| 111 | Belgium        | 2020-05-25 00:00:00 |        258 |         137 |   57479 |     9519 | True         |
| 122 | France         | 2020-05-25 00:00:00 |        708 |         412 |  184448 |    28995 | True         |