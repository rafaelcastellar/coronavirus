# **Predições**
Para experiência, estou fazendo predições simples sobre a quantidade de casos e mortes diárias. Como são séries temporais (*time-series*), estou usando [Facebook Prophet](https://facebook.github.io/prophet/docs/quick_start.html) que também é desenhado para este tipo de predição de uma maneira bem mais simples. Isso funciona muito bem na maioria das vezes; porém, algumas vezes há um grande salto entre os números que impactam no desempenho do modelo e leva um tempo (medições) para ser absorvido e compreendidos.

Essas predições foram feitas com os dados mundiais da pandemia Covid19 até **2020-05-06**.

Como há muitos paises para terem seus dados submetidos ao modelo de predição de uma só vez, selecionei alguns mais o Brasil:
['Brazil', 'Italy', 'United Kingdom', 'Spain', 'US', 'Belgium', 'France'].
***Dica**: você mesmo pode definir no notebook *[prediction.ipynb](../prediction.ipynb)* quais países você prefere fazer a predição.*


## A predição
As predições estão sendo realizadas sobre os dados diários de casos e de mortes. Em seguida, os dados previstos são acumulados para que tenhamos a projeção acumulada. Estão sendo previstos os próximos 10 dias.
Ao ffim, é gerado o arquivo CSV contendo todas as previsões.

#### Os últimos 5 dias da pandemia no Brasil e os próximos 10 dias previstos
*predicted? = True* significa que são dados de predição; *=False* significa que são dados reais.
|    | country   | ds                  |   case_day |   death_day |   cases |   deaths | predicted?   |
|---:|:----------|:--------------------|-----------:|------------:|--------:|---------:|:-------------|
| 66 | Brazil    | 2020-05-02 00:00:00 |       4898 |         349 |   97100 |     6761 | False        |
| 67 | Brazil    | 2020-05-03 00:00:00 |       4726 |         290 |  101826 |     7051 | False        |
| 68 | Brazil    | 2020-05-04 00:00:00 |       6794 |         316 |  108620 |     7367 | False        |
| 69 | Brazil    | 2020-05-05 00:00:00 |       6835 |         571 |  115455 |     7938 | False        |
| 70 | Brazil    | 2020-05-06 00:00:00 |      11156 |         650 |  126611 |     8588 | False        |
| 71 | Brazil    | 2020-05-07 00:00:00 |       7383 |         490 |  133994 |     9078 | True         |
| 72 | Brazil    | 2020-05-08 00:00:00 |       7289 |         478 |  141283 |     9556 | True         |
| 73 | Brazil    | 2020-05-09 00:00:00 |       7483 |         476 |  148766 |    10032 | True         |
| 74 | Brazil    | 2020-05-10 00:00:00 |       7338 |         453 |  156104 |    10485 | True         |
| 75 | Brazil    | 2020-05-11 00:00:00 |       7710 |         475 |  163814 |    10960 | True         |
| 76 | Brazil    | 2020-05-12 00:00:00 |       8222 |         542 |  172036 |    11502 | True         |
| 77 | Brazil    | 2020-05-13 00:00:00 |       8991 |         554 |  181027 |    12056 | True         |
| 78 | Brazil    | 2020-05-14 00:00:00 |       8932 |         577 |  189959 |    12633 | True         |
| 79 | Brazil    | 2020-05-15 00:00:00 |       8838 |         564 |  198797 |    13197 | True         |
| 80 | Brazil    | 2020-05-16 00:00:00 |       9031 |         563 |  207828 |    13760 | True         |

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
|  71 | Brazil         | 2020-05-07 00:00:00 |       7383 |         490 |  133994 |     9078 | True         |
|  97 | Italy          | 2020-05-07 00:00:00 |       2511 |         630 |  216968 |    30314 | True         |
|  97 | United Kingdom | 2020-05-07 00:00:00 |       6088 |         880 |  208447 |    31030 | True         |
|  96 | Spain          | 2020-05-07 00:00:00 |       5173 |         628 |  225498 |    26485 | True         |
| 106 | US             | 2020-05-07 00:00:00 |      35032 |        2199 | 1263635 |    75630 | True         |
|  93 | Belgium        | 2020-05-07 00:00:00 |       1305 |         249 |   52086 |     8588 | True         |
| 104 | France         | 2020-05-07 00:00:00 |       4047 |         691 |  178271 |    26503 | True         |

 **Para depois e amanhã** 
|     | country        | ds                  |   case_day |   death_day |   cases |   deaths | predicted?   |
|----:|:---------------|:--------------------|-----------:|------------:|--------:|---------:|:-------------|
|  72 | Brazil         | 2020-05-08 00:00:00 |       7289 |         478 |  141283 |     9556 | True         |
|  98 | Italy          | 2020-05-08 00:00:00 |       2910 |         691 |  219878 |    31005 | True         |
|  98 | United Kingdom | 2020-05-08 00:00:00 |       6804 |         927 |  215251 |    31957 | True         |
|  97 | Spain          | 2020-05-08 00:00:00 |       3923 |         608 |  229421 |    27093 | True         |
| 107 | US             | 2020-05-08 00:00:00 |      35983 |        2202 | 1299618 |    77832 | True         |
|  94 | Belgium        | 2020-05-08 00:00:00 |       1371 |         254 |   53457 |     8842 | True         |
| 105 | France         | 2020-05-08 00:00:00 |       3558 |         675 |  181829 |    27178 | True         |