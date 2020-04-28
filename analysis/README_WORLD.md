[<img src="../data/bandeiras/UK.png" width="30"  /> English version](README_WORLD_EN.md)

# **Análises e monitoramento**
Estas análises são relativas aos dados da pandemia Covid19 até a data de **2020-04-27**.

Como existem muitos países, colocar em um gráfico todos seus dados tornaria a leitura e compreensão inviáveis, selecionei os seguintes países mais o Brasil para serem comparados entre si:['Brazil', 'Italy', 'United Kingdom', 'Spain', 'US', 'France', 'Belgium'].

Alguns países não estão no *dataset* da ONU, então não conseguimos analisá-los por sua populações. Estes podem ser encontrados fim do notebook *[data_engineering.ipynb](../data_engineering.ipynb)*.

***Dica**: você pode alterar você mesmo neste notebook quais países você prefere comparar.*

## Top 5 países mais letais + Brasil
|    | country        |   day | date                |   cases |   case_day |   deaths |   death_day |   cases_million |   deaths_million |   avg7_cases_million |   avg7_deaths_million |   avg7_recoveries_million |
|---:|:---------------|------:|:--------------------|--------:|-----------:|---------:|------------:|----------------:|-----------------:|---------------------:|----------------------:|--------------------------:|
|  1 | Belgium        |    84 | 2020-04-27 00:00:00 |   46687 |        553 |     7207 |         113 |            47.9 |              9.8 |                   82 |                    17 |                        24 |
|  2 | Ireland        |    59 | 2020-04-27 00:00:00 |   19648 |        386 |     1102 |          15 |            79.1 |              3.1 |                  116 |                    12 |                       267 |
|  3 | Sweden         |    88 | 2020-04-27 00:00:00 |   18926 |        286 |     2274 |          80 |            28.5 |              8   |                   59 |                     9 |                         6 |
|  4 | United Kingdom |    88 | 2020-04-27 00:00:00 |  158348 |       4311 |    21157 |         363 |            63.8 |              5.4 |                   68 |                     9 |                         0 |
|  5 | San Marino     |    61 | 2020-04-27 00:00:00 |     538 |          0 |       41 |           0 |             0   |              0   |                  320 |                     8 |                        12 |
| 23 | Brazil         |    62 | 2020-04-27 00:00:00 |   67446 |       4346 |     4603 |         317 |            20.6 |              1.5 |                   18 |                     1 |                         6 |


 ## Top 5 países mais transmissíveis + Brasil
|    | country    |   day | date                |   cases |   case_day |   deaths |   death_day |   cases_million |   deaths_million |   avg7_cases_million |   avg7_deaths_million |   avg7_recoveries_million |
|---:|:-----------|------:|:--------------------|--------:|-----------:|---------:|------------:|----------------:|-----------------:|---------------------:|----------------------:|--------------------------:|
|  1 | San Marino |    61 | 2020-04-27 00:00:00 |     538 |          0 |       41 |           0 |             0   |              0   |                  320 |                     8 |                        12 |
|  2 | Qatar      |    59 | 2020-04-27 00:00:00 |   11244 |        957 |       10 |           0 |           337.9 |              0   |                  263 |                     0 |                        25 |
|  3 | Singapore  |    96 | 2020-04-27 00:00:00 |   14423 |        799 |       14 |           2 |           137.7 |              0.3 |                  157 |                     0 |                         7 |
|  4 | Ireland    |    59 | 2020-04-27 00:00:00 |   19648 |        386 |     1102 |          15 |            79.1 |              3.1 |                  116 |                    12 |                       267 |
|  5 | Ecuador    |    58 | 2020-04-27 00:00:00 |   23240 |        521 |      663 |          87 |            30   |              5   |                  107 |                     1 |                         3 |
| 34 | Brazil     |    62 | 2020-04-27 00:00:00 |   67446 |       4346 |     4603 |         317 |            20.6 |              1.5 |                   18 |                     1 |                         6 |
----------------------
## Análises mundiais
### Casos e mortes
![](world_cases_deaths.png)

 ### Casos, mortes e recuperações por milhão
Milhão de população noramilza os números de modo que a comparação entre países fica mais adequada. Como podemos ver, os primeiros gráficos nos mostram quão agressivo é a pandemia na Itália e Espanha.
![](world_cases_deaths_million.png)

 ### Casos ativos, uma visão mundial, % de recuperações e letalidade
![](world_active_cases_percentages.png)
----------------------
## Análises do Brasil


 ### Casos, mortes e recuperações
![](brazil_number_million_variation.png)

 ### Médias móveis dos últimos 7 dias
![](brazil_movingAvg.png)