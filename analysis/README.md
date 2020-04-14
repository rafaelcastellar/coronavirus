# **Analysis and monitoring**
These analysis are related to the Covid19 pandemic data up to **2020-04-13**.

As there are many countries to have all of their data plotted together, I selected a few of them plus Brazil to be compared with:['Brazil', 'Italy', 'United Kingdom', 'Spain', 'US', 'China', 'France'].

Some countries are not in UN dataset, so we can not analyse them by population. They can be found at the end of the *[data_engineering.ipynb](../data_engineering.ipynb)*.

*Tip: you can set yourself at the analysis notebook which countries you prefer to compare*

## Top 5 deadliest countries + Brazil
|     | country    |   day | date                |   cases |   case_day |   deaths |   death_day |   cases_million |   deaths_million |   avg7_cases_million |   avg7_deaths_million |   avg7_recoveries_million |
|----:|:-----------|------:|:--------------------|--------:|-----------:|---------:|------------:|----------------:|-----------------:|---------------------:|----------------------:|--------------------------:|
|   1 | Belgium    |    69 | 2020-04-12 00:00:00 |   29647 |       1629 |     3600 |         254 |           141.2 |             22   |                  123 |                    26 |                        33 |
|   2 | Andorra    |    42 | 2020-04-12 00:00:00 |     638 |         37 |       29 |           3 |           479.6 |             38.9 |                  253 |                    20 |                       188 |
|   3 | France     |    80 | 2020-04-12 00:00:00 |  133670 |       2943 |    14412 |         561 |            45.2 |              8.6 |                   87 |                    13 |                        24 |
|   4 | Spain      |    72 | 2020-04-12 00:00:00 |  166831 |       3804 |    17209 |         603 |            81.4 |             12.9 |                  107 |                    13 |                        74 |
|   5 | San Marino |    46 | 2020-04-12 00:00:00 |     356 |          0 |       35 |           0 |             0   |              0   |                  379 |                    12 |                        75 |
| 139 | Brazil     |    47 | 2020-04-12 00:00:00 |   22192 |       1465 |     1223 |          99 |             6.9 |              0.5 |                    7 |                     0 |                         0 |


 ## Top 5 most transmissible countries + Brazil
|    | country    |   day | date                |   cases |   case_day |   deaths |   death_day |   cases_million |   deaths_million |   avg7_cases_million |   avg7_deaths_million |   avg7_recoveries_million |
|---:|:-----------|------:|:--------------------|--------:|-----------:|---------:|------------:|----------------:|-----------------:|---------------------:|----------------------:|--------------------------:|
|  1 | San Marino |    46 | 2020-04-12 00:00:00 |     356 |          0 |       35 |           0 |             0   |              0   |                  379 |                    12 |                        75 |
|  2 | Andorra    |    42 | 2020-04-12 00:00:00 |     638 |         37 |       29 |           3 |           479.6 |             38.9 |                  253 |                    20 |                       188 |
|  3 | Ireland    |    44 | 2020-04-12 00:00:00 |    9655 |        727 |      334 |          14 |           148.9 |              2.9 |                  136 |                     5 |                         0 |
|  4 | Belgium    |    69 | 2020-04-12 00:00:00 |   29647 |       1629 |     3600 |         254 |           141.2 |             22   |                  123 |                    26 |                        33 |
|  5 | Luxembourg |    44 | 2020-04-12 00:00:00 |    3281 |         11 |       66 |           4 |            17.9 |              6.5 |                  110 |                     6 |                         0 |
| 56 | Brazil     |    47 | 2020-04-12 00:00:00 |   22192 |       1465 |     1223 |          99 |             6.9 |              0.5 |                    7 |                     0 |                         0 |
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