[<img src="https://raw.githubusercontent.com/NovelCOVID/API/master/assets/flags/gb.png" width="30"  /> English version](README_WORLD_EN.md)

# **Análises e monitoramento**
Estas análises são relativas aos dados da pandemia Covid19 até a data de **2020-04-19**.

Como existem muitos países, colocar em um gráfico todos seus dados tornaria a leitura e compreensão inviáveis, selecionei os seguintes países mais o Brasil para serem comparados entre si:['Brazil', 'Italy', 'United Kingdom', 'Spain', 'US', 'France', 'Belgium'].

Alguns países não estão no *dataset* da ONU, então não conseguimos analisá-los por sua populações. Estes podem ser encontrados fim do notebook *[data_engineering.ipynb](../data_engineering.ipynb)*.

***Dica**: você pode alterar você mesmo neste notebook quais países você prefere comparar.*

## Top 5 países mais letais + Brasil
|     | country        |   day | date                |   cases |   case_day |   deaths |   death_day |   cases_million |   deaths_million |   avg7_cases_million |   avg7_deaths_million |   avg7_recoveries_million |
|----:|:---------------|------:|:--------------------|--------:|-----------:|---------:|------------:|----------------:|-----------------:|---------------------:|----------------------:|--------------------------:|
|   1 | Belgium        |    76 | 2020-04-19 00:00:00 |   38496 |       1313 |     5683 |         230 |           113.8 |             19.9 |                  109 |                    25 |                        28 |
|   2 | San Marino     |    53 | 2020-04-19 00:00:00 |     461 |          6 |       39 |           0 |           177.2 |              0   |                  442 |                    16 |                        29 |
|   3 | Andorra        |    49 | 2020-04-19 00:00:00 |     713 |          9 |       36 |           1 |           116.7 |             13   |                  138 |                    12 |                       198 |
|   4 | France         |    87 | 2020-04-19 00:00:00 |  154097 |       4948 |    19744 |         399 |            76   |              6.1 |                   71 |                    11 |                        21 |
|   5 | United Kingdom |    80 | 2020-04-19 00:00:00 |  121172 |       5858 |    16095 |         597 |            86.7 |              8.8 |                   76 |                    11 |                         0 |
| 141 | Brazil         |    54 | 2020-04-19 00:00:00 |   38654 |       1996 |     2462 |         108 |             9.5 |              0.5 |                   11 |                     0 |                        14 |


 ## Top 5 países mais transmissíveis + Brasil
|    | country    |   day | date                |   cases |   case_day |   deaths |   death_day |   cases_million |   deaths_million |   avg7_cases_million |   avg7_deaths_million |   avg7_recoveries_million |
|---:|:-----------|------:|:--------------------|--------:|-----------:|---------:|------------:|----------------:|-----------------:|---------------------:|----------------------:|--------------------------:|
|  1 | San Marino |    53 | 2020-04-19 00:00:00 |     461 |          6 |       39 |           0 |           177.2 |              0   |                  442 |                    16 |                        29 |
|  2 | Ireland    |    51 | 2020-04-19 00:00:00 |   15251 |        493 |      610 |          39 |           101   |              8   |                  163 |                     8 |                         1 |
|  3 | Andorra    |    49 | 2020-04-19 00:00:00 |     713 |          9 |       36 |           1 |           116.7 |             13   |                  138 |                    12 |                       198 |
|  4 | Qatar      |    51 | 2020-04-19 00:00:00 |    5448 |        440 |        8 |           0 |           155.4 |              0   |                  124 |                     0 |                        12 |
|  5 | Belgium    |    76 | 2020-04-19 00:00:00 |   38496 |       1313 |     5683 |         230 |           113.8 |             19.9 |                  109 |                    25 |                        28 |
| 45 | Brazil     |    54 | 2020-04-19 00:00:00 |   38654 |       1996 |     2462 |         108 |             9.5 |              0.5 |                   11 |                     0 |                        14 |
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