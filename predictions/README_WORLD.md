# **Predições**
Para experiência, estou fazendo predições simples sobre a quantidade de casos e mortes diárias. Como são séries temporais (*time-series*), estou usando [Facebook Prophet](https://facebook.github.io/prophet/docs/quick_start.html) que também é desenhado para este tipo de predição de uma maneira bem mais simples. Isso funciona muito bem na maioria das vezes; porém, algumas vezes há um grande salto entre os números que impactam no desempenho do modelo e leva um tempo (medições) para ser absorvido e compreendidos.

Essas predições foram feitas com os dados mundiais da pandemia Covid19 até **2020-06-03**.

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
|  94 | Brazil    | 2020-05-30 00:00:00 |      33274 |         956 |  498440 |    28834 | False        |
|  95 | Brazil    | 2020-05-31 00:00:00 |      16409 |         480 |  514849 |    29314 | False        |
|  96 | Brazil    | 2020-06-01 00:00:00 |      11598 |         623 |  526447 |    29937 | False        |
|  97 | Brazil    | 2020-06-02 00:00:00 |      28936 |        1262 |  555383 |    31199 | False        |
|  98 | Brazil    | 2020-06-03 00:00:00 |      28633 |        1349 |  584016 |    32548 | False        |
|  99 | Brazil    | 2020-06-04 00:00:00 |      24514 |        1162 |  608530 |    33710 | True         |
| 100 | Brazil    | 2020-06-05 00:00:00 |      25269 |        1171 |  633799 |    34881 | True         |
| 101 | Brazil    | 2020-06-06 00:00:00 |      25325 |        1127 |  659124 |    36008 | True         |
| 102 | Brazil    | 2020-06-07 00:00:00 |      23557 |        1028 |  682681 |    37036 | True         |
| 103 | Brazil    | 2020-06-08 00:00:00 |      23855 |        1093 |  706536 |    38129 | True         |
| 104 | Brazil    | 2020-06-09 00:00:00 |      26246 |        1254 |  732782 |    39383 | True         |
| 105 | Brazil    | 2020-06-10 00:00:00 |      27744 |        1255 |  760526 |    40638 | True         |
| 106 | Brazil    | 2020-06-11 00:00:00 |      28105 |        1294 |  788631 |    41932 | True         |
| 107 | Brazil    | 2020-06-12 00:00:00 |      28860 |        1304 |  817491 |    43236 | True         |
| 108 | Brazil    | 2020-06-13 00:00:00 |      28916 |        1259 |  846407 |    44495 | True         |

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
|  99 | Brazil         | 2020-06-04 00:00:00 |      24514 |        1162 |  608530 |    33710 | True         |
| 125 | Italy          | 2020-06-04 00:00:00 |         -7 |          25 |  233829 |    33626 | True         |
| 125 | United Kingdom | 2020-06-04 00:00:00 |       2670 |         684 |  284355 |    40495 | True         |
| 124 | Spain          | 2020-06-04 00:00:00 |       2499 |           8 |  243188 |    27136 | True         |
| 134 | US             | 2020-06-04 00:00:00 |      31756 |        1967 | 1883276 |   109142 | True         |
| 121 | Belgium        | 2020-06-04 00:00:00 |        150 |          50 |   58835 |     9572 | True         |
| 132 | France         | 2020-06-04 00:00:00 |        964 |         186 |  194142 |    29210 | True         |

 **Para depois e amanhã** 
|     | country        | ds                  |   case_day |   death_day |   cases |   deaths | predicted?   |
|----:|:---------------|:--------------------|-----------:|------------:|--------:|---------:|:-------------|
| 100 | Brazil         | 2020-06-05 00:00:00 |      25269 |        1171 |  633799 |    34881 | True         |
| 126 | Italy          | 2020-06-05 00:00:00 |        -51 |          45 |  233778 |    33671 | True         |
| 126 | United Kingdom | 2020-06-05 00:00:00 |       3153 |         707 |  287508 |    41202 | True         |
| 125 | Spain          | 2020-06-05 00:00:00 |       2254 |          17 |  245442 |    27153 | True         |
| 135 | US             | 2020-06-05 00:00:00 |      32216 |        1921 | 1915492 |   111063 | True         |
| 122 | Belgium        | 2020-06-05 00:00:00 |        177 |          53 |   59012 |     9625 | True         |
| 133 | France         | 2020-06-05 00:00:00 |        422 |         153 |  194564 |    29363 | True         |