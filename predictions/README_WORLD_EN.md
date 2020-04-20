# **Predictions**
For experience, I'm running simple predictions over the cases and deaths per day. As they are time-series, I'm using [Facebook Prophet](https://facebook.github.io/prophet/docs/quick_start.html) that is also designed for this kind of prediction in a very simpler way. It works well for most of the time; sometimes there is a huge leap and it takes more time and more data to be understood.

These predictions were made with Covid19 pandemic data from **2020-04-19**.

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
| 49 | Brazil    | 2020-04-15 00:00:00 |       3058 |         204 |   28320 |     1736 | False        |
| 50 | Brazil    | 2020-04-16 00:00:00 |       2105 |         188 |   30425 |     1924 | False        |
| 51 | Brazil    | 2020-04-17 00:00:00 |       3257 |         217 |   33682 |     2141 | False        |
| 52 | Brazil    | 2020-04-18 00:00:00 |       2976 |         213 |   36658 |     2354 | False        |
| 53 | Brazil    | 2020-04-19 00:00:00 |       1996 |         108 |   38654 |     2462 | False        |
| 54 | Brazil    | 2020-04-20 00:00:00 |       2137 |         127 |   40791 |     2589 | True         |
| 55 | Brazil    | 2020-04-21 00:00:00 |       2485 |         151 |   43276 |     2740 | True         |
| 56 | Brazil    | 2020-04-22 00:00:00 |       2727 |         157 |   46003 |     2897 | True         |
| 57 | Brazil    | 2020-04-23 00:00:00 |       2657 |         161 |   48660 |     3058 | True         |
| 58 | Brazil    | 2020-04-24 00:00:00 |       2752 |         156 |   51412 |     3214 | True         |
| 59 | Brazil    | 2020-04-25 00:00:00 |       2717 |         157 |   54129 |     3371 | True         |
| 60 | Brazil    | 2020-04-26 00:00:00 |       2617 |         144 |   56746 |     3515 | True         |
| 61 | Brazil    | 2020-04-27 00:00:00 |       2640 |         151 |   59386 |     3666 | True         |
| 62 | Brazil    | 2020-04-28 00:00:00 |       2988 |         175 |   62374 |     3841 | True         |
| 63 | Brazil    | 2020-04-29 00:00:00 |       3230 |         182 |   65604 |     4023 | True         |

 #### The predicted Brazil's cumulative curves
![](brazil_predictions.png)

Facebook's Prophet automatically generates charts about the behaviour of the analysed and predicted data. That has a good visual information. Here are for the Brazil's prediction:
### Cases
![](brazil_prophet_cases.png)

 ### Deaths
![](brazil_prophet_deaths.png)
#### Finally, the predictions for selected countries for:
**Tomorrow**
|    | country        | ds                  |   case_day |   death_day |   cases |   deaths | predicted?   |
|---:|:---------------|:--------------------|-----------:|------------:|--------:|---------:|:-------------|
| 54 | Brazil         | 2020-04-20 00:00:00 |       2137 |         127 |   40791 |     2589 | True         |
| 80 | Italy          | 2020-04-20 00:00:00 |       5105 |         760 |  184077 |    24420 | True         |
| 80 | United Kingdom | 2020-04-20 00:00:00 |       6106 |         880 |  127278 |    16975 | True         |
| 79 | Spain          | 2020-04-20 00:00:00 |       6621 |         727 |  205295 |    21180 | True         |
| 89 | US             | 2020-04-20 00:00:00 |      36383 |        2680 |  795469 |    43341 | True         |
| 76 | Belgium        | 2020-04-20 00:00:00 |       1303 |         329 |   39799 |     6012 | True         |
| 87 | France         | 2020-04-20 00:00:00 |       5325 |         836 |  159422 |    20580 | True         |

 **The day after tomorrow** 
|    | country        | ds                  |   case_day |   death_day |   cases |   deaths | predicted?   |
|---:|:---------------|:--------------------|-----------:|------------:|--------:|---------:|:-------------|
| 55 | Brazil         | 2020-04-21 00:00:00 |       2485 |         151 |   43276 |     2740 | True         |
| 81 | Italy          | 2020-04-21 00:00:00 |       5045 |         782 |  189122 |    25202 | True         |
| 81 | United Kingdom | 2020-04-21 00:00:00 |       6329 |         949 |  133607 |    17924 | True         |
| 80 | Spain          | 2020-04-21 00:00:00 |       6422 |         698 |  211717 |    21878 | True         |
| 90 | US             | 2020-04-21 00:00:00 |      37563 |        2917 |  833032 |    46258 | True         |
| 77 | Belgium        | 2020-04-21 00:00:00 |       1340 |         365 |   41139 |     6377 | True         |
| 88 | France         | 2020-04-21 00:00:00 |       5608 |         915 |  165030 |    21495 | True         |