# **Analysis and monitoring**
These analysis are related to the Covid19 pandemic data up to **2020-04-11**.

As there are many countries to have all of their data plotted together, I selected a few of them plus Brazil to be compared with:['Brazil', 'Italy', 'United Kingdom', 'Spain', 'US', 'China', 'France'].

Some countries are not in UN dataset, so we can not analyse them by population. They can be found at the end of the *[data_engineering.ipynb](../data_engineering.ipynb)*.

*Tip: you can set yourself at the analysis notebook which countries you prefer to compare*

## Top 5 deadliest countries + Brazil
|     | country    |   day | date                |   cases |   case_day |   deaths |   death_day |   cases_million |   deaths_million |   avg7_cases_million |   avg7_deaths_million |   avg7_recoveries_million |
|----:|:-----------|------:|:--------------------|--------:|-----------:|---------:|------------:|----------------:|-----------------:|---------------------:|----------------------:|--------------------------:|
|   1 | Belgium    |    67 | 2020-04-10 00:00:00 |   26667 |       1684 |     3019 |         496 |           145.9 |             43   |                  122 |                    23 |                        33 |
|   2 | Andorra    |    40 | 2020-04-10 00:00:00 |     601 |         18 |       26 |           1 |           233.3 |             13   |                  299 |                    18 |                       101 |
|   3 | San Marino |    44 | 2020-04-10 00:00:00 |     344 |         11 |       34 |           0 |           324.8 |              0   |                  417 |                    16 |                       122 |
|   4 | Spain      |    70 | 2020-04-10 00:00:00 |  158273 |       5051 |    16081 |         634 |           108.1 |             13.6 |                  119 |                    14 |                        76 |
|   5 | France     |    78 | 2020-04-10 00:00:00 |  125931 |       7150 |    13215 |         987 |           109.8 |             15.2 |                  133 |                    14 |                        24 |
| 139 | Brazil     |    45 | 2020-04-10 00:00:00 |   19638 |       1546 |     1057 |         107 |             7.3 |              0.5 |                    7 |                     0 |                         0 |


 ## Top 5 most transmissible countries + Brazil
|    | country    |   day | date                |   cases |   case_day |   deaths |   death_day |   cases_million |   deaths_million |   avg7_cases_million |   avg7_deaths_million |   avg7_recoveries_million |
|---:|:-----------|------:|:--------------------|--------:|-----------:|---------:|------------:|----------------:|-----------------:|---------------------:|----------------------:|--------------------------:|
|  1 | San Marino |    44 | 2020-04-10 00:00:00 |     344 |         11 |       34 |           0 |           324.8 |              0   |                  417 |                    16 |                       122 |
|  2 | Andorra    |    40 | 2020-04-10 00:00:00 |     601 |         18 |       26 |           1 |           233.3 |             13   |                  299 |                    18 |                       101 |
|  3 | Luxembourg |    42 | 2020-04-10 00:00:00 |    3223 |        108 |       54 |           2 |           175.4 |              3.2 |                  141 |                     5 |                         0 |
|  4 | France     |    78 | 2020-04-10 00:00:00 |  125931 |       7150 |    13215 |         987 |           109.8 |             15.2 |                  133 |                    14 |                        24 |
|  5 | Iceland    |    43 | 2020-04-10 00:00:00 |    1675 |         27 |        7 |           1 |            79.6 |              2.9 |                  131 |                     1 |                       186 |
| 55 | Brazil     |    45 | 2020-04-10 00:00:00 |   19638 |       1546 |     1057 |         107 |             7.3 |              0.5 |                    7 |                     0 |                         0 |
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