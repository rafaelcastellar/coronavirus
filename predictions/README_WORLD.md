# **Predições**
Para experiência, estou fazendo predições simples sobre a quantidade de casos e mortes diárias. Como são séries temporais (*time-series*), estou usando [Facebook Prophet](https://facebook.github.io/prophet/docs/quick_start.html) que também é desenhado para este tipo de predição de uma maneira bem mais simples. Isso funciona muito bem na maioria das vezes; porém, algumas vezes há um grande salto entre os números que impactam no desempenho do modelo e leva um tempo (medições) para ser absorvido e compreendidos.

Essas predições foram feitas com os dados mundiais da pandemia Covid19 até **2020-05-29**.

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
|  89 | Brazil    | 2020-05-25 00:00:00 |      11687 |         807 |  374898 |    23473 | False        |
|  90 | Brazil    | 2020-05-26 00:00:00 |      16324 |        1039 |  391222 |    24512 | False        |
|  91 | Brazil    | 2020-05-27 00:00:00 |      20599 |        1086 |  411821 |    25598 | False        |
|  92 | Brazil    | 2020-05-28 00:00:00 |      26417 |        1156 |  438238 |    26754 | False        |
|  93 | Brazil    | 2020-05-29 00:00:00 |      26928 |        1124 |  465166 |    27878 | False        |
|  94 | Brazil    | 2020-05-30 00:00:00 |      20460 |        1054 |  485626 |    28932 | True         |
|  95 | Brazil    | 2020-05-31 00:00:00 |      19852 |         986 |  505478 |    29918 | True         |
|  96 | Brazil    | 2020-06-01 00:00:00 |      20550 |        1046 |  526028 |    30964 | True         |
|  97 | Brazil    | 2020-06-02 00:00:00 |      21797 |        1171 |  547825 |    32135 | True         |
|  98 | Brazil    | 2020-06-03 00:00:00 |      23436 |        1168 |  571261 |    33303 | True         |
|  99 | Brazil    | 2020-06-04 00:00:00 |      24118 |        1226 |  595379 |    34529 | True         |
| 100 | Brazil    | 2020-06-05 00:00:00 |      24869 |        1237 |  620248 |    35766 | True         |
| 101 | Brazil    | 2020-06-06 00:00:00 |      23991 |        1201 |  644239 |    36967 | True         |
| 102 | Brazil    | 2020-06-07 00:00:00 |      23383 |        1133 |  667622 |    38100 | True         |
| 103 | Brazil    | 2020-06-08 00:00:00 |      24081 |        1193 |  691703 |    39293 | True         |

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
|  94 | Brazil         | 2020-05-30 00:00:00 |      20460 |        1054 |  485626 |    28932 | True         |
| 120 | Italy          | 2020-05-30 00:00:00 |        384 |         118 |  232632 |    33347 | True         |
| 120 | United Kingdom | 2020-05-30 00:00:00 |       3407 |         680 |  276429 |    38923 | True         |
| 119 | Spain          | 2020-05-30 00:00:00 |       2220 |          27 |  241147 |    27148 | True         |
| 129 | US             | 2020-05-30 00:00:00 |      32148 |        1933 | 1778167 |   104742 | True         |
| 116 | Belgium        | 2020-05-30 00:00:00 |        301 |          78 |   58362 |     9508 | True         |
| 127 | France         | 2020-05-30 00:00:00 |         54 |         158 |  187147 |    28875 | True         |

 **Para depois e amanhã** 
|     | country        | ds                  |   case_day |   death_day |   cases |   deaths | predicted?   |
|----:|:---------------|:--------------------|-----------:|------------:|--------:|---------:|:-------------|
|  95 | Brazil         | 2020-05-31 00:00:00 |      19852 |         986 |  505478 |    29918 | True         |
| 121 | Italy          | 2020-05-31 00:00:00 |         81 |          51 |  232713 |    33398 | True         |
| 121 | United Kingdom | 2020-05-31 00:00:00 |       3366 |         546 |  279795 |    39469 | True         |
| 120 | Spain          | 2020-05-31 00:00:00 |       2193 |          10 |  243340 |    27158 | True         |
| 130 | US             | 2020-05-31 00:00:00 |      30208 |        1694 | 1808375 |   106436 | True         |
| 117 | Belgium        | 2020-05-31 00:00:00 |        253 |          67 |   58615 |     9575 | True         |
| 128 | France         | 2020-05-31 00:00:00 |       1147 |         122 |  188294 |    28997 | True         |