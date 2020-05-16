# **Predictions**
For experience, I'm running simple predictions over the cases and deaths per day. As they are time-series, I'm using [Facebook Prophet](https://facebook.github.io/prophet/docs/quick_start.html) that is also designed for this kind of prediction in a very simpler way. It works well for most of the time; sometimes there is a huge leap and it takes more time and more data to be understood.

These predictions were made with Covid19 pandemic data from **2020-05-15**.

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
| 75 | Brazil    | 2020-05-11 00:00:00 |       6895 |         530 |  169594 |    11653 | False        |
| 76 | Brazil    | 2020-05-12 00:00:00 |       8620 |         808 |  178214 |    12461 | False        |
| 77 | Brazil    | 2020-05-13 00:00:00 |      11923 |         779 |  190137 |    13240 | False        |
| 78 | Brazil    | 2020-05-14 00:00:00 |      13028 |         759 |  203165 |    13999 | False        |
| 79 | Brazil    | 2020-05-15 00:00:00 |      17126 |         963 |  220291 |    14962 | False        |
| 80 | Brazil    | 2020-05-16 00:00:00 |      11252 |         744 |  231543 |    15706 | True         |
| 81 | Brazil    | 2020-05-17 00:00:00 |      10964 |         713 |  242507 |    16419 | True         |
| 82 | Brazil    | 2020-05-18 00:00:00 |      11407 |         744 |  253914 |    17163 | True         |
| 83 | Brazil    | 2020-05-19 00:00:00 |      12110 |         835 |  266024 |    17998 | True         |
| 84 | Brazil    | 2020-05-20 00:00:00 |      13206 |         849 |  279230 |    18847 | True         |
| 85 | Brazil    | 2020-05-21 00:00:00 |      13469 |         884 |  292699 |    19731 | True         |
| 86 | Brazil    | 2020-05-22 00:00:00 |      13961 |         914 |  306660 |    20645 | True         |
| 87 | Brazil    | 2020-05-23 00:00:00 |      13535 |         886 |  320195 |    21531 | True         |
| 88 | Brazil    | 2020-05-24 00:00:00 |      13247 |         855 |  333442 |    22386 | True         |
| 89 | Brazil    | 2020-05-25 00:00:00 |      13690 |         886 |  347132 |    23272 | True         |

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
|  80 | Brazil         | 2020-05-16 00:00:00 |      11252 |         744 |  231543 |    15706 | True         |
| 106 | Italy          | 2020-05-16 00:00:00 |       3837 |         585 |  227722 |    32195 | True         |
| 106 | United Kingdom | 2020-05-16 00:00:00 |       5739 |         807 |  243743 |    34885 | True         |
| 105 | Spain          | 2020-05-16 00:00:00 |       3910 |         478 |  244118 |    27937 | True         |
| 115 | US             | 2020-05-16 00:00:00 |      33667 |        2143 | 1476491 |    89673 | True         |
| 102 | Belgium        | 2020-05-16 00:00:00 |       1045 |         200 |   55689 |     9159 | True         |
| 113 | France         | 2020-05-16 00:00:00 |       1638 |         536 |  181383 |    28068 | True         |

 **The day after tomorrow** 
|     | country        | ds                  |   case_day |   death_day |   cases |   deaths | predicted?   |
|----:|:---------------|:--------------------|-----------:|------------:|--------:|---------:|:-------------|
|  81 | Brazil         | 2020-05-17 00:00:00 |      10964 |         713 |  242507 |    16419 | True         |
| 107 | Italy          | 2020-05-17 00:00:00 |       3614 |         525 |  231336 |    32720 | True         |
| 107 | United Kingdom | 2020-05-17 00:00:00 |       5797 |         687 |  249540 |    35572 | True         |
| 106 | Spain          | 2020-05-17 00:00:00 |       3917 |         475 |  248035 |    28412 | True         |
| 116 | US             | 2020-05-17 00:00:00 |      32093 |        1929 | 1508584 |    91602 | True         |
| 103 | Belgium        | 2020-05-17 00:00:00 |       1013 |         190 |   56702 |     9349 | True         |
| 114 | France         | 2020-05-17 00:00:00 |       2920 |         470 |  184303 |    28538 | True         |