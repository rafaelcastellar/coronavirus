[<img src="../data/bandeiras/PT.png" width="30"   /> Versão em português](README_WORLD.md)

# **Analysis and monitoring**
These analysis are related to the Covid19 pandemic data up to **2020-04-30**.

As there are many countries to have all of their data plotted together, I selected a few of them plus Brazil to be compared with:['Brazil', 'Italy', 'United Kingdom', 'Spain', 'US', 'France', 'Belgium'].

Some countries are not in UN dataset, so we can not analyse them by population. They can be found at the end of the *[data_engineering.ipynb](../data_engineering.ipynb)*.

*Tip: you can set yourself at the analysis notebook which countries you prefer to compare*

## Top 5 deadliest countries + Brazil
|    | country        |   day | date                |   cases |   case_day |   deaths |   death_day |   cases_million |   deaths_million |   avg7_cases_million |   avg7_deaths_million |   avg7_recoveries_million |
|---:|:---------------|------:|:--------------------|--------:|-----------:|---------:|------------:|----------------:|-----------------:|---------------------:|----------------------:|--------------------------:|
|  1 | Belgium        |    87 | 2020-04-30 00:00:00 |   48519 |        660 |     7594 |          93 |            57.2 |              8.1 |                   70 |                    13 |                        22 |
|  2 | Ireland        |    62 | 2020-04-30 00:00:00 |   20612 |        359 |     1232 |          42 |            73.5 |              8.6 |                   87 |                    12 |                       121 |
|  3 | United Kingdom |    91 | 2020-04-30 00:00:00 |  172481 |       6040 |    26842 |         676 |            89.4 |             10   |                   70 |                    10 |                         0 |
|  4 | Andorra        |    60 | 2020-04-30 00:00:00 |     745 |          2 |       42 |           0 |            25.9 |              0   |                   40 |                     9 |                       250 |
|  5 | Sweden         |    91 | 2020-04-30 00:00:00 |   21092 |        790 |     2586 |         124 |            78.7 |             12.4 |                   61 |                     8 |                         6 |
| 21 | Brazil         |    65 | 2020-04-30 00:00:00 |   87187 |       7502 |     6006 |         493 |            35.5 |              2.3 |                   25 |                     1 |                         6 |


 ## Top 5 most transmissible countries + Brazil
|    | country    |   day | date                |   cases |   case_day |   deaths |   death_day |   cases_million |   deaths_million |   avg7_cases_million |   avg7_deaths_million |   avg7_recoveries_million |
|---:|:-----------|------:|:--------------------|--------:|-----------:|---------:|------------:|----------------:|-----------------:|---------------------:|----------------------:|--------------------------:|
|  1 | San Marino |    64 | 2020-04-30 00:00:00 |     569 |          6 |       41 |           0 |           177.2 |              0   |                  286 |                     4 |                        63 |
|  2 | Qatar      |    62 | 2020-04-30 00:00:00 |   13409 |        845 |       10 |           0 |           298.4 |              0   |                  284 |                     0 |                        31 |
|  3 | Singapore  |    99 | 2020-04-30 00:00:00 |   16169 |        528 |       15 |           1 |            91   |              0.2 |                  122 |                     0 |                         7 |
|  4 | Ecuador    |    61 | 2020-04-30 00:00:00 |   24934 |        259 |      900 |          17 |            14.9 |              1   |                  113 |                     2 |                         1 |
|  5 | Maldives   |    54 | 2020-04-30 00:00:00 |     468 |        190 |        1 |           0 |           357.8 |              0   |                   96 |                     0 |                         0 |
| 28 | Brazil     |    65 | 2020-04-30 00:00:00 |   87187 |       7502 |     6006 |         493 |            35.5 |              2.3 |                   25 |                     1 |                         6 |
----------------------
## World' analysis
### Cases, deaths and recoveries
![](world_cases_deaths.png)

 ### Cases, deaths and recoveries per million
Million of population normalizes the features so they can me better comparable among the selected countries. As we can see, the first charts shows us how aggressive the pandemic is in Italy, Spain and somehow in France.
![](world_cases_deaths_million.png)

 ### Active cases, world overview, % recoveries and mortality
![](world_active_cases_percentages.png)
----------------------
## Brazil's analysis


 ### Cases, deaths and recoveries
![](brazil_number_million_variation.png)

 ### Moving averages (last 7 days)
![](brazil_movingAvg.png)