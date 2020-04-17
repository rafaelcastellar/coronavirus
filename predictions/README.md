# **Predictions**
For experience, I'm running simple predictions over the cases and deaths per day. As they are time-series, I'm using [Facebook Prophet](https://facebook.github.io/prophet/docs/quick_start.html) that is also designed for this kind of prediction in a very simpler way. It works well for most of the time; sometimes there is a huge leap and it takes sometime more data to be understood.

These predictions were made with Covid19 pandemic data from **2020-04-16**.

As there are many countries to have their data predicted in a row, I selected a few of them plus Brazil to be predicted:
['Brazil', 'Italy', 'United Kingdom', 'Spain', 'US', 'Belgium', 'France'].
***Tip**: you can set yourself at the *[prediction.ipynb](../prediction.ipynb)* notebook which countries you prefer to predict*


## The prediction
As Facebook Prophet predicts time-series data and it is running the prediction over cases per day and deaths per day. After that, I compute theirs cumulatives.It is predicting for the next 10 days.
By the end, a CSV file containing all the predicted data is generated.

#### The Brazil's last 5 days and predicted next 10 days
*predicted? = True* means the line is a prediction; *=False* means they are real numbers.
|    | country   | ds                  |   case_day |   death_day |   cases |   deaths | predicted?   |
|---:|:----------|:--------------------|-----------:|------------:|--------:|---------:|:-------------|
| 46 | Brazil    | 2020-04-12 00:00:00 |       1465 |          99 |   22192 |     1223 | False        |
| 47 | Brazil    | 2020-04-13 00:00:00 |       1238 |         105 |   23430 |     1328 | False        |
| 48 | Brazil    | 2020-04-14 00:00:00 |       1832 |         204 |   25262 |     1532 | False        |
| 49 | Brazil    | 2020-04-15 00:00:00 |       3058 |         204 |   28320 |     1736 | False        |
| 50 | Brazil    | 2020-04-16 00:00:00 |       2105 |         188 |   30425 |     1924 | False        |
| 51 | Brazil    | 2020-04-17 00:00:00 |       1927 |         109 |   32352 |     2033 | True         |
| 52 | Brazil    | 2020-04-18 00:00:00 |       1923 |         111 |   34275 |     2144 | True         |
| 53 | Brazil    | 2020-04-19 00:00:00 |       1946 |         111 |   36221 |     2255 | True         |
| 54 | Brazil    | 2020-04-20 00:00:00 |       1948 |         116 |   38169 |     2371 | True         |
| 55 | Brazil    | 2020-04-21 00:00:00 |       2293 |         140 |   40462 |     2511 | True         |
| 56 | Brazil    | 2020-04-22 00:00:00 |       2513 |         145 |   42975 |     2656 | True         |
| 57 | Brazil    | 2020-04-23 00:00:00 |       2437 |         149 |   45412 |     2805 | True         |
| 58 | Brazil    | 2020-04-24 00:00:00 |       2362 |         130 |   47774 |     2935 | True         |
| 59 | Brazil    | 2020-04-25 00:00:00 |       2358 |         132 |   50132 |     3067 | True         |
| 60 | Brazil    | 2020-04-26 00:00:00 |       2381 |         132 |   52513 |     3199 | True         |

 #### The predicted Brazil's cumulative curves
The prediction are over the daily data, so, here they were cumulated and plotted with the actual data:
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
| 51 | Brazil         | 2020-04-17 00:00:00 |       1927 |         109 |   32352 |     2033 | True         |
| 77 | Italy          | 2020-04-17 00:00:00 |       5913 |         820 |  174854 |    22990 | True         |
| 77 | United Kingdom | 2020-04-17 00:00:00 |       6533 |         946 |  110678 |    14705 | True         |
| 76 | Spain          | 2020-04-17 00:00:00 |       6775 |         730 |  191723 |    20045 | True         |
| 86 | US             | 2020-04-17 00:00:00 |      36087 |        2617 |  703888 |    35533 | True         |
| 73 | Belgium        | 2020-04-17 00:00:00 |       1456 |         347 |   36265 |     5204 | True         |
| 84 | France         | 2020-04-17 00:00:00 |       6273 |         978 |  153364 |    18919 | True         |

 **The day after tomorrow** 
|    | country        | ds                  |   case_day |   death_day |   cases |   deaths | predicted?   |
|---:|:---------------|:--------------------|-----------:|------------:|--------:|---------:|:-------------|
| 52 | Brazil         | 2020-04-18 00:00:00 |       1923 |         111 |   34275 |     2144 | True         |
| 78 | Italy          | 2020-04-18 00:00:00 |       5949 |         805 |  180803 |    23795 | True         |
| 78 | United Kingdom | 2020-04-18 00:00:00 |       6196 |         970 |  116874 |    15675 | True         |
| 77 | Spain          | 2020-04-18 00:00:00 |       6906 |         747 |  198629 |    20792 | True         |
| 87 | US             | 2020-04-18 00:00:00 |      36524 |        2692 |  740412 |    38225 | True         |
| 74 | Belgium        | 2020-04-18 00:00:00 |       1525 |         338 |   37790 |     5542 | True         |
| 85 | France         | 2020-04-18 00:00:00 |       6152 |         947 |  159516 |    19866 | True         |