[<img src="../data/bandeiras/UK.png" width="30"  /> English version](README_SP_EN.md)

# **Análises e monitoramento**

### Letalidade dos estados brasileiros
O nível de letalidade demonstrado no mapa é definido a partir da média móvel dos últimos 7 dias da letalidade de cada estado.
<img src="maps/saoPauloMapDeaths.png" width="100%"  />
### Transmissão das cidades do estado de São Paulo
O nível de transmissão no mapa é definido a partir da média móvel dos últimos 7 dias da quantidade de casos acumulados de cada cidade do estado.

<img src="maps/saoPauloMapCases.png" width="100%"  />

Estas análises são relativas aos dados da pandemia Covid19 no estado de São Paulo até a data de **2020-04-28**.

Como existem muitas cidades, colocar em um único gráfico todos seus dados tornaria a leitura e compreensão inviáveis, desta forma, foram selecionadas as 5 mais mortais:['osasco' 'sao bernardo do campo' 'guarulhos' 'santos' 'santa gertrudes'
 'lucelia'].


***Dica**: você mesmo pode alterar neste notebook quais cidades você prefere comparar.*

## Top 5 cidades mais letais do estado de São Paulo (+ Santa Gertrudes e Lucélia)
|     | city                     | date                |   day |   case_day |   cases |   death_day |   deaths |   avg7_cases |   avg7_deaths |   avg7_perc_death |   perc_death |
|----:|:-------------------------|:--------------------|------:|-----------:|--------:|------------:|---------:|-------------:|--------------:|------------------:|-------------:|
|   1 | juquitiba                | 2020-04-28 00:00:00 |    12 |          0 |       3 |           0 |        3 |            0 |             0 |               100 |          100 |
|   2 | caiabu                   | 2020-04-28 00:00:00 |    18 |          0 |       1 |           0 |        1 |            0 |             0 |               100 |          100 |
|   3 | santo antonio da alegria | 2020-04-28 00:00:00 |    12 |          0 |       1 |           0 |        1 |            0 |             0 |               100 |          100 |
|   4 | conchas                  | 2020-04-28 00:00:00 |    15 |          0 |       1 |           0 |        1 |            0 |             0 |               100 |          100 |
|   5 | iepe                     | 2020-04-28 00:00:00 |    10 |          0 |       1 |           0 |        1 |            0 |             0 |               100 |          100 |
| 176 | santa gertrudes          | 2020-04-28 00:00:00 |    13 |          0 |       1 |           0 |        0 |            0 |             0 |                 0 |            0 |
| 262 | lucelia                  | 2020-04-28 00:00:00 |     6 |          0 |       4 |           0 |        2 |            0 |             0 |                 0 |           50 |


 ## Top 5 cidades mais transmissíveis do estado de São Paulo (+ Santa Gertrudes e Lucélia)
|     | city                  | date                |   day |   case_day |   cases |   death_day |   deaths |   avg7_cases |   avg7_deaths |   avg7_perc_death |   perc_death |
|----:|:----------------------|:--------------------|------:|-----------:|--------:|------------:|---------:|-------------:|--------------:|------------------:|-------------:|
|   1 | sao paulo             | 2020-04-28 00:00:00 |    31 |       1408 |   15397 |         149 |     1321 |          722 |            81 |              8.22 |         8.58 |
|   2 | osasco                | 2020-04-28 00:00:00 |    31 |         48 |     646 |           4 |       66 |           46 |             5 |             10.15 |        10.22 |
|   3 | sao bernardo do campo | 2020-04-28 00:00:00 |    31 |         55 |     566 |           1 |       36 |           36 |             2 |              6.6  |         6.36 |
|   4 | guarulhos             | 2020-04-28 00:00:00 |    31 |         64 |     562 |           0 |       52 |           33 |             3 |             10.43 |         9.25 |
|   5 | santos                | 2020-04-28 00:00:00 |    29 |         32 |     495 |          14 |       41 |           24 |             3 |              6.1  |         8.28 |
| 172 | santa gertrudes       | 2020-04-28 00:00:00 |    13 |          0 |       1 |           0 |        0 |            0 |             0 |              0    |         0    |
| 265 | lucelia               | 2020-04-28 00:00:00 |     6 |          0 |       4 |           0 |        2 |            0 |             0 |              0    |        50    |
----------------------
## Casos e mortes
![](saoPaulo_cities_cases_deaths.png)

 [Comparativos do estado de São Paulo com outros estados do Brasil podem ser encontratos aqui.](https://github.com/rafaelcastellar/coronavirus/blob/master/analysis/README.md#casos-e-mortes)