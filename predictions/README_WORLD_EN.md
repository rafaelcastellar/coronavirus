# **Predictions**
For experience, I'm running simple predictions over the cases and deaths per day. As they are time-series, I'm using [Facebook Prophet](https://facebook.github.io/prophet/docs/quick_start.html) that is also designed for this kind of prediction in a very simpler way. It works well for most of the time; sometimes there is a huge leap and it takes more time and more data to be understood.

These predictions were made with Covid19 pandemic data from **2020-04-17**.

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
| 47 | Brazil    | 2020-04-13 00:00:00 |       1238 |         105 |   23430 |     1328 | False        |
| 48 | Brazil    | 2020-04-14 00:00:00 |       1832 |         204 |   25262 |     1532 | False        |
| 49 | Brazil    | 2020-04-15 00:00:00 |       3058 |         204 |   28320 |     1736 | False        |
| 50 | Brazil    | 2020-04-16 00:00:00 |       2105 |         188 |   30425 |     1924 | False        |
| 51 | Brazil    | 2020-04-17 00:00:00 |       3257 |         217 |   33682 |     2141 | False        |
| 52 | Brazil    | 2020-04-18 00:00:00 |       2012 |         117 |   35694 |     2258 | True         |
| 53 | Brazil    | 2020-04-19 00:00:00 |       2035 |         117 |   37729 |     2375 | True         |
| 54 | Brazil    | 2020-04-20 00:00:00 |       2038 |         123 |   39767 |     2498 | True         |
| 55 | Brazil    | 2020-04-21 00:00:00 |       2381 |         146 |   42148 |     2644 | True         |
| 56 | Brazil    | 2020-04-22 00:00:00 |       2612 |         152 |   44760 |     2796 | True         |
| 57 | Brazil    | 2020-04-23 00:00:00 |       2537 |         157 |   47297 |     2953 | True         |
| 58 | Brazil    | 2020-04-24 00:00:00 |       2631 |         151 |   49928 |     3104 | True         |
| 59 | Brazil    | 2020-04-25 00:00:00 |       2473 |         140 |   52401 |     3244 | True         |
| 60 | Brazil    | 2020-04-26 00:00:00 |       2496 |         140 |   54897 |     3384 | True         |
| 61 | Brazil    | 2020-04-27 00:00:00 |       2499 |         146 |   57396 |     3530 | True         |

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
| 52 | Brazil         | 2020-04-18 00:00:00 |       2012 |         117 |   35694 |     2258 | True         |
| 78 | Italy          | 2020-04-18 00:00:00 |       5845 |         795 |  178279 |    23540 | True         |
| 78 | United Kingdom | 2020-04-18 00:00:00 |       6106 |         996 |  115875 |    15603 | True         |
| 77 | Spain          | 2020-04-18 00:00:00 |       6872 |         746 |  197711 |    20748 | True         |
| 87 | US             | 2020-04-18 00:00:00 |      37153 |        2809 |  736859 |    39582 | True         |
| 74 | Belgium        | 2020-04-18 00:00:00 |       1698 |         343 |   37836 |     5506 | True         |
| 85 | France         | 2020-04-18 00:00:00 |       5165 |         921 |  154295 |    19624 | True         |

 **The day after tomorrow** 
|    | country        | ds                  |   case_day |   death_day |   cases |   deaths | predicted?   |
|---:|:---------------|:--------------------|-----------:|------------:|--------:|---------:|:-------------|
| 53 | Brazil         | 2020-04-19 00:00:00 |       2035 |         117 |   37729 |     2375 | True         |
| 79 | Italy          | 2020-04-19 00:00:00 |       5651 |         765 |  183930 |    24305 | True         |
| 79 | United Kingdom | 2020-04-19 00:00:00 |       6331 |         984 |  122206 |    16587 | True         |
| 78 | Spain          | 2020-04-19 00:00:00 |       6481 |         755 |  204192 |    21503 | True         |
| 88 | US             | 2020-04-19 00:00:00 |      37275 |        2858 |  774134 |    42440 | True         |
| 75 | Belgium        | 2020-04-19 00:00:00 |       1687 |         343 |   39523 |     5849 | True         |
| 86 | France         | 2020-04-19 00:00:00 |       6698 |         879 |  160993 |    20503 | True         |