# **Predições**
Para experiência, estou fazendo predições simples sobre a quantidade de casos e mortes diárias. Como são séries temporais (*time-series*), estou usando [Facebook Prophet](https://facebook.github.io/prophet/docs/quick_start.html) que também é desenhado para este tipo de predição de uma maneira bem mais simples. Isso funciona muito bem na maioria das vezes; porém, algumas vezes há um grande salto entre os números que impactam no desempenho do modelo e leva um tempo (medições) para ser absorvido e compreendidos.

Essas predições foram feitas com os dados mundiais da pandemia Covid19 até **2020-06-22**.

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
| 113 | Brazil    | 2020-06-18 00:00:00 |      22765 |        1238 |  978142 |    47748 | False        |
| 114 | Brazil    | 2020-06-19 00:00:00 |      54771 |        1206 | 1032913 |    48954 | False        |
| 115 | Brazil    | 2020-06-20 00:00:00 |      34666 |        1022 | 1067579 |    49976 | False        |
| 116 | Brazil    | 2020-06-21 00:00:00 |      15762 |         615 | 1083341 |    50591 | False        |
| 117 | Brazil    | 2020-06-22 00:00:00 |      23129 |         680 | 1106470 |    51271 | False        |
| 118 | Brazil    | 2020-06-23 00:00:00 |      32937 |        1273 | 1139407 |    52544 | True         |
| 119 | Brazil    | 2020-06-24 00:00:00 |      34119 |        1273 | 1173526 |    53817 | True         |
| 120 | Brazil    | 2020-06-25 00:00:00 |      34082 |        1319 | 1207608 |    55136 | True         |
| 121 | Brazil    | 2020-06-26 00:00:00 |      36288 |        1273 | 1243896 |    56409 | True         |
| 122 | Brazil    | 2020-06-27 00:00:00 |      34648 |        1215 | 1278544 |    57624 | True         |
| 123 | Brazil    | 2020-06-28 00:00:00 |      31311 |        1065 | 1309855 |    58689 | True         |
| 124 | Brazil    | 2020-06-29 00:00:00 |      31983 |        1129 | 1341838 |    59818 | True         |
| 125 | Brazil    | 2020-06-30 00:00:00 |      36313 |        1366 | 1378151 |    61184 | True         |
| 126 | Brazil    | 2020-07-01 00:00:00 |      37494 |        1366 | 1415645 |    62550 | True         |
| 127 | Brazil    | 2020-07-02 00:00:00 |      37458 |        1412 | 1453103 |    63962 | True         |

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
| 118 | Brazil         | 2020-06-23 00:00:00 |      32937 |        1273 | 1139407 |    52544 | True         |
| 144 | Italy          | 2020-06-23 00:00:00 |       -769 |         -39 |  238079 |    34618 | True         |
| 144 | United Kingdom | 2020-06-23 00:00:00 |        851 |         247 |  308027 |    42978 | True         |
| 143 | Spain          | 2020-06-23 00:00:00 |       -476 |         -52 |  246391 |    28272 | True         |
| 153 | US             | 2020-06-23 00:00:00 |      24786 |         995 | 2337088 |   121397 | True         |
| 140 | Belgium        | 2020-06-23 00:00:00 |       -199 |         -13 |   60351 |     9683 | True         |
| 151 | France         | 2020-06-23 00:00:00 |        -25 |          -5 |  200067 |    29661 | True         |

 **Para depois e amanhã** 
|     | country        | ds                  |   case_day |   death_day |   cases |   deaths | predicted?   |
|----:|:---------------|:--------------------|-----------:|------------:|--------:|---------:|:-------------|
| 119 | Brazil         | 2020-06-24 00:00:00 |      34119 |        1273 | 1173526 |    53817 | True         |
| 145 | Italy          | 2020-06-24 00:00:00 |       -628 |         -49 |  237451 |    34569 | True         |
| 145 | United Kingdom | 2020-06-24 00:00:00 |        746 |         216 |  308773 |    43194 | True         |
| 144 | Spain          | 2020-06-24 00:00:00 |        -54 |         -18 |  246337 |    28254 | True         |
| 154 | US             | 2020-06-24 00:00:00 |      25791 |        1053 | 2362879 |   122450 | True         |
| 141 | Belgium        | 2020-06-24 00:00:00 |       -113 |          -5 |   60238 |     9678 | True         |
| 152 | France         | 2020-06-24 00:00:00 |       -422 |          -8 |  199645 |    29653 | True         |