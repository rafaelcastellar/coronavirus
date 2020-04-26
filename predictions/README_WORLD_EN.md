# **Predictions**
For experience, I'm running simple predictions over the cases and deaths per day. As they are time-series, I'm using [Facebook Prophet](https://facebook.github.io/prophet/docs/quick_start.html) that is also designed for this kind of prediction in a very simpler way. It works well for most of the time; sometimes there is a huge leap and it takes more time and more data to be understood.

These predictions were made with Covid19 pandemic data from **2020-04-25**.

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
| 55 | Brazil    | 2020-04-21 00:00:00 |       2336 |         154 |   43079 |     2741 | False        |
| 56 | Brazil    | 2020-04-22 00:00:00 |       2678 |         165 |   45757 |     2906 | False        |
| 57 | Brazil    | 2020-04-23 00:00:00 |       4279 |         425 |   50036 |     3331 | False        |
| 58 | Brazil    | 2020-04-24 00:00:00 |       4007 |         373 |   54043 |     3704 | False        |
| 59 | Brazil    | 2020-04-25 00:00:00 |       5281 |         353 |   59324 |     4057 | False        |
| 60 | Brazil    | 2020-04-26 00:00:00 |       3073 |         216 |   62397 |     4273 | True         |
| 61 | Brazil    | 2020-04-27 00:00:00 |       3101 |         226 |   65498 |     4499 | True         |
| 62 | Brazil    | 2020-04-28 00:00:00 |       3448 |         252 |   68946 |     4751 | True         |
| 63 | Brazil    | 2020-04-29 00:00:00 |       3726 |         262 |   72672 |     5013 | True         |
| 64 | Brazil    | 2020-04-30 00:00:00 |       3855 |         297 |   76527 |     5310 | True         |
| 65 | Brazil    | 2020-05-01 00:00:00 |       3925 |         288 |   80452 |     5598 | True         |
| 66 | Brazil    | 2020-05-02 00:00:00 |       4045 |         289 |   84497 |     5887 | True         |
| 67 | Brazil    | 2020-05-03 00:00:00 |       3721 |         265 |   88218 |     6152 | True         |
| 68 | Brazil    | 2020-05-04 00:00:00 |       3749 |         274 |   91967 |     6426 | True         |
| 69 | Brazil    | 2020-05-05 00:00:00 |       4096 |         301 |   96063 |     6727 | True         |

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
| 60 | Brazil         | 2020-04-26 00:00:00 |       3073 |         216 |   62397 |     4273 | True         |
| 86 | Italy          | 2020-04-26 00:00:00 |       5223 |         725 |  200574 |    27109 | True         |
| 86 | United Kingdom | 2020-04-26 00:00:00 |       6308 |         863 |  155877 |    21244 | True         |
| 85 | Spain          | 2020-04-26 00:00:00 |       6464 |         697 |  230223 |    23599 | True         |
| 95 | US             | 2020-04-26 00:00:00 |      36520 |        2633 |  974674 |    56388 | True         |
| 82 | Belgium        | 2020-04-26 00:00:00 |       1553 |         275 |   46878 |     7192 | True         |
| 93 | France         | 2020-04-26 00:00:00 |       6109 |         636 |  167753 |    23284 | True         |

 **The day after tomorrow** 
|    | country        | ds                  |   case_day |   death_day |   cases |   deaths | predicted?   |
|---:|:---------------|:--------------------|-----------:|------------:|--------:|---------:|:-------------|
| 61 | Brazil         | 2020-04-27 00:00:00 |       3101 |         226 |   65498 |     4499 | True         |
| 87 | Italy          | 2020-04-27 00:00:00 |       4832 |         745 |  205406 |    27854 | True         |
| 87 | United Kingdom | 2020-04-27 00:00:00 |       6078 |         843 |  161955 |    22087 | True         |
| 86 | Spain          | 2020-04-27 00:00:00 |       6341 |         708 |  236564 |    24307 | True         |
| 96 | US             | 2020-04-27 00:00:00 |      36934 |        2630 | 1011608 |    59018 | True         |
| 83 | Belgium        | 2020-04-27 00:00:00 |       1412 |         277 |   48290 |     7469 | True         |
| 94 | France         | 2020-04-27 00:00:00 |       4749 |         691 |  172502 |    23975 | True         |