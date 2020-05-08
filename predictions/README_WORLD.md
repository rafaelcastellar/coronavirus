# **Predições**
Para experiência, estou fazendo predições simples sobre a quantidade de casos e mortes diárias. Como são séries temporais (*time-series*), estou usando [Facebook Prophet](https://facebook.github.io/prophet/docs/quick_start.html) que também é desenhado para este tipo de predição de uma maneira bem mais simples. Isso funciona muito bem na maioria das vezes; porém, algumas vezes há um grande salto entre os números que impactam no desempenho do modelo e leva um tempo (medições) para ser absorvido e compreendidos.

Essas predições foram feitas com os dados mundiais da pandemia Covid19 até **2020-05-07**.

Como há muitos paises para terem seus dados submetidos ao modelo de predição de uma só vez, selecionei alguns mais o Brasil:
['Brazil', 'Italy', 'United Kingdom', 'Spain', 'US', 'Belgium', 'France'].
***Dica**: você mesmo pode definir no notebook *[prediction.ipynb](../prediction.ipynb)* quais países você prefere fazer a predição.*


## A predição
As predições estão sendo realizadas sobre os dados diários de casos e de mortes. Em seguida, os dados previstos são acumulados para que tenhamos a projeção acumulada. Estão sendo previstos os próximos 10 dias.
Ao ffim, é gerado o arquivo CSV contendo todas as previsões.

#### Os últimos 5 dias da pandemia no Brasil e os próximos 10 dias previstos
*predicted? = True* significa que são dados de predição; *=False* significa que são dados reais.
|    | country   | ds                  |   case_day |   death_day |   cases |   deaths | predicted?   |
|---:|:----------|:--------------------|-----------:|------------:|--------:|---------:|:-------------|
| 67 | Brazil    | 2020-05-03 00:00:00 |       4726 |         290 |  101826 |     7051 | False        |
| 68 | Brazil    | 2020-05-04 00:00:00 |       6794 |         316 |  108620 |     7367 | False        |
| 69 | Brazil    | 2020-05-05 00:00:00 |       6835 |         571 |  115455 |     7938 | False        |
| 70 | Brazil    | 2020-05-06 00:00:00 |      11156 |         650 |  126611 |     8588 | False        |
| 71 | Brazil    | 2020-05-07 00:00:00 |       9162 |         602 |  135773 |     9190 | False        |
| 72 | Brazil    | 2020-05-08 00:00:00 |       7556 |         491 |  143329 |     9681 | True         |
| 73 | Brazil    | 2020-05-09 00:00:00 |       7763 |         490 |  151092 |    10171 | True         |
| 74 | Brazil    | 2020-05-10 00:00:00 |       7633 |         468 |  158725 |    10639 | True         |
| 75 | Brazil    | 2020-05-11 00:00:00 |       8027 |         491 |  166752 |    11130 | True         |
| 76 | Brazil    | 2020-05-12 00:00:00 |       8544 |         558 |  175296 |    11688 | True         |
| 77 | Brazil    | 2020-05-13 00:00:00 |       9330 |         570 |  184626 |    12258 | True         |
| 78 | Brazil    | 2020-05-14 00:00:00 |       9445 |         605 |  194071 |    12863 | True         |
| 79 | Brazil    | 2020-05-15 00:00:00 |       9226 |         583 |  203297 |    13446 | True         |
| 80 | Brazil    | 2020-05-16 00:00:00 |       9433 |         583 |  212730 |    14029 | True         |
| 81 | Brazil    | 2020-05-17 00:00:00 |       9303 |         560 |  222033 |    14589 | True         |

 #### As curvas acumuladas previstas para o Brasil
![](brazil_predictions.png)

 O Facebook Prophet gera automaticamente gráficos do comportamento sazonal dos dados, o que provê boas informações visuais. Aqui estão sobre as predições do Brasil:
### Casos
![](brazil_prophet_cases.png)

 ### Mortes
![](brazil_prophet_deaths.png)
#### Finalmente, as predições para os países selecionados para:
**Para amanhã**
|     | country        | ds                  |   case_day |   death_day |   cases |   deaths | predicted?   |
|----:|:---------------|:--------------------|-----------:|------------:|--------:|---------:|:-------------|
|  72 | Brazil         | 2020-05-08 00:00:00 |       7556 |         491 |  143329 |     9681 | True         |
|  98 | Italy          | 2020-05-08 00:00:00 |       2813 |         498 |  218671 |    30456 | True         |
|  98 | United Kingdom | 2020-05-08 00:00:00 |       6753 |         915 |  214730 |    31604 | True         |
|  97 | Spain          | 2020-05-08 00:00:00 |       4768 |         596 |  236088 |    26666 | True         |
| 107 | US             | 2020-05-08 00:00:00 |      35454 |        2227 | 1292477 |    77889 | True         |
|  94 | Belgium        | 2020-05-08 00:00:00 |       1351 |         249 |   52771 |     8664 | True         |
| 105 | France         | 2020-05-08 00:00:00 |       3557 |         651 |  179402 |    26641 | True         |

 **Para depois e amanhã** 
|     | country        | ds                  |   case_day |   death_day |   cases |   deaths | predicted?   |
|----:|:---------------|:--------------------|-----------:|------------:|--------:|---------:|:-------------|
|  73 | Brazil         | 2020-05-09 00:00:00 |       7763 |         490 |  151092 |    10171 | True         |
|  99 | Italy          | 2020-05-09 00:00:00 |       2716 |         486 |  221387 |    30942 | True         |
|  99 | United Kingdom | 2020-05-09 00:00:00 |       6290 |         891 |  221020 |    32495 | True         |
|  98 | Spain          | 2020-05-09 00:00:00 |       4837 |         591 |  240925 |    27257 | True         |
| 108 | US             | 2020-05-09 00:00:00 |      35014 |        2223 | 1327491 |    80112 | True         |
|  95 | Belgium        | 2020-05-09 00:00:00 |       1345 |         236 |   54116 |     8900 | True         |
| 106 | France         | 2020-05-09 00:00:00 |       3375 |         604 |  182777 |    27245 | True         |