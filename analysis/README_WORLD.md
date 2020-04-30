[<img src="../data/bandeiras/UK.png" width="30"  /> English version](README_WORLD_EN.md)

# **Análises e monitoramento**
Estas análises são relativas aos dados da pandemia Covid19 até a data de **2020-04-29**.

Como existem muitos países, colocar em um gráfico todos seus dados tornaria a leitura e compreensão inviáveis, selecionei os seguintes países mais o Brasil para serem comparados entre si:['Brazil', 'Italy', 'United Kingdom', 'Spain', 'US', 'France', 'Belgium'].

Alguns países não estão no *dataset* da ONU, então não conseguimos analisá-los por sua populações. Estes podem ser encontrados fim do notebook *[data_engineering.ipynb](../data_engineering.ipynb)*.

***Dica**: você pode alterar você mesmo neste notebook quais países você prefere comparar.*

## Top 5 países mais letais + Brasil
|    | country        |   day | date                |   cases |   case_day |   deaths |   death_day |   cases_million |   deaths_million |   avg7_cases_million |   avg7_deaths_million |   avg7_recoveries_million |
|---:|:---------------|------:|:--------------------|--------:|-----------:|---------:|------------:|----------------:|-----------------:|---------------------:|----------------------:|--------------------------:|
|  1 | United Kingdom |    90 | 2020-04-29 00:00:00 |  166441 |       4091 |    26166 |        4421 |            60.6 |             65.5 |                   67 |                    16 |                         0 |
|  2 | Belgium        |    86 | 2020-04-29 00:00:00 |   47859 |        525 |     7501 |         170 |            45.5 |             14.7 |                   73 |                    15 |                        22 |
|  3 | Ireland        |    61 | 2020-04-29 00:00:00 |   20253 |        376 |     1190 |          31 |            77   |              6.3 |                  104 |                    12 |                       121 |
|  4 | Andorra        |    59 | 2020-04-29 00:00:00 |     743 |          0 |       42 |           1 |             0   |             13   |                   37 |                     9 |                       211 |
|  5 | Spain          |    89 | 2020-04-29 00:00:00 |  236899 |       4771 |    24275 |         453 |           102.1 |              9.7 |                   87 |                     7 |                       143 |
| 26 | Brazil         |    64 | 2020-04-29 00:00:00 |   79685 |       6450 |     5513 |         430 |            30.6 |              2   |                   22 |                     1 |                         5 |


 ## Top 5 países mais transmissíveis + Brasil
|    | country    |   day | date                |   cases |   case_day |   deaths |   death_day |   cases_million |   deaths_million |   avg7_cases_million |   avg7_deaths_million |   avg7_recoveries_million |
|---:|:-----------|------:|:--------------------|--------:|-----------:|---------:|------------:|----------------:|-----------------:|---------------------:|----------------------:|--------------------------:|
|  1 | San Marino |    63 | 2020-04-29 00:00:00 |     563 |         10 |       41 |           0 |           295.3 |              0   |                  316 |                     4 |                        29 |
|  2 | Qatar      |    61 | 2020-04-29 00:00:00 |   12564 |        643 |       10 |           0 |           227   |              0   |                  273 |                     0 |                        27 |
|  3 | Singapore  |    98 | 2020-04-29 00:00:00 |   15641 |        690 |       14 |           0 |           118.9 |              0   |                  135 |                     0 |                         7 |
|  4 | Ecuador    |    60 | 2020-04-29 00:00:00 |   24675 |        417 |      883 |          12 |            24   |              0.7 |                  113 |                     2 |                         2 |
|  5 | Ireland    |    61 | 2020-04-29 00:00:00 |   20253 |        376 |     1190 |          31 |            77   |              6.3 |                  104 |                    12 |                       121 |
| 29 | Brazil     |    64 | 2020-04-29 00:00:00 |   79685 |       6450 |     5513 |         430 |            30.6 |              2   |                   22 |                     1 |                         5 |
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