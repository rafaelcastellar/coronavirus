[<img src="../data/bandeiras/UK.png" width="30"  /> English version](README_SP_EN.md)

# **Análises e monitoramento**

### Letalidade dos estados brasileiros
O nível de letalidade demonstrado no mapa é definido a partir da média móvel dos últimos 7 dias da letalidade de cada estado.
<img src="maps/saoPauloMapDeaths.png" width="100%"  />
### Transmissão das cidades do estado de São Paulo
O nível de transmissão no mapa é definido a partir da média móvel dos últimos 7 dias da quantidade de casos acumulados de cada cidade do estado.

<img src="maps/saoPauloMapCases.png" width="100%"  />

Estas análises são relativas aos dados da pandemia Covid19 no estado de São Paulo até a data de **2020-04-26**.

Como existem muitas cidades, colocar em um único gráfico todos seus dados tornaria a leitura e compreensão inviáveis, desta forma, foram selecionadas as 5 mais mortais:['osasco' 'guarulhos' 'sao bernardo do campo' 'santos' 'santa gertrudes'
 'lucelia'].


***Dica**: você mesmo pode alterar neste notebook quais cidades você prefere comparar.*

## Top 5 cidades mais letais do estado de São Paulo (+ Santa Gertrudes e Lucélia)
|     | city                     | date                |   day |   case_day |   cases |   death_day |   deaths |   avg7_cases |   avg7_deaths |   avg7_perc_death |   perc_death |
|----:|:-------------------------|:--------------------|------:|-----------:|--------:|------------:|---------:|-------------:|--------------:|------------------:|-------------:|
|   1 | santo antonio da alegria | 2020-04-26 00:00:00 |    10 |          0 |       1 |           0 |        1 |            0 |             0 |               100 |       100    |
|   2 | juquitiba                | 2020-04-26 00:00:00 |    10 |          0 |       1 |           0 |        1 |            0 |             0 |               100 |       100    |
|   3 | eldorado                 | 2020-04-26 00:00:00 |    18 |          0 |       1 |           0 |        1 |            0 |             0 |               100 |       100    |
|   4 | conchas                  | 2020-04-26 00:00:00 |    13 |          0 |       1 |           0 |        1 |            0 |             0 |               100 |       100    |
|   5 | caiabu                   | 2020-04-26 00:00:00 |    16 |          0 |       1 |           0 |        1 |            0 |             0 |               100 |       100    |
| 174 | santa gertrudes          | 2020-04-26 00:00:00 |    11 |          0 |       1 |           0 |        0 |            0 |             0 |                 0 |         0    |
| 245 | lucelia                  | 2020-04-26 00:00:00 |     4 |          0 |       3 |           0 |        2 |            0 |             0 |                 0 |        66.67 |


 ## Top 5 cidades mais transmissíveis do estado de São Paulo (+ Santa Gertrudes e Lucélia)
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
## Casos e mortes
![](saoPaulo_cities_cases_deaths.png)

 [Comparativos do estado de São Paulo com outros estados do Brasil podem ser encontratos aqui.](https://github.com/rafaelcastellar/coronavirus/blob/master/analysis/README.md#casos-e-mortes)