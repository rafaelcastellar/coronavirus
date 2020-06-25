# **Predições**
Para experiência, estou fazendo predições simples sobre a quantidade de casos e mortes diárias. Como são séries temporais (*time-series*), estou usando [Facebook Prophet](https://facebook.github.io/prophet/docs/quick_start.html) que também é desenhado para este tipo de predição de uma maneira bem mais simples. Isso funciona muito bem na maioria das vezes; porém, algumas vezes há um grande salto entre os números que impactam no desempenho do modelo e leva um tempo (medições) para ser absorvido e compreendidos.

Essas predições foram feitas com os dados mundiais da pandemia Covid19 até **2020-06-24**.

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
| 115 | Brazil    | 2020-06-20 00:00:00 |      34666 |        1022 | 1067579 |    49976 | False        |
| 116 | Brazil    | 2020-06-21 00:00:00 |      15762 |         615 | 1083341 |    50591 | False        |
| 117 | Brazil    | 2020-06-22 00:00:00 |      23129 |         680 | 1106470 |    51271 | False        |
| 118 | Brazil    | 2020-06-23 00:00:00 |      39436 |        1374 | 1145906 |    52645 | False        |
| 119 | Brazil    | 2020-06-24 00:00:00 |      42725 |        1185 | 1188631 |    53830 | False        |
| 120 | Brazil    | 2020-06-25 00:00:00 |      34966 |        1303 | 1223597 |    55133 | True         |
| 121 | Brazil    | 2020-06-26 00:00:00 |      37189 |        1257 | 1260786 |    56390 | True         |
| 122 | Brazil    | 2020-06-27 00:00:00 |      35564 |        1198 | 1296350 |    57588 | True         |
| 123 | Brazil    | 2020-06-28 00:00:00 |      32246 |        1049 | 1328596 |    58637 | True         |
| 124 | Brazil    | 2020-06-29 00:00:00 |      32939 |        1112 | 1361535 |    59749 | True         |
| 125 | Brazil    | 2020-06-30 00:00:00 |      37657 |        1354 | 1399192 |    61103 | True         |
| 126 | Brazil    | 2020-07-01 00:00:00 |      38967 |        1345 | 1438159 |    62448 | True         |
| 127 | Brazil    | 2020-07-02 00:00:00 |      38528 |        1393 | 1476687 |    63841 | True         |
| 128 | Brazil    | 2020-07-03 00:00:00 |      40751 |        1347 | 1517438 |    65188 | True         |
| 129 | Brazil    | 2020-07-04 00:00:00 |      39125 |        1288 | 1556563 |    66476 | True         |

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
| 120 | Brazil         | 2020-06-25 00:00:00 |      34966 |        1303 | 1223597 |    55133 | True         |
| 146 | Italy          | 2020-06-25 00:00:00 |       -451 |         -58 |  239087 |    34586 | True         |
| 146 | United Kingdom | 2020-06-25 00:00:00 |        739 |         159 |  309491 |    43324 | True         |
| 145 | Spain          | 2020-06-25 00:00:00 |        -70 |         -24 |  247379 |    28303 | True         |
| 155 | US             | 2020-06-25 00:00:00 |      29181 |         942 | 2410550 |   122921 | True         |
| 142 | Belgium        | 2020-06-25 00:00:00 |        -87 |         -10 |   60920 |     9716 | True         |
| 153 | France         | 2020-06-25 00:00:00 |        219 |          11 |  200815 |    29745 | True         |

 **Para depois e amanhã** 
|     | country        | ds                  |   case_day |   death_day |   cases |   deaths | predicted?   |
|----:|:---------------|:--------------------|-----------:|------------:|--------:|---------:|:-------------|
| 121 | Brazil         | 2020-06-26 00:00:00 |      37189 |        1257 | 1260786 |    56390 | True         |
| 147 | Italy          | 2020-06-26 00:00:00 |       -516 |         -45 |  238571 |    34541 | True         |
| 147 | United Kingdom | 2020-06-26 00:00:00 |       1142 |         190 |  310633 |    43514 | True         |
| 146 | Spain          | 2020-06-26 00:00:00 |       -319 |          44 |  247060 |    28347 | True         |
| 156 | US             | 2020-06-26 00:00:00 |      29781 |         869 | 2440331 |   123790 | True         |
| 143 | Belgium        | 2020-06-26 00:00:00 |        -59 |          -8 |   60861 |     9708 | True         |
| 154 | France         | 2020-06-26 00:00:00 |       -147 |         -17 |  200668 |    29728 | True         |