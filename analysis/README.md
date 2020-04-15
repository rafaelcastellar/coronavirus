# **Analysis and monitoring**
These analysis are related to the Covid19 pandemic data up to **2020-04-14**.

As there are many countries to have all of their data plotted together, I selected a few of them plus Brazil to be compared with:['Brazil', 'Italy', 'United Kingdom', 'Spain', 'US', 'France', 'Belgium'].

Some countries are not in UN dataset, so we can not analyse them by population. They can be found at the end of the *[data_engineering.ipynb](../data_engineering.ipynb)*.

*Tip: you can set yourself at the analysis notebook which countries you prefer to compare*

## Top 5 deadliest countries + Brazil
|     | country        |   day | date                |   cases |   case_day |   deaths |   death_day |   cases_million |   deaths_million |   avg7_cases_million |   avg7_deaths_million |   avg7_recoveries_million |
|----:|:---------------|------:|:--------------------|--------:|-----------:|---------:|------------:|----------------:|-----------------:|---------------------:|----------------------:|--------------------------:|
|   1 | Belgium        |    71 | 2020-04-14 00:00:00 |   31119 |        530 |     4157 |         254 |            45.9 |             22   |                  110 |                    26 |                        33 |
|   2 | Andorra        |    44 | 2020-04-14 00:00:00 |     659 |         13 |       31 |           2 |           168.5 |             25.9 |                  211 |                    16 |                       164 |
|   3 | United Kingdom |    75 | 2020-04-14 00:00:00 |   94845 |       5275 |    12129 |         782 |            78.1 |             11.6 |                   82 |                    12 |                         0 |
|   4 | Spain          |    74 | 2020-04-14 00:00:00 |  172541 |       2442 |    18056 |         300 |            52.3 |              6.4 |                   93 |                    12 |                        74 |
|   5 | France         |    82 | 2020-04-14 00:00:00 |  131361 |      -6514 |    15748 |         762 |          -100   |             11.7 |                   46 |                    11 |                        21 |
| 141 | Brazil         |    49 | 2020-04-14 00:00:00 |   25262 |       1832 |     1532 |         204 |             8.7 |              1   |                    7 |                     0 |                         1 |


 ## Top 5 most transmissible countries + Brazil
|    | country    |   day | date                |   cases |   case_day |   deaths |   death_day |   cases_million |   deaths_million |   avg7_cases_million |   avg7_deaths_million |   avg7_recoveries_million |
|---:|:-----------|------:|:--------------------|--------:|-----------:|---------:|------------:|----------------:|-----------------:|---------------------:|----------------------:|--------------------------:|
|  1 | San Marino |    48 | 2020-04-14 00:00:00 |     371 |         15 |       36 |           1 |           442.9 |             29.5 |                  388 |                     8 |                        54 |
|  2 | Andorra    |    44 | 2020-04-14 00:00:00 |     659 |         13 |       31 |           2 |           168.5 |             25.9 |                  211 |                    16 |                       164 |
|  3 | Ireland    |    46 | 2020-04-14 00:00:00 |   11479 |        832 |      406 |          41 |           170.4 |              8.4 |                  168 |                     5 |                         0 |
|  4 | Belgium    |    71 | 2020-04-14 00:00:00 |   31119 |        530 |     4157 |         254 |            45.9 |             22   |                  110 |                    26 |                        33 |
|  5 | Spain      |    74 | 2020-04-14 00:00:00 |  172541 |       2442 |    18056 |         300 |            52.3 |              6.4 |                   93 |                    12 |                        74 |
| 53 | Brazil     |    49 | 2020-04-14 00:00:00 |   25262 |       1832 |     1532 |         204 |             8.7 |              1   |                    7 |                     0 |                         1 |
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