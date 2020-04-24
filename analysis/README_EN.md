[<img src="https://raw.githubusercontent.com/NovelCOVID/API/master/assets/flags/br.png" width="30"  /> Versão em português](README_WORLD.md)

# **Analysis and monitoring**

### Lethality of the brazilian states
The lethality level shown in this map is defined from the moving average of the last 7 days of each state lethality.
<img src="brazilMap.png" width="100%"  />

These analysis are related to Brazil Convid19 pandemic data up to **2020-04-23**.

As there are too many states to have their data plotted together, were selected the 10 deadliest:['PB' 'PE' 'RJ' 'AM' 'AL' 'PI' 'SP' 'SE' 'CE' 'PR'].


***Tip**: you can yourself select in this notebook which states you prefer to compare.*

## Top 10 deadliest states of Brazil
|    | state   | date                |   day |   case_day |   cases |   death_day |   deaths |   avg7_cases |   avg7_deaths |   avg7_perc_death |   perc_death |
|---:|:--------|:--------------------|------:|-----------:|--------:|------------:|---------:|-------------:|--------------:|------------------:|-------------:|
|  1 | PB      | 2020-04-23 00:00:00 |    36 |         44 |     345 |           1 |       40 |           25 |             2 |             12.64 |        11.59 |
|  2 | PE      | 2020-04-23 00:00:00 |    43 |        221 |    3519 |          30 |      312 |          262 |            21 |              8.92 |         8.87 |
|  3 | RJ      | 2020-04-23 00:00:00 |    50 |        620 |    6172 |          40 |      530 |          318 |            32 |              8.5  |         8.59 |
|  4 | AM      | 2020-04-23 00:00:00 |    40 |        409 |    2888 |          27 |      234 |          167 |            15 |              8.42 |         8.1  |
|  5 | AL      | 2020-04-23 00:00:00 |    47 |         81 |     324 |           2 |       22 |           33 |             2 |              7.96 |         6.79 |
|  6 | PI      | 2020-04-23 00:00:00 |    35 |         11 |     217 |           0 |       15 |           18 |             1 |              7.34 |         6.91 |
|  7 | SP      | 2020-04-23 00:00:00 |    58 |        826 |   16740 |         211 |     1345 |          738 |            70 |              7.26 |         8.03 |
|  8 | SE      | 2020-04-23 00:00:00 |    40 |          7 |     124 |           1 |        8 |           10 |             0 |              6.33 |         6.45 |
|  9 | CE      | 2020-04-23 00:00:00 |    38 |        688 |    4598 |          33 |      266 |          316 |            20 |              5.76 |         5.79 |
| 10 | PR      | 2020-04-23 00:00:00 |    43 |         19 |    1082 |           3 |       60 |           35 |             2 |              5.07 |         5.55 |


 ## Top 10 most transmissible states of Brazil
|    | state   | date                |   day |   case_day |   cases |   death_day |   deaths |   avg7_cases |   avg7_deaths |   avg7_perc_death |   perc_death |
|---:|:--------|:--------------------|------:|-----------:|--------:|------------:|---------:|-------------:|--------------:|------------------:|-------------:|
|  1 | SP      | 2020-04-23 00:00:00 |    58 |        826 |   16740 |         211 |     1345 |          738 |            70 |              7.26 |         8.03 |
|  2 | RJ      | 2020-04-23 00:00:00 |    50 |        620 |    6172 |          40 |      530 |          318 |            32 |              8.5  |         8.59 |
|  3 | CE      | 2020-04-23 00:00:00 |    38 |        688 |    4598 |          33 |      266 |          316 |            20 |              5.76 |         5.79 |
|  4 | PE      | 2020-04-23 00:00:00 |    43 |        221 |    3519 |          30 |      312 |          262 |            21 |              8.92 |         8.87 |
|  5 | AM      | 2020-04-23 00:00:00 |    40 |        409 |    2888 |          27 |      234 |          167 |            15 |              8.42 |         8.1  |
|  6 | MA      | 2020-04-23 00:00:00 |    34 |        153 |    1757 |          10 |       76 |          151 |             5 |              4.29 |         4.33 |
|  7 | BA      | 2020-04-23 00:00:00 |    49 |        145 |    1789 |           9 |       59 |          119 |             4 |              3.3  |         3.3  |
|  8 | PA      | 2020-04-23 00:00:00 |    36 |         72 |    1267 |          10 |       53 |          118 |             4 |              4.31 |         4.18 |
|  9 | ES      | 2020-04-23 00:00:00 |    49 |         50 |    1363 |           8 |       42 |           87 |             2 |              2.84 |         3.08 |
| 10 | MG      | 2020-04-23 00:00:00 |    47 |         25 |    1308 |           4 |       51 |           50 |             2 |              3.57 |         3.9  |
----------------------
## Cases and deaths
![](brazilian_states_cases_deaths.png)

 [Comparison of Brazil and among some other contries around the world can be found here.](README_WORLD_EN.md#brazils-analysis)