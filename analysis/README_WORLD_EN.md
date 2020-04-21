[<img src="https://raw.githubusercontent.com/NovelCOVID/API/master/assets/flags/br.png" width="30"  /> Versão em português](README_WORLD.md)

# **Analysis and monitoring**
These analysis are related to the Covid19 pandemic data up to **2020-04-20**.

As there are many countries to have all of their data plotted together, I selected a few of them plus Brazil to be compared with:['Brazil', 'Italy', 'United Kingdom', 'Spain', 'US', 'France', 'Belgium'].

Some countries are not in UN dataset, so we can not analyse them by population. They can be found at the end of the *[data_engineering.ipynb](../data_engineering.ipynb)*.

*Tip: you can set yourself at the analysis notebook which countries you prefer to compare*

## Top 5 deadliest countries + Brazil
|     | country        |   day | date                |   cases |   case_day |   deaths |   death_day |   cases_million |   deaths_million |   avg7_cases_million |   avg7_deaths_million |   avg7_recoveries_million |
|----:|:---------------|------:|:--------------------|--------:|-----------:|---------:|------------:|----------------:|-----------------:|---------------------:|----------------------:|--------------------------:|
|   1 | Belgium        |    77 | 2020-04-20 00:00:00 |   39983 |       1487 |     5828 |         145 |           128.9 |             12.6 |                  116 |                    23 |                        27 |
|   2 | San Marino     |    54 | 2020-04-20 00:00:00 |     462 |          1 |       39 |           0 |            29.5 |              0   |                  447 |                    16 |                        33 |
|   3 | Andorra        |    50 | 2020-04-20 00:00:00 |     717 |          4 |       37 |           1 |            51.8 |             13   |                  131 |                    14 |                       222 |
|   4 | France         |    88 | 2020-04-20 00:00:00 |  156480 |       2383 |    20292 |         548 |            36.6 |              8.4 |                   68 |                    11 |                        22 |
|   5 | United Kingdom |    81 | 2020-04-20 00:00:00 |  125856 |       4684 |    16550 |         455 |            69.4 |              6.7 |                   76 |                    10 |                         0 |
| 141 | Brazil         |    55 | 2020-04-20 00:00:00 |   40743 |       2089 |     2587 |         125 |             9.9 |              0.6 |                   11 |                     0 |                        14 |


 ## Top 5 most transmissible countries + Brazil
|    | country    |   day | date                |   cases |   case_day |   deaths |   death_day |   cases_million |   deaths_million |   avg7_cases_million |   avg7_deaths_million |   avg7_recoveries_million |
|---:|:-----------|------:|:--------------------|--------:|-----------:|---------:|------------:|----------------:|-----------------:|---------------------:|----------------------:|--------------------------:|
|  1 | San Marino |    54 | 2020-04-20 00:00:00 |     462 |          1 |       39 |           0 |            29.5 |              0   |                  447 |                    16 |                        33 |
|  2 | Ireland    |    52 | 2020-04-20 00:00:00 |   15652 |        401 |      687 |          77 |            82.1 |             15.8 |                  146 |                     9 |                         1 |
|  3 | Qatar      |    52 | 2020-04-20 00:00:00 |    6015 |        567 |        9 |           1 |           200.2 |              0.4 |                  140 |                     0 |                        11 |
|  4 | Andorra    |    50 | 2020-04-20 00:00:00 |     717 |          4 |       37 |           1 |            51.8 |             13   |                  131 |                    14 |                       222 |
|  5 | Singapore  |    89 | 2020-04-20 00:00:00 |    8014 |       1426 |       11 |           0 |           245.7 |              0   |                  125 |                     0 |                         5 |
| 47 | Brazil     |    55 | 2020-04-20 00:00:00 |   40743 |       2089 |     2587 |         125 |             9.9 |              0.6 |                   11 |                     0 |                        14 |
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