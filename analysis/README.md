[<img src="https://raw.githubusercontent.com/NovelCOVID/API/master/assets/flags/gb.png" width="30"  /> English version](README_EN.md)

# **Análises e monitoramento**

### Letalidade dos estados brasileiros
O nível de letalidade demonstrado no mapa é definido a partir da média móvel dos últimos 7 dias da letalidade de cada estado.
<img src="brazilMap.png" width="100%"  />

Estas análises são relativas aos dados da pandemia Covid19 no Brasil até a data de **2020-12-04**.

Como existem muitos estados, colocar em um único gráfico todos seus dados tornaria a leitura e compreensão inviáveis, desta forma, foram selecionados os 10 mais mortais:['PI' 'PB' 'SE' 'PE' 'SP' 'AL' 'RO' 'RJ' 'GO' 'AM'].


***Dica**: você pode alterar você mesmo neste notebook quais estados você prefere comparar.*

## Top 10 estados mais letais do Brasil
|    | state   | date                |   day |   case_day |   cases |   death_day |   deaths |   avg7_cases |   avg7_deaths |   avg7_perc_death |   perc_death |
|---:|:--------|:--------------------|------:|-----------:|--------:|------------:|---------:|-------------:|--------------:|------------------:|-------------:|
|  1 | PI      | 2020-12-04 00:00:00 |    24 |          3 |      44 |           0 |        7 |            3 |             0 |             16.3  |        15.91 |
|  2 | PB      | 2020-12-04 00:00:00 |    25 |         16 |     101 |           2 |       13 |            9 |             1 |             12.11 |        12.87 |
|  3 | SE      | 2020-12-04 00:00:00 |    29 |          2 |      44 |           0 |        4 |            1 |             0 |             10.44 |         9.09 |
|  4 | PE      | 2020-12-04 00:00:00 |    32 |        144 |     960 |          13 |       85 |          108 |             9 |             10.26 |         8.85 |
|  5 | SP      | 2020-12-04 00:00:00 |    47 |        336 |    8755 |          28 |      588 |          590 |            44 |              6.53 |         6.72 |
|  6 | AL      | 2020-12-04 00:00:00 |    36 |          0 |      48 |           0 |        3 |            2 |             0 |              6.48 |         6.25 |
|  7 | RO      | 2020-12-04 00:00:00 |    24 |          2 |      35 |           0 |        2 |            3 |             0 |              6.2  |         5.71 |
|  8 | RJ      | 2020-12-04 00:00:00 |    39 |        248 |    2855 |          15 |      170 |          208 |            15 |              5.57 |         5.95 |
|  9 | GO      | 2020-12-04 00:00:00 |    31 |         20 |     229 |           4 |       14 |           16 |             1 |              4.48 |         6.11 |
| 10 | AM      | 2020-12-04 00:00:00 |    29 |        156 |    1206 |           9 |       62 |          112 |             6 |              4.38 |         5.14 |


 ## Top 10 estados mais transmissíveis do Brasil
|    | state   | date                |   day |   case_day |   cases |   death_day |   deaths |   avg7_cases |   avg7_deaths |   avg7_perc_death |   perc_death |
|---:|:--------|:--------------------|------:|-----------:|--------:|------------:|---------:|-------------:|--------------:|------------------:|-------------:|
|  1 | SP      | 2020-12-04 00:00:00 |    47 |        336 |    8755 |          28 |      588 |          590 |            44 |              6.53 |         6.72 |
|  2 | RJ      | 2020-12-04 00:00:00 |    39 |        248 |    2855 |          15 |      170 |          208 |            15 |              5.57 |         5.95 |
|  3 | CE      | 2020-12-04 00:00:00 |    27 |         94 |    1676 |           7 |       74 |          121 |             6 |              3.65 |         4.42 |
|  4 | AM      | 2020-12-04 00:00:00 |    29 |        156 |    1206 |           9 |       62 |          112 |             6 |              4.38 |         5.14 |
|  5 | PE      | 2020-12-04 00:00:00 |    32 |        144 |     960 |          13 |       85 |          108 |             9 |             10.26 |         8.85 |
|  6 | SC      | 2020-12-04 00:00:00 |    31 |         36 |     768 |           3 |       24 |           58 |             2 |              2.93 |         3.12 |
|  7 | MG      | 2020-12-04 00:00:00 |    36 |         56 |     806 |           3 |       20 |           44 |             2 |              2.21 |         2.48 |
|  8 | MA      | 2020-12-04 00:00:00 |    23 |         54 |     398 |           3 |       24 |           43 |             3 |              4.37 |         6.03 |
|  9 | PR      | 2020-12-04 00:00:00 |    32 |         62 |     738 |           4 |       30 |           42 |             3 |              3.42 |         4.07 |
| 10 | BA      | 2020-12-04 00:00:00 |    38 |         38 |     673 |           0 |       21 |           38 |             1 |              2.99 |         3.12 |
----------------------
## Casos e mortes
![](brazilian_states_cases_deaths.png)

 [Comparativos do Brasil com outro países do mundo podem ser encontratos aqui.](README_WORLD.md#an%C3%A1lises-do-brasil)