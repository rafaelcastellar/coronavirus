# **Predictions**
For experience, I'm running simple predictions over the cases and deaths per day. As they are time-series, I'm using [Facebook Prophet](https://facebook.github.io/prophet/docs/quick_start.html) that is also designed for this kind of prediction in a very simpler way. It works well for most of the time; sometimes there is a huge leap and it takes more time and more data to be understood.

These predictions were made with Covid19 pandemic data from **2020-04-26**.

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
| 56 | Brazil    | 2020-04-22 00:00:00 |       2678 |         165 |   45757 |     2906 | False        |
| 57 | Brazil    | 2020-04-23 00:00:00 |       4279 |         425 |   50036 |     3331 | False        |
| 58 | Brazil    | 2020-04-24 00:00:00 |       4007 |         373 |   54043 |     3704 | False        |
| 59 | Brazil    | 2020-04-25 00:00:00 |       5281 |         353 |   59324 |     4057 | False        |
| 60 | Brazil    | 2020-04-26 00:00:00 |       3776 |         229 |   63100 |     4286 | False        |
| 61 | Brazil    | 2020-04-27 00:00:00 |       3214 |         231 |   66314 |     4517 | True         |
| 62 | Brazil    | 2020-04-28 00:00:00 |       3563 |         258 |   69877 |     4775 | True         |
| 63 | Brazil    | 2020-04-29 00:00:00 |       3846 |         267 |   73723 |     5042 | True         |
| 64 | Brazil    | 2020-04-30 00:00:00 |       3978 |         302 |   77701 |     5344 | True         |
| 65 | Brazil    | 2020-05-01 00:00:00 |       4051 |         294 |   81752 |     5638 | True         |
| 66 | Brazil    | 2020-05-02 00:00:00 |       4181 |         296 |   85933 |     5934 | True         |
| 67 | Brazil    | 2020-05-03 00:00:00 |       3945 |         273 |   89878 |     6207 | True         |
| 68 | Brazil    | 2020-05-04 00:00:00 |       3909 |         282 |   93787 |     6489 | True         |
| 69 | Brazil    | 2020-05-05 00:00:00 |       4259 |         308 |   98046 |     6797 | True         |
| 70 | Brazil    | 2020-05-06 00:00:00 |       4542 |         318 |  102588 |     7115 | True         |

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
| 61 | Brazil         | 2020-04-27 00:00:00 |       3214 |         231 |   66314 |     4517 | True         |
| 87 | Italy          | 2020-04-27 00:00:00 |       4729 |         728 |  202404 |    27372 | True         |
| 87 | United Kingdom | 2020-04-27 00:00:00 |       5929 |         786 |  159966 |    21580 | True         |
| 86 | Spain          | 2020-04-27 00:00:00 |       6209 |         693 |  232838 |    23883 | True         |
| 96 | US             | 2020-04-27 00:00:00 |      35332 |        2419 | 1001117 |    57300 | True         |
| 83 | Belgium        | 2020-04-27 00:00:00 |       1387 |         264 |   47521 |     7358 | True         |
| 94 | France         | 2020-04-27 00:00:00 |       4581 |         678 |  166801 |    23568 | True         |

 **The day after tomorrow** 
|    | country        | ds                  |   case_day |   death_day |   cases |   deaths | predicted?   |
|---:|:---------------|:--------------------|-----------:|------------:|--------:|---------:|:-------------|
| 62 | Brazil         | 2020-04-28 00:00:00 |       3563 |         258 |   69877 |     4775 | True         |
| 88 | Italy          | 2020-04-28 00:00:00 |       4713 |         755 |  207117 |    28127 | True         |
| 88 | United Kingdom | 2020-04-28 00:00:00 |       6074 |         874 |  166040 |    22454 | True         |
| 87 | Spain          | 2020-04-28 00:00:00 |       6229 |         670 |  239067 |    24553 | True         |
| 97 | US             | 2020-04-28 00:00:00 |      36421 |        2675 | 1037538 |    59975 | True         |
| 84 | Belgium        | 2020-04-28 00:00:00 |       1369 |         299 |   48890 |     7657 | True         |
| 95 | France         | 2020-04-28 00:00:00 |       4790 |         744 |  171591 |    24312 | True         |