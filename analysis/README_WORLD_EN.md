[<img src="../data/bandeiras/PT.png" width="30"   /> Versão em português](README_WORLD.md)

# **Analysis and monitoring**
These analysis are related to the Covid19 pandemic data up to **2020-04-28**.

As there are many countries to have all of their data plotted together, I selected a few of them plus Brazil to be compared with:['Brazil', 'Italy', 'United Kingdom', 'Spain', 'US', 'France', 'Belgium'].

Some countries are not in UN dataset, so we can not analyse them by population. They can be found at the end of the *[data_engineering.ipynb](../data_engineering.ipynb)*.

*Tip: you can set yourself at the analysis notebook which countries you prefer to compare*

## Top 5 deadliest countries + Brazil
|    | country        |   day | date                |   cases |   case_day |   deaths |   death_day |   cases_million |   deaths_million |   avg7_cases_million |   avg7_deaths_million |   avg7_recoveries_million |
|---:|:---------------|------:|:--------------------|--------:|-----------:|---------:|------------:|----------------:|-----------------:|---------------------:|----------------------:|--------------------------:|
|  1 | Belgium        |    85 | 2020-04-28 00:00:00 |   47334 |        647 |     7331 |         124 |            56.1 |             10.7 |                   78 |                    16 |                        24 |
|  2 | Ireland        |    60 | 2020-04-28 00:00:00 |   19877 |        229 |     1159 |          57 |            46.9 |             11.7 |                  112 |                    12 |                         0 |
|  3 | United Kingdom |    89 | 2020-04-28 00:00:00 |  162350 |       4002 |    21745 |         588 |            59.3 |              8.7 |                   68 |                     9 |                         0 |
|  4 | Sweden         |    89 | 2020-04-28 00:00:00 |   19621 |        695 |     2355 |          81 |            69.2 |              8.1 |                   61 |                     8 |                         6 |
|  5 | Spain          |    88 | 2020-04-28 00:00:00 |  232128 |       2706 |    23822 |         301 |            57.9 |              6.4 |                   85 |                     7 |                       126 |
| 25 | Brazil         |    63 | 2020-04-28 00:00:00 |   73235 |       5789 |     5083 |         480 |            27.4 |              2.3 |                   20 |                     1 |                         6 |


 ## Top 5 most transmissible countries + Brazil
|    | country    |   day | date                |   cases |   case_day |   deaths |   death_day |   cases_million |   deaths_million |   avg7_cases_million |   avg7_deaths_million |   avg7_recoveries_million |
|---:|:-----------|------:|:--------------------|--------:|-----------:|---------:|------------:|----------------:|-----------------:|---------------------:|----------------------:|--------------------------:|
|  1 | San Marino |    62 | 2020-04-28 00:00:00 |     553 |         15 |       41 |           0 |           442.9 |              0   |                  324 |                     4 |                         8 |
|  2 | Qatar      |    60 | 2020-04-28 00:00:00 |   11921 |        677 |       10 |           0 |           239   |              0   |                  271 |                     0 |                        26 |
|  3 | Singapore  |    97 | 2020-04-28 00:00:00 |   14951 |        528 |       14 |           0 |            91   |              0   |                  143 |                     0 |                         7 |
|  4 | Ecuador    |    59 | 2020-04-28 00:00:00 |   24258 |       1018 |      871 |         208 |            58.6 |             12   |                  113 |                     2 |                         2 |
|  5 | Ireland    |    60 | 2020-04-28 00:00:00 |   19877 |        229 |     1159 |          57 |            46.9 |             11.7 |                  112 |                    12 |                         0 |
| 31 | Brazil     |    63 | 2020-04-28 00:00:00 |   73235 |       5789 |     5083 |         480 |            27.4 |              2.3 |                   20 |                     1 |                         6 |
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