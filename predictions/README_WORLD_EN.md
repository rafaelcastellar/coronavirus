# **Predictions**
For experience, I'm running simple predictions over the cases and deaths per day. As they are time-series, I'm using [Facebook Prophet](https://facebook.github.io/prophet/docs/quick_start.html) that is also designed for this kind of prediction in a very simpler way. It works well for most of the time; sometimes there is a huge leap and it takes more time and more data to be understood.

These predictions were made with Covid19 pandemic data from **2020-05-03**.

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
| 63 | Brazil    | 2020-04-29 00:00:00 |       6450 |         430 |   79685 |     5513 | False        |
| 64 | Brazil    | 2020-04-30 00:00:00 |       7502 |         493 |   87187 |     6006 | False        |
| 65 | Brazil    | 2020-05-01 00:00:00 |       5015 |         406 |   92202 |     6412 | False        |
| 66 | Brazil    | 2020-05-02 00:00:00 |       4898 |         349 |   97100 |     6761 | False        |
| 67 | Brazil    | 2020-05-03 00:00:00 |       4726 |         290 |  101826 |     7051 | False        |
| 68 | Brazil    | 2020-05-04 00:00:00 |       5243 |         357 |  107069 |     7408 | True         |
| 69 | Brazil    | 2020-05-05 00:00:00 |       5759 |         401 |  112828 |     7809 | True         |
| 70 | Brazil    | 2020-05-06 00:00:00 |       6123 |         406 |  118951 |     8215 | True         |
| 71 | Brazil    | 2020-05-07 00:00:00 |       6393 |         446 |  125344 |     8661 | True         |
| 72 | Brazil    | 2020-05-08 00:00:00 |       6257 |         431 |  131601 |     9092 | True         |
| 73 | Brazil    | 2020-05-09 00:00:00 |       6409 |         428 |  138010 |     9520 | True         |
| 74 | Brazil    | 2020-05-10 00:00:00 |       6218 |         403 |  144228 |     9923 | True         |
| 75 | Brazil    | 2020-05-11 00:00:00 |       6391 |         428 |  150619 |    10351 | True         |
| 76 | Brazil    | 2020-05-12 00:00:00 |       6907 |         472 |  157526 |    10823 | True         |
| 77 | Brazil    | 2020-05-13 00:00:00 |       7271 |         477 |  164797 |    11300 | True         |

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
|  68 | Brazil         | 2020-05-04 00:00:00 |       5243 |         357 |  107069 |     7408 | True         |
|  94 | Italy          | 2020-05-04 00:00:00 |       4210 |         670 |  214927 |    29554 | True         |
|  94 | United Kingdom | 2020-05-04 00:00:00 |       5847 |         774 |  193689 |    29294 | True         |
|  93 | Spain          | 2020-05-04 00:00:00 |       4829 |         641 |  222295 |    25905 | True         |
| 103 | US             | 2020-05-04 00:00:00 |      32835 |        2126 | 1190875 |    69808 | True         |
|  90 | Belgium        | 2020-05-04 00:00:00 |       1250 |         219 |   51156 |     8063 | True         |
| 101 | France         | 2020-05-04 00:00:00 |       4025 |         626 |  172950 |    25526 | True         |

 **The day after tomorrow** 
|     | country        | ds                  |   case_day |   death_day |   cases |   deaths | predicted?   |
|----:|:---------------|:--------------------|-----------:|------------:|--------:|---------:|:-------------|
|  69 | Brazil         | 2020-05-05 00:00:00 |       5759 |         401 |  112828 |     7809 | True         |
|  95 | Italy          | 2020-05-05 00:00:00 |       4222 |         699 |  219149 |    30253 | True         |
|  95 | United Kingdom | 2020-05-05 00:00:00 |       5937 |         930 |  199626 |    30224 | True         |
|  94 | Spain          | 2020-05-05 00:00:00 |       4807 |         617 |  227102 |    26522 | True         |
| 104 | US             | 2020-05-05 00:00:00 |      33826 |        2368 | 1224701 |    72176 | True         |
|  91 | Belgium        | 2020-05-05 00:00:00 |       1229 |         251 |   52385 |     8314 | True         |
| 102 | France         | 2020-05-05 00:00:00 |       4173 |         681 |  177123 |    26207 | True         |