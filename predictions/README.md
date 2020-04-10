# **Predictions**
For experience, I'm running simple predictions over the cases and deaths per day. As they are time-series, I'm using [Facebook Prophet](https://facebook.github.io/prophet/docs/quick_start.html) that is also designed for this kind of prediction in a very simpler way. It works well for most of the time; sometimes there is a huge leap and it takes sometime more data to be understood.

These predictions were made with Covid19 pandemic data from **2020-04-09**.

As there are many countries to have their data predicted in a row, I selected a few of them plus Brazil to be predicted:
['Brazil', 'Italy', 'United Kingdom', 'Spain', 'US', 'China', 'France'].
***Tip**: you can set yourself at the *[prediction.ipynb](../prediction.ipynb)* notebook which countries you prefer to predict*


## The prediction
As Facebook Prophet predicts time-series data and it is running the prediction over cases per day and deaths per day. After that, I compute theirs cumulatives.It is predicting for the next 10 days.
By the end, a CSV file containing all the predicted data is generated.

#### The Brazil's prediction for the next 10 days
|    | country   | ds                  |   case_day |   death_day |   cases |   deaths | predicted?   |
|---:|:----------|:--------------------|-----------:|------------:|--------:|---------:|:-------------|
| 44 | Brazil    | 2020-04-10 00:00:00 |       1197 |          62 |   19289 |     1012 | True         |
| 45 | Brazil    | 2020-04-11 00:00:00 |       1247 |          71 |   20536 |     1083 | True         |
| 46 | Brazil    | 2020-04-12 00:00:00 |       1188 |          65 |   21724 |     1148 | True         |
| 47 | Brazil    | 2020-04-13 00:00:00 |       1206 |          71 |   22930 |     1219 | True         |
| 48 | Brazil    | 2020-04-14 00:00:00 |       1487 |          82 |   24417 |     1301 | True         |
| 49 | Brazil    | 2020-04-15 00:00:00 |       1557 |          87 |   25974 |     1388 | True         |
| 50 | Brazil    | 2020-04-16 00:00:00 |       1586 |          94 |   27560 |     1482 | True         |
| 51 | Brazil    | 2020-04-17 00:00:00 |       1457 |          77 |   29017 |     1559 | True         |
| 52 | Brazil    | 2020-04-18 00:00:00 |       1507 |          86 |   30524 |     1645 | True         |
| 53 | Brazil    | 2020-04-19 00:00:00 |       1448 |          81 |   31972 |     1726 | True         |

 #### The predicted Brazil's cumulative curves
The prediction are over the daily data, so, here they were cumulated and plotted with the actual data:
![](brazil_predictions.png)

Facebook's Prophet automatically generates charts about the behaviour of the analysed and predicted data. That has a good visual information. Here are for the Brazil's prediction:
### Cases
![](brazil_prophet_cases.png)

 ### Deaths
![](brazil_prophet_deaths.png)
#### Finally, the predictions for selected countries for:
**Tomorrow**
|    | country        | ds                  |   case_day |   death_day |   cases |   deaths | predicted?   |
|---:|:---------------|:--------------------|-----------:|------------:|--------:|---------:|:-------------|
| 44 | Brazil         | 2020-04-10 00:00:00 |       1197 |          62 |   19289 |     1012 | True         |
| 70 | Italy          | 2020-04-10 00:00:00 |       6015 |         812 |  149641 |    19091 | True         |
| 70 | United Kingdom | 2020-04-10 00:00:00 |       5315 |         400 |   71187 |     8393 | True         |
| 69 | Spain          | 2020-04-10 00:00:00 |       6696 |         873 |  159918 |    16320 | True         |
| 79 | US             | 2020-04-10 00:00:00 |      37376 |         707 |  498813 |    17185 | True         |
| 79 | China          | 2020-04-10 00:00:00 |       -464 |          -9 |   82419 |     3330 | True         |
| 77 | France         | 2020-04-10 00:00:00 |       6108 |         868 |  124889 |    13096 | True         |

 **The day after tomorrow** 
|    | country        | ds                  |   case_day |   death_day |   cases |   deaths | predicted?   |
|---:|:---------------|:--------------------|-----------:|------------:|--------:|---------:|:-------------|
| 45 | Brazil         | 2020-04-11 00:00:00 |       1247 |          71 |   20536 |     1083 | True         |
| 71 | Italy          | 2020-04-11 00:00:00 |       5980 |         789 |  155621 |    19880 | True         |
| 71 | United Kingdom | 2020-04-11 00:00:00 |       5312 |         413 |   76499 |     8806 | True         |
| 70 | Spain          | 2020-04-11 00:00:00 |       6916 |         902 |  166834 |    17222 | True         |
| 80 | US             | 2020-04-11 00:00:00 |      38771 |         730 |  537584 |    17915 | True         |
| 80 | China          | 2020-04-11 00:00:00 |       -797 |          10 |   81622 |     3340 | True         |
| 78 | France         | 2020-04-11 00:00:00 |       8045 |         870 |  132934 |    13966 | True         |