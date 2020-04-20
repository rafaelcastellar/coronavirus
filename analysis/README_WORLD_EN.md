[<img src="https://raw.githubusercontent.com/NovelCOVID/API/master/assets/flags/br.png" width="30"  /> Versão em português](README_WORLD.md)

# **Analysis and monitoring**
These analysis are related to the Covid19 pandemic data up to **2020-04-19**.

As there are many countries to have all of their data plotted together, I selected a few of them plus Brazil to be compared with:['Brazil', 'Italy', 'United Kingdom', 'Spain', 'US', 'France', 'Belgium'].

Some countries are not in UN dataset, so we can not analyse them by population. They can be found at the end of the *[data_engineering.ipynb](../data_engineering.ipynb)*.

*Tip: you can set yourself at the analysis notebook which countries you prefer to compare*

## Top 5 deadliest countries + Brazil
|     | country        |   day | date                |   cases |   case_day |   deaths |   death_day |   cases_million |   deaths_million |   avg7_cases_million |   avg7_deaths_million |   avg7_recoveries_million |
|----:|:---------------|------:|:--------------------|--------:|-----------:|---------:|------------:|----------------:|-----------------:|---------------------:|----------------------:|--------------------------:|
|   1 | Belgium        |    76 | 2020-04-19 00:00:00 |   38496 |       1313 |     5683 |         230 |           113.8 |             19.9 |                  109 |                    25 |                        28 |
|   2 | San Marino     |    53 | 2020-04-19 00:00:00 |     461 |          6 |       39 |           0 |           177.2 |              0   |                  442 |                    16 |                        29 |
|   3 | Andorra        |    49 | 2020-04-19 00:00:00 |     713 |          9 |       36 |           1 |           116.7 |             13   |                  138 |                    12 |                       198 |
|   4 | France         |    87 | 2020-04-19 00:00:00 |  154097 |       4948 |    19744 |         399 |            76   |              6.1 |                   71 |                    11 |                        21 |
|   5 | United Kingdom |    80 | 2020-04-19 00:00:00 |  121172 |       5858 |    16095 |         597 |            86.7 |              8.8 |                   76 |                    11 |                         0 |
| 141 | Brazil         |    54 | 2020-04-19 00:00:00 |   38654 |       1996 |     2462 |         108 |             9.5 |              0.5 |                   11 |                     0 |                        14 |


 ## Top 5 most transmissible countries + Brazil
|    | country    |   day | date                |   cases |   case_day |   deaths |   death_day |   cases_million |   deaths_million |   avg7_cases_million |   avg7_deaths_million |   avg7_recoveries_million |
|---:|:-----------|------:|:--------------------|--------:|-----------:|---------:|------------:|----------------:|-----------------:|---------------------:|----------------------:|--------------------------:|
|  1 | San Marino |    53 | 2020-04-19 00:00:00 |     461 |          6 |       39 |           0 |           177.2 |              0   |                  442 |                    16 |                        29 |
|  2 | Ireland    |    51 | 2020-04-19 00:00:00 |   15251 |        493 |      610 |          39 |           101   |              8   |                  163 |                     8 |                         1 |
|  3 | Andorra    |    49 | 2020-04-19 00:00:00 |     713 |          9 |       36 |           1 |           116.7 |             13   |                  138 |                    12 |                       198 |
|  4 | Qatar      |    51 | 2020-04-19 00:00:00 |    5448 |        440 |        8 |           0 |           155.4 |              0   |                  124 |                     0 |                        12 |
|  5 | Belgium    |    76 | 2020-04-19 00:00:00 |   38496 |       1313 |     5683 |         230 |           113.8 |             19.9 |                  109 |                    25 |                        28 |
| 45 | Brazil     |    54 | 2020-04-19 00:00:00 |   38654 |       1996 |     2462 |         108 |             9.5 |              0.5 |                   11 |                     0 |                        14 |
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