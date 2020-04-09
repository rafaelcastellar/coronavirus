# **Analysis and monitoring**
These analysis are related to the Covid19 pandemic data up to **2020-04-07**.

As there are many countries to have all of their data plotted together, I selected a few of them plus Brazil to be compared with:['Brazil', 'Italy', 'United Kingdom', 'Spain', 'US', 'China', 'France'].
Some countries are not in UN dataset, so we can not analyse them by population. They can be found at the end of the *[data_engineering.ipynb](../data_engineering.ipynb)*.
*Tip: you can set yourself at the analysis notebook which countries you prefer to compare*

## Top 5 deadliest countries + Brazil
|     | country    |   day | date                |   cases |   case_day |   deaths |   death_day |   cases_million |   deaths_million |   avg7_cases_million |   avg7_deaths_million |   avg7_recoveries_million |
|----:|:-----------|------:|:--------------------|--------:|-----------:|---------:|------------:|----------------:|-----------------:|---------------------:|----------------------:|--------------------------:|
|   1 | San Marino |    40 | 2020-04-06 00:00:00 |     266 |          0 |       32 |           0 |             0   |              0   |                  151 |                    29 |                        92 |
|   2 | Andorra    |    36 | 2020-04-06 00:00:00 |     525 |         24 |       21 |           3 |           311.1 |             38.9 |                  287 |                    24 |                        38 |
|   3 | Spain      |    66 | 2020-04-06 00:00:00 |  136675 |       5029 |    13341 |         700 |           107.6 |             15   |                  148 |                    17 |                        72 |
|   4 | Belgium    |    63 | 2020-04-06 00:00:00 |   20814 |       1123 |     1632 |         185 |            97.3 |             16   |                  110 |                    13 |                        30 |
|   5 | France     |    74 | 2020-04-06 00:00:00 |   98963 |       5190 |     8926 |         833 |            79.7 |             12.8 |                  118 |                    12 |                        20 |
| 139 | Brazil     |    41 | 2020-04-06 00:00:00 |   12161 |       1031 |      564 |          78 |             4.9 |              0.4 |                    5 |                     0 |                         0 |


 ## Top 5 most transmissible countries + Brazil
|    | country    |   day | date                |   cases |   case_day |   deaths |   death_day |   cases_million |   deaths_million |   avg7_cases_million |   avg7_deaths_million |   avg7_recoveries_million |
|---:|:-----------|------:|:--------------------|--------:|-----------:|---------:|------------:|----------------:|-----------------:|---------------------:|----------------------:|--------------------------:|
|  1 | Andorra    |    36 | 2020-04-06 00:00:00 |     525 |         24 |       21 |           3 |           311.1 |             38.9 |                  287 |                    24 |                        38 |
|  2 | Iceland    |    39 | 2020-04-06 00:00:00 |    1562 |         76 |        6 |           2 |           224.2 |              5.9 |                  200 |                     1 |                       127 |
|  3 | Luxembourg |    38 | 2020-04-06 00:00:00 |    2843 |         39 |       41 |           5 |            63.3 |              8.1 |                  198 |                     4 |                       106 |
|  4 | San Marino |    40 | 2020-04-06 00:00:00 |     266 |          0 |       32 |           0 |             0   |              0   |                  151 |                    29 |                        92 |
|  5 | Spain      |    66 | 2020-04-06 00:00:00 |  136675 |       5029 |    13341 |         700 |           107.6 |             15   |                  148 |                    17 |                        72 |
| 61 | Brazil     |    41 | 2020-04-06 00:00:00 |   12161 |       1031 |      564 |          78 |             4.9 |              0.4 |                    5 |                     0 |                         0 |
----------------------
## World' analysis
### Cases and deaths
![](world_cases_deaths.png)

 ### Cases and deaths per million
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