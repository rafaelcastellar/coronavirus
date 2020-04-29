# **Predictions**
For experience, I'm running simple predictions over the cases and deaths per day. As they are time-series, I'm using [Facebook Prophet](https://facebook.github.io/prophet/docs/quick_start.html) that is also designed for this kind of prediction in a very simpler way. It works well for most of the time; sometimes there is a huge leap and it takes more time and more data to be understood.

These predictions were made with Covid19 pandemic data from **2020-04-28**.

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
| 58 | Brazil    | 2020-04-24 00:00:00 |       4007 |         373 |   54043 |     3704 | False        |
| 59 | Brazil    | 2020-04-25 00:00:00 |       5281 |         353 |   59324 |     4057 | False        |
| 60 | Brazil    | 2020-04-26 00:00:00 |       3776 |         229 |   63100 |     4286 | False        |
| 61 | Brazil    | 2020-04-27 00:00:00 |       4346 |         317 |   67446 |     4603 | False        |
| 62 | Brazil    | 2020-04-28 00:00:00 |       5789 |         480 |   73235 |     5083 | False        |
| 63 | Brazil    | 2020-04-29 00:00:00 |       4243 |         290 |   77478 |     5373 | True         |
| 64 | Brazil    | 2020-04-30 00:00:00 |       4391 |         326 |   81869 |     5699 | True         |
| 65 | Brazil    | 2020-05-01 00:00:00 |       4482 |         319 |   86351 |     6018 | True         |
| 66 | Brazil    | 2020-05-02 00:00:00 |       4627 |         321 |   90978 |     6339 | True         |
| 67 | Brazil    | 2020-05-03 00:00:00 |       4405 |         298 |   95383 |     6637 | True         |
| 68 | Brazil    | 2020-05-04 00:00:00 |       4517 |         317 |   99900 |     6954 | True         |
| 69 | Brazil    | 2020-05-05 00:00:00 |       5003 |         360 |  104903 |     7314 | True         |
| 70 | Brazil    | 2020-05-06 00:00:00 |       5101 |         348 |  110004 |     7662 | True         |
| 71 | Brazil    | 2020-05-07 00:00:00 |       5250 |         384 |  115254 |     8046 | True         |
| 72 | Brazil    | 2020-05-08 00:00:00 |       5340 |         376 |  120594 |     8422 | True         |

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
| 63 | Brazil         | 2020-04-29 00:00:00 |       4243 |         290 |   77478 |     5373 | True         |
| 89 | Italy          | 2020-04-29 00:00:00 |       4863 |         713 |  206368 |    28072 | True         |
| 89 | United Kingdom | 2020-04-29 00:00:00 |       6058 |         745 |  168408 |    22490 | True         |
| 88 | Spain          | 2020-04-29 00:00:00 |       6769 |         715 |  238897 |    24537 | True         |
| 98 | US             | 2020-04-29 00:00:00 |      35765 |        2463 | 1048347 |    60818 | True         |
| 85 | Belgium        | 2020-04-29 00:00:00 |       1500 |         252 |   48834 |     7583 | True         |
| 96 | France         | 2020-04-29 00:00:00 |       4052 |         740 |  173105 |    24434 | True         |

 **The day after tomorrow** 
|    | country        | ds                  |   case_day |   death_day |   cases |   deaths | predicted?   |
|---:|:---------------|:--------------------|-----------:|------------:|--------:|---------:|:-------------|
| 64 | Brazil         | 2020-04-30 00:00:00 |       4391 |         326 |   81869 |     5699 | True         |
| 90 | Italy          | 2020-04-30 00:00:00 |       4921 |         703 |  211289 |    28775 | True         |
| 90 | United Kingdom | 2020-04-30 00:00:00 |       6005 |         747 |  174413 |    23237 | True         |
| 89 | Spain          | 2020-04-30 00:00:00 |       6854 |         706 |  245751 |    25243 | True         |
| 99 | US             | 2020-04-30 00:00:00 |      37531 |        2483 | 1085878 |    63301 | True         |
| 86 | Belgium        | 2020-04-30 00:00:00 |       1499 |         271 |   50333 |     7854 | True         |
| 97 | France         | 2020-04-30 00:00:00 |       5005 |         771 |  178110 |    25205 | True         |