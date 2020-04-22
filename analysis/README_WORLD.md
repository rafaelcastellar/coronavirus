[<img src="https://raw.githubusercontent.com/NovelCOVID/API/master/assets/flags/gb.png" width="30"  /> English version](README_WORLD_EN.md)

# **Análises e monitoramento**
Estas análises são relativas aos dados da pandemia Covid19 até a data de **2020-04-21**.

Como existem muitos países, colocar em um gráfico todos seus dados tornaria a leitura e compreensão inviáveis, selecionei os seguintes países mais o Brasil para serem comparados entre si:['Brazil', 'Italy', 'United Kingdom', 'Spain', 'US', 'France', 'Belgium'].

Alguns países não estão no *dataset* da ONU, então não conseguimos analisá-los por sua populações. Estes podem ser encontrados fim do notebook *[data_engineering.ipynb](../data_engineering.ipynb)*.

***Dica**: você pode alterar você mesmo neste notebook quais países você prefere comparar.*

## Top 5 países mais letais + Brasil
|     | country        |   day | date                |   cases |   case_day |   deaths |   death_day |   cases_million |   deaths_million |   avg7_cases_million |   avg7_deaths_million |   avg7_recoveries_million |
|----:|:---------------|------:|:--------------------|--------:|-----------:|---------:|------------:|----------------:|-----------------:|---------------------:|----------------------:|--------------------------:|
|   1 | Belgium        |    78 | 2020-04-21 00:00:00 |   40956 |        973 |     5998 |         170 |            84.3 |             14.7 |                  121 |                    22 |                        26 |
|   2 | San Marino     |    55 | 2020-04-21 00:00:00 |     476 |         14 |       40 |           1 |           413.4 |             29.5 |                  442 |                    16 |                        37 |
|   3 | Andorra        |    51 | 2020-04-21 00:00:00 |     717 |          0 |       37 |           0 |             0   |              0   |                  107 |                    11 |                       285 |
|   4 | France         |    89 | 2020-04-21 00:00:00 |  159297 |       2817 |    20829 |         537 |            43.3 |              8.2 |                   61 |                    11 |                        23 |
|   5 | United Kingdom |    82 | 2020-04-21 00:00:00 |  130172 |       4316 |    17378 |         828 |            63.9 |             12.3 |                   74 |                    11 |                         0 |
| 141 | Brazil         |    56 | 2020-04-21 00:00:00 |   43079 |       2336 |     2741 |         154 |            11.1 |              0.7 |                   12 |                     0 |                        13 |


 ## Top 5 países mais transmissíveis + Brasil
|    | country    |   day | date                |   cases |   case_day |   deaths |   death_day |   cases_million |   deaths_million |   avg7_cases_million |   avg7_deaths_million |   avg7_recoveries_million |
|---:|:-----------|------:|:--------------------|--------:|-----------:|---------:|------------:|----------------:|-----------------:|---------------------:|----------------------:|--------------------------:|
|  1 | San Marino |    55 | 2020-04-21 00:00:00 |     476 |         14 |       40 |           1 |           413.4 |             29.5 |                  442 |                    16 |                        37 |
|  2 | Qatar      |    53 | 2020-04-21 00:00:00 |    6533 |        518 |        9 |           0 |           182.9 |              0   |                  156 |                     0 |                        12 |
|  3 | Singapore  |    90 | 2020-04-21 00:00:00 |    9125 |       1111 |       11 |           0 |           191.4 |              0   |                  144 |                     0 |                         5 |
|  4 | Ireland    |    53 | 2020-04-21 00:00:00 |   16040 |        388 |      730 |          43 |            79.5 |              8.8 |                  133 |                     9 |                       269 |
|  5 | Belgium    |    78 | 2020-04-21 00:00:00 |   40956 |        973 |     5998 |         170 |            84.3 |             14.7 |                  121 |                    22 |                        26 |
| 45 | Brazil     |    56 | 2020-04-21 00:00:00 |   43079 |       2336 |     2741 |         154 |            11.1 |              0.7 |                   12 |                     0 |                        13 |
----------------------
## Análises mundiais
### Casos e mortes
![](world_cases_deaths.png)

 ### Casos e mortes por milhão
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