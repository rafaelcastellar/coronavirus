# **Analysis and monitoring**
These analysis are related to the Covid19 pandemic data up to **2020-04-10**.

As there are many countries to have all of their data plotted together, I selected a few of them plus Brazil to be compared with:['Brazil', 'Italy', 'United Kingdom', 'Spain', 'US', 'China', 'France'].

Some countries are not in UN dataset, so we can not analyse them by population. They can be found at the end of the *[data_engineering.ipynb](../data_engineering.ipynb)*.

*Tip: you can set yourself at the analysis notebook which countries you prefer to compare*

## Top 5 deadliest countries + Brazil
|     | country    |   day | date                |   cases |   case_day |   deaths |   death_day |   cases_million |   deaths_million |   avg7_cases_million |   avg7_deaths_million |   avg7_recoveries_million |
|----:|:-----------|------:|:--------------------|--------:|-----------:|---------:|------------:|----------------:|-----------------:|---------------------:|----------------------:|--------------------------:|
|   1 | Belgium    |    66 | 2020-04-09 00:00:00 |   24983 |       1580 |     2523 |         283 |           136.9 |             24.5 |                  119 |                    18 |                        33 |
|   2 | Andorra    |    39 | 2020-04-09 00:00:00 |     583 |         19 |       25 |           2 |           246.3 |             25.9 |                  287 |                    18 |                        88 |
|   3 | San Marino |    43 | 2020-04-09 00:00:00 |     333 |         54 |       34 |           0 |          1594.6 |              0   |                  371 |                    16 |                       118 |
|   4 | Spain      |    69 | 2020-04-09 00:00:00 |  153222 |       5002 |    15447 |         655 |           107   |             14   |                  125 |                    15 |                        77 |
|   5 | France     |    77 | 2020-04-09 00:00:00 |  118781 |       4822 |    12228 |        1341 |            74   |             20.6 |                  129 |                    14 |                        23 |
| 138 | Brazil     |    44 | 2020-04-09 00:00:00 |   18092 |       1922 |      950 |         131 |             9.1 |              0.6 |                    6 |                     0 |                         0 |


 ## Top 5 most transmissible countries + Brazil
|    | country    |   day | date                |   cases |   case_day |   deaths |   death_day |   cases_million |   deaths_million |   avg7_cases_million |   avg7_deaths_million |   avg7_recoveries_million |
|---:|:-----------|------:|:--------------------|--------:|-----------:|---------:|------------:|----------------:|-----------------:|---------------------:|----------------------:|--------------------------:|
|  1 | San Marino |    43 | 2020-04-09 00:00:00 |     333 |         54 |       34 |           0 |          1594.6 |              0   |                  371 |                    16 |                       118 |
|  2 | Andorra    |    39 | 2020-04-09 00:00:00 |     583 |         19 |       25 |           2 |           246.3 |             25.9 |                  287 |                    18 |                        88 |
|  3 | Luxembourg |    41 | 2020-04-09 00:00:00 |    3115 |         81 |       52 |           6 |           131.6 |              9.7 |                  145 |                     5 |                        97 |
|  4 | Iceland    |    42 | 2020-04-09 00:00:00 |    1648 |         32 |        6 |           0 |            94.4 |              0   |                  138 |                     0 |                       170 |
|  5 | France     |    77 | 2020-04-09 00:00:00 |  118781 |       4822 |    12228 |        1341 |            74   |             20.6 |                  129 |                    14 |                        23 |
| 58 | Brazil     |    44 | 2020-04-09 00:00:00 |   18092 |       1922 |      950 |         131 |             9.1 |              0.6 |                    6 |                     0 |                         0 |
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