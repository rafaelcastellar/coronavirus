# **Predições**
Para experiência, estou fazendo predições simples sobre a quantidade de casos e mortes diárias. Como são séries temporais (*time-series*), estou usando [Facebook Prophet](https://facebook.github.io/prophet/docs/quick_start.html) que também é desenhado para este tipo de predição de uma maneira bem mais simples. Isso funciona muito bem na maioria das vezes; porém, algumas vezes há um grande salto entre os números que impactam no desempenho do modelo e leva um tempo (medições) para ser absorvido e compreendidos.

Essas predições foram feitas com os dados mundiais da pandemia Covid19 até **2020-06-21**.

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
| 112 | Brazil    | 2020-06-17 00:00:00 |      32188 |        1269 |  955377 |    46510 | False        |
| 113 | Brazil    | 2020-06-18 00:00:00 |      22765 |        1238 |  978142 |    47748 | False        |
| 114 | Brazil    | 2020-06-19 00:00:00 |      54771 |        1206 | 1032913 |    48954 | False        |
| 115 | Brazil    | 2020-06-20 00:00:00 |          0 |        1022 | 1032913 |    49976 | False        |
| 116 | Brazil    | 2020-06-21 00:00:00 |      50428 |         615 | 1083341 |    50591 | False        |
| 117 | Brazil    | 2020-06-22 00:00:00 |      28253 |        1077 | 1111594 |    51668 | True         |
| 118 | Brazil    | 2020-06-23 00:00:00 |      32212 |        1292 | 1143806 |    52960 | True         |
| 119 | Brazil    | 2020-06-24 00:00:00 |      33448 |        1291 | 1177254 |    54251 | True         |
| 120 | Brazil    | 2020-06-25 00:00:00 |      33384 |        1337 | 1210638 |    55588 | True         |
| 121 | Brazil    | 2020-06-26 00:00:00 |      35559 |        1292 | 1246197 |    56880 | True         |
| 122 | Brazil    | 2020-06-27 00:00:00 |      31862 |        1234 | 1278059 |    58114 | True         |
| 123 | Brazil    | 2020-06-28 00:00:00 |      32569 |        1086 | 1310628 |    59200 | True         |
| 124 | Brazil    | 2020-06-29 00:00:00 |      31481 |        1173 | 1342109 |    60373 | True         |
| 125 | Brazil    | 2020-06-30 00:00:00 |      35440 |        1388 | 1377549 |    61761 | True         |
| 126 | Brazil    | 2020-07-01 00:00:00 |      36676 |        1387 | 1414225 |    63148 | True         |

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
| 117 | Brazil         | 2020-06-22 00:00:00 |      28253 |        1077 | 1111594 |    51668 | True         |
| 143 | Italy          | 2020-06-22 00:00:00 |       -849 |         -57 |  237778 |    34577 | True         |
| 143 | United Kingdom | 2020-06-22 00:00:00 |        708 |          82 |  306926 |    42799 | True         |
| 142 | Spain          | 2020-06-22 00:00:00 |        233 |        -126 |  246868 |    28197 | True         |
| 152 | US             | 2020-06-22 00:00:00 |      24417 |         636 | 2304296 |   120605 | True         |
| 139 | Belgium        | 2020-06-22 00:00:00 |       -196 |         -32 |   60354 |     9664 | True         |
| 150 | France         | 2020-06-22 00:00:00 |       -174 |         -28 |  199545 |    29615 | True         |

 **Para depois e amanhã** 
|     | country        | ds                  |   case_day |   death_day |   cases |   deaths | predicted?   |
|----:|:---------------|:--------------------|-----------:|------------:|--------:|---------:|:-------------|
| 118 | Brazil         | 2020-06-23 00:00:00 |      32212 |        1292 | 1143806 |    52960 | True         |
| 144 | Italy          | 2020-06-23 00:00:00 |       -846 |         -41 |  236932 |    34536 | True         |
| 144 | United Kingdom | 2020-06-23 00:00:00 |        827 |         245 |  307753 |    43044 | True         |
| 143 | Spain          | 2020-06-23 00:00:00 |        653 |         -38 |  247521 |    28159 | True         |
| 153 | US             | 2020-06-23 00:00:00 |      25203 |         932 | 2329499 |   121537 | True         |
| 140 | Belgium        | 2020-06-23 00:00:00 |       -249 |         -15 |   60105 |     9649 | True         |
| 151 | France         | 2020-06-23 00:00:00 |       -117 |          -3 |  199428 |    29612 | True         |