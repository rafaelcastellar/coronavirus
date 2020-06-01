# **Predictions**
For experience, I'm running simple predictions over the cases and deaths per day. As they are time-series, I'm using [Facebook Prophet](https://facebook.github.io/prophet/docs/quick_start.html) that is also designed for this kind of prediction in a very simpler way. It works well for most of the time; sometimes there is a huge leap and it takes more time and more data to be understood.

These predictions were made with Covid19 pandemic data from **2020-05-31**.

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
|  91 | Brazil    | 2020-05-27 00:00:00 |      20599 |        1086 |  411821 |    25598 | False        |
|  92 | Brazil    | 2020-05-28 00:00:00 |      26417 |        1156 |  438238 |    26754 | False        |
|  93 | Brazil    | 2020-05-29 00:00:00 |      26928 |        1124 |  465166 |    27878 | False        |
|  94 | Brazil    | 2020-05-30 00:00:00 |      33274 |         956 |  498440 |    28834 | False        |
|  95 | Brazil    | 2020-05-31 00:00:00 |      16409 |         480 |  514849 |    29314 | False        |
|  96 | Brazil    | 2020-06-01 00:00:00 |      21174 |         982 |  536023 |    30296 | True         |
|  97 | Brazil    | 2020-06-02 00:00:00 |      22433 |        1106 |  558456 |    31402 | True         |
|  98 | Brazil    | 2020-06-03 00:00:00 |      24101 |        1102 |  582557 |    32504 | True         |
|  99 | Brazil    | 2020-06-04 00:00:00 |      24790 |        1158 |  607347 |    33662 | True         |
| 100 | Brazil    | 2020-06-05 00:00:00 |      25553 |        1167 |  632900 |    34829 | True         |
| 101 | Brazil    | 2020-06-06 00:00:00 |      25609 |        1123 |  658509 |    35952 | True         |
| 102 | Brazil    | 2020-06-07 00:00:00 |      23859 |        1023 |  682368 |    36975 | True         |
| 103 | Brazil    | 2020-06-08 00:00:00 |      24867 |        1113 |  707235 |    38088 | True         |
| 104 | Brazil    | 2020-06-09 00:00:00 |      26126 |        1237 |  733361 |    39325 | True         |
| 105 | Brazil    | 2020-06-10 00:00:00 |      27794 |        1233 |  761155 |    40558 | True         |

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
|  96 | Brazil         | 2020-06-01 00:00:00 |      21174 |         982 |  536023 |    30296 | True         |
| 122 | Italy          | 2020-06-01 00:00:00 |       -319 |          74 |  232678 |    33489 | True         |
| 122 | United Kingdom | 2020-06-01 00:00:00 |       2802 |         534 |  279373 |    39105 | True         |
| 121 | Spain          | 2020-06-01 00:00:00 |       1581 |        -100 |  241423 |    27027 | True         |
| 131 | US             | 2020-06-01 00:00:00 |      29978 |        1717 | 1820150 |   106098 | True         |
| 118 | Belgium        | 2020-06-01 00:00:00 |         56 |          36 |   58437 |     9503 | True         |
| 129 | France         | 2020-06-01 00:00:00 |        623 |         177 |  189802 |    28982 | True         |

 **The day after tomorrow** 
|     | country        | ds                  |   case_day |   death_day |   cases |   deaths | predicted?   |
|----:|:---------------|:--------------------|-----------:|------------:|--------:|---------:|:-------------|
|  97 | Brazil         | 2020-06-02 00:00:00 |      22433 |        1106 |  558456 |    31402 | True         |
| 123 | Italy          | 2020-06-02 00:00:00 |       -334 |          90 |  232344 |    33579 | True         |
| 123 | United Kingdom | 2020-06-02 00:00:00 |       2911 |         725 |  282284 |    39830 | True         |
| 122 | Spain          | 2020-06-02 00:00:00 |       2074 |           0 |  243497 |    27027 | True         |
| 132 | US             | 2020-06-02 00:00:00 |      30744 |        2031 | 1850894 |   108129 | True         |
| 119 | Belgium        | 2020-06-02 00:00:00 |          0 |          58 |   58437 |     9561 | True         |
| 130 | France         | 2020-06-02 00:00:00 |        725 |         198 |  190527 |    29180 | True         |