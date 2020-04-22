[<img src="https://raw.githubusercontent.com/NovelCOVID/API/master/assets/flags/br.png" width="30"  /> Versão em português](README_WORLD.md)

# **Analysis and monitoring**
These analysis are related to the Covid19 pandemic data up to **2020-04-21**.

As there are many countries to have all of their data plotted together, I selected a few of them plus Brazil to be compared with:['Brazil', 'Italy', 'United Kingdom', 'Spain', 'US', 'France', 'Belgium'].

Some countries are not in UN dataset, so we can not analyse them by population. They can be found at the end of the *[data_engineering.ipynb](../data_engineering.ipynb)*.

*Tip: you can set yourself at the analysis notebook which countries you prefer to compare*

## Top 5 deadliest countries + Brazil
|     | country        |   day | date                |   cases |   case_day |   deaths |   death_day |   cases_million |   deaths_million |   avg7_cases_million |   avg7_deaths_million |   avg7_recoveries_million |
|----:|:---------------|------:|:--------------------|--------:|-----------:|---------:|------------:|----------------:|-----------------:|---------------------:|----------------------:|--------------------------:|
|   1 | Belgium        |    78 | 2020-04-21 00:00:00 |   40956 |        973 |     5998 |         170 |            84.3 |             14.7 |                  121 |                    22 |                        26 |
|   2 | San Marino     |    55 | 2020-04-21 00:00:00 |     476 |         14 |       40 |           1 |           413.4 |             29.5 |                  442 |                    16 |                        37 |
|   3 | Andorra        |    51 | 2020-04-21 00:00:00 |     717 |          0 |       37 |           0 |             0   |              0   |                  107 |                    11 |                       285 |
|   4 | France         |    89 | 2020-04-21 00:00:00 |  159297 |       2817 |    20829 |         537 |            43.3 |              8.2 |                   61 |                    11 |                        23 |
|   5 | United Kingdom |    82 | 2020-04-21 00:00:00 |  130172 |       4316 |    17378 |         828 |            63.9 |             12.3 |                   74 |                    11 |                         0 |
| 141 | Brazil         |    56 | 2020-04-21 00:00:00 |   43079 |       2336 |     2741 |         154 |            11.1 |              0.7 |                   12 |                     0 |                        13 |


 ## Top 5 most transmissible countries + Brazil
|    | country    |   day | date                |   cases |   case_day |   deaths |   death_day |   cases_million |   deaths_million |   avg7_cases_million |   avg7_deaths_million |   avg7_recoveries_million |
|---:|:-----------|------:|:--------------------|--------:|-----------:|---------:|------------:|----------------:|-----------------:|---------------------:|----------------------:|--------------------------:|
|  1 | San Marino |    55 | 2020-04-21 00:00:00 |     476 |         14 |       40 |           1 |           413.4 |             29.5 |                  442 |                    16 |                        37 |
|  2 | Qatar      |    53 | 2020-04-21 00:00:00 |    6533 |        518 |        9 |           0 |           182.9 |              0   |                  156 |                     0 |                        12 |
|  3 | Singapore  |    90 | 2020-04-21 00:00:00 |    9125 |       1111 |       11 |           0 |           191.4 |              0   |                  144 |                     0 |                         5 |
|  4 | Ireland    |    53 | 2020-04-21 00:00:00 |   16040 |        388 |      730 |          43 |            79.5 |              8.8 |                  133 |                     9 |                       269 |
|  5 | Belgium    |    78 | 2020-04-21 00:00:00 |   40956 |        973 |     5998 |         170 |            84.3 |             14.7 |                  121 |                    22 |                        26 |
| 45 | Brazil     |    56 | 2020-04-21 00:00:00 |   43079 |       2336 |     2741 |         154 |            11.1 |              0.7 |                   12 |                     0 |                        13 |
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