[<img src="../data/bandeiras/UK.png" width="30"  /> English version](README_WORLD_EN.md)

# **Análises e monitoramento**
Estas análises são relativas aos dados da pandemia Covid19 até a data de **2020-04-30**.

Como existem muitos países, colocar em um gráfico todos seus dados tornaria a leitura e compreensão inviáveis, selecionei os seguintes países mais o Brasil para serem comparados entre si:['Brazil', 'Italy', 'United Kingdom', 'Spain', 'US', 'France', 'Belgium'].

Alguns países não estão no *dataset* da ONU, então não conseguimos analisá-los por sua populações. Estes podem ser encontrados fim do notebook *[data_engineering.ipynb](../data_engineering.ipynb)*.

***Dica**: você pode alterar você mesmo neste notebook quais países você prefere comparar.*

## Top 5 países mais mortais + Brasil
|    | country        |   day | date                |   cases |   case_day |   deaths |   death_day |   cases_million |   deaths_million |   avg7_cases_million |   avg7_deaths_million |   avg7_recoveries_million |
|---:|:---------------|------:|:--------------------|--------:|-----------:|---------:|------------:|----------------:|-----------------:|---------------------:|----------------------:|--------------------------:|
|  1 | Belgium        |    87 | 2020-04-30 00:00:00 |   48519 |        660 |     7594 |          93 |            57.2 |              8.1 |                   70 |                    13 |                        22 |
|  2 | Ireland        |    62 | 2020-04-30 00:00:00 |   20612 |        359 |     1232 |          42 |            73.5 |              8.6 |                   87 |                    12 |                       121 |
|  3 | United Kingdom |    91 | 2020-04-30 00:00:00 |  172481 |       6040 |    26842 |         676 |            89.4 |             10   |                   70 |                    10 |                         0 |
|  4 | Andorra        |    60 | 2020-04-30 00:00:00 |     745 |          2 |       42 |           0 |            25.9 |              0   |                   40 |                     9 |                       250 |
|  5 | Sweden         |    91 | 2020-04-30 00:00:00 |   21092 |        790 |     2586 |         124 |            78.7 |             12.4 |                   61 |                     8 |                         6 |
| 21 | Brazil         |    65 | 2020-04-30 00:00:00 |   87187 |       7502 |     6006 |         493 |            35.5 |              2.3 |                   25 |                     1 |                         6 |


 ## Top 5 países mais transmissíveis + Brasil
|    | country    |   day | date                |   cases |   case_day |   deaths |   death_day |   cases_million |   deaths_million |   avg7_cases_million |   avg7_deaths_million |   avg7_recoveries_million |
|---:|:-----------|------:|:--------------------|--------:|-----------:|---------:|------------:|----------------:|-----------------:|---------------------:|----------------------:|--------------------------:|
|  1 | San Marino |    64 | 2020-04-30 00:00:00 |     569 |          6 |       41 |           0 |           177.2 |              0   |                  286 |                     4 |                        63 |
|  2 | Qatar      |    62 | 2020-04-30 00:00:00 |   13409 |        845 |       10 |           0 |           298.4 |              0   |                  284 |                     0 |                        31 |
|  3 | Singapore  |    99 | 2020-04-30 00:00:00 |   16169 |        528 |       15 |           1 |            91   |              0.2 |                  122 |                     0 |                         7 |
|  4 | Ecuador    |    61 | 2020-04-30 00:00:00 |   24934 |        259 |      900 |          17 |            14.9 |              1   |                  113 |                     2 |                         1 |
|  5 | Maldives   |    54 | 2020-04-30 00:00:00 |     468 |        190 |        1 |           0 |           357.8 |              0   |                   96 |                     0 |                         0 |
| 28 | Brazil     |    65 | 2020-04-30 00:00:00 |   87187 |       7502 |     6006 |         493 |            35.5 |              2.3 |                   25 |                     1 |                         6 |
----------------------
## Análises mundiais
### Casos e mortes
![](world_cases_deaths.png)

 ### Casos, mortes e recuperações por milhão
Milhão de população noramilza os números de modo que a comparação entre países fica mais adequada. Como podemos ver, os primeiros gráficos nos mostram quão agressivo é a pandemia na Itália e Espanha.
![](world_cases_deaths_million.png)

 ### Casos ativos, uma visão mundial, % de recuperações e mortalidade
![](world_active_cases_percentages.png)
----------------------
## Análises do Brasil


 ### Casos, mortes e recuperações
![](brazil_number_million_variation.png)

 ### Médias móveis dos últimos 7 dias
![](brazil_movingAvg.png)