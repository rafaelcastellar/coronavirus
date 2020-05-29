# **Predictions**
For experience, I'm running simple predictions over the cases and deaths per day. As they are time-series, I'm using [Facebook Prophet](https://facebook.github.io/prophet/docs/quick_start.html) that is also designed for this kind of prediction in a very simpler way. It works well for most of the time; sometimes there is a huge leap and it takes more time and more data to be understood.

These predictions were made with Covid19 pandemic data from **2020-05-28**.

As there are many countries to have their data predicted in a row, I selected a few of them plus Brazil to be predicted:
['Brazil', 'Italy', 'United Kingdom', 'Spain', 'US', 'Belgium', 'France'].
***Tip**: you can set yourself at the *[prediction.ipynb](../prediction.ipynb)* notebook which countries you prefer to predict*


## The prediction
As Facebook Prophet predicts time-series data and it is running the prediction over cases per day and deaths per day. After that, I compute theirs cumulatives.It is predicting for the next 10 days.
By the end, a CSV file containing all the predicted data is generated.

#### The Brazil's last 5 days and next predicted 10 days
*predicted? = True* means the line is a prediction; *=False* means they are real numbers.
|     | country   | ds                  |   case_day |   death_day |   cases |   deaths | predicted?   |
|----:|:----------|:--------------------|-----------:|------------:|--------:|---------:|:-------------|
|  88 | Brazil    | 2020-05-24 00:00:00 |      15813 |         653 |  363211 |    22666 | False        |
|  89 | Brazil    | 2020-05-25 00:00:00 |      11687 |         807 |  374898 |    23473 | False        |
|  90 | Brazil    | 2020-05-26 00:00:00 |      16324 |        1039 |  391222 |    24512 | False        |
|  91 | Brazil    | 2020-05-27 00:00:00 |      20599 |        1086 |  411821 |    25598 | False        |
|  92 | Brazil    | 2020-05-28 00:00:00 |      26417 |        1156 |  438238 |    26754 | False        |
|  93 | Brazil    | 2020-05-29 00:00:00 |      20283 |        1085 |  458521 |    27839 | True         |
|  94 | Brazil    | 2020-05-30 00:00:00 |      19832 |        1052 |  478353 |    28891 | True         |
|  95 | Brazil    | 2020-05-31 00:00:00 |      19223 |         984 |  497576 |    29875 | True         |
|  96 | Brazil    | 2020-06-01 00:00:00 |      19887 |        1044 |  517463 |    30919 | True         |
|  97 | Brazil    | 2020-06-02 00:00:00 |      21101 |        1170 |  538564 |    32089 | True         |
|  98 | Brazil    | 2020-06-03 00:00:00 |      22700 |        1166 |  561264 |    33255 | True         |
|  99 | Brazil    | 2020-06-04 00:00:00 |      23359 |        1223 |  584623 |    34478 | True         |
| 100 | Brazil    | 2020-06-05 00:00:00 |      23620 |        1232 |  608243 |    35710 | True         |
| 101 | Brazil    | 2020-06-06 00:00:00 |      23170 |        1199 |  631413 |    36909 | True         |
| 102 | Brazil    | 2020-06-07 00:00:00 |      22560 |        1131 |  653973 |    38040 | True         |

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
|  93 | Brazil         | 2020-05-29 00:00:00 |      20283 |        1085 |  458521 |    27839 | True         |
| 119 | Italy          | 2020-05-29 00:00:00 |        422 |         143 |  232154 |    33285 | True         |
| 119 | United Kingdom | 2020-05-29 00:00:00 |       4338 |         747 |  275261 |    38666 | True         |
| 118 | Spain          | 2020-05-29 00:00:00 |       2696 |          73 |  240965 |    27192 | True         |
| 128 | US             | 2020-05-29 00:00:00 |      33517 |        1983 | 1755270 |   103599 | True         |
| 115 | Belgium        | 2020-05-29 00:00:00 |        329 |          69 |   58178 |     9457 | True         |
| 126 | France         | 2020-05-29 00:00:00 |        421 |         262 |  186955 |    28927 | True         |

 **The day after tomorrow** 
|     | country        | ds                  |   case_day |   death_day |   cases |   deaths | predicted?   |
|----:|:---------------|:--------------------|-----------:|------------:|--------:|---------:|:-------------|
|  94 | Brazil         | 2020-05-30 00:00:00 |      19832 |        1052 |  478353 |    28891 | True         |
| 120 | Italy          | 2020-05-30 00:00:00 |        467 |         131 |  232621 |    33416 | True         |
| 120 | United Kingdom | 2020-05-30 00:00:00 |       3815 |         713 |  279076 |    39379 | True         |
| 119 | Spain          | 2020-05-30 00:00:00 |       2340 |          17 |  243305 |    27209 | True         |
| 129 | US             | 2020-05-30 00:00:00 |      32903 |        1950 | 1788173 |   105549 | True         |
| 116 | Belgium        | 2020-05-30 00:00:00 |        302 |          52 |   58480 |     9509 | True         |
| 127 | France         | 2020-05-30 00:00:00 |        129 |         200 |  187084 |    29127 | True         |