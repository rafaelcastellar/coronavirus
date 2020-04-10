# **Predictions**
For experience, I'm running simple predictions over the cases and deaths per day. As they are time-series, I'm using [Facebook Prophet](https://facebook.github.io/prophet/docs/quick_start.html) that is also designed for this kind of prediction in a very simpler way. It works well for most of the time; sometimes there is a huge leap and it takes sometime more data to be understood.

These predictions were made with Covid19 pandemic data from **2020-04-09**.

As there are many countries to have their data predicted in a row, I selected a few of them plus Brazil to be predicted:
['Brazil', 'Italy', 'United Kingdom', 'Spain', 'US', 'China', 'France'].
***Tip**: you can set yourself at the *[prediction.ipynb](../prediction.ipynb)* notebook which countries you prefer to predict*


## The prediction
As Facebook Prophet predicts time-series data and it is running the prediction over cases per day and deaths per day. After that, I compute theirs cumulatives.It is predicting for the next 10 days.
By the end, a CSV file containing all the predicted data is generated.

#### The Brazil's last 5 days and predicted next 10 days
*predicted? = True* means the line is a prediction; *=False* means they are real numbers.
|    | country   | ds                  |   case_day |   death_day |   cases |   deaths | predicted?   |   cap |
|---:|:----------|:--------------------|-----------:|------------:|--------:|---------:|:-------------|------:|
| 39 | Brazil    | 2020-04-05 00:00:00 |        770 |          41 |   11130 |      486 | False        |  3000 |
| 40 | Brazil    | 2020-04-06 00:00:00 |       1031 |          78 |   12161 |      564 | False        |  3000 |
| 41 | Brazil    | 2020-04-07 00:00:00 |       1873 |         122 |   14034 |      686 | False        |  3000 |
| 42 | Brazil    | 2020-04-08 00:00:00 |       2136 |         133 |   16170 |      819 | False        |  3000 |
| 43 | Brazil    | 2020-04-09 00:00:00 |       1922 |         131 |   18092 |      950 | False        |  3000 |
| 44 | Brazil    | 2020-04-10 00:00:00 |       1933 |          62 |   20025 |     1012 | True         |   nan |
| 45 | Brazil    | 2020-04-11 00:00:00 |       2054 |          71 |   22079 |     1083 | True         |   nan |
| 46 | Brazil    | 2020-04-12 00:00:00 |       2057 |          65 |   24136 |     1148 | True         |   nan |
| 47 | Brazil    | 2020-04-13 00:00:00 |       2128 |          71 |   26264 |     1219 | True         |   nan |
| 48 | Brazil    | 2020-04-14 00:00:00 |       2451 |          82 |   28715 |     1301 | True         |   nan |
| 49 | Brazil    | 2020-04-15 00:00:00 |       2497 |          87 |   31212 |     1388 | True         |   nan |
| 50 | Brazil    | 2020-04-16 00:00:00 |       2554 |          94 |   33766 |     1482 | True         |   nan |
| 51 | Brazil    | 2020-04-17 00:00:00 |       2549 |          77 |   36315 |     1559 | True         |   nan |
| 52 | Brazil    | 2020-04-18 00:00:00 |       2619 |          86 |   38934 |     1645 | True         |   nan |
| 53 | Brazil    | 2020-04-19 00:00:00 |       2570 |          81 |   41504 |     1726 | True         |   nan |

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
|    | country        | ds                  |   case_day |   death_day |   cases |   deaths | predicted?   |   cap |
|---:|:---------------|:--------------------|-----------:|------------:|--------:|---------:|:-------------|------:|
| 44 | Brazil         | 2020-04-10 00:00:00 |       1197 |          62 |   19289 |     1012 | True         |   nan |
| 70 | Italy          | 2020-04-10 00:00:00 |       6015 |         812 |  149641 |    19091 | True         |   nan |
| 70 | United Kingdom | 2020-04-10 00:00:00 |       5315 |         400 |   71187 |     8393 | True         |   nan |
| 69 | Spain          | 2020-04-10 00:00:00 |       6696 |         873 |  159918 |    16320 | True         |   nan |
| 79 | US             | 2020-04-10 00:00:00 |      37376 |         707 |  498813 |    17185 | True         |   nan |
| 79 | China          | 2020-04-10 00:00:00 |       -464 |          -9 |   82419 |     3330 | True         |   nan |
| 77 | France         | 2020-04-10 00:00:00 |       6108 |         868 |  124889 |    13096 | True         |   nan |
| 44 | Brazil         | 2020-04-10 00:00:00 |       1197 |          62 |   19289 |     1012 | True         |   nan |
| 44 | Brazil         | 2020-04-10 00:00:00 |         23 |          62 |   18115 |     1012 | True         |   nan |
| 44 | Brazil         | 2020-04-10 00:00:00 |         23 |          62 |   18115 |     1012 | True         |   nan |
| 44 | Brazil         | 2020-04-10 00:00:00 |       1933 |          62 |   20025 |     1012 | True         |   nan |

 **The day after tomorrow** 
|    | country        | ds                  |   case_day |   death_day |   cases |   deaths | predicted?   |   cap |
|---:|:---------------|:--------------------|-----------:|------------:|--------:|---------:|:-------------|------:|
| 45 | Brazil         | 2020-04-11 00:00:00 |       1247 |          71 |   20536 |     1083 | True         |   nan |
| 71 | Italy          | 2020-04-11 00:00:00 |       5980 |         789 |  155621 |    19880 | True         |   nan |
| 71 | United Kingdom | 2020-04-11 00:00:00 |       5312 |         413 |   76499 |     8806 | True         |   nan |
| 70 | Spain          | 2020-04-11 00:00:00 |       6916 |         902 |  166834 |    17222 | True         |   nan |
| 80 | US             | 2020-04-11 00:00:00 |      38771 |         730 |  537584 |    17915 | True         |   nan |
| 80 | China          | 2020-04-11 00:00:00 |       -797 |          10 |   81622 |     3340 | True         |   nan |
| 78 | France         | 2020-04-11 00:00:00 |       8045 |         870 |  132934 |    13966 | True         |   nan |
| 45 | Brazil         | 2020-04-11 00:00:00 |       1247 |          71 |   20536 |     1083 | True         |   nan |
| 45 | Brazil         | 2020-04-11 00:00:00 |         70 |          71 |   18185 |     1083 | True         |   nan |
| 45 | Brazil         | 2020-04-11 00:00:00 |         70 |          71 |   18185 |     1083 | True         |   nan |
| 45 | Brazil         | 2020-04-11 00:00:00 |       2054 |          71 |   22079 |     1083 | True         |   nan |