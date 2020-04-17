[<img src="https://raw.githubusercontent.com/NovelCOVID/API/master/assets/flags/br.png" width="40"  /> Versão em português](README_WORLD.md)

# **Analysis and monitoring**

### Lethality of the brazilian states
The lethality level shown in this map is defined from the moving average of the last 7 days of each state lethality.
<iframe src="brazilMap.html" width=100% height=600></iframe>

These analysis are related to Brazil Convid19 pandemic data up to **2020-04-15**.

As there are too many states to have their data plotted together, were selected the 10 deadliest:['PI' 'PB' 'SE' 'PE' 'SP' 'AL' 'RJ' 'MA' 'AM' 'PA'].


***Tip**: you can yourself select in this notebook which states you prefer to compare.*

## Top 10 deadliest states of Brazil
|    | state   | date                |   day |   case_day |   cases |   death_day |   deaths |   avg7_cases |   avg7_deaths |   avg7_perc_death |   perc_death |
|---:|:--------|:--------------------|------:|-----------:|--------:|------------:|---------:|-------------:|--------------:|------------------:|-------------:|
|  1 | PI      | 2020-04-15 00:00:00 |    27 |         17 |      75 |           0 |        8 |            6 |             0 |             15.25 |        10.67 |
|  2 | PB      | 2020-04-15 00:00:00 |    28 |         15 |     151 |           5 |       21 |           15 |             2 |             12.83 |        13.91 |
|  3 | SE      | 2020-04-15 00:00:00 |    32 |          1 |      46 |           0 |        4 |            1 |             0 |              9.3  |         8.7  |
|  4 | PE      | 2020-04-15 00:00:00 |    35 |        200 |    1484 |          28 |      143 |          154 |            13 |              9.24 |         9.64 |
|  5 | SP      | 2020-04-15 00:00:00 |    50 |       1672 |   11043 |          83 |      778 |          619 |            50 |              6.84 |         7.05 |
|  6 | AL      | 2020-04-15 00:00:00 |    39 |         10 |      82 |           1 |        5 |            6 |             0 |              6.42 |         6.1  |
|  7 | RJ      | 2020-04-15 00:00:00 |    42 |        333 |    3743 |          41 |      265 |          257 |            22 |              6.12 |         7.08 |
|  8 | MA      | 2020-04-15 00:00:00 |    26 |        152 |     630 |           2 |       34 |           57 |             3 |              5.74 |         5.4  |
|  9 | AM      | 2020-04-15 00:00:00 |    32 |         70 |    1554 |          16 |      106 |          107 |            10 |              5.46 |         6.82 |
| 10 | PA      | 2020-04-15 00:00:00 |    28 |         61 |     384 |           2 |       21 |           31 |             2 |              5.18 |         5.47 |


 ## Top 10 most transmissible states of Brazil
|    | state   | date                |   day |   case_day |   cases |   death_day |   deaths |   avg7_cases |   avg7_deaths |   avg7_perc_death |   perc_death |
|---:|:--------|:--------------------|------:|-----------:|--------:|------------:|---------:|-------------:|--------------:|------------------:|-------------:|
|  1 | SP      | 2020-04-15 00:00:00 |    50 |       1672 |   11043 |          83 |      778 |          619 |            50 |              6.84 |         7.05 |
|  2 | RJ      | 2020-04-15 00:00:00 |    42 |        333 |    3743 |          41 |      265 |          257 |            22 |              6.12 |         7.08 |
|  3 | PE      | 2020-04-15 00:00:00 |    35 |        200 |    1484 |          28 |      143 |          154 |            13 |              9.24 |         9.64 |
|  4 | CE      | 2020-04-15 00:00:00 |    30 |        152 |    2157 |           9 |      116 |          123 |            10 |              4.6  |         5.38 |
|  5 | AM      | 2020-04-15 00:00:00 |    32 |         70 |    1554 |          16 |      106 |          107 |            10 |              5.46 |         6.82 |
|  6 | MA      | 2020-04-15 00:00:00 |    26 |        152 |     630 |           2 |       34 |           57 |             3 |              5.74 |         5.4  |
|  7 | SC      | 2020-04-15 00:00:00 |    34 |         27 |     853 |           2 |       28 |           56 |             1 |              3.07 |         3.28 |
|  8 | ES      | 2020-04-15 00:00:00 |    41 |         94 |     557 |           1 |       18 |           47 |             1 |              2.8  |         3.23 |
|  9 | BA      | 2020-04-15 00:00:00 |    41 |         48 |     807 |           5 |       27 |           44 |             1 |              3.18 |         3.35 |
| 10 | MG      | 2020-04-15 00:00:00 |    39 |         19 |     903 |           3 |       30 |           41 |             2 |              2.67 |         3.32 |
----------------------
## Cases and deaths
![](brazilian_states_cases_deaths.png)

 [Comparison of Brazil and among some other contries around the world can be found here.](README_WORLD_EN.md#brazils-analysis)