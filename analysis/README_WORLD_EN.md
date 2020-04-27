[<img src="../data/bandeiras/PT.png" width="30"   /> Versão em português](README_WORLD.md)

# **Analysis and monitoring**
These analysis are related to the Covid19 pandemic data up to **2020-04-26**.

As there are many countries to have all of their data plotted together, I selected a few of them plus Brazil to be compared with:['Brazil', 'Italy', 'United Kingdom', 'Spain', 'US', 'France', 'Belgium'].

Some countries are not in UN dataset, so we can not analyse them by population. They can be found at the end of the *[data_engineering.ipynb](../data_engineering.ipynb)*.

*Tip: you can set yourself at the analysis notebook which countries you prefer to compare*

## Top 5 deadliest countries + Brazil
|    | country        |   day | date                |   cases |   case_day |   deaths |   death_day |   cases_million |   deaths_million |   avg7_cases_million |   avg7_deaths_million |   avg7_recoveries_million |
|---:|:---------------|------:|:--------------------|--------:|-----------:|---------:|------------:|----------------:|-----------------:|---------------------:|----------------------:|--------------------------:|
|  1 | Belgium        |    83 | 2020-04-26 00:00:00 |   46134 |        809 |     7094 |         177 |            70.1 |             15.3 |                   94 |                    17 |                        25 |
|  2 | Ireland        |    58 | 2020-04-26 00:00:00 |   19262 |        701 |     1087 |          24 |           143.6 |              4.9 |                  117 |                    13 |                       267 |
|  3 | Sweden         |    87 | 2020-04-26 00:00:00 |   18640 |        463 |     2194 |           2 |            46.1 |              0.2 |                   60 |                     9 |                         6 |
|  4 | United Kingdom |    87 | 2020-04-26 00:00:00 |  154037 |       4468 |    20794 |         413 |            66.2 |              6.1 |                   69 |                     9 |                         0 |
|  5 | San Marino     |    60 | 2020-04-26 00:00:00 |     538 |         25 |       41 |           1 |           738.2 |             29.5 |                  324 |                     8 |                        16 |
| 26 | Brazil         |    61 | 2020-04-26 00:00:00 |   63100 |       3776 |     4286 |         229 |            17.9 |              1.1 |                   16 |                     1 |                         5 |


 ## Top 5 most transmissible countries + Brazil
|    | country    |   day | date                |   cases |   case_day |   deaths |   death_day |   cases_million |   deaths_million |   avg7_cases_million |   avg7_deaths_million |   avg7_recoveries_million |
|---:|:-----------|------:|:--------------------|--------:|-----------:|---------:|------------:|----------------:|-----------------:|---------------------:|----------------------:|--------------------------:|
|  1 | San Marino |    60 | 2020-04-26 00:00:00 |     538 |         25 |       41 |           1 |           738.2 |             29.5 |                  324 |                     8 |                        16 |
|  2 | Qatar      |    58 | 2020-04-26 00:00:00 |   10287 |        929 |       10 |           0 |           328   |              0   |                  244 |                     0 |                        24 |
|  3 | Singapore  |    95 | 2020-04-26 00:00:00 |   13624 |        931 |       12 |           0 |           160.4 |              0   |                  173 |                     0 |                         7 |
|  4 | Ireland    |    58 | 2020-04-26 00:00:00 |   19262 |        701 |     1087 |          24 |           143.6 |              4.9 |                  117 |                    13 |                       267 |
|  5 | Ecuador    |    57 | 2020-04-26 00:00:00 |   22719 |          0 |      576 |           0 |             0   |              0   |                  108 |                     0 |                         2 |
| 37 | Brazil     |    61 | 2020-04-26 00:00:00 |   63100 |       3776 |     4286 |         229 |            17.9 |              1.1 |                   16 |                     1 |                         5 |
----------------------
## World' analysis
### Cases, deaths and recoveries
![](world_cases_deaths.png)

 ### Cases, deaths and recoveries per million
Million of population normalizes the features so they can me better comparable among the selected countries. As we can see, the first charts shows us how aggressive the pandemic is in Italy, Spain and somehow in France.
![](world_cases_deaths_million.png)

 ### Active cases, world overview, % recoveries and lethality
![](world_active_cases_percentages.png)
----------------------
## Brazil's analysis


 ### Cases, deaths and recoveries
![](brazil_number_million_variation.png)

 ### Moving averages (last 7 days)
![](brazil_movingAvg.png)