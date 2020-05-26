# **Predictions**
For experience, I'm running simple predictions over the cases and deaths per day. As they are time-series, I'm using [Facebook Prophet](https://facebook.github.io/prophet/docs/quick_start.html) that is also designed for this kind of prediction in a very simpler way. It works well for most of the time; sometimes there is a huge leap and it takes more time and more data to be understood.

These predictions were made with Covid19 pandemic data from **2020-05-25**.

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
| 85 | Brazil    | 2020-05-21 00:00:00 |      18508 |        1188 |  310087 |    20047 | False        |
| 86 | Brazil    | 2020-05-22 00:00:00 |      20803 |        1001 |  330890 |    21048 | False        |
| 87 | Brazil    | 2020-05-23 00:00:00 |      16508 |         965 |  347398 |    22013 | False        |
| 88 | Brazil    | 2020-05-24 00:00:00 |      15813 |         653 |  363211 |    22666 | False        |
| 89 | Brazil    | 2020-05-25 00:00:00 |      11687 |         807 |  374898 |    23473 | False        |
| 90 | Brazil    | 2020-05-26 00:00:00 |      16735 |         995 |  391633 |    24468 | True         |
| 91 | Brazil    | 2020-05-27 00:00:00 |      18062 |         987 |  409695 |    25455 | True         |
| 92 | Brazil    | 2020-05-28 00:00:00 |      18272 |        1042 |  427967 |    26497 | True         |
| 93 | Brazil    | 2020-05-29 00:00:00 |      18953 |        1055 |  446920 |    27552 | True         |
| 94 | Brazil    | 2020-05-30 00:00:00 |      18432 |        1021 |  465352 |    28573 | True         |
| 95 | Brazil    | 2020-05-31 00:00:00 |      17752 |         951 |  483104 |    29524 | True         |
| 96 | Brazil    | 2020-06-01 00:00:00 |      18377 |        1011 |  501481 |    30535 | True         |
| 97 | Brazil    | 2020-06-02 00:00:00 |      19583 |        1133 |  521064 |    31668 | True         |
| 98 | Brazil    | 2020-06-03 00:00:00 |      20909 |        1124 |  541973 |    32792 | True         |
| 99 | Brazil    | 2020-06-04 00:00:00 |      21120 |        1179 |  563093 |    33971 | True         |

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
|  90 | Brazil         | 2020-05-26 00:00:00 |      16735 |         995 |  391633 |    24468 | True         |
| 116 | Italy          | 2020-05-26 00:00:00 |         74 |         154 |  230232 |    33031 | True         |
| 116 | United Kingdom | 2020-05-26 00:00:00 |       3761 |         815 |  266723 |    37811 | True         |
| 115 | Spain          | 2020-05-26 00:00:00 |       2400 |          82 |  238163 |    26916 | True         |
| 125 | US             | 2020-05-26 00:00:00 |      31066 |        2118 | 1693368 |   100338 | True         |
| 112 | Belgium        | 2020-05-26 00:00:00 |        218 |          85 |   57560 |     9397 | True         |
| 123 | France         | 2020-05-26 00:00:00 |        831 |         355 |  184013 |    28815 | True         |

 **The day after tomorrow** 
|     | country        | ds                  |   case_day |   death_day |   cases |   deaths | predicted?   |
|----:|:---------------|:--------------------|-----------:|------------:|--------:|---------:|:-------------|
|  91 | Brazil         | 2020-05-27 00:00:00 |      18062 |         987 |  409695 |    25455 | True         |
| 117 | Italy          | 2020-05-27 00:00:00 |        219 |         137 |  230451 |    33168 | True         |
| 117 | United Kingdom | 2020-05-27 00:00:00 |       3850 |         773 |  270573 |    38584 | True         |
| 116 | Spain          | 2020-05-27 00:00:00 |       3015 |         141 |  241178 |    27057 | True         |
| 126 | US             | 2020-05-27 00:00:00 |      32047 |        2165 | 1725415 |   102503 | True         |
| 113 | Belgium        | 2020-05-27 00:00:00 |        321 |          94 |   57881 |     9491 | True         |
| 124 | France         | 2020-05-27 00:00:00 |         30 |         367 |  184043 |    29182 | True         |