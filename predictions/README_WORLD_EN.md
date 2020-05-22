# **Predictions**
For experience, I'm running simple predictions over the cases and deaths per day. As they are time-series, I'm using [Facebook Prophet](https://facebook.github.io/prophet/docs/quick_start.html) that is also designed for this kind of prediction in a very simpler way. It works well for most of the time; sometimes there is a huge leap and it takes more time and more data to be understood.

These predictions were made with Covid19 pandemic data from **2020-05-21**.

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
| 81 | Brazil    | 2020-05-17 00:00:00 |       7569 |         456 |  241080 |    16118 | False        |
| 82 | Brazil    | 2020-05-18 00:00:00 |      14288 |         735 |  255368 |    16853 | False        |
| 83 | Brazil    | 2020-05-19 00:00:00 |      16517 |        1130 |  271885 |    17983 | False        |
| 84 | Brazil    | 2020-05-20 00:00:00 |      19694 |         876 |  291579 |    18859 | False        |
| 85 | Brazil    | 2020-05-21 00:00:00 |      18508 |        1188 |  310087 |    20047 | False        |
| 86 | Brazil    | 2020-05-22 00:00:00 |      15514 |         939 |  325601 |    20986 | True         |
| 87 | Brazil    | 2020-05-23 00:00:00 |      15311 |         906 |  340912 |    21892 | True         |
| 88 | Brazil    | 2020-05-24 00:00:00 |      14634 |         858 |  355546 |    22750 | True         |
| 89 | Brazil    | 2020-05-25 00:00:00 |      15657 |         912 |  371203 |    23662 | True         |
| 90 | Brazil    | 2020-05-26 00:00:00 |      16520 |        1029 |  387723 |    24691 | True         |
| 91 | Brazil    | 2020-05-27 00:00:00 |      17823 |        1022 |  405546 |    25713 | True         |
| 92 | Brazil    | 2020-05-28 00:00:00 |      18017 |        1078 |  423563 |    26791 | True         |
| 93 | Brazil    | 2020-05-29 00:00:00 |      18295 |        1088 |  441858 |    27879 | True         |
| 94 | Brazil    | 2020-05-30 00:00:00 |      18091 |        1056 |  459949 |    28935 | True         |
| 95 | Brazil    | 2020-05-31 00:00:00 |      17414 |        1008 |  477363 |    29943 | True         |

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
|  86 | Brazil         | 2020-05-22 00:00:00 |      15514 |         939 |  325601 |    20986 | True         |
| 112 | Italy          | 2020-05-22 00:00:00 |        912 |         233 |  228918 |    32719 | True         |
| 112 | United Kingdom | 2020-05-22 00:00:00 |       5797 |         813 |  258458 |    36937 | True         |
| 111 | Spain          | 2020-05-22 00:00:00 |       3547 |         452 |  246609 |    28392 | True         |
| 121 | US             | 2020-05-22 00:00:00 |      34372 |        2078 | 1611519 |    96780 | True         |
| 108 | Belgium        | 2020-05-22 00:00:00 |        513 |         192 |   56748 |     9378 | True         |
| 119 | France         | 2020-05-22 00:00:00 |       1187 |         519 |  183253 |    28737 | True         |

 **The day after tomorrow** 
|     | country        | ds                  |   case_day |   death_day |   cases |   deaths | predicted?   |
|----:|:---------------|:--------------------|-----------:|------------:|--------:|---------:|:-------------|
|  87 | Brazil         | 2020-05-23 00:00:00 |      15311 |         906 |  340912 |    21892 | True         |
| 113 | Italy          | 2020-05-23 00:00:00 |        960 |         220 |  229878 |    32939 | True         |
| 113 | United Kingdom | 2020-05-23 00:00:00 |       5314 |         779 |  263772 |    37716 | True         |
| 112 | Spain          | 2020-05-23 00:00:00 |       3251 |         436 |  249860 |    28828 | True         |
| 122 | US             | 2020-05-23 00:00:00 |      33854 |        2054 | 1645373 |    98834 | True         |
| 109 | Belgium        | 2020-05-23 00:00:00 |        483 |         177 |   57231 |     9555 | True         |
| 120 | France         | 2020-05-23 00:00:00 |        902 |         462 |  184155 |    29199 | True         |