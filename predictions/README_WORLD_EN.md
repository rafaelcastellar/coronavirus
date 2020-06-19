# **Predictions**
For experience, I'm running simple predictions over the cases and deaths per day. As they are time-series, I'm using [Facebook Prophet](https://facebook.github.io/prophet/docs/quick_start.html) that is also designed for this kind of prediction in a very simpler way. It works well for most of the time; sometimes there is a huge leap and it takes more time and more data to be understood.

These predictions were made with Covid19 pandemic data from **2020-06-18**.

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
| 109 | Brazil    | 2020-06-14 00:00:00 |      17110 |         612 |  867624 |    43332 | False        |
| 110 | Brazil    | 2020-06-15 00:00:00 |      20647 |         627 |  888271 |    43959 | False        |
| 111 | Brazil    | 2020-06-16 00:00:00 |      34918 |        1282 |  923189 |    45241 | False        |
| 112 | Brazil    | 2020-06-17 00:00:00 |      32188 |        1269 |  955377 |    46510 | False        |
| 113 | Brazil    | 2020-06-18 00:00:00 |      22765 |        1238 |  978142 |    47748 | False        |
| 114 | Brazil    | 2020-06-19 00:00:00 |      30948 |        1232 | 1009090 |    48980 | True         |
| 115 | Brazil    | 2020-06-20 00:00:00 |      30440 |        1182 | 1039530 |    50162 | True         |
| 116 | Brazil    | 2020-06-21 00:00:00 |      28056 |        1051 | 1067586 |    51213 | True         |
| 117 | Brazil    | 2020-06-22 00:00:00 |      28301 |        1115 | 1095887 |    52328 | True         |
| 118 | Brazil    | 2020-06-23 00:00:00 |      32268 |        1331 | 1128155 |    53659 | True         |
| 119 | Brazil    | 2020-06-24 00:00:00 |      33446 |        1331 | 1161601 |    54990 | True         |
| 120 | Brazil    | 2020-06-25 00:00:00 |      33398 |        1377 | 1194999 |    56367 | True         |
| 121 | Brazil    | 2020-06-26 00:00:00 |      34193 |        1335 | 1229192 |    57702 | True         |
| 122 | Brazil    | 2020-06-27 00:00:00 |      33685 |        1285 | 1262877 |    58987 | True         |
| 123 | Brazil    | 2020-06-28 00:00:00 |      31301 |        1154 | 1294178 |    60141 | True         |

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
| 114 | Brazil         | 2020-06-19 00:00:00 |      30948 |        1232 | 1009090 |    48980 | True         |
| 140 | Italy          | 2020-06-19 00:00:00 |       -410 |         -17 |  237749 |    34497 | True         |
| 140 | United Kingdom | 2020-06-19 00:00:00 |       1589 |         289 |  303939 |    42662 | True         |
| 139 | Spain          | 2020-06-19 00:00:00 |       1205 |         -48 |  246836 |    27088 | True         |
| 149 | US             | 2020-06-19 00:00:00 |      27175 |        1048 | 2218227 |   119482 | True         |
| 136 | Belgium        | 2020-06-19 00:00:00 |         30 |          -5 |   60378 |     9678 | True         |
| 147 | France         | 2020-06-19 00:00:00 |       -111 |          21 |  197872 |    29627 | True         |

 **The day after tomorrow** 
|     | country        | ds                  |   case_day |   death_day |   cases |   deaths | predicted?   |
|----:|:---------------|:--------------------|-----------:|------------:|--------:|---------:|:-------------|
| 115 | Brazil         | 2020-06-20 00:00:00 |      30440 |        1182 | 1039530 |    50162 | True         |
| 141 | Italy          | 2020-06-20 00:00:00 |       -373 |         -26 |  237376 |    34471 | True         |
| 141 | United Kingdom | 2020-06-20 00:00:00 |       1077 |         237 |  305016 |    42899 | True         |
| 140 | Spain          | 2020-06-20 00:00:00 |        863 |         -98 |  247699 |    26990 | True         |
| 150 | US             | 2020-06-20 00:00:00 |      26084 |         965 | 2244311 |   120447 | True         |
| 137 | Belgium        | 2020-06-20 00:00:00 |          4 |         -21 |   60382 |     9657 | True         |
| 148 | France         | 2020-06-20 00:00:00 |       -305 |         -35 |  197567 |    29592 | True         |