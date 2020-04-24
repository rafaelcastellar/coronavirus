[<img src="https://raw.githubusercontent.com/NovelCOVID/API/master/assets/flags/gb.png" width="30"  /> English version](README_WORLD_EN.md)

# **Análises e monitoramento**
Estas análises são relativas aos dados da pandemia Covid19 até a data de **2020-04-22**.

Como existem muitos países, colocar em um gráfico todos seus dados tornaria a leitura e compreensão inviáveis, selecionei os seguintes países mais o Brasil para serem comparados entre si:['Brazil', 'Italy', 'United Kingdom', 'Spain', 'US', 'France', 'Belgium'].

Alguns países não estão no *dataset* da ONU, então não conseguimos analisá-los por sua populações. Estes podem ser encontrados fim do notebook *[data_engineering.ipynb](../data_engineering.ipynb)*.

***Dica**: você pode alterar você mesmo neste notebook quais países você prefere comparar.*

## Top 5 países mais letais + Brasil
|     | country        |   day | date                |   cases |   case_day |   deaths |   death_day |   cases_million |   deaths_million |   avg7_cases_million |   avg7_deaths_million |   avg7_recoveries_million |
|----:|:---------------|------:|:--------------------|--------:|-----------:|---------:|------------:|----------------:|-----------------:|---------------------:|----------------------:|--------------------------:|
|   1 | Belgium        |    79 | 2020-04-22 00:00:00 |   41889 |        933 |     6262 |         264 |            80.9 |             22.9 |                  102 |                    22 |                        28 |
|   2 | San Marino     |    56 | 2020-04-22 00:00:00 |     488 |         12 |       40 |           0 |           354.4 |              0   |                  489 |                    16 |                        37 |
|   3 | United Kingdom |    83 | 2020-04-22 00:00:00 |  134638 |       4466 |    18151 |         773 |            66.1 |             11.4 |                   74 |                    11 |                         0 |
|   4 | Sweden         |    83 | 2020-04-22 00:00:00 |   16004 |        682 |     1937 |         172 |            68   |             17.1 |                   58 |                    10 |                         2 |
|   5 | Spain          |    82 | 2020-04-22 00:00:00 |  208389 |       4211 |    21717 |         435 |            90.1 |              9.3 |                   93 |                     9 |                        46 |
| 140 | Brazil         |    57 | 2020-04-22 00:00:00 |   45757 |       2678 |     2906 |         165 |            12.7 |              0.8 |                   11 |                     0 |                         7 |


 ## Top 5 países mais transmissíveis + Brasil
|    | country    |   day | date                |   cases |   case_day |   deaths |   death_day |   cases_million |   deaths_million |   avg7_cases_million |   avg7_deaths_million |   avg7_recoveries_million |
|---:|:-----------|------:|:--------------------|--------:|-----------:|---------:|------------:|----------------:|-----------------:|---------------------:|----------------------:|--------------------------:|
|  1 | San Marino |    56 | 2020-04-22 00:00:00 |     488 |         12 |       40 |           0 |           354.4 |              0   |                  489 |                    16 |                        37 |
|  2 | Qatar      |    54 | 2020-04-22 00:00:00 |    7141 |        608 |       10 |           1 |           214.7 |              0.4 |                  173 |                     0 |                        14 |
|  3 | Singapore  |    91 | 2020-04-22 00:00:00 |   10141 |       1016 |       12 |           1 |           175   |              0.2 |                  158 |                     0 |                         5 |
|  4 | Ireland    |    54 | 2020-04-22 00:00:00 |   16671 |        631 |      769 |          39 |           129.2 |              8   |                  120 |                     9 |                       267 |
|  5 | Belgium    |    79 | 2020-04-22 00:00:00 |   41889 |        933 |     6262 |         264 |            80.9 |             22.9 |                  102 |                    22 |                        28 |
| 44 | Brazil     |    57 | 2020-04-22 00:00:00 |   45757 |       2678 |     2906 |         165 |            12.7 |              0.8 |                   11 |                     0 |                         7 |
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