[<img src="../data/bandeiras/PT.png" width="30"   /> Versão em português](README.md)

# **Analysis and monitoring**

### Mortality of the brazilian states
The mortality level shown in this map is defined from the moving average of the last 7 days of each state mortality.
<img src="maps/brazilMapDeaths.png" width="80%"  />
### Transmission of the brazilian states
O level of transmission on the map is defined from the moving average of the last 7 days of the cumulative cases of each state.
<img src="maps/brazilMapCases.png" width="80%"  />

These analysis are related to Brazil Convid19 pandemic data up to **2020-05-01**.

As there are too many states to have their data plotted together, were selected the 10 deadliest:['RJ' 'PB' 'PE' 'SP' 'AM' 'PR' 'PA' 'CE' 'MA' 'PI'].


***Tip**: you can yourself select in this notebook which states you prefer to compare.*

## Top 10 deadliest states of Brazil
|    | state   | date                |   day |   case_day |   cases |   death_day |   deaths |   avg7_cases |   avg7_deaths |   avg7_perc_death |   perc_death |
|---:|:--------|:--------------------|------:|-----------:|--------:|------------:|---------:|-------------:|--------------:|------------------:|-------------:|
|  1 | RJ      | 2020-05-01 00:00:00 |    58 |        713 |   10166 |          67 |      921 |          554 |            50 |              8.9  |         9.06 |
|  2 | PB      | 2020-05-01 00:00:00 |    44 |        112 |     926 |           5 |       67 |           77 |             3 |              8.69 |         7.24 |
|  3 | PE      | 2020-05-01 00:00:00 |    51 |        458 |    7334 |          38 |      603 |          476 |            35 |              8.47 |         8.22 |
|  4 | SP      | 2020-05-01 00:00:00 |    66 |       1676 |   30374 |         136 |     2511 |         1792 |           142 |              8.37 |         8.27 |
|  5 | AM      | 2020-05-01 00:00:00 |    48 |        469 |    5723 |          51 |      476 |          361 |            31 |              8.06 |         8.32 |
|  6 | PR      | 2020-05-01 00:00:00 |    51 |         40 |    1447 |           6 |       89 |           46 |             3 |              6.11 |         6.15 |
|  7 | PA      | 2020-05-01 00:00:00 |    44 |        300 |    3176 |          27 |      235 |          247 |            22 |              6.02 |         7.4  |
|  8 | CE      | 2020-05-01 00:00:00 |    46 |        273 |    7879 |          23 |      505 |          439 |            31 |              5.97 |         6.41 |
|  9 | MA      | 2020-05-01 00:00:00 |    42 |        316 |    3506 |          20 |      204 |          222 |            16 |              5.46 |         5.82 |
| 10 | PI      | 2020-05-01 00:00:00 |    43 |         87 |     600 |           0 |       24 |           49 |             1 |              5.11 |         4    |


 ## Top 10 most transmissible states of Brazil
|    | state   | date                |   day |   case_day |   cases |   death_day |   deaths |   avg7_cases |   avg7_deaths |   avg7_perc_death |   perc_death |
|---:|:--------|:--------------------|------:|-----------:|--------:|------------:|---------:|-------------:|--------------:|------------------:|-------------:|
|  1 | SP      | 2020-05-01 00:00:00 |    66 |       1676 |   30374 |         136 |     2511 |         1792 |           142 |              8.37 |         8.27 |
|  2 | RJ      | 2020-05-01 00:00:00 |    58 |        713 |   10166 |          67 |      921 |          554 |            50 |              8.9  |         9.06 |
|  3 | PE      | 2020-05-01 00:00:00 |    51 |        458 |    7334 |          38 |      603 |          476 |            35 |              8.47 |         8.22 |
|  4 | CE      | 2020-05-01 00:00:00 |    46 |        273 |    7879 |          23 |      505 |          439 |            31 |              5.97 |         6.41 |
|  5 | AM      | 2020-05-01 00:00:00 |    48 |        469 |    5723 |          51 |      476 |          361 |            31 |              8.06 |         8.32 |
|  6 | PA      | 2020-05-01 00:00:00 |    44 |        300 |    3176 |          27 |      235 |          247 |            22 |              6.02 |         7.4  |
|  7 | MA      | 2020-05-01 00:00:00 |    42 |        316 |    3506 |          20 |      204 |          222 |            16 |              5.46 |         5.82 |
|  8 | ES      | 2020-05-01 00:00:00 |    57 |        197 |    2662 |          13 |       96 |          183 |             7 |              3.3  |         3.61 |
|  9 | SC      | 2020-05-01 00:00:00 |    50 |        309 |    2394 |           2 |       48 |          174 |             0 |              2.79 |         2.01 |
| 10 | BA      | 2020-05-01 00:00:00 |    57 |        234 |    3085 |          13 |      117 |          160 |             7 |              3.48 |         3.79 |
----------------------
## Cases and deaths
![](brazilian_states_cases_deaths.png)

 [Comparison of Brazil among other contries around the world can be found here.](https://github.com/rafaelcastellar/coronavirus/blob/master/analysis/README_WORLD_EN.md#brazils-analysis)