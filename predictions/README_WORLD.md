# **Predições**
Para experiência, estou fazendo predições simples sobre a quantidade de casos e mortes diárias. Como são séries temporais (*time-series*), estou usando [Facebook Prophet](https://facebook.github.io/prophet/docs/quick_start.html) que também é desenhado para este tipo de predição de uma maneira bem mais simples. Isso funciona muito bem na maioria das vezes; porém, algumas vezes há um grande salto entre os números que impactam no desempenho do modelo e leva um tempo (medições) para ser absorvido e compreendidos.

Essas predições foram feitas com os dados mundiais da pandemia Covid19 até **2020-06-02**.

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
|  93 | Brazil    | 2020-05-29 00:00:00 |      26928 |        1124 |  465166 |    27878 | False        |
|  94 | Brazil    | 2020-05-30 00:00:00 |      33274 |         956 |  498440 |    28834 | False        |
|  95 | Brazil    | 2020-05-31 00:00:00 |      16409 |         480 |  514849 |    29314 | False        |
|  96 | Brazil    | 2020-06-01 00:00:00 |      11598 |         623 |  526447 |    29937 | False        |
|  97 | Brazil    | 2020-06-02 00:00:00 |      28936 |        1262 |  555383 |    31199 | False        |
|  98 | Brazil    | 2020-06-03 00:00:00 |      23418 |        1086 |  578801 |    32285 | True         |
|  99 | Brazil    | 2020-06-04 00:00:00 |      24081 |        1140 |  602882 |    33425 | True         |
| 100 | Brazil    | 2020-06-05 00:00:00 |      24820 |        1149 |  627702 |    34574 | True         |
| 101 | Brazil    | 2020-06-06 00:00:00 |      24849 |        1104 |  652551 |    35678 | True         |
| 102 | Brazil    | 2020-06-07 00:00:00 |      23073 |        1004 |  675624 |    36682 | True         |
| 103 | Brazil    | 2020-06-08 00:00:00 |      23369 |        1068 |  698993 |    37750 | True         |
| 104 | Brazil    | 2020-06-09 00:00:00 |      25758 |        1228 |  724751 |    38978 | True         |
| 105 | Brazil    | 2020-06-10 00:00:00 |      26885 |        1212 |  751636 |    40190 | True         |
| 106 | Brazil    | 2020-06-11 00:00:00 |      27549 |        1267 |  779185 |    41457 | True         |
| 107 | Brazil    | 2020-06-12 00:00:00 |      28288 |        1275 |  807473 |    42732 | True         |

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
|  98 | Brazil         | 2020-06-03 00:00:00 |      23418 |        1086 |  578801 |    32285 | True         |
| 124 | Italy          | 2020-06-03 00:00:00 |       -132 |          64 |  233383 |    33594 | True         |
| 124 | United Kingdom | 2020-06-03 00:00:00 |       2568 |         701 |  282375 |    40153 | True         |
| 123 | Spain          | 2020-06-03 00:00:00 |       2505 |          43 |  242800 |    27170 | True         |
| 133 | US             | 2020-06-03 00:00:00 |      30638 |        2034 | 1862459 |   108214 | True         |
| 120 | Belgium        | 2020-06-03 00:00:00 |         92 |          66 |   58707 |     9571 | True         |
| 131 | France         | 2020-06-03 00:00:00 |       -227 |         178 |  189071 |    29121 | True         |

 **Para depois e amanhã** 
|     | country        | ds                  |   case_day |   death_day |   cases |   deaths | predicted?   |
|----:|:---------------|:--------------------|-----------:|------------:|--------:|---------:|:-------------|
|  99 | Brazil         | 2020-06-04 00:00:00 |      24081 |        1140 |  602882 |    33425 | True         |
| 125 | Italy          | 2020-06-04 00:00:00 |        -21 |          51 |  233362 |    33645 | True         |
| 125 | United Kingdom | 2020-06-04 00:00:00 |       2682 |         687 |  285057 |    40840 | True         |
| 124 | Spain          | 2020-06-04 00:00:00 |       2578 |          12 |  245378 |    27182 | True         |
| 134 | US             | 2020-06-04 00:00:00 |      32660 |        1960 | 1895119 |   110174 | True         |
| 121 | Belgium        | 2020-06-04 00:00:00 |        114 |          54 |   58821 |     9625 | True         |
| 132 | France         | 2020-06-04 00:00:00 |        622 |         193 |  189693 |    29314 | True         |