# **Predictions**
For experience, I'm running simple predictions over the cases and deaths per day. As they are time-series, I'm using [Facebook Prophet](https://facebook.github.io/prophet/docs/quick_start.html) that is also designed for this kind of prediction in a very simpler way. It works well for most of the time; sometimes there is a huge leap and it takes more time and more data to be understood.

These predictions were made with Covid19 pandemic data from **2020-05-04**.

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
| 64 | Brazil    | 2020-04-30 00:00:00 |       7502 |         493 |   87187 |     6006 | False        |
| 65 | Brazil    | 2020-05-01 00:00:00 |       5015 |         406 |   92202 |     6412 | False        |
| 66 | Brazil    | 2020-05-02 00:00:00 |       4898 |         349 |   97100 |     6761 | False        |
| 67 | Brazil    | 2020-05-03 00:00:00 |       4726 |         290 |  101826 |     7051 | False        |
| 68 | Brazil    | 2020-05-04 00:00:00 |       6794 |         316 |  108620 |     7367 | False        |
| 69 | Brazil    | 2020-05-05 00:00:00 |       5958 |         394 |  114578 |     7761 | True         |
| 70 | Brazil    | 2020-05-06 00:00:00 |       6336 |         399 |  120914 |     8160 | True         |
| 71 | Brazil    | 2020-05-07 00:00:00 |       6615 |         438 |  127529 |     8598 | True         |
| 72 | Brazil    | 2020-05-08 00:00:00 |       6488 |         423 |  134017 |     9021 | True         |
| 73 | Brazil    | 2020-05-09 00:00:00 |       6646 |         420 |  140663 |     9441 | True         |
| 74 | Brazil    | 2020-05-10 00:00:00 |       6459 |         394 |  147122 |     9835 | True         |
| 75 | Brazil    | 2020-05-11 00:00:00 |       6798 |         415 |  153920 |    10250 | True         |
| 76 | Brazil    | 2020-05-12 00:00:00 |       7188 |         462 |  161108 |    10712 | True         |
| 77 | Brazil    | 2020-05-13 00:00:00 |       7566 |         467 |  168674 |    11179 | True         |
| 78 | Brazil    | 2020-05-14 00:00:00 |       7845 |         506 |  176519 |    11685 | True         |

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
|  69 | Brazil         | 2020-05-05 00:00:00 |       5958 |         394 |  114578 |     7761 | True         |
|  95 | Italy          | 2020-05-05 00:00:00 |       4133 |         582 |  216071 |    29661 | True         |
|  95 | United Kingdom | 2020-05-05 00:00:00 |       5820 |         916 |  197652 |    29725 | True         |
|  94 | Spain          | 2020-05-05 00:00:00 |       4667 |         601 |  222678 |    26029 | True         |
| 104 | US             | 2020-05-05 00:00:00 |      33579 |        2288 | 1213954 |    71210 | True         |
|  91 | Belgium        | 2020-05-05 00:00:00 |       1201 |         246 |   51468 |     8170 | True         |
| 102 | France         | 2020-05-05 00:00:00 |       4130 |         691 |  173713 |    25895 | True         |

 **The day after tomorrow** 
|     | country        | ds                  |   case_day |   death_day |   cases |   deaths | predicted?   |
|----:|:---------------|:--------------------|-----------:|------------:|--------:|---------:|:-------------|
|  70 | Brazil         | 2020-05-06 00:00:00 |       6336 |         399 |  120914 |     8160 | True         |
|  96 | Italy          | 2020-05-06 00:00:00 |       4439 |         558 |  220510 |    30219 | True         |
|  96 | United Kingdom | 2020-05-06 00:00:00 |       6082 |         892 |  203734 |    30617 | True         |
|  95 | Spain          | 2020-05-06 00:00:00 |       5450 |         677 |  228128 |    26706 | True         |
| 105 | US             | 2020-05-06 00:00:00 |      34556 |        2338 | 1248510 |    73548 | True         |
|  92 | Belgium        | 2020-05-06 00:00:00 |       1365 |         241 |   52833 |     8411 | True         |
| 103 | France         | 2020-05-06 00:00:00 |       3124 |         710 |  176837 |    26605 | True         |