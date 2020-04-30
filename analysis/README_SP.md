[<img src="../data/bandeiras/UK.png" width="30"  /> English version](README_SP_EN.md)

# **Análises e monitoramento**

### Letalidade dos estados brasileiros
O nível de letalidade demonstrado no mapa é definido a partir da média móvel dos últimos 7 dias da letalidade de cada estado.
<img src="maps/saoPauloMapDeaths.png" width="100%"  />
### Transmissão das cidades do estado de São Paulo
O nível de transmissão no mapa é definido a partir da média móvel dos últimos 7 dias da quantidade de casos acumulados de cada cidade do estado.

<img src="maps/saoPauloMapCases.png" width="100%"  />

Estas análises são relativas aos dados da pandemia Covid19 no estado de São Paulo até a data de **2020-04-29**.

Como existem muitas cidades, colocar em um único gráfico todos seus dados tornaria a leitura e compreensão inviáveis, desta forma, foram selecionadas as 5 mais mortais:['osasco' 'guarulhos' 'sao bernardo do campo' 'santos' 'santa gertrudes'
 'lucelia'].


***Dica**: você mesmo pode alterar neste notebook quais cidades você prefere comparar.*

## Top 5 cidades mais letais do estado de São Paulo (+ Santa Gertrudes e Lucélia)
|     | city                       | date                |   day |   case_day |   cases |   death_day |   deaths |   avg7_cases |   avg7_deaths |   avg7_perc_death |   perc_death |
|----:|:---------------------------|:--------------------|------:|-----------:|--------:|------------:|---------:|-------------:|--------------:|------------------:|-------------:|
|   1 | juquitiba                  | 2020-04-29 00:00:00 |    13 |          0 |       3 |           0 |        3 |            0 |             0 |            100    |          100 |
|   2 | pitangueiras               | 2020-04-29 00:00:00 |     7 |          0 |       1 |           0 |        1 |            0 |             0 |            100    |          100 |
|   3 | conchas                    | 2020-04-29 00:00:00 |    16 |          0 |       1 |           0 |        1 |            0 |             0 |            100    |          100 |
|   4 | santo antonio da alegria   | 2020-04-29 00:00:00 |    13 |          0 |       1 |           0 |        1 |            0 |             0 |            100    |          100 |
|   5 | santa rita do passa quatro | 2020-04-29 00:00:00 |     7 |          0 |       1 |           0 |        1 |            0 |             0 |            100    |          100 |
| 197 | santa gertrudes            | 2020-04-29 00:00:00 |    14 |          0 |       1 |           0 |        0 |            0 |             0 |              0    |            0 |
|  12 | lucelia                    | 2020-04-29 00:00:00 |     7 |          0 |       4 |           0 |        2 |            0 |             0 |             64.29 |           50 |


 ## Top 5 cidades mais transmissíveis do estado de São Paulo (+ Santa Gertrudes e Lucélia)
|     | city                  | date                |   day |   case_day |   cases |   death_day |   deaths |   avg7_cases |   avg7_deaths |   avg7_perc_death |   perc_death |
|----:|:----------------------|:--------------------|------:|-----------:|--------:|------------:|---------:|-------------:|--------------:|------------------:|-------------:|
|   1 | sao paulo             | 2020-04-29 00:00:00 |    32 |       1241 |   16638 |         118 |     1439 |          849 |            94 |              8.42 |         8.65 |
|   2 | osasco                | 2020-04-29 00:00:00 |    32 |         55 |     701 |           5 |       71 |           49 |             5 |             10.3  |        10.13 |
|   3 | guarulhos             | 2020-04-29 00:00:00 |    32 |        104 |     666 |          12 |       64 |           47 |             5 |             10.59 |         9.61 |
|   4 | sao bernardo do campo | 2020-04-29 00:00:00 |    32 |         50 |     616 |           4 |       40 |           39 |             2 |              6.69 |         6.49 |
|   5 | santos                | 2020-04-29 00:00:00 |    30 |         39 |     534 |           5 |       46 |           30 |             3 |              6.49 |         8.61 |
| 179 | santa gertrudes       | 2020-04-29 00:00:00 |    14 |          0 |       1 |           0 |        0 |            0 |             0 |              0    |         0    |
| 268 | lucelia               | 2020-04-29 00:00:00 |     7 |          0 |       4 |           0 |        2 |            0 |             0 |             64.29 |        50    |
----------------------
## Casos e mortes
![](saoPaulo_cities_cases_deaths.png)

 [Comparativos do estado de São Paulo com outros estados do Brasil podem ser encontratos aqui.](https://github.com/rafaelcastellar/coronavirus/blob/master/analysis/README.md#casos-e-mortes)