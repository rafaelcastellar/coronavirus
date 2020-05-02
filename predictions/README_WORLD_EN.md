# **Predictions**
For experience, I'm running simple predictions over the cases and deaths per day. As they are time-series, I'm using [Facebook Prophet](https://facebook.github.io/prophet/docs/quick_start.html) that is also designed for this kind of prediction in a very simpler way. It works well for most of the time; sometimes there is a huge leap and it takes more time and more data to be understood.

These predictions were made with Covid19 pandemic data from **2020-05-01**.

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
| 61 | Brazil    | 2020-04-27 00:00:00 |       4346 |         317 |   67446 |     4603 | False        |
| 62 | Brazil    | 2020-04-28 00:00:00 |       5789 |         480 |   73235 |     5083 | False        |
| 63 | Brazil    | 2020-04-29 00:00:00 |       6450 |         430 |   79685 |     5513 | False        |
| 64 | Brazil    | 2020-04-30 00:00:00 |       7502 |         493 |   87187 |     6006 | False        |
| 65 | Brazil    | 2020-05-01 00:00:00 |       5015 |         406 |   92202 |     6412 | False        |
| 66 | Brazil    | 2020-05-02 00:00:00 |       5511 |         372 |   97713 |     6784 | True         |
| 67 | Brazil    | 2020-05-03 00:00:00 |       5324 |         351 |  103037 |     7135 | True         |
| 68 | Brazil    | 2020-05-04 00:00:00 |       5472 |         372 |  108509 |     7507 | True         |
| 69 | Brazil    | 2020-05-05 00:00:00 |       6000 |         416 |  114509 |     7923 | True         |
| 70 | Brazil    | 2020-05-06 00:00:00 |       6375 |         421 |  120884 |     8344 | True         |
| 71 | Brazil    | 2020-05-07 00:00:00 |       6658 |         462 |  127542 |     8806 | True         |
| 72 | Brazil    | 2020-05-08 00:00:00 |       6535 |         448 |  134077 |     9254 | True         |
| 73 | Brazil    | 2020-05-09 00:00:00 |       6760 |         449 |  140837 |     9703 | True         |
| 74 | Brazil    | 2020-05-10 00:00:00 |       6574 |         428 |  147411 |    10131 | True         |
| 75 | Brazil    | 2020-05-11 00:00:00 |       6721 |         449 |  154132 |    10580 | True         |

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
|  66 | Brazil         | 2020-05-02 00:00:00 |       5511 |         372 |   97713 |     6784 | True         |
|  92 | Italy          | 2020-05-02 00:00:00 |       5030 |         711 |  212458 |    28947 | True         |
|  92 | United Kingdom | 2020-05-02 00:00:00 |       6211 |         894 |  184896 |    28477 | True         |
|  91 | Spain          | 2020-05-02 00:00:00 |       5080 |         616 |  218515 |    25159 | True         |
| 101 | US             | 2020-05-02 00:00:00 |      33954 |        2485 | 1137415 |    67428 | True         |
|  88 | Belgium        | 2020-05-02 00:00:00 |       1480 |         250 |   50512 |     7953 | True         |
|  99 | France         | 2020-05-02 00:00:00 |       3822 |         675 |  171127 |    25303 | True         |

 **The day after tomorrow** 
|     | country        | ds                  |   case_day |   death_day |   cases |   deaths | predicted?   |
|----:|:---------------|:--------------------|-----------:|------------:|--------:|---------:|:-------------|
|  67 | Brazil         | 2020-05-03 00:00:00 |       5324 |         351 |  103037 |     7135 | True         |
|  93 | Italy          | 2020-05-03 00:00:00 |       4830 |         670 |  217288 |    29617 | True         |
|  93 | United Kingdom | 2020-05-03 00:00:00 |       6344 |         785 |  191240 |    29262 | True         |
|  92 | Spain          | 2020-05-03 00:00:00 |       5124 |         645 |  223639 |    25804 | True         |
| 102 | US             | 2020-05-03 00:00:00 |      32877 |        2336 | 1170292 |    69764 | True         |
|  89 | Belgium        | 2020-05-03 00:00:00 |       1467 |         235 |   51979 |     8188 | True         |
| 100 | France         | 2020-05-03 00:00:00 |       5407 |         603 |  176534 |    25906 | True         |