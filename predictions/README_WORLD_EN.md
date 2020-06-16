# **Predictions**
For experience, I'm running simple predictions over the cases and deaths per day. As they are time-series, I'm using [Facebook Prophet](https://facebook.github.io/prophet/docs/quick_start.html) that is also designed for this kind of prediction in a very simpler way. It works well for most of the time; sometimes there is a huge leap and it takes more time and more data to be understood.

These predictions were made with Covid19 pandemic data from **2020-06-15**.

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
| 106 | Brazil    | 2020-06-11 00:00:00 |      30412 |        1239 |  802828 |    40919 | False        |
| 107 | Brazil    | 2020-06-12 00:00:00 |      25982 |         909 |  828810 |    41828 | False        |
| 108 | Brazil    | 2020-06-13 00:00:00 |      21704 |         892 |  850514 |    42720 | False        |
| 109 | Brazil    | 2020-06-14 00:00:00 |      17110 |         612 |  867624 |    43332 | False        |
| 110 | Brazil    | 2020-06-15 00:00:00 |      20647 |         627 |  888271 |    43959 | False        |
| 111 | Brazil    | 2020-06-16 00:00:00 |      28859 |        1213 |  917130 |    45172 | True         |
| 112 | Brazil    | 2020-06-17 00:00:00 |      30296 |        1214 |  947426 |    46386 | True         |
| 113 | Brazil    | 2020-06-18 00:00:00 |      30840 |        1264 |  978266 |    47650 | True         |
| 114 | Brazil    | 2020-06-19 00:00:00 |      31181 |        1219 | 1009447 |    48869 | True         |
| 115 | Brazil    | 2020-06-20 00:00:00 |      30690 |        1169 | 1040137 |    50038 | True         |
| 116 | Brazil    | 2020-06-21 00:00:00 |      28312 |        1038 | 1068449 |    51076 | True         |
| 117 | Brazil    | 2020-06-22 00:00:00 |      28562 |        1102 | 1097011 |    52178 | True         |
| 118 | Brazil    | 2020-06-23 00:00:00 |      32166 |        1313 | 1129177 |    53491 | True         |
| 119 | Brazil    | 2020-06-24 00:00:00 |      33603 |        1314 | 1162780 |    54805 | True         |
| 120 | Brazil    | 2020-06-25 00:00:00 |      34147 |        1364 | 1196927 |    56169 | True         |

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
| 111 | Brazil         | 2020-06-16 00:00:00 |      28859 |        1213 |  917130 |    45172 | True         |
| 137 | Italy          | 2020-06-16 00:00:00 |       -699 |         -17 |  236591 |    34354 | True         |
| 137 | United Kingdom | 2020-06-16 00:00:00 |       1243 |         301 |  299973 |    42122 | True         |
| 136 | Spain          | 2020-06-16 00:00:00 |       1097 |         -65 |  245569 |    27071 | True         |
| 146 | US             | 2020-06-16 00:00:00 |      23660 |        1281 | 2137686 |   117408 | True         |
| 133 | Belgium        | 2020-06-16 00:00:00 |       -127 |           2 |   59973 |     9663 | True         |
| 144 | France         | 2020-06-16 00:00:00 |        207 |          38 |  197223 |    29477 | True         |

 **The day after tomorrow** 
|     | country        | ds                  |   case_day |   death_day |   cases |   deaths | predicted?   |
|----:|:---------------|:--------------------|-----------:|------------:|--------:|---------:|:-------------|
| 112 | Brazil         | 2020-06-17 00:00:00 |      30296 |        1214 |  947426 |    46386 | True         |
| 138 | Italy          | 2020-06-17 00:00:00 |       -565 |         -29 |  236026 |    34325 | True         |
| 138 | United Kingdom | 2020-06-17 00:00:00 |       1144 |         270 |  301117 |    42392 | True         |
| 137 | Spain          | 2020-06-17 00:00:00 |       1578 |         -31 |  247147 |    27040 | True         |
| 147 | US             | 2020-06-17 00:00:00 |      24587 |        1345 | 2162273 |   118753 | True         |
| 134 | Belgium        | 2020-06-17 00:00:00 |        -38 |           9 |   59935 |     9672 | True         |
| 145 | France         | 2020-06-17 00:00:00 |       -231 |          39 |  196992 |    29516 | True         |