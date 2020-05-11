# **Predições**
Para experiência, estou fazendo predições simples sobre a quantidade de casos e mortes diárias. Como são séries temporais (*time-series*), estou usando [Facebook Prophet](https://facebook.github.io/prophet/docs/quick_start.html) que também é desenhado para este tipo de predição de uma maneira bem mais simples. Isso funciona muito bem na maioria das vezes; porém, algumas vezes há um grande salto entre os números que impactam no desempenho do modelo e leva um tempo (medições) para ser absorvido e compreendidos.

Essas predições foram feitas com os dados mundiais da pandemia Covid19 até **2020-05-10**.

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
| 70 | Brazil    | 2020-05-06 00:00:00 |      11156 |         650 |  126611 |     8588 | False        |
| 71 | Brazil    | 2020-05-07 00:00:00 |       9162 |         602 |  135773 |     9190 | False        |
| 72 | Brazil    | 2020-05-08 00:00:00 |      11121 |         827 |  146894 |    10017 | False        |
| 73 | Brazil    | 2020-05-09 00:00:00 |       9167 |         639 |  156061 |    10656 | False        |
| 74 | Brazil    | 2020-05-10 00:00:00 |       6638 |         467 |  162699 |    11123 | False        |
| 75 | Brazil    | 2020-05-11 00:00:00 |       8399 |         539 |  171098 |    11662 | True         |
| 76 | Brazil    | 2020-05-12 00:00:00 |       8941 |         607 |  180039 |    12269 | True         |
| 77 | Brazil    | 2020-05-13 00:00:00 |       9765 |         622 |  189804 |    12891 | True         |
| 78 | Brazil    | 2020-05-14 00:00:00 |       9894 |         658 |  199698 |    13549 | True         |
| 79 | Brazil    | 2020-05-15 00:00:00 |      10013 |         669 |  209711 |    14218 | True         |
| 80 | Brazil    | 2020-05-16 00:00:00 |      10038 |         654 |  219749 |    14872 | True         |
| 81 | Brazil    | 2020-05-17 00:00:00 |       9706 |         618 |  229455 |    15490 | True         |
| 82 | Brazil    | 2020-05-18 00:00:00 |      10241 |         647 |  239696 |    16137 | True         |
| 83 | Brazil    | 2020-05-19 00:00:00 |      10783 |         715 |  250479 |    16852 | True         |
| 84 | Brazil    | 2020-05-20 00:00:00 |      11607 |         730 |  262086 |    17582 | True         |

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
|  75 | Brazil         | 2020-05-11 00:00:00 |       8399 |         539 |  171098 |    11662 | True         |
| 101 | Italy          | 2020-05-11 00:00:00 |       3556 |         581 |  222626 |    31141 | True         |
| 101 | United Kingdom | 2020-05-11 00:00:00 |       5719 |         726 |  226168 |    32656 | True         |
| 100 | Spain          | 2020-05-11 00:00:00 |       4228 |         543 |  238603 |    27164 | True         |
| 110 | US             | 2020-05-11 00:00:00 |      32430 |        2056 | 1361690 |    81582 | True         |
|  97 | Belgium        | 2020-05-11 00:00:00 |        852 |         205 |   53933 |     8861 | True         |
| 108 | France         | 2020-05-11 00:00:00 |       3525 |         580 |  181649 |    26963 | True         |

 **Para depois e amanhã** 
|     | country        | ds                  |   case_day |   death_day |   cases |   deaths | predicted?   |
|----:|:---------------|:--------------------|-----------:|------------:|--------:|---------:|:-------------|
|  76 | Brazil         | 2020-05-12 00:00:00 |       8941 |         607 |  180039 |    12269 | True         |
| 102 | Italy          | 2020-05-12 00:00:00 |       3555 |         610 |  226181 |    31751 | True         |
| 102 | United Kingdom | 2020-05-12 00:00:00 |       5822 |         899 |  231990 |    33555 | True         |
| 101 | Spain          | 2020-05-12 00:00:00 |       4263 |         522 |  242866 |    27686 | True         |
| 111 | US             | 2020-05-12 00:00:00 |      33445 |        2343 | 1395135 |    83925 | True         |
|  98 | Belgium        | 2020-05-12 00:00:00 |        813 |         234 |   54746 |     9095 | True         |
| 109 | France         | 2020-05-12 00:00:00 |       3693 |         633 |  185342 |    27596 | True         |