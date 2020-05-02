[<img src="../data/bandeiras/PT.png" width="30"   /> Versão em português](README_SP.md)

# **Analysis and monitoring**

### Mortality of the San Paulo's cities
The mortality level shown in this map is defined from the moving average of the last 7 days of each city mortality of the San Paulo state.
<img src="maps/saoPauloMapDeaths.png" width="80%"  />
### Transmission of the San Paulo's cities
The tranmission level shown in this map is defined from the moving average of the last 7 days of each city's cumulative cases.
<img src="maps/saoPauloMapCases.png" width="80%"  />

These analysis are related to state of San Paulo Convid19 pandemic data up to **2020-05-01**.

As there are too many cities to have their data plotted together, were selected the 5 deadliest:['osasco' 'guarulhos' 'sao bernardo do campo' 'santo andre'
 'santa gertrudes' 'lucelia' 'rio claro'].


***Tip**: you can yourself select in this notebook which states you prefer to compare.*

## Top 5 deadliest cities of the state of San Paulo (+ Santa Gertrudes, Rio Claro and Lucelia cities) of Brazil
|     | city                       | date                |   day |   case_day |   cases |   death_day |   deaths |   avg7_cases |   avg7_deaths |   avg7_perc_death |   perc_death |
|----:|:---------------------------|:--------------------|------:|-----------:|--------:|------------:|---------:|-------------:|--------------:|------------------:|-------------:|
|   1 | rincao                     | 2020-05-01 00:00:00 |    18 |          0 |       1 |           0 |        1 |            0 |             0 |            100    |       100    |
|   2 | jarinu                     | 2020-05-01 00:00:00 |     8 |          0 |       1 |           0 |        1 |            0 |             0 |            100    |       100    |
|   3 | conchas                    | 2020-05-01 00:00:00 |    18 |          0 |       1 |           0 |        1 |            0 |             0 |            100    |       100    |
|   4 | santo antonio da alegria   | 2020-05-01 00:00:00 |    15 |          0 |       1 |           0 |        1 |            0 |             0 |            100    |       100    |
|   5 | santa rita do passa quatro | 2020-05-01 00:00:00 |     9 |          0 |       1 |           0 |        1 |            0 |             0 |            100    |       100    |
|  17 | lucelia                    | 2020-05-01 00:00:00 |     9 |          3 |       7 |           0 |        2 |            0 |             0 |             51.7  |        28.57 |
|  22 | rio claro                  | 2020-05-01 00:00:00 |    33 |          0 |      18 |           0 |        8 |            0 |             0 |             43.58 |        44.44 |
| 212 | santa gertrudes            | 2020-05-01 00:00:00 |    16 |          0 |       1 |           0 |        0 |            0 |             0 |              0    |         0    |


 ## Top 5 most transmissible cities of state of San Paulo (+ Santa Gertrudes and Lucelia cities)
|     | city                  | date                |   day |   case_day |   cases |   death_day |   deaths |   avg7_cases |   avg7_deaths |   avg7_perc_death |   perc_death |
|----:|:----------------------|:--------------------|------:|-----------:|--------:|------------:|---------:|-------------:|--------------:|------------------:|-------------:|
|   1 | sao paulo             | 2020-05-01 00:00:00 |    34 |        938 |   19087 |          85 |     1607 |         1041 |            85 |              8.44 |         8.42 |
|   2 | osasco                | 2020-05-01 00:00:00 |    34 |         66 |     828 |          11 |       85 |           62 |             6 |             10.15 |        10.27 |
|   3 | guarulhos             | 2020-05-01 00:00:00 |    34 |         67 |     804 |           5 |       75 |           57 |             4 |              9.95 |         9.33 |
|   4 | sao bernardo do campo | 2020-05-01 00:00:00 |    34 |         23 |     705 |           0 |       45 |           40 |             2 |              6.56 |         6.38 |
|   5 | santo andre           | 2020-05-01 00:00:00 |    34 |         46 |     565 |           5 |       34 |           38 |             2 |              5.59 |         6.02 |
| 176 | rio claro             | 2020-05-01 00:00:00 |    33 |          0 |      18 |           0 |        8 |            0 |             0 |             43.58 |        44.44 |
| 187 | santa gertrudes       | 2020-05-01 00:00:00 |    16 |          0 |       1 |           0 |        0 |            0 |             0 |              0    |         0    |
| 264 | lucelia               | 2020-05-01 00:00:00 |     9 |          3 |       7 |           0 |        2 |            0 |             0 |             51.7  |        28.57 |
----------------------
## Cases and deaths
![](saoPaulo_cities_cases_deaths.png)

 [Comparison of San Paulo among other Brazilian states can be found here.](https://github.com/rafaelcastellar/coronavirus/blob/master/analysis/README_EN.md#cases-and-deaths)