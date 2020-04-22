# **Predictions**
For experience, I'm running simple predictions over the cases and deaths per day. As they are time-series, I'm using [Facebook Prophet](https://facebook.github.io/prophet/docs/quick_start.html) that is also designed for this kind of prediction in a very simpler way. It works well for most of the time; sometimes there is a huge leap and it takes more time and more data to be understood.

These predictions were made with Covid19 pandemic data from **2020-04-21**.

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
| 51 | Brazil    | 2020-04-17 00:00:00 |       3257 |         217 |   33682 |     2141 | False        |
| 52 | Brazil    | 2020-04-18 00:00:00 |       2976 |         213 |   36658 |     2354 | False        |
| 53 | Brazil    | 2020-04-19 00:00:00 |       1996 |         108 |   38654 |     2462 | False        |
| 54 | Brazil    | 2020-04-20 00:00:00 |       2089 |         125 |   40743 |     2587 | False        |
| 55 | Brazil    | 2020-04-21 00:00:00 |       2336 |         154 |   43079 |     2741 | False        |
| 56 | Brazil    | 2020-04-22 00:00:00 |       2416 |         157 |   45495 |     2898 | True         |
| 57 | Brazil    | 2020-04-23 00:00:00 |       2323 |         162 |   47818 |     3060 | True         |
| 58 | Brazil    | 2020-04-24 00:00:00 |       2398 |         156 |   50216 |     3216 | True         |
| 59 | Brazil    | 2020-04-25 00:00:00 |       2343 |         157 |   52559 |     3373 | True         |
| 60 | Brazil    | 2020-04-26 00:00:00 |       2223 |         144 |   54782 |     3517 | True         |
| 61 | Brazil    | 2020-04-27 00:00:00 |       2220 |         151 |   57002 |     3668 | True         |
| 62 | Brazil    | 2020-04-28 00:00:00 |       2536 |         176 |   59538 |     3844 | True         |
| 63 | Brazil    | 2020-04-29 00:00:00 |       2769 |         182 |   62307 |     4026 | True         |
| 64 | Brazil    | 2020-04-30 00:00:00 |       2675 |         186 |   64982 |     4212 | True         |
| 65 | Brazil    | 2020-05-01 00:00:00 |       2750 |         180 |   67732 |     4392 | True         |

 #### The predicted Brazil's cumulative curves
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
| 56 | Brazil         | 2020-04-22 00:00:00 |       2416 |         157 |   45495 |     2898 | True         |
| 82 | Italy          | 2020-04-22 00:00:00 |       5172 |         753 |  189129 |    25401 | True         |
| 82 | United Kingdom | 2020-04-22 00:00:00 |       6291 |         910 |  136463 |    18288 | True         |
| 81 | Spain          | 2020-04-22 00:00:00 |       6969 |         752 |  211147 |    22034 | True         |
| 91 | US             | 2020-04-22 00:00:00 |      37578 |        2706 |  861364 |    47551 | True         |
| 78 | Belgium        | 2020-04-22 00:00:00 |       1606 |         296 |   42562 |     6294 | True         |
| 89 | France         | 2020-04-22 00:00:00 |       4898 |         858 |  164195 |    21687 | True         |

 **The day after tomorrow** 
|    | country        | ds                  |   case_day |   death_day |   cases |   deaths | predicted?   |
|---:|:---------------|:--------------------|-----------:|------------:|--------:|---------:|:-------------|
| 57 | Brazil         | 2020-04-23 00:00:00 |       2323 |         162 |   47818 |     3060 | True         |
| 83 | Italy          | 2020-04-23 00:00:00 |       5301 |         740 |  194430 |    26141 | True         |
| 83 | United Kingdom | 2020-04-23 00:00:00 |       6255 |         935 |  142718 |    19223 | True         |
| 82 | Spain          | 2020-04-23 00:00:00 |       7024 |         741 |  218171 |    22775 | True         |
| 92 | US             | 2020-04-23 00:00:00 |      39587 |        2945 |  900951 |    50496 | True         |
| 79 | Belgium        | 2020-04-23 00:00:00 |       1611 |         323 |   44173 |     6617 | True         |
| 90 | France         | 2020-04-23 00:00:00 |       5557 |         898 |  169752 |    22585 | True         |