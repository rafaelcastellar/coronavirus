# **Predições**
Para experiência, estou fazendo predições simples sobre a quantidade de casos e mortes diárias. Como são séries temporais (*time-series*), estou usando [Facebook Prophet](https://facebook.github.io/prophet/docs/quick_start.html) que também é desenhado para este tipo de predição de uma maneira bem mais simples. Isso funciona muito bem na maioria das vezes; porém, algumas vezes há um grande salto entre os números que impactam no desempenho do modelo e leva um tempo (medições) para ser absorvido e compreendidos.

Essas predições foram feitas com os dados mundiais da pandemia Covid19 até **2020-05-08**.

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
| 68 | Brazil    | 2020-05-04 00:00:00 |       6794 |         316 |  108620 |     7367 | False        |
| 69 | Brazil    | 2020-05-05 00:00:00 |       6835 |         571 |  115455 |     7938 | False        |
| 70 | Brazil    | 2020-05-06 00:00:00 |      11156 |         650 |  126611 |     8588 | False        |
| 71 | Brazil    | 2020-05-07 00:00:00 |       9162 |         602 |  135773 |     9190 | False        |
| 72 | Brazil    | 2020-05-08 00:00:00 |      11121 |         827 |  146894 |    10017 | False        |
| 73 | Brazil    | 2020-05-09 00:00:00 |       8228 |         530 |  155122 |    10547 | True         |
| 74 | Brazil    | 2020-05-10 00:00:00 |       8111 |         509 |  163233 |    11056 | True         |
| 75 | Brazil    | 2020-05-11 00:00:00 |       8518 |         533 |  171751 |    11589 | True         |
| 76 | Brazil    | 2020-05-12 00:00:00 |       9065 |         602 |  180816 |    12191 | True         |
| 77 | Brazil    | 2020-05-13 00:00:00 |       9894 |         616 |  190710 |    12807 | True         |
| 78 | Brazil    | 2020-05-14 00:00:00 |      10038 |         652 |  200748 |    13459 | True         |
| 79 | Brazil    | 2020-05-15 00:00:00 |      10164 |         663 |  210912 |    14122 | True         |
| 80 | Brazil    | 2020-05-16 00:00:00 |      10111 |         637 |  221023 |    14759 | True         |
| 81 | Brazil    | 2020-05-17 00:00:00 |       9994 |         616 |  231017 |    15375 | True         |
| 82 | Brazil    | 2020-05-18 00:00:00 |      10401 |         640 |  241418 |    16015 | True         |

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
|  73 | Brazil         | 2020-05-09 00:00:00 |       8228 |         530 |  155122 |    10547 | True         |
|  99 | Italy          | 2020-05-09 00:00:00 |       4451 |         661 |  221636 |    30862 | True         |
|  99 | United Kingdom | 2020-05-09 00:00:00 |       6156 |         883 |  218785 |    32199 | True         |
|  98 | Spain          | 2020-05-09 00:00:00 |       4745 |         580 |  237475 |    26879 | True         |
| 108 | US             | 2020-05-09 00:00:00 |      34738 |        2229 | 1318667 |    79409 | True         |
|  95 | Belgium        | 2020-05-09 00:00:00 |       1318 |         232 |   53329 |     8753 | True         |
| 106 | France         | 2020-05-09 00:00:00 |       3339 |         597 |  180571 |    26830 | True         |

 **Para depois e amanhã** 
|     | country        | ds                  |   case_day |   death_day |   cases |   deaths | predicted?   |
|----:|:---------------|:--------------------|-----------:|------------:|--------:|---------:|:-------------|
|  74 | Brazil         | 2020-05-10 00:00:00 |       8111 |         509 |  163233 |    11056 | True         |
| 100 | Italy          | 2020-05-10 00:00:00 |       4228 |         601 |  225864 |    31463 | True         |
| 100 | United Kingdom | 2020-05-10 00:00:00 |       6231 |         760 |  225016 |    32959 | True         |
|  99 | Spain          | 2020-05-10 00:00:00 |       4624 |         579 |  242099 |    27458 | True         |
| 109 | US             | 2020-05-10 00:00:00 |      33504 |        2070 | 1352171 |    81479 | True         |
|  96 | Belgium        | 2020-05-10 00:00:00 |       1299 |         219 |   54628 |     8972 | True         |
| 107 | France         | 2020-05-10 00:00:00 |       4764 |         526 |  185335 |    27356 | True         |