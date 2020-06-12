# **Predictions**
For experience, I'm running simple predictions over the cases and deaths per day. As they are time-series, I'm using [Facebook Prophet](https://facebook.github.io/prophet/docs/quick_start.html) that is also designed for this kind of prediction in a very simpler way. It works well for most of the time; sometimes there is a huge leap and it takes more time and more data to be understood.

These predictions were made with Covid19 pandemic data from **2020-06-11**.

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
| 102 | Brazil    | 2020-06-07 00:00:00 |      18912 |         525 |  691758 |    36455 | False        |
| 103 | Brazil    | 2020-06-08 00:00:00 |      15654 |         679 |  707412 |    37134 | False        |
| 104 | Brazil    | 2020-06-09 00:00:00 |      32091 |        1272 |  739503 |    38406 | False        |
| 105 | Brazil    | 2020-06-10 00:00:00 |      32913 |        1274 |  772416 |    39680 | False        |
| 106 | Brazil    | 2020-06-11 00:00:00 |      30412 |        1239 |  802828 |    40919 | False        |
| 107 | Brazil    | 2020-06-12 00:00:00 |      30105 |        1225 |  832933 |    42144 | True         |
| 108 | Brazil    | 2020-06-13 00:00:00 |      29908 |        1175 |  862841 |    43319 | True         |
| 109 | Brazil    | 2020-06-14 00:00:00 |      27718 |        1055 |  890559 |    44374 | True         |
| 110 | Brazil    | 2020-06-15 00:00:00 |      27795 |        1124 |  918354 |    45498 | True         |
| 111 | Brazil    | 2020-06-16 00:00:00 |      31153 |        1312 |  949507 |    46810 | True         |
| 112 | Brazil    | 2020-06-17 00:00:00 |      32658 |        1315 |  982165 |    48125 | True         |
| 113 | Brazil    | 2020-06-18 00:00:00 |      33261 |        1367 | 1015426 |    49492 | True         |
| 114 | Brazil    | 2020-06-19 00:00:00 |      33921 |        1344 | 1049347 |    50836 | True         |
| 115 | Brazil    | 2020-06-20 00:00:00 |      33723 |        1294 | 1083070 |    52130 | True         |
| 116 | Brazil    | 2020-06-21 00:00:00 |      31534 |        1174 | 1114604 |    53304 | True         |

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
| 107 | Brazil         | 2020-06-12 00:00:00 |      30105 |        1225 |  832933 |    42144 | True         |
| 133 | Italy          | 2020-06-12 00:00:00 |       -232 |          12 |  235910 |    34179 | True         |
| 133 | United Kingdom | 2020-06-12 00:00:00 |       2106 |         384 |  295381 |    41748 | True         |
| 132 | Spain          | 2020-06-12 00:00:00 |       1672 |         -23 |  244742 |    27113 | True         |
| 142 | US             | 2020-06-12 00:00:00 |      27261 |        1778 | 2050608 |   115598 | True         |
| 129 | Belgium        | 2020-06-12 00:00:00 |         84 |          28 |   59795 |     9664 | True         |
| 140 | France         | 2020-06-12 00:00:00 |         52 |          77 |  195256 |    29426 | True         |

 **The day after tomorrow** 
|     | country        | ds                  |   case_day |   death_day |   cases |   deaths | predicted?   |
|----:|:---------------|:--------------------|-----------:|------------:|--------:|---------:|:-------------|
| 108 | Brazil         | 2020-06-13 00:00:00 |      29908 |        1175 |  862841 |    43319 | True         |
| 134 | Italy          | 2020-06-13 00:00:00 |       -201 |           1 |  235709 |    34180 | True         |
| 134 | United Kingdom | 2020-06-13 00:00:00 |       1572 |         331 |  296953 |    42079 | True         |
| 133 | Spain          | 2020-06-13 00:00:00 |       1305 |         -73 |  246047 |    27040 | True         |
| 143 | US             | 2020-06-13 00:00:00 |      26167 |        1714 | 2076775 |   117312 | True         |
| 130 | Belgium        | 2020-06-13 00:00:00 |         57 |          11 |   59852 |     9675 | True         |
| 141 | France         | 2020-06-13 00:00:00 |       -144 |          19 |  195112 |    29445 | True         |