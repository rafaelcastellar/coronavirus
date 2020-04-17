[<img src="https://raw.githubusercontent.com/NovelCOVID/API/master/assets/flags/br.png" width="40"  /> Versão em português](README_WORLD.md)

 #**Analysis and monitoring**
These analysis are related to the Covid19 pandemic data up to **2020-04-16**.

As there are many countries to have all of their data plotted together, I selected a few of them plus Brazil to be compared with:['Brazil', 'Italy', 'United Kingdom', 'Spain', 'US', 'France', 'Belgium'].

Some countries are not in UN dataset, so we can not analyse them by population. They can be found at the end of the *[data_engineering.ipynb](../data_engineering.ipynb)*.

*Tip: you can set yourself at the analysis notebook which countries you prefer to compare*

## Top 5 deadliest countries + Brazil
|     | country        |   day | date                |   cases |   case_day |   deaths |   death_day |   cases_million |   deaths_million |   avg7_cases_million |   avg7_deaths_million |   avg7_recoveries_million |
|----:|:---------------|------:|:--------------------|--------:|-----------:|---------:|------------:|----------------:|-----------------:|---------------------:|----------------------:|--------------------------:|
|   1 | Belgium        |    73 | 2020-04-16 00:00:00 |   34809 |       1236 |     4857 |         417 |           107.1 |             36.1 |                  121 |                    28 |                        29 |
|   2 | San Marino     |    50 | 2020-04-16 00:00:00 |     426 |         54 |       38 |           2 |          1594.6 |             59.1 |                  392 |                    16 |                        25 |
|   3 | Andorra        |    46 | 2020-04-16 00:00:00 |     673 |          0 |       33 |           0 |             0   |              0   |                  166 |                    14 |                       205 |
|   4 | France         |    84 | 2020-04-16 00:00:00 |  147091 |      12509 |    17941 |         753 |           192.1 |             11.6 |                  131 |                    12 |                        21 |
|   5 | United Kingdom |    77 | 2020-04-16 00:00:00 |  104145 |       4662 |    13759 |         865 |            69   |             12.8 |                   80 |                    12 |                         0 |
| 140 | Brazil         |    51 | 2020-04-16 00:00:00 |   30425 |       2105 |     1924 |         188 |            10   |              0.9 |                    8 |                     0 |                         9 |


 ## Top 5 most transmissible countries + Brazil
|    | country    |   day | date                |   cases |   case_day |   deaths |   death_day |   cases_million |   deaths_million |   avg7_cases_million |   avg7_deaths_million |   avg7_recoveries_million |
|---:|:-----------|------:|:--------------------|--------:|-----------:|---------:|------------:|----------------:|-----------------:|---------------------:|----------------------:|--------------------------:|
|  1 | San Marino |    50 | 2020-04-16 00:00:00 |     426 |         54 |       38 |           2 |          1594.6 |             59.1 |                  392 |                    16 |                        25 |
|  2 | Ireland    |    48 | 2020-04-16 00:00:00 |   13271 |        724 |      486 |          42 |           148.3 |              8.6 |                  195 |                     6 |                         1 |
|  3 | Andorra    |    46 | 2020-04-16 00:00:00 |     673 |          0 |       33 |           0 |             0   |              0   |                  166 |                    14 |                       205 |
|  4 | France     |    84 | 2020-04-16 00:00:00 |  147091 |      12509 |    17941 |         753 |           192.1 |             11.6 |                  131 |                    12 |                        21 |
|  5 | Belgium    |    73 | 2020-04-16 00:00:00 |   34809 |       1236 |     4857 |         417 |           107.1 |             36.1 |                  121 |                    28 |                        29 |
| 52 | Brazil     |    51 | 2020-04-16 00:00:00 |   30425 |       2105 |     1924 |         188 |            10   |              0.9 |                    8 |                     0 |                         9 |
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