# **Predictions**
For experience, I'm running simple predictions over the cases and deaths per day. As they are time-series, I'm using [Facebook Prophet](https://facebook.github.io/prophet/docs/quick_start.html) that is also designed for this kind of prediction in a very simpler way. It works well for most of the time; sometimes there is a huge leap and it takes more time and more data to be understood.

These predictions were made with Covid19 pandemic data from **2020-06-03**.

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
|  94 | Brazil    | 2020-05-30 00:00:00 |      33274 |         956 |  498440 |    28834 | False        |
|  95 | Brazil    | 2020-05-31 00:00:00 |      16409 |         480 |  514849 |    29314 | False        |
|  96 | Brazil    | 2020-06-01 00:00:00 |      11598 |         623 |  526447 |    29937 | False        |
|  97 | Brazil    | 2020-06-02 00:00:00 |      28936 |        1262 |  555383 |    31199 | False        |
|  98 | Brazil    | 2020-06-03 00:00:00 |      28633 |        1349 |  584016 |    32548 | False        |
|  99 | Brazil    | 2020-06-04 00:00:00 |      24514 |        1162 |  608530 |    33710 | True         |
| 100 | Brazil    | 2020-06-05 00:00:00 |      25269 |        1171 |  633799 |    34881 | True         |
| 101 | Brazil    | 2020-06-06 00:00:00 |      25325 |        1127 |  659124 |    36008 | True         |
| 102 | Brazil    | 2020-06-07 00:00:00 |      23557 |        1028 |  682681 |    37036 | True         |
| 103 | Brazil    | 2020-06-08 00:00:00 |      23855 |        1093 |  706536 |    38129 | True         |
| 104 | Brazil    | 2020-06-09 00:00:00 |      26246 |        1254 |  732782 |    39383 | True         |
| 105 | Brazil    | 2020-06-10 00:00:00 |      27744 |        1255 |  760526 |    40638 | True         |
| 106 | Brazil    | 2020-06-11 00:00:00 |      28105 |        1294 |  788631 |    41932 | True         |
| 107 | Brazil    | 2020-06-12 00:00:00 |      28860 |        1304 |  817491 |    43236 | True         |
| 108 | Brazil    | 2020-06-13 00:00:00 |      28916 |        1259 |  846407 |    44495 | True         |

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
|  99 | Brazil         | 2020-06-04 00:00:00 |      24514 |        1162 |  608530 |    33710 | True         |
| 125 | Italy          | 2020-06-04 00:00:00 |         -7 |          25 |  233829 |    33626 | True         |
| 125 | United Kingdom | 2020-06-04 00:00:00 |       2670 |         684 |  284355 |    40495 | True         |
| 124 | Spain          | 2020-06-04 00:00:00 |       2499 |           8 |  243188 |    27136 | True         |
| 134 | US             | 2020-06-04 00:00:00 |      31756 |        1967 | 1883276 |   109142 | True         |
| 121 | Belgium        | 2020-06-04 00:00:00 |        150 |          50 |   58835 |     9572 | True         |
| 132 | France         | 2020-06-04 00:00:00 |        964 |         186 |  194142 |    29210 | True         |

 **The day after tomorrow** 
|     | country        | ds                  |   case_day |   death_day |   cases |   deaths | predicted?   |
|----:|:---------------|:--------------------|-----------:|------------:|--------:|---------:|:-------------|
| 100 | Brazil         | 2020-06-05 00:00:00 |      25269 |        1171 |  633799 |    34881 | True         |
| 126 | Italy          | 2020-06-05 00:00:00 |        -51 |          45 |  233778 |    33671 | True         |
| 126 | United Kingdom | 2020-06-05 00:00:00 |       3153 |         707 |  287508 |    41202 | True         |
| 125 | Spain          | 2020-06-05 00:00:00 |       2254 |          17 |  245442 |    27153 | True         |
| 135 | US             | 2020-06-05 00:00:00 |      32216 |        1921 | 1915492 |   111063 | True         |
| 122 | Belgium        | 2020-06-05 00:00:00 |        177 |          53 |   59012 |     9625 | True         |
| 133 | France         | 2020-06-05 00:00:00 |        422 |         153 |  194564 |    29363 | True         |