# **Predições**
Para experiência, estou fazendo predições simples sobre a quantidade de casos e mortes diárias. Como são séries temporais (*time-series*), estou usando [Facebook Prophet](https://facebook.github.io/prophet/docs/quick_start.html) que também é desenhado para este tipo de predição de uma maneira bem mais simples. Isso funciona muito bem na maioria das vezes; porém, algumas vezes há um grande salto entre os números que impactam no desempenho do modelo e leva um tempo (medições) para ser absorvido e compreendidos.

Essas predições foram feitas com os dados mundiais da pandemia Covid19 até **2020-06-14**.

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
| 105 | Brazil    | 2020-06-10 00:00:00 |      32913 |        1274 |  772416 |    39680 | False        |
| 106 | Brazil    | 2020-06-11 00:00:00 |      30412 |        1239 |  802828 |    40919 | False        |
| 107 | Brazil    | 2020-06-12 00:00:00 |      25982 |         909 |  828810 |    41828 | False        |
| 108 | Brazil    | 2020-06-13 00:00:00 |      21704 |         892 |  850514 |    42720 | False        |
| 109 | Brazil    | 2020-06-14 00:00:00 |      17110 |         612 |  867624 |    43332 | False        |
| 110 | Brazil    | 2020-06-15 00:00:00 |      25852 |        1056 |  893476 |    44388 | True         |
| 111 | Brazil    | 2020-06-16 00:00:00 |      29162 |        1242 |  922638 |    45630 | True         |
| 112 | Brazil    | 2020-06-17 00:00:00 |      30597 |        1243 |  953235 |    46873 | True         |
| 113 | Brazil    | 2020-06-18 00:00:00 |      31149 |        1294 |  984384 |    48167 | True         |
| 114 | Brazil    | 2020-06-19 00:00:00 |      31497 |        1250 | 1015881 |    49417 | True         |
| 115 | Brazil    | 2020-06-20 00:00:00 |      31012 |        1201 | 1046893 |    50618 | True         |
| 116 | Brazil    | 2020-06-21 00:00:00 |      28639 |        1070 | 1075532 |    51688 | True         |
| 117 | Brazil    | 2020-06-22 00:00:00 |      29217 |        1162 | 1104749 |    52850 | True         |
| 118 | Brazil    | 2020-06-23 00:00:00 |      32526 |        1348 | 1137275 |    54198 | True         |
| 119 | Brazil    | 2020-06-24 00:00:00 |      33962 |        1349 | 1171237 |    55547 | True         |

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
| 110 | Brazil         | 2020-06-15 00:00:00 |      25852 |        1056 |  893476 |    44388 | True         |
| 136 | Italy          | 2020-06-15 00:00:00 |       -759 |         -30 |  236230 |    34315 | True         |
| 136 | United Kingdom | 2020-06-15 00:00:00 |       1001 |         185 |  298758 |    41968 | True         |
| 135 | Spain          | 2020-06-15 00:00:00 |       -909 |        -176 |  243382 |    26960 | True         |
| 145 | US             | 2020-06-15 00:00:00 |      22568 |        1172 | 2116626 |   116904 | True         |
| 132 | Belgium        | 2020-06-15 00:00:00 |       -115 |         -19 |   59914 |     9636 | True         |
| 143 | France         | 2020-06-15 00:00:00 |         -8 |          18 |  196856 |    29428 | True         |

 **Para depois e amanhã** 
|     | country        | ds                  |   case_day |   death_day |   cases |   deaths | predicted?   |
|----:|:---------------|:--------------------|-----------:|------------:|--------:|---------:|:-------------|
| 111 | Brazil         | 2020-06-16 00:00:00 |      29162 |        1242 |  922638 |    45630 | True         |
| 137 | Italy          | 2020-06-16 00:00:00 |       -760 |         -16 |  235470 |    34299 | True         |
| 137 | United Kingdom | 2020-06-16 00:00:00 |       1102 |         346 |  299860 |    42314 | True         |
| 136 | Spain          | 2020-06-16 00:00:00 |       -535 |         -86 |  242847 |    26874 | True         |
| 146 | US             | 2020-06-16 00:00:00 |      23146 |        1474 | 2139772 |   118378 | True         |
| 133 | Belgium        | 2020-06-16 00:00:00 |       -169 |          -1 |   59745 |     9635 | True         |
| 144 | France         | 2020-06-16 00:00:00 |         54 |          41 |  196910 |    29469 | True         |