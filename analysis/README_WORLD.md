[<img src="https://raw.githubusercontent.com/NovelCOVID/API/master/assets/flags/gb.png" width="30"  /> English version](README_WORLD_EN.md)

# **Análises e monitoramento**
Estas análises são relativas aos dados da pandemia Covid19 até a data de **2020-04-20**.

Como existem muitos países, colocar em um gráfico todos seus dados tornaria a leitura e compreensão inviáveis, selecionei os seguintes países mais o Brasil para serem comparados entre si:['Brazil', 'Italy', 'United Kingdom', 'Spain', 'US', 'France', 'Belgium'].

Alguns países não estão no *dataset* da ONU, então não conseguimos analisá-los por sua populações. Estes podem ser encontrados fim do notebook *[data_engineering.ipynb](../data_engineering.ipynb)*.

***Dica**: você pode alterar você mesmo neste notebook quais países você prefere comparar.*

## Top 5 países mais letais + Brasil
|     | country        |   day | date                |   cases |   case_day |   deaths |   death_day |   cases_million |   deaths_million |   avg7_cases_million |   avg7_deaths_million |   avg7_recoveries_million |
|----:|:---------------|------:|:--------------------|--------:|-----------:|---------:|------------:|----------------:|-----------------:|---------------------:|----------------------:|--------------------------:|
|   1 | Belgium        |    77 | 2020-04-20 00:00:00 |   39983 |       1487 |     5828 |         145 |           128.9 |             12.6 |                  116 |                    23 |                        27 |
|   2 | San Marino     |    54 | 2020-04-20 00:00:00 |     462 |          1 |       39 |           0 |            29.5 |              0   |                  447 |                    16 |                        33 |
|   3 | Andorra        |    50 | 2020-04-20 00:00:00 |     717 |          4 |       37 |           1 |            51.8 |             13   |                  131 |                    14 |                       222 |
|   4 | France         |    88 | 2020-04-20 00:00:00 |  156480 |       2383 |    20292 |         548 |            36.6 |              8.4 |                   68 |                    11 |                        22 |
|   5 | United Kingdom |    81 | 2020-04-20 00:00:00 |  125856 |       4684 |    16550 |         455 |            69.4 |              6.7 |                   76 |                    10 |                         0 |
| 141 | Brazil         |    55 | 2020-04-20 00:00:00 |   40743 |       2089 |     2587 |         125 |             9.9 |              0.6 |                   11 |                     0 |                        14 |


 ## Top 5 países mais transmissíveis + Brasil
|    | country    |   day | date                |   cases |   case_day |   deaths |   death_day |   cases_million |   deaths_million |   avg7_cases_million |   avg7_deaths_million |   avg7_recoveries_million |
|---:|:-----------|------:|:--------------------|--------:|-----------:|---------:|------------:|----------------:|-----------------:|---------------------:|----------------------:|--------------------------:|
|  1 | San Marino |    54 | 2020-04-20 00:00:00 |     462 |          1 |       39 |           0 |            29.5 |              0   |                  447 |                    16 |                        33 |
|  2 | Ireland    |    52 | 2020-04-20 00:00:00 |   15652 |        401 |      687 |          77 |            82.1 |             15.8 |                  146 |                     9 |                         1 |
|  3 | Qatar      |    52 | 2020-04-20 00:00:00 |    6015 |        567 |        9 |           1 |           200.2 |              0.4 |                  140 |                     0 |                        11 |
|  4 | Andorra    |    50 | 2020-04-20 00:00:00 |     717 |          4 |       37 |           1 |            51.8 |             13   |                  131 |                    14 |                       222 |
|  5 | Singapore  |    89 | 2020-04-20 00:00:00 |    8014 |       1426 |       11 |           0 |           245.7 |              0   |                  125 |                     0 |                         5 |
| 47 | Brazil     |    55 | 2020-04-20 00:00:00 |   40743 |       2089 |     2587 |         125 |             9.9 |              0.6 |                   11 |                     0 |                        14 |
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