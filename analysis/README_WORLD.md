[<img src="https://raw.githubusercontent.com/NovelCOVID/API/master/assets/flags/gb.png" width="30"  /> English version](README_WORLD_EN.md)

# **Análises e monitoramento**
Estas análises são relativas aos dados da pandemia Covid19 até a data de **2020-04-17**.

Como existem muitos países, colocar em um gráfico todos seus dados tornaria a leitura e compreensão inviáveis, selecionei os seguintes países mais o Brasil para serem comparados entre si:['Brazil', 'Italy', 'United Kingdom', 'Spain', 'US', 'France', 'Belgium'].

Alguns países não estão no *dataset* da ONU, então não conseguimos analisá-los por sua populações. Estes podem ser encontrados fim do notebook *[data_engineering.ipynb](../data_engineering.ipynb)*.

***Dica**: você pode alterar você mesmo neste notebook quais países você prefere comparar.*

## Top 5 países mais letais + Brasil
|     | country    |   day | date                |   cases |   case_day |   deaths |   death_day |   cases_million |   deaths_million |   avg7_cases_million |   avg7_deaths_million |   avg7_recoveries_million |
|----:|:-----------|------:|:--------------------|--------:|-----------:|---------:|------------:|----------------:|-----------------:|---------------------:|----------------------:|--------------------------:|
|   1 | Belgium    |    74 | 2020-04-17 00:00:00 |   36138 |       1329 |     5163 |         306 |           115.2 |             26.5 |                  117 |                    26 |                        29 |
|   2 | San Marino |    51 | 2020-04-17 00:00:00 |     435 |          9 |       39 |           1 |           265.8 |             29.5 |                  383 |                    21 |                        29 |
|   3 | Andorra    |    47 | 2020-04-17 00:00:00 |     696 |         23 |       35 |           2 |           298.1 |             25.9 |                  175 |                    16 |                       222 |
|   4 | France     |    85 | 2020-04-17 00:00:00 |  149130 |       2039 |    18703 |         762 |            31.3 |             11.7 |                  125 |                    12 |                        21 |
|   5 | Spain      |    77 | 2020-04-17 00:00:00 |  190839 |       5891 |    20002 |         687 |           126   |             14.7 |                   99 |                    11 |                        58 |
| 140 | Brazil     |    52 | 2020-04-17 00:00:00 |   33682 |       3257 |     2141 |         217 |            15.4 |              1   |                    9 |                     0 |                         9 |


 ## Top 5 países mais transmissíveis + Brasil
|    | country    |   day | date                |   cases |   case_day |   deaths |   death_day |   cases_million |   deaths_million |   avg7_cases_million |   avg7_deaths_million |   avg7_recoveries_million |
|---:|:-----------|------:|:--------------------|--------:|-----------:|---------:|------------:|----------------:|-----------------:|---------------------:|----------------------:|--------------------------:|
|  1 | San Marino |    51 | 2020-04-17 00:00:00 |     435 |          9 |       39 |           1 |           265.8 |             29.5 |                  383 |                    21 |                        29 |
|  2 | Andorra    |    47 | 2020-04-17 00:00:00 |     696 |         23 |       35 |           2 |           298.1 |             25.9 |                  175 |                    16 |                       222 |
|  3 | Ireland    |    49 | 2020-04-17 00:00:00 |   13980 |        709 |      530 |          44 |           145.2 |              9   |                  172 |                     7 |                         1 |
|  4 | France     |    85 | 2020-04-17 00:00:00 |  149130 |       2039 |    18703 |         762 |            31.3 |             11.7 |                  125 |                    12 |                        21 |
|  5 | Belgium    |    74 | 2020-04-17 00:00:00 |   36138 |       1329 |     5163 |         306 |           115.2 |             26.5 |                  117 |                    26 |                        29 |
| 50 | Brazil     |    52 | 2020-04-17 00:00:00 |   33682 |       3257 |     2141 |         217 |            15.4 |              1   |                    9 |                     0 |                         9 |
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