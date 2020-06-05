# **Predições**
Para experiência, estou fazendo predições simples sobre a quantidade de casos e mortes diárias. Como são séries temporais (*time-series*), estou usando [Facebook Prophet](https://facebook.github.io/prophet/docs/quick_start.html) que também é desenhado para este tipo de predição de uma maneira bem mais simples. Isso funciona muito bem na maioria das vezes; porém, algumas vezes há um grande salto entre os números que impactam no desempenho do modelo e leva um tempo (medições) para ser absorvido e compreendidos.

Essas predições foram feitas com os dados mundiais da pandemia Covid19 até **2020-06-04**.

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
|  95 | Brazil    | 2020-05-31 00:00:00 |      16409 |         480 |  514849 |    29314 | False        |
|  96 | Brazil    | 2020-06-01 00:00:00 |      11598 |         623 |  526447 |    29937 | False        |
|  97 | Brazil    | 2020-06-02 00:00:00 |      28936 |        1262 |  555383 |    31199 | False        |
|  98 | Brazil    | 2020-06-03 00:00:00 |      28633 |        1349 |  584016 |    32548 | False        |
|  99 | Brazil    | 2020-06-04 00:00:00 |      30925 |        1473 |  614941 |    34021 | False        |
| 100 | Brazil    | 2020-06-05 00:00:00 |      26273 |        1199 |  641214 |    35220 | True         |
| 101 | Brazil    | 2020-06-06 00:00:00 |      26367 |        1155 |  667581 |    36375 | True         |
| 102 | Brazil    | 2020-06-07 00:00:00 |      24647 |        1056 |  692228 |    37431 | True         |
| 103 | Brazil    | 2020-06-08 00:00:00 |      24995 |        1122 |  717223 |    38553 | True         |
| 104 | Brazil    | 2020-06-09 00:00:00 |      27428 |        1283 |  744651 |    39836 | True         |
| 105 | Brazil    | 2020-06-10 00:00:00 |      28990 |        1287 |  773641 |    41123 | True         |
| 106 | Brazil    | 2020-06-11 00:00:00 |      29817 |        1347 |  803458 |    42470 | True         |
| 107 | Brazil    | 2020-06-12 00:00:00 |      30251 |        1338 |  833709 |    43808 | True         |
| 108 | Brazil    | 2020-06-13 00:00:00 |      30345 |        1294 |  864054 |    45102 | True         |
| 109 | Brazil    | 2020-06-14 00:00:00 |      28626 |        1195 |  892680 |    46297 | True         |

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
| 100 | Brazil         | 2020-06-05 00:00:00 |      26273 |        1199 |  641214 |    35220 | True         |
| 126 | Italy          | 2020-06-05 00:00:00 |          3 |          70 |  234016 |    33759 | True         |
| 126 | United Kingdom | 2020-06-05 00:00:00 |       3162 |         621 |  286656 |    40608 | True         |
| 125 | Spain          | 2020-06-05 00:00:00 |       2134 |          11 |  243157 |    27144 | True         |
| 135 | US             | 2020-06-05 00:00:00 |      32673 |        1885 | 1905333 |   110096 | True         |
| 122 | Belgium        | 2020-06-05 00:00:00 |        139 |          53 |   58906 |     9601 | True         |
| 133 | France         | 2020-06-05 00:00:00 |        156 |         157 |  192436 |    29225 | True         |

 **Para depois e amanhã** 
|     | country        | ds                  |   case_day |   death_day |   cases |   deaths | predicted?   |
|----:|:---------------|:--------------------|-----------:|------------:|--------:|---------:|:-------------|
| 101 | Brazil         | 2020-06-06 00:00:00 |      26367 |        1155 |  667581 |    36375 | True         |
| 127 | Italy          | 2020-06-06 00:00:00 |         42 |          60 |  234058 |    33819 | True         |
| 127 | United Kingdom | 2020-06-06 00:00:00 |       2618 |         579 |  289274 |    41187 | True         |
| 126 | Spain          | 2020-06-06 00:00:00 |       1758 |         -41 |  244915 |    27103 | True         |
| 136 | US             | 2020-06-06 00:00:00 |      32058 |        1842 | 1937391 |   111938 | True         |
| 123 | Belgium        | 2020-06-06 00:00:00 |        107 |          36 |   59013 |     9637 | True         |
| 134 | France         | 2020-06-06 00:00:00 |        -52 |          97 |  192384 |    29322 | True         |