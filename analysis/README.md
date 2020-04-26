[<img src="../data/bandeiras/UK.png" width="30"  /> English version](README_EN.md)

# **Análises e monitoramento**

### Letalidade dos estados brasileiros
O nível de letalidade demonstrado no mapa é definido a partir da média móvel dos últimos 7 dias da letalidade de cada estado.
<img src="maps/brazilMapDeaths.png" width="80%"  />
### Transmissão dos estados brasileiros
O nível de transmissão no mapa é definido a partir da média móvel dos últimos 7 dias da quantidade de casos acumulados de cada estado.

<img src="maps/brazilMapCases.png" width="80%"  />

Estas análises são relativas aos dados da pandemia Covid19 no Brasil até a data de **2020-04-25**.

Como existem muitos estados, colocar em um único gráfico todos seus dados tornaria a leitura e compreensão inviáveis, desta forma, foram selecionados os 10 mais mortais:['PB' 'RJ' 'PE' 'AM' 'AL' 'SP' 'PI' 'SE' 'CE' 'PR'].


***Dica**: você mesmo pode alterar neste notebook quais estados você prefere comparar.*

## Top 10 estados mais letais do Brasil
|    | state   | date                |   day |   case_day |   cases |   death_day |   deaths |   avg7_cases |   avg7_deaths |   avg7_perc_death |   perc_death |
|---:|:--------|:--------------------|------:|-----------:|--------:|------------:|---------:|-------------:|--------------:|------------------:|-------------:|
|  1 | PB      | 2020-04-25 00:00:00 |    38 |         61 |     447 |           2 |       46 |           34 |             2 |             12.02 |        10.29 |
|  2 | RJ      | 2020-04-25 00:00:00 |    52 |        546 |    6828 |          45 |      615 |          326 |            32 |              8.75 |         9.01 |
|  3 | PE      | 2020-04-25 00:00:00 |    45 |        508 |    4507 |          29 |      381 |          330 |            25 |              8.73 |         8.45 |
|  4 | AM      | 2020-04-25 00:00:00 |    42 |        441 |    3635 |          32 |      287 |          248 |            18 |              8.33 |         7.9  |
|  5 | AL      | 2020-04-25 00:00:00 |    49 |         88 |     501 |           2 |       29 |           52 |             3 |              8.05 |         5.79 |
|  6 | SP      | 2020-04-25 00:00:00 |    60 |       2178 |   20004 |         155 |     1667 |          872 |            96 |              7.61 |         8.33 |
|  7 | PI      | 2020-04-25 00:00:00 |    37 |         41 |     297 |           1 |       17 |           24 |             1 |              6.88 |         5.72 |
|  8 | SE      | 2020-04-25 00:00:00 |    42 |          9 |     153 |           1 |        9 |           11 |             0 |              5.88 |         5.88 |
|  9 | CE      | 2020-04-25 00:00:00 |    40 |        621 |    5421 |          26 |      310 |          341 |            19 |              5.8  |         5.72 |
| 10 | PR      | 2020-04-25 00:00:00 |    45 |         21 |    1140 |           5 |       69 |           27 |             3 |              5.37 |         6.05 |


 ## Top 10 estados mais transmissíveis do Brasil
|    | state   | date                |   day |   case_day |   cases |   death_day |   deaths |   avg7_cases |   avg7_deaths |   avg7_perc_death |   perc_death |
|---:|:--------|:--------------------|------:|-----------:|--------:|------------:|---------:|-------------:|--------------:|------------------:|-------------:|
|  1 | SP      | 2020-04-25 00:00:00 |    60 |       2178 |   20004 |         155 |     1667 |          872 |            96 |              7.61 |         8.33 |
|  2 | CE      | 2020-04-25 00:00:00 |    40 |        621 |    5421 |          26 |      310 |          341 |            19 |              5.8  |         5.72 |
|  3 | PE      | 2020-04-25 00:00:00 |    45 |        508 |    4507 |          29 |      381 |          330 |            25 |              8.73 |         8.45 |
|  4 | RJ      | 2020-04-25 00:00:00 |    52 |        546 |    6828 |          45 |      615 |          326 |            32 |              8.75 |         9.01 |
|  5 | AM      | 2020-04-25 00:00:00 |    42 |        441 |    3635 |          32 |      287 |          248 |            18 |              8.33 |         7.9  |
|  6 | MA      | 2020-04-25 00:00:00 |    36 |        154 |    2105 |          12 |      100 |          152 |             8 |              4.3  |         4.75 |
|  7 | PA      | 2020-04-25 00:00:00 |    38 |        133 |    1579 |          11 |       86 |          134 |             7 |              4.42 |         5.45 |
|  8 | BA      | 2020-04-25 00:00:00 |    51 |        119 |    2081 |           6 |       70 |          126 |             4 |              3.32 |         3.36 |
|  9 | ES      | 2020-04-25 00:00:00 |    51 |        214 |    1595 |           5 |       47 |           91 |             2 |              2.86 |         2.95 |
| 10 | MG      | 2020-04-25 00:00:00 |    49 |         62 |    1481 |           4 |       58 |           57 |             2 |              3.67 |         3.92 |
----------------------
## Casos e mortes
![](brazilian_states_cases_deaths.png)

 [Comparativos do Brasil com outro países do mundo podem ser encontratos aqui.](https://github.com/rafaelcastellar/coronavirus/blob/master/analysis/README_WORLD.md#an%C3%A1lises-do-brasil)