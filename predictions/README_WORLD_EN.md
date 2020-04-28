# **Predictions**
For experience, I'm running simple predictions over the cases and deaths per day. As they are time-series, I'm using [Facebook Prophet](https://facebook.github.io/prophet/docs/quick_start.html) that is also designed for this kind of prediction in a very simpler way. It works well for most of the time; sometimes there is a huge leap and it takes more time and more data to be understood.

These predictions were made with Covid19 pandemic data from **2020-04-27**.

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
| 57 | Brazil    | 2020-04-23 00:00:00 |       4279 |         425 |   50036 |     3331 | False        |
| 58 | Brazil    | 2020-04-24 00:00:00 |       4007 |         373 |   54043 |     3704 | False        |
| 59 | Brazil    | 2020-04-25 00:00:00 |       5281 |         353 |   59324 |     4057 | False        |
| 60 | Brazil    | 2020-04-26 00:00:00 |       3776 |         229 |   63100 |     4286 | False        |
| 61 | Brazil    | 2020-04-27 00:00:00 |       4346 |         317 |   67446 |     4603 | False        |
| 62 | Brazil    | 2020-04-28 00:00:00 |       3669 |         264 |   71115 |     4867 | True         |
| 63 | Brazil    | 2020-04-29 00:00:00 |       3957 |         274 |   75072 |     5141 | True         |
| 64 | Brazil    | 2020-04-30 00:00:00 |       4094 |         309 |   79166 |     5450 | True         |
| 65 | Brazil    | 2020-05-01 00:00:00 |       4172 |         302 |   83338 |     5752 | True         |
| 66 | Brazil    | 2020-05-02 00:00:00 |       4307 |         303 |   87645 |     6055 | True         |
| 67 | Brazil    | 2020-05-03 00:00:00 |       4067 |         280 |   91712 |     6335 | True         |
| 68 | Brazil    | 2020-05-04 00:00:00 |       4162 |         299 |   95874 |     6634 | True         |
| 69 | Brazil    | 2020-05-05 00:00:00 |       4401 |         317 |  100275 |     6951 | True         |
| 70 | Brazil    | 2020-05-06 00:00:00 |       4689 |         327 |  104964 |     7278 | True         |
| 71 | Brazil    | 2020-05-07 00:00:00 |       4826 |         362 |  109790 |     7640 | True         |

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
| 62 | Brazil         | 2020-04-28 00:00:00 |       3669 |         264 |   71115 |     4867 | True         |
| 88 | Italy          | 2020-04-28 00:00:00 |       4623 |         742 |  204037 |    27719 | True         |
| 88 | United Kingdom | 2020-04-28 00:00:00 |       5925 |         814 |  164273 |    21971 | True         |
| 87 | Spain          | 2020-04-28 00:00:00 |       6097 |         657 |  235519 |    24178 | True         |
| 97 | US             | 2020-04-28 00:00:00 |      35975 |        2597 | 1024172 |    58856 | True         |
| 84 | Belgium        | 2020-04-28 00:00:00 |       1339 |         282 |   48026 |     7489 | True         |
| 95 | France         | 2020-04-28 00:00:00 |       4744 |         737 |  170707 |    24064 | True         |

 **The day after tomorrow** 
|    | country        | ds                  |   case_day |   death_day |   cases |   deaths | predicted?   |
|---:|:---------------|:--------------------|-----------:|------------:|--------:|---------:|:-------------|
| 63 | Brazil         | 2020-04-29 00:00:00 |       3957 |         274 |   75072 |     5141 | True         |
| 89 | Italy          | 2020-04-29 00:00:00 |       4957 |         726 |  208994 |    28445 | True         |
| 89 | United Kingdom | 2020-04-29 00:00:00 |       6217 |         837 |  170490 |    22808 | True         |
| 88 | Spain          | 2020-04-29 00:00:00 |       6877 |         726 |  242396 |    24904 | True         |
| 98 | US             | 2020-04-29 00:00:00 |      36745 |        2634 | 1060917 |    61490 | True         |
| 85 | Belgium        | 2020-04-29 00:00:00 |       1526 |         272 |   49552 |     7761 | True         |
| 96 | France         | 2020-04-29 00:00:00 |       4089 |         751 |  174796 |    24815 | True         |