# **Predictions**
For experience, I'm running simple predictions over the cases and deaths per day. As they are time-series, I'm using [Facebook Prophet](https://facebook.github.io/prophet/docs/quick_start.html) that is also designed for this kind of prediction in a very simpler way. It works well for most of the time; sometimes there is a huge leap and it takes more time and more data to be understood.

These predictions were made with Covid19 pandemic data from **2020-05-12**.

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
| 72 | Brazil    | 2020-05-08 00:00:00 |      11121 |         827 |  146894 |    10017 | False        |
| 73 | Brazil    | 2020-05-09 00:00:00 |       9167 |         639 |  156061 |    10656 | False        |
| 74 | Brazil    | 2020-05-10 00:00:00 |       6638 |         467 |  162699 |    11123 | False        |
| 75 | Brazil    | 2020-05-11 00:00:00 |       6895 |         530 |  169594 |    11653 | False        |
| 76 | Brazil    | 2020-05-12 00:00:00 |       8620 |         808 |  178214 |    12461 | False        |
| 77 | Brazil    | 2020-05-13 00:00:00 |       9337 |         645 |  187551 |    13106 | True         |
| 78 | Brazil    | 2020-05-14 00:00:00 |       9445 |         682 |  196996 |    13788 | True         |
| 79 | Brazil    | 2020-05-15 00:00:00 |       9543 |         694 |  206539 |    14482 | True         |
| 80 | Brazil    | 2020-05-16 00:00:00 |       9547 |         679 |  216086 |    15161 | True         |
| 81 | Brazil    | 2020-05-17 00:00:00 |       9194 |         645 |  225280 |    15806 | True         |
| 82 | Brazil    | 2020-05-18 00:00:00 |       9555 |         674 |  234835 |    16480 | True         |
| 83 | Brazil    | 2020-05-19 00:00:00 |      10177 |         762 |  245012 |    17242 | True         |
| 84 | Brazil    | 2020-05-20 00:00:00 |      10968 |         762 |  255980 |    18004 | True         |
| 85 | Brazil    | 2020-05-21 00:00:00 |      11076 |         799 |  267056 |    18803 | True         |
| 86 | Brazil    | 2020-05-22 00:00:00 |      11175 |         811 |  278231 |    19614 | True         |

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
|  77 | Brazil         | 2020-05-13 00:00:00 |       9337 |         645 |  187551 |    13106 | True         |
| 103 | Italy          | 2020-05-13 00:00:00 |       3807 |         572 |  225023 |    31483 | True         |
| 103 | United Kingdom | 2020-05-13 00:00:00 |       5983 |         854 |  233724 |    33623 | True         |
| 102 | Spain          | 2020-05-13 00:00:00 |       4644 |         564 |  242699 |    27484 | True         |
| 112 | US             | 2020-05-13 00:00:00 |      33040 |        2286 | 1402416 |    84642 | True         |
|  99 | Belgium        | 2020-05-13 00:00:00 |        954 |         235 |   54733 |     8996 | True         |
| 110 | France         | 2020-05-13 00:00:00 |       2851 |         616 |  183660 |    27610 | True         |

 **The day after tomorrow** 
|     | country        | ds                  |   case_day |   death_day |   cases |   deaths | predicted?   |
|----:|:---------------|:--------------------|-----------:|------------:|--------:|---------:|:-------------|
|  78 | Brazil         | 2020-05-14 00:00:00 |       9445 |         682 |  196996 |    13788 | True         |
| 104 | Italy          | 2020-05-14 00:00:00 |       3833 |         554 |  228856 |    32037 | True         |
| 104 | United Kingdom | 2020-05-14 00:00:00 |       6022 |         847 |  239746 |    34470 | True         |
| 103 | Spain          | 2020-05-14 00:00:00 |       4610 |         540 |  247309 |    28024 | True         |
| 113 | US             | 2020-05-14 00:00:00 |      34707 |        2239 | 1437123 |    86881 | True         |
| 100 | Belgium        | 2020-05-14 00:00:00 |        979 |         228 |   55712 |     9224 | True         |
| 111 | France         | 2020-05-14 00:00:00 |       3523 |         628 |  187183 |    28238 | True         |