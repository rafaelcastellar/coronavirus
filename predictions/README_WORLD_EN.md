# **Predictions**
For experience, I'm running simple predictions over the cases and deaths per day. As they are time-series, I'm using [Facebook Prophet](https://facebook.github.io/prophet/docs/quick_start.html) that is also designed for this kind of prediction in a very simpler way. It works well for most of the time; sometimes there is a huge leap and it takes more time and more data to be understood.

These predictions were made with Covid19 pandemic data from **2020-04-22**.

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
| 52 | Brazil    | 2020-04-18 00:00:00 |       2976 |         213 |   36658 |     2354 | False        |
| 53 | Brazil    | 2020-04-19 00:00:00 |       1996 |         108 |   38654 |     2462 | False        |
| 54 | Brazil    | 2020-04-20 00:00:00 |       2089 |         125 |   40743 |     2587 | False        |
| 55 | Brazil    | 2020-04-21 00:00:00 |       2336 |         154 |   43079 |     2741 | False        |
| 56 | Brazil    | 2020-04-22 00:00:00 |       2678 |         165 |   45757 |     2906 | False        |
| 57 | Brazil    | 2020-04-23 00:00:00 |       2605 |         162 |   48362 |     3068 | True         |
| 58 | Brazil    | 2020-04-24 00:00:00 |       2698 |         157 |   51060 |     3225 | True         |
| 59 | Brazil    | 2020-04-25 00:00:00 |       2661 |         158 |   53721 |     3383 | True         |
| 60 | Brazil    | 2020-04-26 00:00:00 |       2559 |         145 |   56280 |     3528 | True         |
| 61 | Brazil    | 2020-04-27 00:00:00 |       2574 |         152 |   58854 |     3680 | True         |
| 62 | Brazil    | 2020-04-28 00:00:00 |       2908 |         176 |   61762 |     3856 | True         |
| 63 | Brazil    | 2020-04-29 00:00:00 |       3161 |         183 |   64923 |     4039 | True         |
| 64 | Brazil    | 2020-04-30 00:00:00 |       3086 |         187 |   68009 |     4226 | True         |
| 65 | Brazil    | 2020-05-01 00:00:00 |       3179 |         181 |   71188 |     4407 | True         |
| 66 | Brazil    | 2020-05-02 00:00:00 |       3141 |         182 |   74329 |     4589 | True         |

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
| 57 | Brazil         | 2020-04-23 00:00:00 |       2605 |         162 |   48362 |     3068 | True         |
| 83 | Italy          | 2020-04-23 00:00:00 |       5241 |         730 |  192568 |    25815 | True         |
| 83 | United Kingdom | 2020-04-23 00:00:00 |       6097 |         905 |  140735 |    19056 | True         |
| 82 | Spain          | 2020-04-23 00:00:00 |       6930 |         729 |  215319 |    22446 | True         |
| 92 | US             | 2020-04-23 00:00:00 |      37046 |        2858 |  877397 |    49480 | True         |
| 79 | Belgium        | 2020-04-23 00:00:00 |       1515 |         320 |   43404 |     6582 | True         |
| 90 | France         | 2020-04-23 00:00:00 |       5326 |         862 |  162451 |    22235 | True         |

 **The day after tomorrow** 
|    | country        | ds                  |   case_day |   death_day |   cases |   deaths | predicted?   |
|---:|:---------------|:--------------------|-----------:|------------:|--------:|---------:|:-------------|
| 58 | Brazil         | 2020-04-24 00:00:00 |       2698 |         157 |   51060 |     3225 | True         |
| 84 | Italy          | 2020-04-24 00:00:00 |       5713 |         817 |  198281 |    26632 | True         |
| 84 | United Kingdom | 2020-04-24 00:00:00 |       6864 |         939 |  147599 |    19995 | True         |
| 83 | Spain          | 2020-04-24 00:00:00 |       6835 |         737 |  222154 |    23183 | True         |
| 93 | US             | 2020-04-24 00:00:00 |      37502 |        2869 |  914899 |    52349 | True         |
| 80 | Belgium        | 2020-04-24 00:00:00 |       1553 |         330 |   44957 |     6912 | True         |
| 91 | France         | 2020-04-24 00:00:00 |       4962 |         864 |  167413 |    23099 | True         |