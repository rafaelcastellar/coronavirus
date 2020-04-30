[<img src="../data/bandeiras/PT.png" width="30"   /> Versão em português](README_WORLD.md)

# **Analysis and monitoring**
These analysis are related to the Covid19 pandemic data up to **2020-04-29**.

As there are many countries to have all of their data plotted together, I selected a few of them plus Brazil to be compared with:['Brazil', 'Italy', 'United Kingdom', 'Spain', 'US', 'France', 'Belgium'].

Some countries are not in UN dataset, so we can not analyse them by population. They can be found at the end of the *[data_engineering.ipynb](../data_engineering.ipynb)*.

*Tip: you can set yourself at the analysis notebook which countries you prefer to compare*

## Top 5 deadliest countries + Brazil
|    | country        |   day | date                |   cases |   case_day |   deaths |   death_day |   cases_million |   deaths_million |   avg7_cases_million |   avg7_deaths_million |   avg7_recoveries_million |
|---:|:---------------|------:|:--------------------|--------:|-----------:|---------:|------------:|----------------:|-----------------:|---------------------:|----------------------:|--------------------------:|
|  1 | United Kingdom |    90 | 2020-04-29 00:00:00 |  166441 |       4091 |    26166 |        4421 |            60.6 |             65.5 |                   67 |                    16 |                         0 |
|  2 | Belgium        |    86 | 2020-04-29 00:00:00 |   47859 |        525 |     7501 |         170 |            45.5 |             14.7 |                   73 |                    15 |                        22 |
|  3 | Ireland        |    61 | 2020-04-29 00:00:00 |   20253 |        376 |     1190 |          31 |            77   |              6.3 |                  104 |                    12 |                       121 |
|  4 | Andorra        |    59 | 2020-04-29 00:00:00 |     743 |          0 |       42 |           1 |             0   |             13   |                   37 |                     9 |                       211 |
|  5 | Spain          |    89 | 2020-04-29 00:00:00 |  236899 |       4771 |    24275 |         453 |           102.1 |              9.7 |                   87 |                     7 |                       143 |
| 26 | Brazil         |    64 | 2020-04-29 00:00:00 |   79685 |       6450 |     5513 |         430 |            30.6 |              2   |                   22 |                     1 |                         5 |


 ## Top 5 most transmissible countries + Brazil
|    | country    |   day | date                |   cases |   case_day |   deaths |   death_day |   cases_million |   deaths_million |   avg7_cases_million |   avg7_deaths_million |   avg7_recoveries_million |
|---:|:-----------|------:|:--------------------|--------:|-----------:|---------:|------------:|----------------:|-----------------:|---------------------:|----------------------:|--------------------------:|
|  1 | San Marino |    63 | 2020-04-29 00:00:00 |     563 |         10 |       41 |           0 |           295.3 |              0   |                  316 |                     4 |                        29 |
|  2 | Qatar      |    61 | 2020-04-29 00:00:00 |   12564 |        643 |       10 |           0 |           227   |              0   |                  273 |                     0 |                        27 |
|  3 | Singapore  |    98 | 2020-04-29 00:00:00 |   15641 |        690 |       14 |           0 |           118.9 |              0   |                  135 |                     0 |                         7 |
|  4 | Ecuador    |    60 | 2020-04-29 00:00:00 |   24675 |        417 |      883 |          12 |            24   |              0.7 |                  113 |                     2 |                         2 |
|  5 | Ireland    |    61 | 2020-04-29 00:00:00 |   20253 |        376 |     1190 |          31 |            77   |              6.3 |                  104 |                    12 |                       121 |
| 29 | Brazil     |    64 | 2020-04-29 00:00:00 |   79685 |       6450 |     5513 |         430 |            30.6 |              2   |                   22 |                     1 |                         5 |
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