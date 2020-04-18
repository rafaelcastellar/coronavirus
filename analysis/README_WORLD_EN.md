[<img src="https://raw.githubusercontent.com/NovelCOVID/API/master/assets/flags/br.png" width="30"  /> Versão em português](README_WORLD.md)

# **Analysis and monitoring**
These analysis are related to the Covid19 pandemic data up to **2020-04-17**.

As there are many countries to have all of their data plotted together, I selected a few of them plus Brazil to be compared with:['Brazil', 'Italy', 'United Kingdom', 'Spain', 'US', 'France', 'Belgium'].

Some countries are not in UN dataset, so we can not analyse them by population. They can be found at the end of the *[data_engineering.ipynb](../data_engineering.ipynb)*.

*Tip: you can set yourself at the analysis notebook which countries you prefer to compare*

## Top 5 deadliest countries + Brazil
|     | country    |   day | date                |   cases |   case_day |   deaths |   death_day |   cases_million |   deaths_million |   avg7_cases_million |   avg7_deaths_million |   avg7_recoveries_million |
|----:|:-----------|------:|:--------------------|--------:|-----------:|---------:|------------:|----------------:|-----------------:|---------------------:|----------------------:|--------------------------:|
|   1 | Belgium    |    74 | 2020-04-17 00:00:00 |   36138 |       1329 |     5163 |         306 |           115.2 |             26.5 |                  117 |                    26 |                        29 |
|   2 | San Marino |    51 | 2020-04-17 00:00:00 |     435 |          9 |       39 |           1 |           265.8 |             29.5 |                  383 |                    21 |                        29 |
|   3 | Andorra    |    47 | 2020-04-17 00:00:00 |     696 |         23 |       35 |           2 |           298.1 |             25.9 |                  175 |                    16 |                       222 |
|   4 | France     |    85 | 2020-04-17 00:00:00 |  149130 |       2039 |    18703 |         762 |            31.3 |             11.7 |                  125 |                    12 |                        21 |
|   5 | Spain      |    77 | 2020-04-17 00:00:00 |  190839 |       5891 |    20002 |         687 |           126   |             14.7 |                   99 |                    11 |                        58 |
| 140 | Brazil     |    52 | 2020-04-17 00:00:00 |   33682 |       3257 |     2141 |         217 |            15.4 |              1   |                    9 |                     0 |                         9 |


 ## Top 5 most transmissible countries + Brazil
|    | country    |   day | date                |   cases |   case_day |   deaths |   death_day |   cases_million |   deaths_million |   avg7_cases_million |   avg7_deaths_million |   avg7_recoveries_million |
|---:|:-----------|------:|:--------------------|--------:|-----------:|---------:|------------:|----------------:|-----------------:|---------------------:|----------------------:|--------------------------:|
|  1 | San Marino |    51 | 2020-04-17 00:00:00 |     435 |          9 |       39 |           1 |           265.8 |             29.5 |                  383 |                    21 |                        29 |
|  2 | Andorra    |    47 | 2020-04-17 00:00:00 |     696 |         23 |       35 |           2 |           298.1 |             25.9 |                  175 |                    16 |                       222 |
|  3 | Ireland    |    49 | 2020-04-17 00:00:00 |   13980 |        709 |      530 |          44 |           145.2 |              9   |                  172 |                     7 |                         1 |
|  4 | France     |    85 | 2020-04-17 00:00:00 |  149130 |       2039 |    18703 |         762 |            31.3 |             11.7 |                  125 |                    12 |                        21 |
|  5 | Belgium    |    74 | 2020-04-17 00:00:00 |   36138 |       1329 |     5163 |         306 |           115.2 |             26.5 |                  117 |                    26 |                        29 |
| 50 | Brazil     |    52 | 2020-04-17 00:00:00 |   33682 |       3257 |     2141 |         217 |            15.4 |              1   |                    9 |                     0 |                         9 |
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