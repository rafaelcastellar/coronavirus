# **Predições**
Para experiência, estou fazendo predições simples sobre a quantidade de casos e mortes diárias. Como são séries temporais (*time-series*), estou usando [Facebook Prophet](https://facebook.github.io/prophet/docs/quick_start.html) que também é desenhado para este tipo de predição de uma maneira bem mais simples. Isso funciona muito bem na maioria das vezes; porém, algumas vezes há um grande salto entre os números que impactam no desempenho do modelo e leva um tempo (medições) para ser absorvido e compreendidos.

Essas predições foram feitas com os dados mundiais da pandemia Covid19 até **2020-06-15**.

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
| 106 | Brazil    | 2020-06-11 00:00:00 |      30412 |        1239 |  802828 |    40919 | False        |
| 107 | Brazil    | 2020-06-12 00:00:00 |      25982 |         909 |  828810 |    41828 | False        |
| 108 | Brazil    | 2020-06-13 00:00:00 |      21704 |         892 |  850514 |    42720 | False        |
| 109 | Brazil    | 2020-06-14 00:00:00 |      17110 |         612 |  867624 |    43332 | False        |
| 110 | Brazil    | 2020-06-15 00:00:00 |      20647 |         627 |  888271 |    43959 | False        |
| 111 | Brazil    | 2020-06-16 00:00:00 |      28859 |        1213 |  917130 |    45172 | True         |
| 112 | Brazil    | 2020-06-17 00:00:00 |      30296 |        1214 |  947426 |    46386 | True         |
| 113 | Brazil    | 2020-06-18 00:00:00 |      30840 |        1264 |  978266 |    47650 | True         |
| 114 | Brazil    | 2020-06-19 00:00:00 |      31181 |        1219 | 1009447 |    48869 | True         |
| 115 | Brazil    | 2020-06-20 00:00:00 |      30690 |        1169 | 1040137 |    50038 | True         |
| 116 | Brazil    | 2020-06-21 00:00:00 |      28312 |        1038 | 1068449 |    51076 | True         |
| 117 | Brazil    | 2020-06-22 00:00:00 |      28562 |        1102 | 1097011 |    52178 | True         |
| 118 | Brazil    | 2020-06-23 00:00:00 |      32166 |        1313 | 1129177 |    53491 | True         |
| 119 | Brazil    | 2020-06-24 00:00:00 |      33603 |        1314 | 1162780 |    54805 | True         |
| 120 | Brazil    | 2020-06-25 00:00:00 |      34147 |        1364 | 1196927 |    56169 | True         |

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
| 111 | Brazil         | 2020-06-16 00:00:00 |      28859 |        1213 |  917130 |    45172 | True         |
| 137 | Italy          | 2020-06-16 00:00:00 |       -699 |         -17 |  236591 |    34354 | True         |
| 137 | United Kingdom | 2020-06-16 00:00:00 |       1243 |         301 |  299973 |    42122 | True         |
| 136 | Spain          | 2020-06-16 00:00:00 |       1097 |         -65 |  245569 |    27071 | True         |
| 146 | US             | 2020-06-16 00:00:00 |      23660 |        1281 | 2137686 |   117408 | True         |
| 133 | Belgium        | 2020-06-16 00:00:00 |       -127 |           2 |   59973 |     9663 | True         |
| 144 | France         | 2020-06-16 00:00:00 |        207 |          38 |  197223 |    29477 | True         |

 **Para depois e amanhã** 
|     | country        | ds                  |   case_day |   death_day |   cases |   deaths | predicted?   |
|----:|:---------------|:--------------------|-----------:|------------:|--------:|---------:|:-------------|
| 112 | Brazil         | 2020-06-17 00:00:00 |      30296 |        1214 |  947426 |    46386 | True         |
| 138 | Italy          | 2020-06-17 00:00:00 |       -565 |         -29 |  236026 |    34325 | True         |
| 138 | United Kingdom | 2020-06-17 00:00:00 |       1144 |         270 |  301117 |    42392 | True         |
| 137 | Spain          | 2020-06-17 00:00:00 |       1578 |         -31 |  247147 |    27040 | True         |
| 147 | US             | 2020-06-17 00:00:00 |      24587 |        1345 | 2162273 |   118753 | True         |
| 134 | Belgium        | 2020-06-17 00:00:00 |        -38 |           9 |   59935 |     9672 | True         |
| 145 | France         | 2020-06-17 00:00:00 |       -231 |          39 |  196992 |    29516 | True         |