[<img src="../data/bandeiras/UK.png" width="30"  /> English version](README_WORLD_EN.md)

# **Análises e monitoramento**
Estas análises são relativas aos dados da pandemia Covid19 até a data de **2020-04-28**.

Como existem muitos países, colocar em um gráfico todos seus dados tornaria a leitura e compreensão inviáveis, selecionei os seguintes países mais o Brasil para serem comparados entre si:['Brazil', 'Italy', 'United Kingdom', 'Spain', 'US', 'France', 'Belgium'].

Alguns países não estão no *dataset* da ONU, então não conseguimos analisá-los por sua populações. Estes podem ser encontrados fim do notebook *[data_engineering.ipynb](../data_engineering.ipynb)*.

***Dica**: você pode alterar você mesmo neste notebook quais países você prefere comparar.*

## Top 5 países mais letais + Brasil
|    | country        |   day | date                |   cases |   case_day |   deaths |   death_day |   cases_million |   deaths_million |   avg7_cases_million |   avg7_deaths_million |   avg7_recoveries_million |
|---:|:---------------|------:|:--------------------|--------:|-----------:|---------:|------------:|----------------:|-----------------:|---------------------:|----------------------:|--------------------------:|
|  1 | Belgium        |    85 | 2020-04-28 00:00:00 |   47334 |        647 |     7331 |         124 |            56.1 |             10.7 |                   78 |                    16 |                        24 |
|  2 | Ireland        |    60 | 2020-04-28 00:00:00 |   19877 |        229 |     1159 |          57 |            46.9 |             11.7 |                  112 |                    12 |                         0 |
|  3 | United Kingdom |    89 | 2020-04-28 00:00:00 |  162350 |       4002 |    21745 |         588 |            59.3 |              8.7 |                   68 |                     9 |                         0 |
|  4 | Sweden         |    89 | 2020-04-28 00:00:00 |   19621 |        695 |     2355 |          81 |            69.2 |              8.1 |                   61 |                     8 |                         6 |
|  5 | Spain          |    88 | 2020-04-28 00:00:00 |  232128 |       2706 |    23822 |         301 |            57.9 |              6.4 |                   85 |                     7 |                       126 |
| 25 | Brazil         |    63 | 2020-04-28 00:00:00 |   73235 |       5789 |     5083 |         480 |            27.4 |              2.3 |                   20 |                     1 |                         6 |


 ## Top 5 países mais transmissíveis + Brasil
|    | country    |   day | date                |   cases |   case_day |   deaths |   death_day |   cases_million |   deaths_million |   avg7_cases_million |   avg7_deaths_million |   avg7_recoveries_million |
|---:|:-----------|------:|:--------------------|--------:|-----------:|---------:|------------:|----------------:|-----------------:|---------------------:|----------------------:|--------------------------:|
|  1 | San Marino |    62 | 2020-04-28 00:00:00 |     553 |         15 |       41 |           0 |           442.9 |              0   |                  324 |                     4 |                         8 |
|  2 | Qatar      |    60 | 2020-04-28 00:00:00 |   11921 |        677 |       10 |           0 |           239   |              0   |                  271 |                     0 |                        26 |
|  3 | Singapore  |    97 | 2020-04-28 00:00:00 |   14951 |        528 |       14 |           0 |            91   |              0   |                  143 |                     0 |                         7 |
|  4 | Ecuador    |    59 | 2020-04-28 00:00:00 |   24258 |       1018 |      871 |         208 |            58.6 |             12   |                  113 |                     2 |                         2 |
|  5 | Ireland    |    60 | 2020-04-28 00:00:00 |   19877 |        229 |     1159 |          57 |            46.9 |             11.7 |                  112 |                    12 |                         0 |
| 31 | Brazil     |    63 | 2020-04-28 00:00:00 |   73235 |       5789 |     5083 |         480 |            27.4 |              2.3 |                   20 |                     1 |                         6 |
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