# **Analysis and monitoring**
These analysis are related to the Covid19 pandemic data up to **2020-04-12**.

As there are many countries to have all of their data plotted together, I selected a few of them plus Brazil to be compared with:['Brazil', 'Italy', 'United Kingdom', 'Spain', 'US', 'China', 'France'].

Some countries are not in UN dataset, so we can not analyse them by population. They can be found at the end of the *[data_engineering.ipynb](../data_engineering.ipynb)*.

*Tip: you can set yourself at the analysis notebook which countries you prefer to compare*

## Top 5 deadliest countries + Brazil
|     | country    |   day | date                |   cases |   case_day |   deaths |   death_day |   cases_million |   deaths_million |   avg7_cases_million |   avg7_deaths_million |   avg7_recoveries_million |
|----:|:-----------|------:|:--------------------|--------:|-----------:|---------:|------------:|----------------:|-----------------:|---------------------:|----------------------:|--------------------------:|
|   1 | Belgium    |    68 | 2020-04-11 00:00:00 |   28018 |       1351 |     3346 |         327 |           117.1 |             28.3 |                  118 |                    25 |                        33 |
|   2 | Andorra    |    41 | 2020-04-11 00:00:00 |     601 |          0 |       26 |           0 |             0   |              0   |                  249 |                    16 |                        92 |
|   3 | Spain      |    71 | 2020-04-11 00:00:00 |  163027 |       4754 |    16606 |         525 |           101.7 |             11.2 |                  112 |                    14 |                        76 |
|   4 | France     |    79 | 2020-04-11 00:00:00 |  130727 |       4796 |    13851 |         636 |            73.6 |              9.8 |                   87 |                    13 |                        24 |
|   5 | San Marino |    45 | 2020-04-11 00:00:00 |     356 |         12 |       35 |           1 |           354.4 |             29.5 |                  409 |                    12 |                       109 |
| 139 | Brazil     |    46 | 2020-04-11 00:00:00 |   20727 |       1089 |     1124 |          67 |             5.2 |              0.3 |                    7 |                     0 |                         0 |


 ## Top 5 most transmissible countries + Brazil
|    | country    |   day | date                |   cases |   case_day |   deaths |   death_day |   cases_million |   deaths_million |   avg7_cases_million |   avg7_deaths_million |   avg7_recoveries_million |
|---:|:-----------|------:|:--------------------|--------:|-----------:|---------:|------------:|----------------:|-----------------:|---------------------:|----------------------:|--------------------------:|
|  1 | San Marino |    45 | 2020-04-11 00:00:00 |     356 |         12 |       35 |           1 |           354.4 |             29.5 |                  409 |                    12 |                       109 |
|  2 | Andorra    |    41 | 2020-04-11 00:00:00 |     601 |          0 |       26 |           0 |             0   |              0   |                  249 |                    16 |                        92 |
|  3 | Ireland    |    43 | 2020-04-11 00:00:00 |    8928 |        839 |      320 |          33 |           171.8 |              6.8 |                  126 |                     5 |                         0 |
|  4 | Luxembourg |    43 | 2020-04-11 00:00:00 |    3270 |         47 |       62 |           8 |            76.3 |             13   |                  125 |                     7 |                         0 |
|  5 | Belgium    |    68 | 2020-04-11 00:00:00 |   28018 |       1351 |     3346 |         327 |           117.1 |             28.3 |                  118 |                    25 |                        33 |
| 57 | Brazil     |    46 | 2020-04-11 00:00:00 |   20727 |       1089 |     1124 |          67 |             5.2 |              0.3 |                    7 |                     0 |                         0 |
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