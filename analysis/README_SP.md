[<img src="../data/bandeiras/UK.png" width="30"  /> English version](README_SP_EN.md)

# **Análises e monitoramento**

### Mortalidade dos estados brasileiros
O nível de mortalidade demonstrado no mapa é definido a partir da média móvel dos últimos 7 dias da mortalidade de cada estado.
<img src="maps/saoPauloMapDeaths.png" width="100%"  />
### Transmissão das cidades do estado de São Paulo
O nível de transmissão no mapa é definido a partir da média móvel dos últimos 7 dias da quantidade de casos acumulados de cada cidade do estado.

<img src="maps/saoPauloMapCases.png" width="100%"  />

Estas análises são relativas aos dados da pandemia Covid19 no estado de São Paulo até a data de **2020-05-01**.

Como existem muitas cidades, colocar em um único gráfico todos seus dados tornaria a leitura e compreensão inviáveis, desta forma, foram selecionadas as 5 mais mortais:['osasco' 'guarulhos' 'sao bernardo do campo' 'santo andre'
 'santa gertrudes' 'lucelia' 'rio claro'].


***Dica**: você mesmo pode alterar neste notebook quais cidades você prefere comparar.*

## Top 5 cidades mais mortais do estado de São Paulo (+ Santa Gertrudes e Lucélia)
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


 ## Top 5 cidades mais transmissíveis do estado de São Paulo (+ Santa Gertrudes, Rio Claro e Lucélia)
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
## Casos e mortes
![](saoPaulo_cities_cases_deaths.png)

 [Comparativos do estado de São Paulo com outros estados do Brasil podem ser encontratos aqui.](https://github.com/rafaelcastellar/coronavirus/blob/master/analysis/README.md#casos-e-mortes)