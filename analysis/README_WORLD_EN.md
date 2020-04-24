[<img src="https://raw.githubusercontent.com/NovelCOVID/API/master/assets/flags/br.png" width="30"  /> Versão em português](README_WORLD.md)

# **Analysis and monitoring**
These analysis are related to the Covid19 pandemic data up to **2020-04-22**.

As there are many countries to have all of their data plotted together, I selected a few of them plus Brazil to be compared with:['Brazil', 'Italy', 'United Kingdom', 'Spain', 'US', 'France', 'Belgium'].

Some countries are not in UN dataset, so we can not analyse them by population. They can be found at the end of the *[data_engineering.ipynb](../data_engineering.ipynb)*.

*Tip: you can set yourself at the analysis notebook which countries you prefer to compare*

## Top 5 deadliest countries + Brazil
|     | country        |   day | date                |   cases |   case_day |   deaths |   death_day |   cases_million |   deaths_million |   avg7_cases_million |   avg7_deaths_million |   avg7_recoveries_million |
|----:|:---------------|------:|:--------------------|--------:|-----------:|---------:|------------:|----------------:|-----------------:|---------------------:|----------------------:|--------------------------:|
|   1 | Belgium        |    79 | 2020-04-22 00:00:00 |   41889 |        933 |     6262 |         264 |            80.9 |             22.9 |                  102 |                    22 |                        28 |
|   2 | San Marino     |    56 | 2020-04-22 00:00:00 |     488 |         12 |       40 |           0 |           354.4 |              0   |                  489 |                    16 |                        37 |
|   3 | United Kingdom |    83 | 2020-04-22 00:00:00 |  134638 |       4466 |    18151 |         773 |            66.1 |             11.4 |                   74 |                    11 |                         0 |
|   4 | Sweden         |    83 | 2020-04-22 00:00:00 |   16004 |        682 |     1937 |         172 |            68   |             17.1 |                   58 |                    10 |                         2 |
|   5 | Spain          |    82 | 2020-04-22 00:00:00 |  208389 |       4211 |    21717 |         435 |            90.1 |              9.3 |                   93 |                     9 |                        46 |
| 140 | Brazil         |    57 | 2020-04-22 00:00:00 |   45757 |       2678 |     2906 |         165 |            12.7 |              0.8 |                   11 |                     0 |                         7 |


 ## Top 5 most transmissible countries + Brazil
|    | country    |   day | date                |   cases |   case_day |   deaths |   death_day |   cases_million |   deaths_million |   avg7_cases_million |   avg7_deaths_million |   avg7_recoveries_million |
|---:|:-----------|------:|:--------------------|--------:|-----------:|---------:|------------:|----------------:|-----------------:|---------------------:|----------------------:|--------------------------:|
|  1 | San Marino |    56 | 2020-04-22 00:00:00 |     488 |         12 |       40 |           0 |           354.4 |              0   |                  489 |                    16 |                        37 |
|  2 | Qatar      |    54 | 2020-04-22 00:00:00 |    7141 |        608 |       10 |           1 |           214.7 |              0.4 |                  173 |                     0 |                        14 |
|  3 | Singapore  |    91 | 2020-04-22 00:00:00 |   10141 |       1016 |       12 |           1 |           175   |              0.2 |                  158 |                     0 |                         5 |
|  4 | Ireland    |    54 | 2020-04-22 00:00:00 |   16671 |        631 |      769 |          39 |           129.2 |              8   |                  120 |                     9 |                       267 |
|  5 | Belgium    |    79 | 2020-04-22 00:00:00 |   41889 |        933 |     6262 |         264 |            80.9 |             22.9 |                  102 |                    22 |                        28 |
| 44 | Brazil     |    57 | 2020-04-22 00:00:00 |   45757 |       2678 |     2906 |         165 |            12.7 |              0.8 |                   11 |                     0 |                         7 |
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