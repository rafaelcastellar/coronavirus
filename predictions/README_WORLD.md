# **Predições**
Para experiência, estou fazendo predições simples sobre a quantidade de casos e mortes diárias. Como são séries temporais (*time-series*), estou usando [Facebook Prophet](https://facebook.github.io/prophet/docs/quick_start.html) que também é desenhado para este tipo de predição de uma maneira bem mais simples. Isso funciona muito bem na maioria das vezes; porém, algumas vezes há um grande salto entre os números que impactam no desempenho do modelo e leva um tempo (medições) para ser absorvido e compreendidos.

Essas predições foram feitas com os dados mundiais da pandemia Covid19 até **2020-05-25**.

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
| 85 | Brazil    | 2020-05-21 00:00:00 |      18508 |        1188 |  310087 |    20047 | False        |
| 86 | Brazil    | 2020-05-22 00:00:00 |      20803 |        1001 |  330890 |    21048 | False        |
| 87 | Brazil    | 2020-05-23 00:00:00 |      16508 |         965 |  347398 |    22013 | False        |
| 88 | Brazil    | 2020-05-24 00:00:00 |      15813 |         653 |  363211 |    22666 | False        |
| 89 | Brazil    | 2020-05-25 00:00:00 |      11687 |         807 |  374898 |    23473 | False        |
| 90 | Brazil    | 2020-05-26 00:00:00 |      16735 |         995 |  391633 |    24468 | True         |
| 91 | Brazil    | 2020-05-27 00:00:00 |      18062 |         987 |  409695 |    25455 | True         |
| 92 | Brazil    | 2020-05-28 00:00:00 |      18272 |        1042 |  427967 |    26497 | True         |
| 93 | Brazil    | 2020-05-29 00:00:00 |      18953 |        1055 |  446920 |    27552 | True         |
| 94 | Brazil    | 2020-05-30 00:00:00 |      18432 |        1021 |  465352 |    28573 | True         |
| 95 | Brazil    | 2020-05-31 00:00:00 |      17752 |         951 |  483104 |    29524 | True         |
| 96 | Brazil    | 2020-06-01 00:00:00 |      18377 |        1011 |  501481 |    30535 | True         |
| 97 | Brazil    | 2020-06-02 00:00:00 |      19583 |        1133 |  521064 |    31668 | True         |
| 98 | Brazil    | 2020-06-03 00:00:00 |      20909 |        1124 |  541973 |    32792 | True         |
| 99 | Brazil    | 2020-06-04 00:00:00 |      21120 |        1179 |  563093 |    33971 | True         |

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
|  90 | Brazil         | 2020-05-26 00:00:00 |      16735 |         995 |  391633 |    24468 | True         |
| 116 | Italy          | 2020-05-26 00:00:00 |         74 |         154 |  230232 |    33031 | True         |
| 116 | United Kingdom | 2020-05-26 00:00:00 |       3761 |         815 |  266723 |    37811 | True         |
| 115 | Spain          | 2020-05-26 00:00:00 |       2400 |          82 |  238163 |    26916 | True         |
| 125 | US             | 2020-05-26 00:00:00 |      31066 |        2118 | 1693368 |   100338 | True         |
| 112 | Belgium        | 2020-05-26 00:00:00 |        218 |          85 |   57560 |     9397 | True         |
| 123 | France         | 2020-05-26 00:00:00 |        831 |         355 |  184013 |    28815 | True         |

 **Para depois e amanhã** 
|     | country        | ds                  |   case_day |   death_day |   cases |   deaths | predicted?   |
|----:|:---------------|:--------------------|-----------:|------------:|--------:|---------:|:-------------|
|  91 | Brazil         | 2020-05-27 00:00:00 |      18062 |         987 |  409695 |    25455 | True         |
| 117 | Italy          | 2020-05-27 00:00:00 |        219 |         137 |  230451 |    33168 | True         |
| 117 | United Kingdom | 2020-05-27 00:00:00 |       3850 |         773 |  270573 |    38584 | True         |
| 116 | Spain          | 2020-05-27 00:00:00 |       3015 |         141 |  241178 |    27057 | True         |
| 126 | US             | 2020-05-27 00:00:00 |      32047 |        2165 | 1725415 |   102503 | True         |
| 113 | Belgium        | 2020-05-27 00:00:00 |        321 |          94 |   57881 |     9491 | True         |
| 124 | France         | 2020-05-27 00:00:00 |         30 |         367 |  184043 |    29182 | True         |