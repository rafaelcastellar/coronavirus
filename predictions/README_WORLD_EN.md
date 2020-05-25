# **Predictions**
For experience, I'm running simple predictions over the cases and deaths per day. As they are time-series, I'm using [Facebook Prophet](https://facebook.github.io/prophet/docs/quick_start.html) that is also designed for this kind of prediction in a very simpler way. It works well for most of the time; sometimes there is a huge leap and it takes more time and more data to be understood.

These predictions were made with Covid19 pandemic data from **2020-05-24**.

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
| 84 | Brazil    | 2020-05-20 00:00:00 |      19694 |         876 |  291579 |    18859 | False        |
| 85 | Brazil    | 2020-05-21 00:00:00 |      18508 |        1188 |  310087 |    20047 | False        |
| 86 | Brazil    | 2020-05-22 00:00:00 |      20803 |        1001 |  330890 |    21048 | False        |
| 87 | Brazil    | 2020-05-23 00:00:00 |      16508 |         965 |  347398 |    22013 | False        |
| 88 | Brazil    | 2020-05-24 00:00:00 |      15813 |         653 |  363211 |    22666 | False        |
| 89 | Brazil    | 2020-05-25 00:00:00 |      16639 |         893 |  379850 |    23559 | True         |
| 90 | Brazil    | 2020-05-26 00:00:00 |      17562 |        1010 |  397412 |    24569 | True         |
| 91 | Brazil    | 2020-05-27 00:00:00 |      18930 |        1003 |  416342 |    25572 | True         |
| 92 | Brazil    | 2020-05-28 00:00:00 |      19168 |        1059 |  435510 |    26631 | True         |
| 93 | Brazil    | 2020-05-29 00:00:00 |      19889 |        1073 |  455399 |    27704 | True         |
| 94 | Brazil    | 2020-05-30 00:00:00 |      19408 |        1039 |  474807 |    28743 | True         |
| 95 | Brazil    | 2020-05-31 00:00:00 |      18762 |         969 |  493569 |    29712 | True         |
| 96 | Brazil    | 2020-06-01 00:00:00 |      19803 |        1036 |  513372 |    30748 | True         |
| 97 | Brazil    | 2020-06-02 00:00:00 |      20727 |        1153 |  534099 |    31901 | True         |
| 98 | Brazil    | 2020-06-03 00:00:00 |      22095 |        1146 |  556194 |    33047 | True         |

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
|  89 | Brazil         | 2020-05-25 00:00:00 |      16639 |         893 |  379850 |    23559 | True         |
| 115 | Italy          | 2020-05-25 00:00:00 |       2224 |         418 |  232082 |    33203 | True         |
| 115 | United Kingdom | 2020-05-25 00:00:00 |       4316 |         592 |  265647 |    37467 | True         |
| 114 | Spain          | 2020-05-25 00:00:00 |       2773 |         447 |  248570 |    29199 | True         |
| 124 | US             | 2020-05-25 00:00:00 |      30772 |        1822 | 1674018 |    99542 | True         |
| 111 | Belgium        | 2020-05-25 00:00:00 |        268 |         142 |   57360 |     9422 | True         |
| 122 | France         | 2020-05-25 00:00:00 |        692 |         451 |  183516 |    28821 | True         |

 **The day after tomorrow** 
|     | country        | ds                  |   case_day |   death_day |   cases |   deaths | predicted?   |
|----:|:---------------|:--------------------|-----------:|------------:|--------:|---------:|:-------------|
|  90 | Brazil         | 2020-05-26 00:00:00 |      17562 |        1010 |  397412 |    24569 | True         |
| 116 | Italy          | 2020-05-26 00:00:00 |       2287 |         447 |  234369 |    33650 | True         |
| 116 | United Kingdom | 2020-05-26 00:00:00 |       4323 |         794 |  269970 |    38261 | True         |
| 115 | Spain          | 2020-05-26 00:00:00 |       2617 |         427 |  251187 |    29626 | True         |
| 125 | US             | 2020-05-26 00:00:00 |      31634 |        2145 | 1705652 |   101687 | True         |
| 112 | Belgium        | 2020-05-26 00:00:00 |        220 |         165 |   57580 |     9587 | True         |
| 123 | France         | 2020-05-26 00:00:00 |        823 |         482 |  184339 |    29303 | True         |