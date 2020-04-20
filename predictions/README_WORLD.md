# **Predições**
Para experiência, estou fazendo predições simples sobre a quantidade de casos e mortes diárias. Como são séries temporais (*time-series*), estou usando [Facebook Prophet](https://facebook.github.io/prophet/docs/quick_start.html) que também é desenhado para este tipo de predição de uma maneira bem mais simples. Isso funciona muito bem na maioria das vezes; porém, algumas vezes há um grande salto entre os números que impactam no desempenho do modelo e leva um tempo (medições) para ser absorvido e compreendidos.

Essas predições foram feitas com os dados mundiais da pandemia Covid19 até **2020-04-19**.

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
| 49 | Brazil    | 2020-04-15 00:00:00 |       3058 |         204 |   28320 |     1736 | False        |
| 50 | Brazil    | 2020-04-16 00:00:00 |       2105 |         188 |   30425 |     1924 | False        |
| 51 | Brazil    | 2020-04-17 00:00:00 |       3257 |         217 |   33682 |     2141 | False        |
| 52 | Brazil    | 2020-04-18 00:00:00 |       2976 |         213 |   36658 |     2354 | False        |
| 53 | Brazil    | 2020-04-19 00:00:00 |       1996 |         108 |   38654 |     2462 | False        |
| 54 | Brazil    | 2020-04-20 00:00:00 |       2137 |         127 |   40791 |     2589 | True         |
| 55 | Brazil    | 2020-04-21 00:00:00 |       2485 |         151 |   43276 |     2740 | True         |
| 56 | Brazil    | 2020-04-22 00:00:00 |       2727 |         157 |   46003 |     2897 | True         |
| 57 | Brazil    | 2020-04-23 00:00:00 |       2657 |         161 |   48660 |     3058 | True         |
| 58 | Brazil    | 2020-04-24 00:00:00 |       2752 |         156 |   51412 |     3214 | True         |
| 59 | Brazil    | 2020-04-25 00:00:00 |       2717 |         157 |   54129 |     3371 | True         |
| 60 | Brazil    | 2020-04-26 00:00:00 |       2617 |         144 |   56746 |     3515 | True         |
| 61 | Brazil    | 2020-04-27 00:00:00 |       2640 |         151 |   59386 |     3666 | True         |
| 62 | Brazil    | 2020-04-28 00:00:00 |       2988 |         175 |   62374 |     3841 | True         |
| 63 | Brazil    | 2020-04-29 00:00:00 |       3230 |         182 |   65604 |     4023 | True         |

 #### As curvas acumuladas previstas para o Brasil
![](brazil_predictions.png)

 O Facebook Prophet gera automaticamente gráficos do comportamento sazonal dos dados, o que provê boas informações visuais. Aqui estão sobre as predições do Brasil:
### Casos
![](brazil_prophet_cases.png)

 ### Mortes
![](brazil_prophet_deaths.png)
#### Finalmente, as predições para os países selecionados para:
**Para amanhã**
|    | country        | ds                  |   case_day |   death_day |   cases |   deaths | predicted?   |
|---:|:---------------|:--------------------|-----------:|------------:|--------:|---------:|:-------------|
| 54 | Brazil         | 2020-04-20 00:00:00 |       2137 |         127 |   40791 |     2589 | True         |
| 80 | Italy          | 2020-04-20 00:00:00 |       5105 |         760 |  184077 |    24420 | True         |
| 80 | United Kingdom | 2020-04-20 00:00:00 |       6106 |         880 |  127278 |    16975 | True         |
| 79 | Spain          | 2020-04-20 00:00:00 |       6621 |         727 |  205295 |    21180 | True         |
| 89 | US             | 2020-04-20 00:00:00 |      36383 |        2680 |  795469 |    43341 | True         |
| 76 | Belgium        | 2020-04-20 00:00:00 |       1303 |         329 |   39799 |     6012 | True         |
| 87 | France         | 2020-04-20 00:00:00 |       5325 |         836 |  159422 |    20580 | True         |

 **Para depois e amanhã** 
|    | country        | ds                  |   case_day |   death_day |   cases |   deaths | predicted?   |
|---:|:---------------|:--------------------|-----------:|------------:|--------:|---------:|:-------------|
| 55 | Brazil         | 2020-04-21 00:00:00 |       2485 |         151 |   43276 |     2740 | True         |
| 81 | Italy          | 2020-04-21 00:00:00 |       5045 |         782 |  189122 |    25202 | True         |
| 81 | United Kingdom | 2020-04-21 00:00:00 |       6329 |         949 |  133607 |    17924 | True         |
| 80 | Spain          | 2020-04-21 00:00:00 |       6422 |         698 |  211717 |    21878 | True         |
| 90 | US             | 2020-04-21 00:00:00 |      37563 |        2917 |  833032 |    46258 | True         |
| 77 | Belgium        | 2020-04-21 00:00:00 |       1340 |         365 |   41139 |     6377 | True         |
| 88 | France         | 2020-04-21 00:00:00 |       5608 |         915 |  165030 |    21495 | True         |