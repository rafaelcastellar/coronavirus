[<img src="../data/bandeiras/UK.png" width="30"  /> English version](README_WORLD_EN.md)

# **Análises e monitoramento**
Estas análises são relativas aos dados da pandemia Covid19 até a data de **2020-04-26**.

Como existem muitos países, colocar em um gráfico todos seus dados tornaria a leitura e compreensão inviáveis, selecionei os seguintes países mais o Brasil para serem comparados entre si:['Brazil', 'Italy', 'United Kingdom', 'Spain', 'US', 'France', 'Belgium'].

Alguns países não estão no *dataset* da ONU, então não conseguimos analisá-los por sua populações. Estes podem ser encontrados fim do notebook *[data_engineering.ipynb](../data_engineering.ipynb)*.

***Dica**: você pode alterar você mesmo neste notebook quais países você prefere comparar.*

## Top 5 países mais letais + Brasil
|    | country        |   day | date                |   cases |   case_day |   deaths |   death_day |   cases_million |   deaths_million |   avg7_cases_million |   avg7_deaths_million |   avg7_recoveries_million |
|---:|:---------------|------:|:--------------------|--------:|-----------:|---------:|------------:|----------------:|-----------------:|---------------------:|----------------------:|--------------------------:|
|  1 | Belgium        |    83 | 2020-04-26 00:00:00 |   46134 |        809 |     7094 |         177 |            70.1 |             15.3 |                   94 |                    17 |                        25 |
|  2 | Ireland        |    58 | 2020-04-26 00:00:00 |   19262 |        701 |     1087 |          24 |           143.6 |              4.9 |                  117 |                    13 |                       267 |
|  3 | Sweden         |    87 | 2020-04-26 00:00:00 |   18640 |        463 |     2194 |           2 |            46.1 |              0.2 |                   60 |                     9 |                         6 |
|  4 | United Kingdom |    87 | 2020-04-26 00:00:00 |  154037 |       4468 |    20794 |         413 |            66.2 |              6.1 |                   69 |                     9 |                         0 |
|  5 | San Marino     |    60 | 2020-04-26 00:00:00 |     538 |         25 |       41 |           1 |           738.2 |             29.5 |                  324 |                     8 |                        16 |
| 26 | Brazil         |    61 | 2020-04-26 00:00:00 |   63100 |       3776 |     4286 |         229 |            17.9 |              1.1 |                   16 |                     1 |                         5 |


 ## Top 5 países mais transmissíveis + Brasil
|    | country    |   day | date                |   cases |   case_day |   deaths |   death_day |   cases_million |   deaths_million |   avg7_cases_million |   avg7_deaths_million |   avg7_recoveries_million |
|---:|:-----------|------:|:--------------------|--------:|-----------:|---------:|------------:|----------------:|-----------------:|---------------------:|----------------------:|--------------------------:|
|  1 | San Marino |    60 | 2020-04-26 00:00:00 |     538 |         25 |       41 |           1 |           738.2 |             29.5 |                  324 |                     8 |                        16 |
|  2 | Qatar      |    58 | 2020-04-26 00:00:00 |   10287 |        929 |       10 |           0 |           328   |              0   |                  244 |                     0 |                        24 |
|  3 | Singapore  |    95 | 2020-04-26 00:00:00 |   13624 |        931 |       12 |           0 |           160.4 |              0   |                  173 |                     0 |                         7 |
|  4 | Ireland    |    58 | 2020-04-26 00:00:00 |   19262 |        701 |     1087 |          24 |           143.6 |              4.9 |                  117 |                    13 |                       267 |
|  5 | Ecuador    |    57 | 2020-04-26 00:00:00 |   22719 |          0 |      576 |           0 |             0   |              0   |                  108 |                     0 |                         2 |
| 37 | Brazil     |    61 | 2020-04-26 00:00:00 |   63100 |       3776 |     4286 |         229 |            17.9 |              1.1 |                   16 |                     1 |                         5 |
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