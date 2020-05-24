# **Predições**
Para experiência, estou fazendo predições simples sobre a quantidade de casos e mortes diárias. Como são séries temporais (*time-series*), estou usando [Facebook Prophet](https://facebook.github.io/prophet/docs/quick_start.html) que também é desenhado para este tipo de predição de uma maneira bem mais simples. Isso funciona muito bem na maioria das vezes; porém, algumas vezes há um grande salto entre os números que impactam no desempenho do modelo e leva um tempo (medições) para ser absorvido e compreendidos.

Essas predições foram feitas com os dados mundiais da pandemia Covid19 até **2020-05-23**.

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
| 83 | Brazil    | 2020-05-19 00:00:00 |      16517 |        1130 |  271885 |    17983 | False        |
| 84 | Brazil    | 2020-05-20 00:00:00 |      19694 |         876 |  291579 |    18859 | False        |
| 85 | Brazil    | 2020-05-21 00:00:00 |      18508 |        1188 |  310087 |    20047 | False        |
| 86 | Brazil    | 2020-05-22 00:00:00 |      20803 |        1001 |  330890 |    21048 | False        |
| 87 | Brazil    | 2020-05-23 00:00:00 |      16508 |         965 |  347398 |    22013 | False        |
| 88 | Brazil    | 2020-05-24 00:00:00 |      15670 |         872 |  363068 |    22885 | True         |
| 89 | Brazil    | 2020-05-25 00:00:00 |      16739 |         926 |  379807 |    23811 | True         |
| 90 | Brazil    | 2020-05-26 00:00:00 |      17673 |        1045 |  397480 |    24856 | True         |
| 91 | Brazil    | 2020-05-27 00:00:00 |      19031 |        1038 |  416511 |    25894 | True         |
| 92 | Brazil    | 2020-05-28 00:00:00 |      19280 |        1095 |  435791 |    26989 | True         |
| 93 | Brazil    | 2020-05-29 00:00:00 |      20017 |        1109 |  455808 |    28098 | True         |
| 94 | Brazil    | 2020-05-30 00:00:00 |      19549 |        1077 |  475357 |    29175 | True         |
| 95 | Brazil    | 2020-05-31 00:00:00 |      18902 |        1026 |  494259 |    30201 | True         |
| 96 | Brazil    | 2020-06-01 00:00:00 |      19972 |        1080 |  514231 |    31281 | True         |
| 97 | Brazil    | 2020-06-02 00:00:00 |      20906 |        1199 |  535137 |    32480 | True         |

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
|  88 | Brazil         | 2020-05-24 00:00:00 |      15670 |         872 |  363068 |    22885 | True         |
| 114 | Italy          | 2020-05-24 00:00:00 |       2672 |         132 |  231999 |    32867 | True         |
| 114 | United Kingdom | 2020-05-24 00:00:00 |       4840 |         612 |  263759 |    37369 | True         |
| 113 | Spain          | 2020-05-24 00:00:00 |       3044 |         427 |  248359 |    29105 | True         |
| 123 | US             | 2020-05-24 00:00:00 |      31442 |        1771 | 1654054 |    98858 | True         |
| 110 | Belgium        | 2020-05-24 00:00:00 |        411 |         145 |   57221 |     9382 | True         |
| 121 | France         | 2020-05-24 00:00:00 |       1589 |         365 |  183740 |    28583 | True         |

 **Para depois e amanhã** 
|     | country        | ds                  |   case_day |   death_day |   cases |   deaths | predicted?   |
|----:|:---------------|:--------------------|-----------:|------------:|--------:|---------:|:-------------|
|  89 | Brazil         | 2020-05-25 00:00:00 |      16739 |         926 |  379807 |    23811 | True         |
| 115 | Italy          | 2020-05-25 00:00:00 |       2324 |         139 |  234323 |    33006 | True         |
| 115 | United Kingdom | 2020-05-25 00:00:00 |       4521 |         617 |  268280 |    37986 | True         |
| 114 | Spain          | 2020-05-25 00:00:00 |       3137 |         445 |  251496 |    29550 | True         |
| 124 | US             | 2020-05-25 00:00:00 |      31243 |        1852 | 1685297 |   100710 | True         |
| 111 | Belgium        | 2020-05-25 00:00:00 |        258 |         137 |   57479 |     9519 | True         |
| 122 | France         | 2020-05-25 00:00:00 |        708 |         412 |  184448 |    28995 | True         |