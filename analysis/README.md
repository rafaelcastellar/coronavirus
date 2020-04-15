# **Analysis and monitoring**
These analysis are related to the Covid19 pandemic data up to **2020-04-13**.

As there are many countries to have all of their data plotted together, I selected a few of them plus Brazil to be compared with:['Brazil', 'Italy', 'United Kingdom', 'Spain', 'US', 'France', 'Belgium'].

Some countries are not in UN dataset, so we can not analyse them by population. They can be found at the end of the *[data_engineering.ipynb](../data_engineering.ipynb)*.

*Tip: you can set yourself at the analysis notebook which countries you prefer to compare*

## Top 5 deadliest countries + Brazil
|     | country        |   day | date                |   cases |   case_day |   deaths |   death_day |   cases_million |   deaths_million |   avg7_cases_million |   avg7_deaths_million |   avg7_recoveries_million |
|----:|:---------------|------:|:--------------------|--------:|-----------:|---------:|------------:|----------------:|-----------------:|---------------------:|----------------------:|--------------------------:|
|   1 | Belgium        |    70 | 2020-04-13 00:00:00 |   30589 |        942 |     3903 |         303 |            81.6 |             26.3 |                  121 |                    28 |                        33 |
|   2 | Andorra        |    43 | 2020-04-13 00:00:00 |     646 |          8 |       29 |           0 |           103.7 |              0   |                  224 |                    14 |                       179 |
|   3 | France         |    81 | 2020-04-13 00:00:00 |  137875 |       4205 |    14986 |         574 |            64.6 |              8.8 |                   85 |                    13 |                        23 |
|   4 | Spain          |    73 | 2020-04-13 00:00:00 |  170099 |       3268 |    17756 |         547 |            69.9 |             11.7 |                  102 |                    13 |                        74 |
|   5 | United Kingdom |    74 | 2020-04-13 00:00:00 |   89570 |       4364 |    11347 |         718 |            64.6 |             10.6 |                   78 |                    12 |                         0 |
| 139 | Brazil         |    48 | 2020-04-13 00:00:00 |   23430 |       1238 |     1328 |         105 |             5.9 |              0.5 |                    7 |                     0 |                         0 |


 ## Top 5 most transmissible countries + Brazil
|    | country    |   day | date                |   cases |   case_day |   deaths |   death_day |   cases_million |   deaths_million |   avg7_cases_million |   avg7_deaths_million |   avg7_recoveries_million |
|---:|:-----------|------:|:--------------------|--------:|-----------:|---------:|------------:|----------------:|-----------------:|---------------------:|----------------------:|--------------------------:|
|  1 | San Marino |    47 | 2020-04-13 00:00:00 |     356 |          0 |       35 |           0 |             0   |              0   |                  379 |                    12 |                        75 |
|  2 | Andorra    |    43 | 2020-04-13 00:00:00 |     646 |          8 |       29 |           0 |           103.7 |              0   |                  224 |                    14 |                       179 |
|  3 | Ireland    |    45 | 2020-04-13 00:00:00 |   10647 |        992 |      365 |          31 |           203.2 |              6.3 |                  154 |                     5 |                         0 |
|  4 | Belgium    |    70 | 2020-04-13 00:00:00 |   30589 |        942 |     3903 |         303 |            81.6 |             26.3 |                  121 |                    28 |                        33 |
|  5 | Luxembourg |    45 | 2020-04-13 00:00:00 |    3292 |         11 |       69 |           3 |            17.9 |              4.9 |                  104 |                     6 |                         0 |
| 57 | Brazil     |    48 | 2020-04-13 00:00:00 |   23430 |       1238 |     1328 |         105 |             5.9 |              0.5 |                    7 |                     0 |                         0 |
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