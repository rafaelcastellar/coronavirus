# **Analysis and monitoring**
These analysis are related to the Covid19 pandemic data upto 2020-04-08.

As we have a big number of countries around ther world to have all of their data ploted togheter, will select a few of them and Brazil to be compared with:['Brazil', 'Italy', 'United Kingdom', 'Spain', 'US', 'China', 'France'].
Some countries are not in UN dataset, so we can not analise them by population. They can be found at the end of the *[data_engineering.ipynb](../data_engineering.ipynb)*.
*Tip: you can set yourself at the analysis notebook which countries you prefer to compare*

## Top 5 deadliest countries + Brazil
|     | country    |   day | date                |   cases |   case_day |   deaths |   death_day |   cases_million |   deaths_million |   avg7_cases_million |   avg7_deaths_million |   avg7_recoveries_million |
|----:|:-----------|------:|:--------------------|--------:|-----------:|---------:|------------:|----------------:|-----------------:|---------------------:|----------------------:|--------------------------:|
|   1 | San Marino |    41 | 2020-04-07 00:00:00 |     279 |         13 |       34 |           2 |           383.9 |             59.1 |                  181 |                    33 |                       113 |
|   2 | Andorra    |    37 | 2020-04-07 00:00:00 |     545 |         20 |       22 |           1 |           259.2 |             13   |                  312 |                    18 |                        53 |
|   3 | Spain      |    67 | 2020-04-07 00:00:00 |  141942 |       5267 |    14045 |         704 |           112.7 |             15.1 |                  140 |                    17 |                        73 |
|   4 | Belgium    |    64 | 2020-04-07 00:00:00 |   22194 |       1380 |     2035 |         403 |           119.6 |             34.9 |                  116 |                    16 |                        30 |
|   5 | France     |    75 | 2020-04-07 00:00:00 |  110065 |      11102 |    10343 |        1417 |           170.5 |             21.8 |                  125 |                    14 |                        21 |
| 138 | Brazil     |    42 | 2020-04-07 00:00:00 |   14034 |       1873 |      686 |         122 |             8.9 |              0.6 |                    5 |                     0 |                         0 |


 ## Top 5 most transmissible countries + Brazil
|    | country    |   day | date                |   cases |   case_day |   deaths |   death_day |   cases_million |   deaths_million |   avg7_cases_million |   avg7_deaths_million |   avg7_recoveries_million |
|---:|:-----------|------:|:--------------------|--------:|-----------:|---------:|------------:|----------------:|-----------------:|---------------------:|----------------------:|--------------------------:|
|  1 | Andorra    |    37 | 2020-04-07 00:00:00 |     545 |         20 |       22 |           1 |           259.2 |             13   |                  312 |                    18 |                        53 |
|  2 | Iceland    |    40 | 2020-04-07 00:00:00 |    1586 |         24 |        6 |           0 |            70.8 |              0   |                  190 |                     1 |                       152 |
|  3 | Luxembourg |    39 | 2020-04-07 00:00:00 |    2970 |        127 |       44 |           3 |           206.3 |              4.9 |                  183 |                     4 |                        97 |
|  4 | San Marino |    41 | 2020-04-07 00:00:00 |     279 |         13 |       34 |           2 |           383.9 |             59.1 |                  181 |                    33 |                       113 |
|  5 | Spain      |    67 | 2020-04-07 00:00:00 |  141942 |       5267 |    14045 |         704 |           112.7 |             15.1 |                  140 |                    17 |                        73 |
| 64 | Brazil     |    42 | 2020-04-07 00:00:00 |   14034 |       1873 |      686 |         122 |             8.9 |              0.6 |                    5 |                     0 |                         0 |
----------------------
## World analysis
### Cases and deaths
![](world_cases_deaths.png)
### Cases and deaths per million
Million of population normalizes the features so they can me better compareble among the selected countries. As we can see, the first charts shows us how agressive the pandemic is in Italy, Spain and somehow in France.
![](world_cases_deaths_million.png)
### Active cases, world overview, % recoveries and lethality
![](world_active_cases_percentages.png)
----------------------
## Brazil analysis

### Cases, deaths and recoveries
![](brazil_number_million_variation.png)
### Moving averages (last 7 days)
![](brazil_movingAvg.png)