[<img src="../data/bandeiras/UK.png" width="30"  /> English version](README_EN.md)

# **Análises e monitoramento**

### Mortalidade dos estados brasileiros
O nível de mortalidade demonstrado no mapa é definido a partir da média móvel dos últimos 7 dias da mortalidade de cada estado.
<img src="maps/brazilMapDeaths.png" width="80%"  />
### Transmissão dos estados brasileiros
O nível de transmissão no mapa é definido a partir da média móvel dos últimos 7 dias da quantidade de casos acumulados de cada estado.

<img src="maps/brazilMapCases.png" width="80%"  />

Estas análises são relativas aos dados da pandemia Covid19 no Brasil até a data de **2020-04-30**.

Como existem muitos estados, colocar em um único gráfico todos seus dados tornaria a leitura e compreensão inviáveis, desta forma, foram selecionados os 10 mais mortais:['PB' 'RJ' 'PE' 'SP' 'AM' 'PR' 'CE' 'PA' 'PI' 'MA'].


***Dica**: você mesmo pode alterar neste notebook quais estados você prefere comparar.*

## Top 10 estados mais mortais do Brasil
|    | state   | date                |   day |   case_day |   cases |   death_day |   deaths |   avg7_cases |   avg7_deaths |   avg7_perc_death |   perc_death |
|---:|:--------|:--------------------|------:|-----------:|--------:|------------:|---------:|-------------:|--------------:|------------------:|-------------:|
|  1 | PB      | 2020-04-30 00:00:00 |    43 |        115 |     814 |           4 |       62 |           67 |             3 |              9.29 |         7.62 |
|  2 | RJ      | 2020-04-30 00:00:00 |    57 |        584 |    9453 |          60 |      854 |          468 |            46 |              8.9  |         9.03 |
|  3 | PE      | 2020-04-30 00:00:00 |    50 |        682 |    6876 |          27 |      565 |          479 |            36 |              8.56 |         8.22 |
|  4 | SP      | 2020-04-30 00:00:00 |    65 |       2540 |   28698 |         128 |     2375 |         1708 |           147 |              8.4  |         8.28 |
|  5 | AM      | 2020-04-30 00:00:00 |    47 |        453 |    5254 |          45 |      425 |          338 |            27 |              8.01 |         8.09 |
|  6 | PR      | 2020-04-30 00:00:00 |    50 |         59 |    1407 |           1 |       83 |           46 |             3 |              6.05 |         5.9  |
|  7 | CE      | 2020-04-30 00:00:00 |    45 |        339 |    7606 |          41 |      482 |          429 |            30 |              5.9  |         6.34 |
|  8 | PA      | 2020-04-30 00:00:00 |    43 |        454 |    2876 |          71 |      208 |          229 |            22 |              5.71 |         7.23 |
|  9 | PI      | 2020-04-30 00:00:00 |    42 |         59 |     513 |           0 |       24 |           42 |             1 |              5.43 |         4.68 |
| 10 | MA      | 2020-04-30 00:00:00 |    41 |        386 |    3190 |          18 |      184 |          204 |            15 |              5.27 |         5.77 |


 ## Top 10 estados mais transmissíveis do Brasil
|    | state   | date                |   day |   case_day |   cases |   death_day |   deaths |   avg7_cases |   avg7_deaths |   avg7_perc_death |   perc_death |
|---:|:--------|:--------------------|------:|-----------:|--------:|------------:|---------:|-------------:|--------------:|------------------:|-------------:|
|  1 | SP      | 2020-04-30 00:00:00 |    65 |       2540 |   28698 |         128 |     2375 |         1708 |           147 |              8.4  |         8.28 |
|  2 | PE      | 2020-04-30 00:00:00 |    50 |        682 |    6876 |          27 |      565 |          479 |            36 |              8.56 |         8.22 |
|  3 | RJ      | 2020-04-30 00:00:00 |    57 |        584 |    9453 |          60 |      854 |          468 |            46 |              8.9  |         9.03 |
|  4 | CE      | 2020-04-30 00:00:00 |    45 |        339 |    7606 |          41 |      482 |          429 |            30 |              5.9  |         6.34 |
|  5 | AM      | 2020-04-30 00:00:00 |    47 |        453 |    5254 |          45 |      425 |          338 |            27 |              8.01 |         8.09 |
|  6 | PA      | 2020-04-30 00:00:00 |    43 |        454 |    2876 |          71 |      208 |          229 |            22 |              5.71 |         7.23 |
|  7 | MA      | 2020-04-30 00:00:00 |    41 |        386 |    3190 |          18 |      184 |          204 |            15 |              5.27 |         5.77 |
|  8 | ES      | 2020-04-30 00:00:00 |    56 |        358 |    2465 |           7 |       83 |          157 |             5 |              3.22 |         3.37 |
|  9 | BA      | 2020-04-30 00:00:00 |    56 |        205 |    2851 |           8 |      104 |          151 |             6 |              3.4  |         3.65 |
| 10 | SC      | 2020-04-30 00:00:00 |    49 |         90 |    2085 |           2 |       46 |          138 |             1 |              3.01 |         2.21 |
----------------------
## Casos e mortes
![](brazilian_states_cases_deaths.png)

 [Comparativos do Brasil com outro países do mundo podem ser encontratos aqui.](https://github.com/rafaelcastellar/coronavirus/blob/master/analysis/README_WORLD.md#an%C3%A1lises-do-brasil)