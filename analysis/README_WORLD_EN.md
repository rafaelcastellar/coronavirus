[<img src="../data/bandeiras/PT.png" width="30"   /> Versão em português](README_WORLD.md)

# **Analysis and monitoring**
These analysis are related to the Covid19 pandemic data up to **2020-04-27**.

As there are many countries to have all of their data plotted together, I selected a few of them plus Brazil to be compared with:['Brazil', 'Italy', 'United Kingdom', 'Spain', 'US', 'France', 'Belgium'].

Some countries are not in UN dataset, so we can not analyse them by population. They can be found at the end of the *[data_engineering.ipynb](../data_engineering.ipynb)*.

*Tip: you can set yourself at the analysis notebook which countries you prefer to compare*

## Top 5 deadliest countries + Brazil
|    | country        |   day | date                |   cases |   case_day |   deaths |   death_day |   cases_million |   deaths_million |   avg7_cases_million |   avg7_deaths_million |   avg7_recoveries_million |
|---:|:---------------|------:|:--------------------|--------:|-----------:|---------:|------------:|----------------:|-----------------:|---------------------:|----------------------:|--------------------------:|
|  1 | Belgium        |    84 | 2020-04-27 00:00:00 |   46687 |        553 |     7207 |         113 |            47.9 |              9.8 |                   82 |                    17 |                        24 |
|  2 | Ireland        |    59 | 2020-04-27 00:00:00 |   19648 |        386 |     1102 |          15 |            79.1 |              3.1 |                  116 |                    12 |                       267 |
|  3 | Sweden         |    88 | 2020-04-27 00:00:00 |   18926 |        286 |     2274 |          80 |            28.5 |              8   |                   59 |                     9 |                         6 |
|  4 | United Kingdom |    88 | 2020-04-27 00:00:00 |  158348 |       4311 |    21157 |         363 |            63.8 |              5.4 |                   68 |                     9 |                         0 |
|  5 | San Marino     |    61 | 2020-04-27 00:00:00 |     538 |          0 |       41 |           0 |             0   |              0   |                  320 |                     8 |                        12 |
| 23 | Brazil         |    62 | 2020-04-27 00:00:00 |   67446 |       4346 |     4603 |         317 |            20.6 |              1.5 |                   18 |                     1 |                         6 |


 ## Top 5 most transmissible countries + Brazil
|    | country    |   day | date                |   cases |   case_day |   deaths |   death_day |   cases_million |   deaths_million |   avg7_cases_million |   avg7_deaths_million |   avg7_recoveries_million |
|---:|:-----------|------:|:--------------------|--------:|-----------:|---------:|------------:|----------------:|-----------------:|---------------------:|----------------------:|--------------------------:|
|  1 | San Marino |    61 | 2020-04-27 00:00:00 |     538 |          0 |       41 |           0 |             0   |              0   |                  320 |                     8 |                        12 |
|  2 | Qatar      |    59 | 2020-04-27 00:00:00 |   11244 |        957 |       10 |           0 |           337.9 |              0   |                  263 |                     0 |                        25 |
|  3 | Singapore  |    96 | 2020-04-27 00:00:00 |   14423 |        799 |       14 |           2 |           137.7 |              0.3 |                  157 |                     0 |                         7 |
|  4 | Ireland    |    59 | 2020-04-27 00:00:00 |   19648 |        386 |     1102 |          15 |            79.1 |              3.1 |                  116 |                    12 |                       267 |
|  5 | Ecuador    |    58 | 2020-04-27 00:00:00 |   23240 |        521 |      663 |          87 |            30   |              5   |                  107 |                     1 |                         3 |
| 34 | Brazil     |    62 | 2020-04-27 00:00:00 |   67446 |       4346 |     4603 |         317 |            20.6 |              1.5 |                   18 |                     1 |                         6 |
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