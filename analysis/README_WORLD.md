[<img src="data/bandeiras/UK.png" width="30"  /> English version](README_EN.md)

# **Análises e monitoramento**
Estas análises são relativas aos dados da pandemia Covid19 até a data de **2020-04-25**.

Como existem muitos países, colocar em um gráfico todos seus dados tornaria a leitura e compreensão inviáveis, selecionei os seguintes países mais o Brasil para serem comparados entre si:['Brazil', 'Italy', 'United Kingdom', 'Spain', 'US', 'France', 'Belgium'].

Alguns países não estão no *dataset* da ONU, então não conseguimos analisá-los por sua populações. Estes podem ser encontrados fim do notebook *[data_engineering.ipynb](../data_engineering.ipynb)*.

***Dica**: você pode alterar você mesmo neste notebook quais países você prefere comparar.*

## Top 5 países mais letais + Brasil
|    | country        |   day | date                |   cases |   case_day |   deaths |   death_day |   cases_million |   deaths_million |   avg7_cases_million |   avg7_deaths_million |   avg7_recoveries_million |
|---:|:---------------|------:|:--------------------|--------:|-----------:|---------:|------------:|----------------:|-----------------:|---------------------:|----------------------:|--------------------------:|
|  1 | Belgium        |    82 | 2020-04-25 00:00:00 |   45325 |       1032 |     6917 |         238 |            89.4 |             20.6 |                  100 |                    18 |                        25 |
|  2 | Ireland        |    57 | 2020-04-25 00:00:00 |   18561 |        377 |     1063 |          49 |            77.2 |             10   |                  111 |                    14 |                       267 |
|  3 | United Kingdom |    86 | 2020-04-25 00:00:00 |  149569 |       4929 |    20381 |         814 |            73   |             12.1 |                   72 |                    10 |                         0 |
|  4 | Sweden         |    86 | 2020-04-25 00:00:00 |   18177 |        610 |     2192 |          40 |            60.8 |              4   |                   62 |                     9 |                         6 |
|  5 | Andorra        |    55 | 2020-04-25 00:00:00 |     738 |          7 |       40 |           0 |            90.7 |              0   |                   62 |                     9 |                       257 |
| 26 | Brazil         |    60 | 2020-04-25 00:00:00 |   59324 |       5281 |     4057 |         353 |            25   |              1.7 |                   15 |                     1 |                        10 |


 ## Top 5 países mais transmissíveis + Brasil
|    | country    |   day | date                |   cases |   case_day |   deaths |   death_day |   cases_million |   deaths_million |   avg7_cases_million |   avg7_deaths_million |   avg7_recoveries_million |
|---:|:-----------|------:|:--------------------|--------:|-----------:|---------:|------------:|----------------:|-----------------:|---------------------:|----------------------:|--------------------------:|
|  1 | San Marino |    59 | 2020-04-25 00:00:00 |     513 |          0 |       40 |           0 |             0   |              0   |                  244 |                     4 |                        16 |
|  2 | Qatar      |    57 | 2020-04-25 00:00:00 |    9358 |        833 |       10 |           0 |           294.1 |              0   |                  219 |                     0 |                        21 |
|  3 | Singapore  |    94 | 2020-04-25 00:00:00 |   12693 |        618 |       12 |           0 |           106.5 |              0   |                  164 |                     0 |                         6 |
|  4 | Ecuador    |    56 | 2020-04-25 00:00:00 |   22719 |          0 |      576 |           0 |             0   |              0   |                  112 |                     0 |                         2 |
|  5 | Ireland    |    57 | 2020-04-25 00:00:00 |   18561 |        377 |     1063 |          49 |            77.2 |             10   |                  111 |                    14 |                       267 |
| 38 | Brazil     |    60 | 2020-04-25 00:00:00 |   59324 |       5281 |     4057 |         353 |            25   |              1.7 |                   15 |                     1 |                        10 |
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