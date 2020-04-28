[<img src="../data/bandeiras/UK.png" width="30"  /> English version](README_SP_EN.md)

# **Análises e monitoramento**

### Letalidade dos estados brasileiros
O nível de letalidade demonstrado no mapa é definido a partir da média móvel dos últimos 7 dias da letalidade de cada estado.
<img src="maps/saoPauloMapDeaths.png" width="100%"  />
### Transmissão das cidades do estado de São Paulo
O nível de transmissão no mapa é definido a partir da média móvel dos últimos 7 dias da quantidade de casos acumulados de cada cidade do estado.

<img src="maps/saoPauloMapCases.png" width="100%"  />

Estas análises são relativas aos dados da pandemia Covid19 no estado de São Paulo até a data de **2020-04-27**.

Como existem muitas cidades, colocar em um único gráfico todos seus dados tornaria a leitura e compreensão inviáveis, desta forma, foram selecionadas as 5 mais mortais:['osasco' 'sao bernardo do campo' 'guarulhos' 'santos' 'santa gertrudes'
 'lucelia'].


***Dica**: você mesmo pode alterar neste notebook quais cidades você prefere comparar.*

## Top 5 cidades mais letais do estado de São Paulo (+ Santa Gertrudes e Lucélia)
|     | city                     | date                |   day |   case_day |   cases |   death_day |   deaths |   avg7_cases |   avg7_deaths |   avg7_perc_death |   perc_death |
|----:|:-------------------------|:--------------------|------:|-----------:|--------:|------------:|---------:|-------------:|--------------:|------------------:|-------------:|
|   1 | juquitiba                | 2020-04-27 00:00:00 |    11 |          2 |       3 |           2 |        3 |            0 |             0 |               100 |          100 |
|   2 | caiabu                   | 2020-04-27 00:00:00 |    17 |          0 |       1 |           0 |        1 |            0 |             0 |               100 |          100 |
|   3 | santo antonio da alegria | 2020-04-27 00:00:00 |    11 |          0 |       1 |           0 |        1 |            0 |             0 |               100 |          100 |
|   4 | conchas                  | 2020-04-27 00:00:00 |    14 |          0 |       1 |           0 |        1 |            0 |             0 |               100 |          100 |
|   5 | iepe                     | 2020-04-27 00:00:00 |     9 |          0 |       1 |           0 |        1 |            0 |             0 |               100 |          100 |
| 160 | santa gertrudes          | 2020-04-27 00:00:00 |    12 |          0 |       1 |           0 |        0 |            0 |             0 |                 0 |            0 |
| 248 | lucelia                  | 2020-04-27 00:00:00 |     5 |          1 |       4 |           0 |        2 |            0 |             0 |                 0 |           50 |


 ## Top 5 cidades mais transmissíveis do estado de São Paulo (+ Santa Gertrudes e Lucélia)
|     | city                  | date                |   day |   case_day |   cases |   death_day |   deaths |   avg7_cases |   avg7_deaths |   avg7_perc_death |   perc_death |
|----:|:----------------------|:--------------------|------:|-----------:|--------:|------------:|---------:|-------------:|--------------:|------------------:|-------------:|
|   1 | sao paulo             | 2020-04-27 00:00:00 |    30 |        476 |   13989 |          58 |     1172 |          596 |            65 |              8.04 |         8.38 |
|   2 | osasco                | 2020-04-27 00:00:00 |    30 |         57 |     598 |           7 |       62 |           42 |             5 |              9.89 |        10.37 |
|   3 | sao bernardo do campo | 2020-04-27 00:00:00 |    30 |         36 |     511 |           4 |       35 |           30 |             2 |              6.61 |         6.85 |
|   4 | guarulhos             | 2020-04-27 00:00:00 |    30 |          3 |     498 |           1 |       52 |           26 |             3 |             10.32 |        10.44 |
|   5 | santos                | 2020-04-27 00:00:00 |    28 |         37 |     463 |           2 |       27 |           21 |             1 |              5.76 |         5.83 |
| 133 | santa gertrudes       | 2020-04-27 00:00:00 |    12 |          0 |       1 |           0 |        0 |            0 |             0 |              0    |         0    |
| 251 | lucelia               | 2020-04-27 00:00:00 |     5 |          1 |       4 |           0 |        2 |            0 |             0 |              0    |        50    |
----------------------
## Casos e mortes
![](saoPaulo_cities_cases_deaths.png)

 [Comparativos do estado de São Paulo com outros estados do Brasil podem ser encontratos aqui.](https://github.com/rafaelcastellar/coronavirus/blob/master/analysis/README.md#casos-e-mortes)