# **Predições**
Para experiência, estou fazendo predições simples sobre a quantidade de casos e mortes diárias. Como são séries temporais (*time-series*), estou usando [Facebook Prophet](https://facebook.github.io/prophet/docs/quick_start.html) que também é desenhado para este tipo de predição de uma maneira bem mais simples. Isso funciona muito bem na maioria das vezes; porém, algumas vezes há um grande salto entre os números que impactam no desempenho do modelo e leva um tempo (medições) para ser absorvido e compreendidos.

Essas predições foram feitas com os dados mundiais da pandemia Covid19 até **2020-06-26**.

Como há muitos paises para terem seus dados submetidos ao modelo de predição de uma só vez, selecionei alguns mais o Brasil:
['Brazil', 'Italy', 'United Kingdom', 'Spain', 'US', 'Belgium', 'France'].
***Dica**: você mesmo pode definir no notebook *[prediction.ipynb](../prediction.ipynb)* quais países você prefere fazer a predição.*


## A predição
As predições estão sendo realizadas sobre os dados diários de casos e de mortes. Em seguida, os dados previstos são acumulados para que tenhamos a projeção acumulada. Estão sendo previstos os próximos 10 dias.
Ao ffim, é gerado o arquivo CSV contendo todas as previsões.

#### Os últimos 5 dias da pandemia no Brasil e os próximos 10 dias previstos
*predicted? = True* significa que são dados de predição; *=False* significa que são dados reais.
|     | country   | ds                  |   case_day |   death_day |   cases |   deaths | predicted?   |
|----:|:----------|:--------------------|-----------:|------------:|--------:|---------:|:-------------|
| 117 | Brazil    | 2020-06-22 00:00:00 |      23129 |         680 | 1106470 |    51271 | False        |
| 118 | Brazil    | 2020-06-23 00:00:00 |      39436 |        1374 | 1145906 |    52645 | False        |
| 119 | Brazil    | 2020-06-24 00:00:00 |      42725 |        1185 | 1188631 |    53830 | False        |
| 120 | Brazil    | 2020-06-25 00:00:00 |      39483 |        1141 | 1228114 |    54971 | False        |
| 121 | Brazil    | 2020-06-26 00:00:00 |      46860 |         990 | 1274974 |    55961 | False        |
| 122 | Brazil    | 2020-06-27 00:00:00 |      36098 |        1187 | 1311072 |    57148 | True         |
| 123 | Brazil    | 2020-06-28 00:00:00 |      32768 |        1039 | 1343840 |    58187 | True         |
| 124 | Brazil    | 2020-06-29 00:00:00 |      33467 |        1102 | 1377307 |    59289 | True         |
| 125 | Brazil    | 2020-06-30 00:00:00 |      38206 |        1342 | 1415513 |    60631 | True         |
| 126 | Brazil    | 2020-07-01 00:00:00 |      39556 |        1332 | 1455069 |    61963 | True         |
| 127 | Brazil    | 2020-07-02 00:00:00 |      39362 |        1371 | 1494431 |    63334 | True         |
| 128 | Brazil    | 2020-07-03 00:00:00 |      41881 |        1320 | 1536312 |    64654 | True         |
| 129 | Brazil    | 2020-07-04 00:00:00 |      39747 |        1276 | 1576059 |    65930 | True         |
| 130 | Brazil    | 2020-07-05 00:00:00 |      36418 |        1128 | 1612477 |    67058 | True         |
| 131 | Brazil    | 2020-07-06 00:00:00 |      37117 |        1190 | 1649594 |    68248 | True         |

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
| 122 | Brazil         | 2020-06-27 00:00:00 |      36098 |        1187 | 1311072 |    57148 | True         |
| 148 | Italy          | 2020-06-27 00:00:00 |       -476 |         -48 |  239613 |    34660 | True         |
| 148 | United Kingdom | 2020-06-27 00:00:00 |        695 |         151 |  311946 |    43649 | True         |
| 147 | Spain          | 2020-06-27 00:00:00 |        581 |         -63 |  248849 |    28275 | True         |
| 157 | US             | 2020-06-27 00:00:00 |      29166 |         883 | 2496720 |   125922 | True         |
| 144 | Belgium        | 2020-06-27 00:00:00 |        -54 |         -22 |   61052 |     9709 | True         |
| 155 | France         | 2020-06-27 00:00:00 |       -262 |         -57 |  201922 |    29724 | True         |

 **Para depois e amanhã** 
|     | country        | ds                  |   case_day |   death_day |   cases |   deaths | predicted?   |
|----:|:---------------|:--------------------|-----------:|------------:|--------:|---------:|:-------------|
| 123 | Brazil         | 2020-06-28 00:00:00 |      32768 |        1039 | 1343840 |    58187 | True         |
| 149 | Italy          | 2020-06-28 00:00:00 |       -717 |        -107 |  238896 |    34553 | True         |
| 149 | United Kingdom | 2020-06-28 00:00:00 |        642 |          12 |  312588 |    43661 | True         |
| 148 | Spain          | 2020-06-28 00:00:00 |        521 |         -75 |  249370 |    28200 | True         |
| 158 | US             | 2020-06-28 00:00:00 |      26644 |         611 | 2523364 |   126533 | True         |
| 145 | Belgium        | 2020-06-28 00:00:00 |        -91 |         -31 |   60961 |     9678 | True         |
| 156 | France         | 2020-06-28 00:00:00 |        541 |         -89 |  202463 |    29635 | True         |