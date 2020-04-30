[<img src="../data/bandeiras/PT.png" width="30"   /> Versão em português](README.md)

# **Analysis and monitoring**

### Mortality of the brazilian states
The mortality level shown in this map is defined from the moving average of the last 7 days of each state mortality.
<img src="maps/brazilMapDeaths.png" width="80%"  />
### Transmission of the brazilian states
O level of transmission on the map is defined from the moving average of the last 7 days of the cumulative cases of each state.
<img src="maps/brazilMapCases.png" width="80%"  />

These analysis are related to Brazil Convid19 pandemic data up to **2020-04-29**.

As there are too many states to have their data plotted together, were selected the 10 deadliest:['PB' 'RJ' 'PE' 'SP' 'AM' 'PR' 'CE' 'PI' 'AL' 'PA'].


***Tip**: you can yourself select in this notebook which states you prefer to compare.*

## Top 10 deadliest states of Brazil
|    | state   | date                |   day |   case_day |   cases |   death_day |   deaths |   avg7_cases |   avg7_deaths |   avg7_perc_death |   perc_death |
|---:|:--------|:--------------------|------:|-----------:|--------:|------------:|---------:|-------------:|--------------:|------------------:|-------------:|
|  1 | PB      | 2020-04-29 00:00:00 |    42 |         66 |     699 |           5 |       58 |           56 |             2 |              9.85 |         8.3  |
|  2 | RJ      | 2020-04-29 00:00:00 |    56 |        365 |    8869 |          56 |      794 |          473 |            43 |              8.84 |         8.95 |
|  3 | PE      | 2020-04-29 00:00:00 |    49 |        470 |    6194 |          30 |      538 |          413 |            36 |              8.65 |         8.69 |
|  4 | SP      | 2020-04-29 00:00:00 |    64 |       2117 |   26158 |         198 |     2247 |         1463 |           159 |              8.37 |         8.59 |
|  5 | AM      | 2020-04-29 00:00:00 |    46 |        464 |    4801 |          29 |      380 |          331 |            24 |              8.01 |         7.92 |
|  6 | PR      | 2020-04-29 00:00:00 |    49 |         77 |    1348 |           5 |       82 |           40 |             3 |              6    |         6.08 |
|  7 | CE      | 2020-04-29 00:00:00 |    44 |        349 |    7267 |          38 |      441 |          479 |            29 |              5.82 |         6.07 |
|  8 | PI      | 2020-04-29 00:00:00 |    41 |         46 |     454 |           3 |       24 |           35 |             1 |              5.75 |         5.29 |
|  9 | AL      | 2020-04-29 00:00:00 |    53 |        180 |     957 |           5 |       41 |          102 |             3 |              5.59 |         4.28 |
| 10 | PA      | 2020-04-29 00:00:00 |    42 |        160 |    2422 |           8 |      137 |          175 |            13 |              5.27 |         5.66 |


 ## Top 10 most transmissible states of Brazil
|    | state   | date                |   day |   case_day |   cases |   death_day |   deaths |   avg7_cases |   avg7_deaths |   avg7_perc_death |   perc_death |
|---:|:--------|:--------------------|------:|-----------:|--------:|------------:|---------:|-------------:|--------------:|------------------:|-------------:|
|  1 | SP      | 2020-04-29 00:00:00 |    64 |       2117 |   26158 |         198 |     2247 |         1463 |           159 |              8.37 |         8.59 |
|  2 | CE      | 2020-04-29 00:00:00 |    44 |        349 |    7267 |          38 |      441 |          479 |            29 |              5.82 |         6.07 |
|  3 | RJ      | 2020-04-29 00:00:00 |    56 |        365 |    8869 |          56 |      794 |          473 |            43 |              8.84 |         8.95 |
|  4 | PE      | 2020-04-29 00:00:00 |    49 |        470 |    6194 |          30 |      538 |          413 |            36 |              8.65 |         8.69 |
|  5 | AM      | 2020-04-29 00:00:00 |    46 |        464 |    4801 |          29 |      380 |          331 |            24 |              8.01 |         7.92 |
|  6 | PA      | 2020-04-29 00:00:00 |    42 |        160 |    2422 |           8 |      137 |          175 |            13 |              5.27 |         5.66 |
|  7 | MA      | 2020-04-29 00:00:00 |    40 |        276 |    2804 |          21 |      166 |          171 |            14 |              5.07 |         5.92 |
|  8 | BA      | 2020-04-29 00:00:00 |    55 |        106 |    2646 |          10 |       96 |          143 |             6 |              3.35 |         3.63 |
|  9 | SC      | 2020-04-29 00:00:00 |    48 |        519 |    1995 |           0 |       44 |          129 |             1 |              3.2  |         2.21 |
| 10 | ES      | 2020-04-29 00:00:00 |    55 |        233 |    2107 |          12 |       76 |          113 |             6 |              3.18 |         3.61 |
----------------------
## Cases and deaths
![](brazilian_states_cases_deaths.png)

 [Comparison of Brazil among other contries around the world can be found here.](https://github.com/rafaelcastellar/coronavirus/blob/master/analysis/README_WORLD_EN.md#brazils-analysis)