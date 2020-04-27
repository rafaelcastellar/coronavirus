[<img src="../data/bandeiras/PT.png" width="30"   /> Versão em português](README_SP.md)

# **Analysis and monitoring**

### Lethality of the San Paulo's cities
The lethality level shown in this map is defined from the moving average of the last 7 days of each city lethality of the San Paulo state.
<img src="maps/saoPauloMapDeaths.png" width="80%"  />
### Transmission of the San Paulo's cities
The tranmission level shown in this map is defined from the moving average of the last 7 days of each city's cumulative cases.
<img src="maps/saoPauloMapCases.png" width="80%"  />

These analysis are related to state of San Paulo Convid19 pandemic data up to **2020-04-26**.

As there are too many cities to have their data plotted together, were selected the 5 deadliest:['osasco' 'guarulhos' 'sao bernardo do campo' 'santos' 'santa gertrudes'
 'lucelia'].


***Tip**: you can yourself select in this notebook which states you prefer to compare.*

## Top 5 deadliest cities of the state of San Paulo (+ Santa Gertrudes and Lucelia cities) of Brazil
|     | city                     | date                |   day |   case_day |   cases |   death_day |   deaths |   avg7_cases |   avg7_deaths |   avg7_perc_death |   perc_death |
|----:|:-------------------------|:--------------------|------:|-----------:|--------:|------------:|---------:|-------------:|--------------:|------------------:|-------------:|
|   1 | santo antonio da alegria | 2020-04-26 00:00:00 |    10 |          0 |       1 |           0 |        1 |            0 |             0 |               100 |       100    |
|   2 | juquitiba                | 2020-04-26 00:00:00 |    10 |          0 |       1 |           0 |        1 |            0 |             0 |               100 |       100    |
|   3 | eldorado                 | 2020-04-26 00:00:00 |    18 |          0 |       1 |           0 |        1 |            0 |             0 |               100 |       100    |
|   4 | conchas                  | 2020-04-26 00:00:00 |    13 |          0 |       1 |           0 |        1 |            0 |             0 |               100 |       100    |
|   5 | caiabu                   | 2020-04-26 00:00:00 |    16 |          0 |       1 |           0 |        1 |            0 |             0 |               100 |       100    |
| 174 | santa gertrudes          | 2020-04-26 00:00:00 |    11 |          0 |       1 |           0 |        0 |            0 |             0 |                 0 |         0    |
| 245 | lucelia                  | 2020-04-26 00:00:00 |     4 |          0 |       3 |           0 |        2 |            0 |             0 |                 0 |        66.67 |


 ## Top 5 most transmissible cities of state of San Paulo (+ Santa Gertrudes and Lucelia cities)
|     | city                  | date                |   day |   case_day |   cases |   death_day |   deaths |   avg7_cases |   avg7_deaths |   avg7_perc_death |   perc_death |
|----:|:----------------------|:--------------------|------:|-----------:|--------:|------------:|---------:|-------------:|--------------:|------------------:|-------------:|
|   1 | sao paulo             | 2020-04-26 00:00:00 |    29 |        415 |   13513 |          15 |     1114 |          549 |            59 |              7.88 |         8.24 |
|   2 | osasco                | 2020-04-26 00:00:00 |    29 |         71 |     541 |           7 |       55 |           38 |             4 |              9.69 |        10.17 |
|   3 | guarulhos             | 2020-04-26 00:00:00 |    29 |         40 |     495 |           0 |       51 |           26 |             3 |             10.09 |        10.3  |
|   4 | sao bernardo do campo | 2020-04-26 00:00:00 |    29 |         12 |     475 |           0 |       31 |           25 |             1 |              6.59 |         6.53 |
|   5 | santos                | 2020-04-26 00:00:00 |    27 |          7 |     426 |           0 |       25 |           19 |             0 |              5.81 |         5.87 |
| 110 | santa gertrudes       | 2020-04-26 00:00:00 |    11 |          0 |       1 |           0 |        0 |            0 |             0 |              0    |         0    |
| 250 | lucelia               | 2020-04-26 00:00:00 |     4 |          0 |       3 |           0 |        2 |            0 |             0 |              0    |        66.67 |
----------------------
## Cases and deaths
![](saoPaulo_cities_cases_deaths.png)

 [Comparison of San Paulo among other Brazilian states can be found here.](https://github.com/rafaelcastellar/coronavirus/blob/master/analysis/README_EN.md#cases-and-deaths)