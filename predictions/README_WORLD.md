# **Predições**
Para experiência, estou fazendo predições simples sobre a quantidade de casos e mortes diárias. Como são séries temporais (*time-series*), estou usando [Facebook Prophet](https://facebook.github.io/prophet/docs/quick_start.html) que também é desenhado para este tipo de predição de uma maneira bem mais simples. Isso funciona muito bem na maioria das vezes; porém, algumas vezes há um grande salto entre os números que impactam no desempenho do modelo e leva um tempo (medições) para ser absorvido e compreendidos.

Essas predições foram feitas com os dados mundiais da pandemia Covid19 até **2020-05-26**.

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
|  86 | Brazil    | 2020-05-22 00:00:00 |      20803 |        1001 |  330890 |    21048 | False        |
|  87 | Brazil    | 2020-05-23 00:00:00 |      16508 |         965 |  347398 |    22013 | False        |
|  88 | Brazil    | 2020-05-24 00:00:00 |      15813 |         653 |  363211 |    22666 | False        |
|  89 | Brazil    | 2020-05-25 00:00:00 |      11687 |         807 |  374898 |    23473 | False        |
|  90 | Brazil    | 2020-05-26 00:00:00 |      16324 |        1039 |  391222 |    24512 | False        |
|  91 | Brazil    | 2020-05-27 00:00:00 |      18001 |         990 |  409223 |    25502 | True         |
|  92 | Brazil    | 2020-05-28 00:00:00 |      18209 |        1045 |  427432 |    26547 | True         |
|  93 | Brazil    | 2020-05-29 00:00:00 |      18889 |        1058 |  446321 |    27605 | True         |
|  94 | Brazil    | 2020-05-30 00:00:00 |      18365 |        1024 |  464686 |    28629 | True         |
|  95 | Brazil    | 2020-05-31 00:00:00 |      17683 |         955 |  482369 |    29584 | True         |
|  96 | Brazil    | 2020-06-01 00:00:00 |      18306 |        1014 |  500675 |    30598 | True         |
|  97 | Brazil    | 2020-06-02 00:00:00 |      19479 |        1140 |  520154 |    31738 | True         |
|  98 | Brazil    | 2020-06-03 00:00:00 |      20830 |        1129 |  540984 |    32867 | True         |
|  99 | Brazil    | 2020-06-04 00:00:00 |      21038 |        1183 |  562022 |    34050 | True         |
| 100 | Brazil    | 2020-06-05 00:00:00 |      21718 |        1196 |  583740 |    35246 | True         |

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
|  91 | Brazil         | 2020-05-27 00:00:00 |      18001 |         990 |  409223 |    25502 | True         |
| 117 | Italy          | 2020-05-27 00:00:00 |        269 |         135 |  230824 |    33090 | True         |
| 117 | United Kingdom | 2020-05-27 00:00:00 |       3893 |         728 |  270907 |    37858 | True         |
| 116 | Spain          | 2020-05-27 00:00:00 |       2985 |         138 |  239607 |    27255 | True         |
| 126 | US             | 2020-05-27 00:00:00 |      32039 |        2118 | 1712952 |   101031 | True         |
| 113 | Belgium        | 2020-05-27 00:00:00 |        299 |         149 |   57754 |     9483 | True         |
| 124 | France         | 2020-05-27 00:00:00 |       -155 |         466 |  182862 |    28999 | True         |

 **Para depois e amanhã** 
|     | country        | ds                  |   case_day |   death_day |   cases |   deaths | predicted?   |
|----:|:---------------|:--------------------|-----------:|------------:|--------:|---------:|:-------------|
|  92 | Brazil         | 2020-05-28 00:00:00 |      18209 |        1045 |  427432 |    26547 | True         |
| 118 | Italy          | 2020-05-28 00:00:00 |        383 |         123 |  231207 |    33213 | True         |
| 118 | United Kingdom | 2020-05-28 00:00:00 |       4055 |         714 |  274962 |    38572 | True         |
| 117 | Spain          | 2020-05-28 00:00:00 |       2960 |         105 |  242567 |    27360 | True         |
| 127 | US             | 2020-05-28 00:00:00 |      33974 |        2059 | 1746926 |   103090 | True         |
| 114 | Belgium        | 2020-05-28 00:00:00 |        319 |         140 |   58073 |     9623 | True         |
| 125 | France         | 2020-05-28 00:00:00 |        547 |         490 |  183409 |    29489 | True         |