[<img src="../data/bandeiras/PT.png" width="30"   /> Versão em português](README_WORLD.md)

# **Analysis and monitoring**
These analysis are related to the Covid19 pandemic data up to **2020-05-01**.

As there are many countries to have all of their data plotted together, I selected a few of them plus Brazil to be compared with:['Brazil', 'Italy', 'United Kingdom', 'Spain', 'US', 'France', 'Belgium'].

Some countries are not in UN dataset, so we can not analyse them by population. They can be found at the end of the *[data_engineering.ipynb](../data_engineering.ipynb)*.

*Tip: you can set yourself at the analysis notebook which countries you prefer to compare*

## Top 5 deadliest countries + Brazil
|    | country        |   day | date                |   cases |   case_day |   deaths |   death_day |   cases_million |   deaths_million |   avg7_cases_million |   avg7_deaths_million |   avg7_recoveries_million |
|---:|:---------------|------:|:--------------------|--------:|-----------:|---------:|------------:|----------------:|-----------------:|---------------------:|----------------------:|--------------------------:|
|  1 | Belgium        |    88 | 2020-05-01 00:00:00 |   49032 |        513 |     7703 |         109 |            44.5 |              9.4 |                   58 |                    12 |                        21 |
|  2 | United Kingdom |    92 | 2020-05-01 00:00:00 |  178685 |       6204 |    27583 |         741 |            91.9 |             11   |                   72 |                    10 |                         0 |
|  3 | Ireland        |    63 | 2020-05-01 00:00:00 |   20833 |        221 |     1265 |          33 |            45.3 |              6.8 |                   77 |                     7 |                       121 |
|  4 | Sweden         |    92 | 2020-05-01 00:00:00 |   21520 |        428 |     2653 |          67 |            42.6 |              6.7 |                   56 |                     7 |                         0 |
|  5 | Spain          |    91 | 2020-05-01 00:00:00 |  213435 |          0 |    24543 |           0 |             0   |              0   |                   31 |                     6 |                        60 |
| 21 | Brazil         |    66 | 2020-05-01 00:00:00 |   92202 |       5015 |     6412 |         406 |            23.8 |              1.9 |                   25 |                     1 |                         7 |


 ## Top 5 most transmissible countries + Brazil
|    | country    |   day | date                |   cases |   case_day |   deaths |   death_day |   cases_million |   deaths_million |   avg7_cases_million |   avg7_deaths_million |   avg7_recoveries_million |
|---:|:-----------|------:|:--------------------|--------:|-----------:|---------:|------------:|----------------:|-----------------:|---------------------:|----------------------:|--------------------------:|
|  1 | San Marino |    65 | 2020-05-01 00:00:00 |     580 |         11 |       41 |           0 |           324.8 |              0   |                  282 |                     4 |                        75 |
|  2 | Qatar      |    63 | 2020-05-01 00:00:00 |   14096 |        687 |       12 |           2 |           242.6 |              0.7 |                  280 |                     0 |                        31 |
|  3 | Singapore  |   100 | 2020-05-01 00:00:00 |   17101 |        932 |       16 |           1 |           160.6 |              0.2 |                  123 |                     0 |                         7 |
|  4 | Maldives   |    55 | 2020-05-01 00:00:00 |     491 |         23 |        1 |           0 |            43.3 |              0   |                   97 |                     0 |                         0 |
|  5 | Belarus    |    64 | 2020-05-01 00:00:00 |   14917 |        890 |       93 |           4 |            94.2 |              0.4 |                   92 |                     0 |                        27 |
| 27 | Brazil     |    66 | 2020-05-01 00:00:00 |   92202 |       5015 |     6412 |         406 |            23.8 |              1.9 |                   25 |                     1 |                         7 |
----------------------
## World' analysis
### Cases, deaths and recoveries
![](world_cases_deaths.png)

 ### Cases, deaths and recoveries per million
Million of population normalizes the features so they can me better comparable among the selected countries. As we can see, the first charts shows us how aggressive the pandemic is in Italy, Spain and somehow in France.
![](world_cases_deaths_million.png)

 ### Active cases, world overview, % recoveries and mortality
![](world_active_cases_percentages.png)
----------------------
## Brazil's analysis


 ### Cases, deaths and recoveries
![](brazil_number_million_variation.png)

 ### Moving averages (last 7 days)
![](brazil_movingAvg.png)