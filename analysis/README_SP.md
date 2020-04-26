[<img src="../data/bandeiras/UK.png" width="30"  /> English version](README_SP_EN.md)

# **Análises e monitoramento**

### Letalidade dos estados brasileiros
O nível de letalidade demonstrado no mapa é definido a partir da média móvel dos últimos 7 dias da letalidade de cada estado.
<img src="maps/saoPauloMapDeaths.png" width="100%"  />
### Transmissão das cidades do estado de São Paulo
O nível de transmissão no mapa é definido a partir da média móvel dos últimos 7 dias da quantidade de casos acumulados de cada cidade do estado.

<img src="maps/saoPauloMapCases.png" width="100%"  />

Estas análises são relativas aos dados da pandemia Covid19 no estado de São Paulo até a data de **2020-04-24**.

Como existem muitas cidades, colocar em um único gráfico todos seus dados tornaria a leitura e compreensão inviáveis, desta forma, foram selecionadas as 5 mais mortais:['osasco' 'sao bernardo do campo' 'guarulhos' 'santa gertrudes' 'lucelia'].


***Dica**: você mesmo pode alterar neste notebook quais cidades você prefere comparar.*

## Top 5 cidades mais letais do estado de São Paulo (+ Santa Gertrudes e Lucélia)
|     | city                     | date                |   day |   case_day |   cases |   death_day |   deaths |   avg7_cases |   avg7_deaths |   avg7_perc_death |   perc_death |
|----:|:-------------------------|:--------------------|------:|-----------:|--------:|------------:|---------:|-------------:|--------------:|------------------:|-------------:|
|   1 | santo antonio da alegria | 2020-04-24 00:00:00 |     8 |          0 |       1 |           0 |        1 |            0 |             0 |               100 |       100    |
|   2 | caiabu                   | 2020-04-24 00:00:00 |    14 |          0 |       1 |           0 |        1 |            0 |             0 |               100 |       100    |
|   3 | eldorado                 | 2020-04-24 00:00:00 |    16 |          0 |       1 |           0 |        1 |            0 |             0 |               100 |       100    |
|   4 | juquitiba                | 2020-04-24 00:00:00 |     8 |          0 |       1 |           0 |        1 |            0 |             0 |               100 |       100    |
|   5 | conchas                  | 2020-04-24 00:00:00 |    11 |          0 |       1 |           0 |        1 |            0 |             0 |               100 |       100    |
| 143 | santa gertrudes          | 2020-04-24 00:00:00 |     9 |          0 |       1 |           0 |        0 |            0 |             0 |                 0 |         0    |
| 235 | lucelia                  | 2020-04-24 00:00:00 |     2 |          1 |       3 |           0 |        2 |            0 |             0 |                 0 |        66.67 |


 ## Top 5 cidades mais transmissíveis do estado de São Paulo (+ Santa Gertrudes e Lucélia)
|     | city                  | date                |   day |   case_day |   cases |   death_day |   deaths |   avg7_cases |   avg7_deaths |   avg7_perc_death |   perc_death |
|----:|:----------------------|:--------------------|------:|-----------:|--------:|------------:|---------:|-------------:|--------------:|------------------:|-------------:|
|   1 | total geral           | 2020-04-24 00:00:00 |     9 |       8455 |   17826 |         817 |     1512 |         2045 |           189 |              7.01 |         8.48 |
|   2 | sao paulo             | 2020-04-24 00:00:00 |    28 |        575 |   11800 |          98 |     1010 |          436 |            52 |              7.58 |         8.56 |
|   3 | osasco                | 2020-04-24 00:00:00 |    27 |         16 |     389 |           4 |       42 |           23 |             3 |              9.51 |        10.8  |
|   4 | sao bernardo do campo | 2020-04-24 00:00:00 |    27 |         63 |     421 |           4 |       29 |           20 |             1 |              6.64 |         6.89 |
|   5 | guarulhos             | 2020-04-24 00:00:00 |    27 |         43 |     399 |           4 |       46 |           14 |             2 |              9.63 |        11.53 |
| 142 | santa gertrudes       | 2020-04-24 00:00:00 |     9 |          0 |       1 |           0 |        0 |            0 |             0 |              0    |         0    |
| 240 | lucelia               | 2020-04-24 00:00:00 |     2 |          1 |       3 |           0 |        2 |            0 |             0 |              0    |        66.67 |
----------------------
## Casos e mortes
![](saoPaulo_cities_cases_deaths.png)

 [Comparativos do estado de São Paulo com outros estados do Brasil podem ser encontratos aqui.](https://github.com/rafaelcastellar/coronavirus/blob/master/analysis/README.md#casos-e-mortes)