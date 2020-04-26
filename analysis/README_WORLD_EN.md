[<img src="https://raw.githubusercontent.com/NovelCOVID/API/master/assets/flags/br.png" width="30"  /> Versão em português](README_WORLD.md)

# **Analysis and monitoring**
These analysis are related to the Covid19 pandemic data up to **2020-04-25**.

As there are many countries to have all of their data plotted together, I selected a few of them plus Brazil to be compared with:['Brazil', 'Italy', 'United Kingdom', 'Spain', 'US', 'France', 'Belgium'].

Some countries are not in UN dataset, so we can not analyse them by population. They can be found at the end of the *[data_engineering.ipynb](../data_engineering.ipynb)*.

*Tip: you can set yourself at the analysis notebook which countries you prefer to compare*

## Top 5 deadliest countries + Brazil
|    | country        |   day | date                |   cases |   case_day |   deaths |   death_day |   cases_million |   deaths_million |   avg7_cases_million |   avg7_deaths_million |   avg7_recoveries_million |
|---:|:---------------|------:|:--------------------|--------:|-----------:|---------:|------------:|----------------:|-----------------:|---------------------:|----------------------:|--------------------------:|
|  1 | Belgium        |    82 | 2020-04-25 00:00:00 |   45325 |       1032 |     6917 |         238 |            89.4 |             20.6 |                  100 |                    18 |                        25 |
|  2 | Ireland        |    57 | 2020-04-25 00:00:00 |   18561 |        377 |     1063 |          49 |            77.2 |             10   |                  111 |                    14 |                       267 |
|  3 | United Kingdom |    86 | 2020-04-25 00:00:00 |  149569 |       4929 |    20381 |         814 |            73   |             12.1 |                   72 |                    10 |                         0 |
|  4 | Sweden         |    86 | 2020-04-25 00:00:00 |   18177 |        610 |     2192 |          40 |            60.8 |              4   |                   62 |                     9 |                         6 |
|  5 | Andorra        |    55 | 2020-04-25 00:00:00 |     738 |          7 |       40 |           0 |            90.7 |              0   |                   62 |                     9 |                       257 |
| 26 | Brazil         |    60 | 2020-04-25 00:00:00 |   59324 |       5281 |     4057 |         353 |            25   |              1.7 |                   15 |                     1 |                        10 |


 ## Top 5 most transmissible countries + Brazil
|    | country    |   day | date                |   cases |   case_day |   deaths |   death_day |   cases_million |   deaths_million |   avg7_cases_million |   avg7_deaths_million |   avg7_recoveries_million |
|---:|:-----------|------:|:--------------------|--------:|-----------:|---------:|------------:|----------------:|-----------------:|---------------------:|----------------------:|--------------------------:|
|  1 | San Marino |    59 | 2020-04-25 00:00:00 |     513 |          0 |       40 |           0 |             0   |              0   |                  244 |                     4 |                        16 |
|  2 | Qatar      |    57 | 2020-04-25 00:00:00 |    9358 |        833 |       10 |           0 |           294.1 |              0   |                  219 |                     0 |                        21 |
|  3 | Singapore  |    94 | 2020-04-25 00:00:00 |   12693 |        618 |       12 |           0 |           106.5 |              0   |                  164 |                     0 |                         6 |
|  4 | Ecuador    |    56 | 2020-04-25 00:00:00 |   22719 |          0 |      576 |           0 |             0   |              0   |                  112 |                     0 |                         2 |
|  5 | Ireland    |    57 | 2020-04-25 00:00:00 |   18561 |        377 |     1063 |          49 |            77.2 |             10   |                  111 |                    14 |                       267 |
| 38 | Brazil     |    60 | 2020-04-25 00:00:00 |   59324 |       5281 |     4057 |         353 |            25   |              1.7 |                   15 |                     1 |                        10 |
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