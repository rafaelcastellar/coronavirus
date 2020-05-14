# **Predictions**
For experience, I'm running simple predictions over the cases and deaths per day. As they are time-series, I'm using [Facebook Prophet](https://facebook.github.io/prophet/docs/quick_start.html) that is also designed for this kind of prediction in a very simpler way. It works well for most of the time; sometimes there is a huge leap and it takes more time and more data to be understood.

These predictions were made with Covid19 pandemic data from **2020-05-13**.

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
| 73 | Brazil    | 2020-05-09 00:00:00 |       9167 |         639 |  156061 |    10656 | False        |
| 74 | Brazil    | 2020-05-10 00:00:00 |       6638 |         467 |  162699 |    11123 | False        |
| 75 | Brazil    | 2020-05-11 00:00:00 |       6895 |         530 |  169594 |    11653 | False        |
| 76 | Brazil    | 2020-05-12 00:00:00 |       8620 |         808 |  178214 |    12461 | False        |
| 77 | Brazil    | 2020-05-13 00:00:00 |      11923 |         779 |  190137 |    13240 | False        |
| 78 | Brazil    | 2020-05-14 00:00:00 |       9844 |         694 |  199981 |    13934 | True         |
| 79 | Brazil    | 2020-05-15 00:00:00 |       9953 |         707 |  209934 |    14641 | True         |
| 80 | Brazil    | 2020-05-16 00:00:00 |       9968 |         692 |  219902 |    15333 | True         |
| 81 | Brazil    | 2020-05-17 00:00:00 |       9626 |         659 |  229528 |    15992 | True         |
| 82 | Brazil    | 2020-05-18 00:00:00 |      10015 |         689 |  239543 |    16681 | True         |
| 83 | Brazil    | 2020-05-19 00:00:00 |      10664 |         779 |  250207 |    17460 | True         |
| 84 | Brazil    | 2020-05-20 00:00:00 |      11698 |         791 |  261905 |    18251 | True         |
| 85 | Brazil    | 2020-05-21 00:00:00 |      11634 |         817 |  273539 |    19068 | True         |
| 86 | Brazil    | 2020-05-22 00:00:00 |      11743 |         830 |  285282 |    19898 | True         |
| 87 | Brazil    | 2020-05-23 00:00:00 |      11758 |         815 |  297040 |    20713 | True         |

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
|  78 | Brazil         | 2020-05-14 00:00:00 |       9844 |         694 |  199981 |    13934 | True         |
| 104 | Italy          | 2020-05-14 00:00:00 |       3659 |         542 |  225763 |    31648 | True         |
| 104 | United Kingdom | 2020-05-14 00:00:00 |       5866 |         834 |  236851 |    34098 | True         |
| 103 | Spain          | 2020-05-14 00:00:00 |       4632 |         553 |  243348 |    27657 | True         |
| 113 | US             | 2020-05-14 00:00:00 |      34254 |        2226 | 1424660 |    86345 | True         |
| 100 | Belgium        | 2020-05-14 00:00:00 |       1145 |         220 |   55126 |     9063 | True         |
| 111 | France         | 2020-05-14 00:00:00 |       2844 |         622 |  181143 |    27699 | True         |

 **The day after tomorrow** 
|     | country        | ds                  |   case_day |   death_day |   cases |   deaths | predicted?   |
|----:|:---------------|:--------------------|-----------:|------------:|--------:|---------:|:-------------|
|  79 | Brazil         | 2020-05-15 00:00:00 |       9953 |         707 |  209934 |    14641 | True         |
| 105 | Italy          | 2020-05-15 00:00:00 |       3978 |         591 |  229741 |    32239 | True         |
| 105 | United Kingdom | 2020-05-15 00:00:00 |       6482 |         879 |  243333 |    34977 | True         |
| 104 | Spain          | 2020-05-15 00:00:00 |       4338 |         537 |  247686 |    28194 | True         |
| 114 | US             | 2020-05-15 00:00:00 |      35057 |        2186 | 1459717 |    88531 | True         |
| 101 | Belgium        | 2020-05-15 00:00:00 |       1201 |         227 |   56327 |     9290 | True         |
| 112 | France         | 2020-05-15 00:00:00 |       2400 |         608 |  183543 |    28307 | True         |