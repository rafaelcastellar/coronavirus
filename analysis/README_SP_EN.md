[<img src="../data/bandeiras/PT.png" width="30"   /> Versão em português](README_SP.md)

# **Analysis and monitoring**

### Mortality of the San Paulo's cities
The mortality level shown in this map is defined from the moving average of the last 7 days of each city mortality of the San Paulo state.
<img src="maps/saoPauloMapDeaths.png" width="80%"  />
### Transmission of the San Paulo's cities
The tranmission level shown in this map is defined from the moving average of the last 7 days of each city's cumulative cases.
<img src="maps/saoPauloMapCases.png" width="80%"  />

These analysis are related to state of San Paulo Convid19 pandemic data up to **2020-04-29**.

As there are too many cities to have their data plotted together, were selected the 5 deadliest:['osasco' 'guarulhos' 'sao bernardo do campo' 'santos' 'santa gertrudes'
 'lucelia' 'rio claro'].


***Tip**: you can yourself select in this notebook which states you prefer to compare.*

## Top 5 deadliest cities of the state of San Paulo (+ Santa Gertrudes, Rio Claro and Lucelia cities) of Brazil
|     | city                       | date                |   day |   case_day |   cases |   death_day |   deaths |   avg7_cases |   avg7_deaths |   avg7_perc_death |   perc_death |
|----:|:---------------------------|:--------------------|------:|-----------:|--------:|------------:|---------:|-------------:|--------------:|------------------:|-------------:|
|   1 | juquitiba                  | 2020-04-29 00:00:00 |    13 |          0 |       3 |           0 |        3 |            0 |             0 |            100    |       100    |
|   2 | pitangueiras               | 2020-04-29 00:00:00 |     7 |          0 |       1 |           0 |        1 |            0 |             0 |            100    |       100    |
|   3 | conchas                    | 2020-04-29 00:00:00 |    16 |          0 |       1 |           0 |        1 |            0 |             0 |            100    |       100    |
|   4 | santo antonio da alegria   | 2020-04-29 00:00:00 |    13 |          0 |       1 |           0 |        1 |            0 |             0 |            100    |       100    |
|   5 | santa rita do passa quatro | 2020-04-29 00:00:00 |     7 |          0 |       1 |           0 |        1 |            0 |             0 |            100    |       100    |
|  12 | lucelia                    | 2020-04-29 00:00:00 |     7 |          0 |       4 |           0 |        2 |            0 |             0 |             64.29 |        50    |
|  25 | rio claro                  | 2020-04-29 00:00:00 |    31 |          1 |      17 |           0 |        7 |            0 |             0 |             40.07 |        41.18 |
| 197 | santa gertrudes            | 2020-04-29 00:00:00 |    14 |          0 |       1 |           0 |        0 |            0 |             0 |              0    |         0    |


 ## Top 5 most transmissible cities of state of San Paulo (+ Santa Gertrudes and Lucelia cities)
|     | city                  | date                |   day |   case_day |   cases |   death_day |   deaths |   avg7_cases |   avg7_deaths |   avg7_perc_death |   perc_death |
|----:|:----------------------|:--------------------|------:|-----------:|--------:|------------:|---------:|-------------:|--------------:|------------------:|-------------:|
|   1 | sao paulo             | 2020-04-29 00:00:00 |    32 |       1241 |   16638 |         118 |     1439 |          849 |            94 |              8.42 |         8.65 |
|   2 | osasco                | 2020-04-29 00:00:00 |    32 |         55 |     701 |           5 |       71 |           49 |             5 |             10.3  |        10.13 |
|   3 | guarulhos             | 2020-04-29 00:00:00 |    32 |        104 |     666 |          12 |       64 |           47 |             5 |             10.59 |         9.61 |
|   4 | sao bernardo do campo | 2020-04-29 00:00:00 |    32 |         50 |     616 |           4 |       40 |           39 |             2 |              6.69 |         6.49 |
|   5 | santos                | 2020-04-29 00:00:00 |    30 |         39 |     534 |           5 |       46 |           30 |             3 |              6.49 |         8.61 |
| 167 | rio claro             | 2020-04-29 00:00:00 |    31 |          1 |      17 |           0 |        7 |            0 |             0 |             40.07 |        41.18 |
| 179 | santa gertrudes       | 2020-04-29 00:00:00 |    14 |          0 |       1 |           0 |        0 |            0 |             0 |              0    |         0    |
| 268 | lucelia               | 2020-04-29 00:00:00 |     7 |          0 |       4 |           0 |        2 |            0 |             0 |             64.29 |        50    |
----------------------
## Cases and deaths
![](saoPaulo_cities_cases_deaths.png)

 [Comparison of San Paulo among other Brazilian states can be found here.](https://github.com/rafaelcastellar/coronavirus/blob/master/analysis/README_EN.md#cases-and-deaths)