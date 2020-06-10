# **Predições**
Para experiência, estou fazendo predições simples sobre a quantidade de casos e mortes diárias. Como são séries temporais (*time-series*), estou usando [Facebook Prophet](https://facebook.github.io/prophet/docs/quick_start.html) que também é desenhado para este tipo de predição de uma maneira bem mais simples. Isso funciona muito bem na maioria das vezes; porém, algumas vezes há um grande salto entre os números que impactam no desempenho do modelo e leva um tempo (medições) para ser absorvido e compreendidos.

Essas predições foram feitas com os dados mundiais da pandemia Covid19 até **2020-06-09**.

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
| 100 | Brazil    | 2020-06-05 00:00:00 |      30830 |        1005 |  645771 |    35026 | False        |
| 101 | Brazil    | 2020-06-06 00:00:00 |      27075 |         904 |  672846 |    35930 | False        |
| 102 | Brazil    | 2020-06-07 00:00:00 |      18912 |         525 |  691758 |    36455 | False        |
| 103 | Brazil    | 2020-06-08 00:00:00 |      15654 |         679 |  707412 |    37134 | False        |
| 104 | Brazil    | 2020-06-09 00:00:00 |      32091 |        1272 |  739503 |    38406 | False        |
| 105 | Brazil    | 2020-06-10 00:00:00 |      28156 |        1188 |  767659 |    39594 | True         |
| 106 | Brazil    | 2020-06-11 00:00:00 |      28955 |        1247 |  796614 |    40841 | True         |
| 107 | Brazil    | 2020-06-12 00:00:00 |      29662 |        1223 |  826276 |    42064 | True         |
| 108 | Brazil    | 2020-06-13 00:00:00 |      29472 |        1174 |  855748 |    43238 | True         |
| 109 | Brazil    | 2020-06-14 00:00:00 |      27297 |        1054 |  883045 |    44292 | True         |
| 110 | Brazil    | 2020-06-15 00:00:00 |      27375 |        1124 |  910420 |    45416 | True         |
| 111 | Brazil    | 2020-06-16 00:00:00 |      30719 |        1313 |  941139 |    46729 | True         |
| 112 | Brazil    | 2020-06-17 00:00:00 |      31902 |        1308 |  973041 |    48037 | True         |
| 113 | Brazil    | 2020-06-18 00:00:00 |      32700 |        1367 | 1005741 |    49404 | True         |
| 114 | Brazil    | 2020-06-19 00:00:00 |      33407 |        1343 | 1039148 |    50747 | True         |

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
| 105 | Brazil         | 2020-06-10 00:00:00 |      28156 |        1188 |  767659 |    39594 | True         |
| 131 | Italy          | 2020-06-10 00:00:00 |       -391 |           2 |  235170 |    34045 | True         |
| 131 | United Kingdom | 2020-06-10 00:00:00 |       1761 |         382 |  292757 |    41350 | True         |
| 130 | Spain          | 2020-06-10 00:00:00 |       1992 |         -13 |  244321 |    27123 | True         |
| 140 | US             | 2020-06-10 00:00:00 |      25194 |        1778 | 1998424 |   113472 | True         |
| 127 | Belgium        | 2020-06-10 00:00:00 |         -3 |          24 |   59434 |     9643 | True         |
| 138 | France         | 2020-06-10 00:00:00 |       -114 |          78 |  194120 |    29377 | True         |

 **Para depois e amanhã** 
|     | country        | ds                  |   case_day |   death_day |   cases |   deaths | predicted?   |
|----:|:---------------|:--------------------|-----------:|------------:|--------:|---------:|:-------------|
| 106 | Brazil         | 2020-06-11 00:00:00 |      28955 |        1247 |  796614 |    40841 | True         |
| 132 | Italy          | 2020-06-11 00:00:00 |       -289 |         -10 |  234881 |    34035 | True         |
| 132 | United Kingdom | 2020-06-11 00:00:00 |       1855 |         351 |  294612 |    41701 | True         |
| 131 | Spain          | 2020-06-11 00:00:00 |       2055 |         -42 |  246376 |    27081 | True         |
| 141 | US             | 2020-06-11 00:00:00 |      27041 |        1707 | 2025465 |   115179 | True         |
| 128 | Belgium        | 2020-06-11 00:00:00 |         18 |          14 |   59452 |     9657 | True         |
| 139 | France         | 2020-06-11 00:00:00 |        440 |          89 |  194560 |    29466 | True         |