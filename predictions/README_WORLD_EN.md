# **Predictions**
For experience, I'm running simple predictions over the cases and deaths per day. As they are time-series, I'm using [Facebook Prophet](https://facebook.github.io/prophet/docs/quick_start.html) that is also designed for this kind of prediction in a very simpler way. It works well for most of the time; sometimes there is a huge leap and it takes more time and more data to be understood.

These predictions were made with Covid19 pandemic data from **2020-05-16**.

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
| 76 | Brazil    | 2020-05-12 00:00:00 |       8620 |         808 |  178214 |    12461 | False        |
| 77 | Brazil    | 2020-05-13 00:00:00 |      11923 |         779 |  190137 |    13240 | False        |
| 78 | Brazil    | 2020-05-14 00:00:00 |      13028 |         759 |  203165 |    13999 | False        |
| 79 | Brazil    | 2020-05-15 00:00:00 |      17126 |         963 |  220291 |    14962 | False        |
| 80 | Brazil    | 2020-05-16 00:00:00 |      13220 |         700 |  233511 |    15662 | False        |
| 81 | Brazil    | 2020-05-17 00:00:00 |      11123 |         708 |  244634 |    16370 | True         |
| 82 | Brazil    | 2020-05-18 00:00:00 |      11571 |         739 |  256205 |    17109 | True         |
| 83 | Brazil    | 2020-05-19 00:00:00 |      12280 |         830 |  268485 |    17939 | True         |
| 84 | Brazil    | 2020-05-20 00:00:00 |      13376 |         844 |  281861 |    18783 | True         |
| 85 | Brazil    | 2020-05-21 00:00:00 |      13637 |         879 |  295498 |    19662 | True         |
| 86 | Brazil    | 2020-05-22 00:00:00 |      14140 |         909 |  309638 |    20571 | True         |
| 87 | Brazil    | 2020-05-23 00:00:00 |      13888 |         876 |  323526 |    21447 | True         |
| 88 | Brazil    | 2020-05-24 00:00:00 |      13460 |         848 |  336986 |    22295 | True         |
| 89 | Brazil    | 2020-05-25 00:00:00 |      13908 |         880 |  350894 |    23175 | True         |
| 90 | Brazil    | 2020-05-26 00:00:00 |      14617 |         971 |  365511 |    24146 | True         |

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
|  81 | Brazil         | 2020-05-17 00:00:00 |      11123 |         708 |  244634 |    16370 | True         |
| 107 | Italy          | 2020-05-17 00:00:00 |       3470 |         500 |  228230 |    32263 | True         |
| 107 | United Kingdom | 2020-05-17 00:00:00 |       5713 |         683 |  247174 |    35229 | True         |
| 106 | Spain          | 2020-05-17 00:00:00 |       3813 |         463 |  244536 |    28026 | True         |
| 116 | US             | 2020-05-17 00:00:00 |      31780 |        1918 | 1499600 |    90672 | True         |
| 103 | Belgium        | 2020-05-17 00:00:00 |        753 |         184 |   55742 |     9189 | True         |
| 114 | France         | 2020-05-17 00:00:00 |       3194 |         455 |  182939 |    27987 | True         |

 **The day after tomorrow** 
|     | country        | ds                  |   case_day |   death_day |   cases |   deaths | predicted?   |
|----:|:---------------|:--------------------|-----------:|------------:|--------:|---------:|:-------------|
|  82 | Brazil         | 2020-05-18 00:00:00 |      11571 |         739 |  256205 |    17109 | True         |
| 108 | Italy          | 2020-05-18 00:00:00 |       3100 |         522 |  231330 |    32785 | True         |
| 108 | United Kingdom | 2020-05-18 00:00:00 |       5452 |         689 |  252626 |    35918 | True         |
| 107 | Spain          | 2020-05-18 00:00:00 |       3854 |         473 |  248390 |    28499 | True         |
| 117 | US             | 2020-05-18 00:00:00 |      31285 |        2001 | 1530885 |    92673 | True         |
| 104 | Belgium        | 2020-05-18 00:00:00 |        602 |         177 |   56344 |     9366 | True         |
| 115 | France         | 2020-05-18 00:00:00 |       2277 |         536 |  185216 |    28523 | True         |