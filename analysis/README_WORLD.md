[<img src="../data/bandeiras/UK.png" width="30"  /> English version](README_WORLD_EN.md)

# **Análises e monitoramento**
Estas análises são relativas aos dados da pandemia Covid19 até a data de **2020-05-01**.

Como existem muitos países, colocar em um gráfico todos seus dados tornaria a leitura e compreensão inviáveis, selecionei os seguintes países mais o Brasil para serem comparados entre si:['Brazil', 'Italy', 'United Kingdom', 'Spain', 'US', 'France', 'Belgium'].

Alguns países não estão no *dataset* da ONU, então não conseguimos analisá-los por sua populações. Estes podem ser encontrados fim do notebook *[data_engineering.ipynb](../data_engineering.ipynb)*.

***Dica**: você pode alterar você mesmo neste notebook quais países você prefere comparar.*

## Top 5 países mais mortais + Brasil
|    | country        |   day | date                |   cases |   case_day |   deaths |   death_day |   cases_million |   deaths_million |   avg7_cases_million |   avg7_deaths_million |   avg7_recoveries_million |
|---:|:---------------|------:|:--------------------|--------:|-----------:|---------:|------------:|----------------:|-----------------:|---------------------:|----------------------:|--------------------------:|
|  1 | Belgium        |    88 | 2020-05-01 00:00:00 |   49032 |        513 |     7703 |         109 |            44.5 |              9.4 |                   58 |                    12 |                        21 |
|  2 | United Kingdom |    92 | 2020-05-01 00:00:00 |  178685 |       6204 |    27583 |         741 |            91.9 |             11   |                   72 |                    10 |                         0 |
|  3 | Ireland        |    63 | 2020-05-01 00:00:00 |   20833 |        221 |     1265 |          33 |            45.3 |              6.8 |                   77 |                     7 |                       121 |
|  4 | Sweden         |    92 | 2020-05-01 00:00:00 |   21520 |        428 |     2653 |          67 |            42.6 |              6.7 |                   56 |                     7 |                         0 |
|  5 | Spain          |    91 | 2020-05-01 00:00:00 |  213435 |          0 |    24543 |           0 |             0   |              0   |                   31 |                     6 |                        60 |
| 21 | Brazil         |    66 | 2020-05-01 00:00:00 |   92202 |       5015 |     6412 |         406 |            23.8 |              1.9 |                   25 |                     1 |                         7 |


 ## Top 5 países mais transmissíveis + Brasil
|    | country    |   day | date                |   cases |   case_day |   deaths |   death_day |   cases_million |   deaths_million |   avg7_cases_million |   avg7_deaths_million |   avg7_recoveries_million |
|---:|:-----------|------:|:--------------------|--------:|-----------:|---------:|------------:|----------------:|-----------------:|---------------------:|----------------------:|--------------------------:|
|  1 | San Marino |    65 | 2020-05-01 00:00:00 |     580 |         11 |       41 |           0 |           324.8 |              0   |                  282 |                     4 |                        75 |
|  2 | Qatar      |    63 | 2020-05-01 00:00:00 |   14096 |        687 |       12 |           2 |           242.6 |              0.7 |                  280 |                     0 |                        31 |
|  3 | Singapore  |   100 | 2020-05-01 00:00:00 |   17101 |        932 |       16 |           1 |           160.6 |              0.2 |                  123 |                     0 |                         7 |
|  4 | Maldives   |    55 | 2020-05-01 00:00:00 |     491 |         23 |        1 |           0 |            43.3 |              0   |                   97 |                     0 |                         0 |
|  5 | Belarus    |    64 | 2020-05-01 00:00:00 |   14917 |        890 |       93 |           4 |            94.2 |              0.4 |                   92 |                     0 |                        27 |
| 27 | Brazil     |    66 | 2020-05-01 00:00:00 |   92202 |       5015 |     6412 |         406 |            23.8 |              1.9 |                   25 |                     1 |                         7 |
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