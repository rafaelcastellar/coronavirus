# **Predições**
Para experiência, estou fazendo predições simples sobre a quantidade de casos e mortes diárias. Como são séries temporais (*time-series*), estou usando [Facebook Prophet](https://facebook.github.io/prophet/docs/quick_start.html) que também é desenhado para este tipo de predição de uma maneira bem mais simples. Isso funciona muito bem na maioria das vezes; porém, algumas vezes há um grande salto entre os números que impactam no desempenho do modelo e leva um tempo (medições) para ser absorvido e compreendidos.

Essas predições foram feitas com os dados mundiais da pandemia Covid19 até **2020-05-30**.

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
|  90 | Brazil    | 2020-05-26 00:00:00 |      16324 |        1039 |  391222 |    24512 | False        |
|  91 | Brazil    | 2020-05-27 00:00:00 |      20599 |        1086 |  411821 |    25598 | False        |
|  92 | Brazil    | 2020-05-28 00:00:00 |      26417 |        1156 |  438238 |    26754 | False        |
|  93 | Brazil    | 2020-05-29 00:00:00 |      26928 |        1124 |  465166 |    27878 | False        |
|  94 | Brazil    | 2020-05-30 00:00:00 |      33274 |         956 |  498440 |    28834 | False        |
|  95 | Brazil    | 2020-05-31 00:00:00 |      21334 |         977 |  519774 |    29811 | True         |
|  96 | Brazil    | 2020-06-01 00:00:00 |      22098 |        1038 |  541872 |    30849 | True         |
|  97 | Brazil    | 2020-06-02 00:00:00 |      23411 |        1163 |  565283 |    32012 | True         |
|  98 | Brazil    | 2020-06-03 00:00:00 |      25129 |        1161 |  590412 |    33173 | True         |
|  99 | Brazil    | 2020-06-04 00:00:00 |      25875 |        1217 |  616287 |    34390 | True         |
| 100 | Brazil    | 2020-06-05 00:00:00 |      26695 |        1228 |  642982 |    35618 | True         |
| 101 | Brazil    | 2020-06-06 00:00:00 |      26794 |        1185 |  669776 |    36803 | True         |
| 102 | Brazil    | 2020-06-07 00:00:00 |      25438 |        1123 |  695214 |    37926 | True         |
| 103 | Brazil    | 2020-06-08 00:00:00 |      26202 |        1183 |  721416 |    39109 | True         |
| 104 | Brazil    | 2020-06-09 00:00:00 |      27515 |        1309 |  748931 |    40418 | True         |

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
|  95 | Brazil         | 2020-05-31 00:00:00 |      21334 |         977 |  519774 |    29811 | True         |
| 121 | Italy          | 2020-05-31 00:00:00 |          0 |          64 |  232664 |    33404 | True         |
| 121 | United Kingdom | 2020-05-31 00:00:00 |       3198 |         532 |  277832 |    38990 | True         |
| 120 | Spain          | 2020-05-31 00:00:00 |       2099 |         -34 |  241690 |    27091 | True         |
| 130 | US             | 2020-05-31 00:00:00 |      30318 |        1659 | 1800483 |   105435 | True         |
| 117 | Belgium        | 2020-05-31 00:00:00 |        203 |          41 |   58389 |     9494 | True         |
| 128 | France         | 2020-05-31 00:00:00 |       1561 |         157 |  190483 |    28931 | True         |

 **Para depois e amanhã** 
|     | country        | ds                  |   case_day |   death_day |   cases |   deaths | predicted?   |
|----:|:---------------|:--------------------|-----------:|------------:|--------:|---------:|:-------------|
|  96 | Brazil         | 2020-06-01 00:00:00 |      22098 |        1038 |  541872 |    30849 | True         |
| 122 | Italy          | 2020-06-01 00:00:00 |       -432 |          74 |  232232 |    33478 | True         |
| 122 | United Kingdom | 2020-06-01 00:00:00 |       2805 |         535 |  280637 |    39525 | True         |
| 121 | Spain          | 2020-06-01 00:00:00 |       1560 |        -144 |  243250 |    26947 | True         |
| 131 | US             | 2020-06-01 00:00:00 |      30024 |        1725 | 1830507 |   107160 | True         |
| 118 | Belgium        | 2020-06-01 00:00:00 |         62 |          30 |   58451 |     9524 | True         |
| 129 | France         | 2020-06-01 00:00:00 |        765 |         200 |  191248 |    29131 | True         |