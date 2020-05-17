# **Predições**
Para experiência, estou fazendo predições simples sobre a quantidade de casos e mortes diárias. Como são séries temporais (*time-series*), estou usando [Facebook Prophet](https://facebook.github.io/prophet/docs/quick_start.html) que também é desenhado para este tipo de predição de uma maneira bem mais simples. Isso funciona muito bem na maioria das vezes; porém, algumas vezes há um grande salto entre os números que impactam no desempenho do modelo e leva um tempo (medições) para ser absorvido e compreendidos.

Essas predições foram feitas com os dados mundiais da pandemia Covid19 até **2020-05-16**.

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
| 76 | Brazil    | 2020-05-12 00:00:00 |       8620 |         808 |  178214 |    12461 | False        |
| 77 | Brazil    | 2020-05-13 00:00:00 |      11923 |         779 |  190137 |    13240 | False        |
| 78 | Brazil    | 2020-05-14 00:00:00 |      13028 |         759 |  203165 |    13999 | False        |
| 79 | Brazil    | 2020-05-15 00:00:00 |      17126 |         963 |  220291 |    14962 | False        |
| 80 | Brazil    | 2020-05-16 00:00:00 |      13220 |         700 |  233511 |    15662 | False        |
| 81 | Brazil    | 2020-05-17 00:00:00 |      11123 |         708 |  244634 |    16370 | True         |
| 82 | Brazil    | 2020-05-18 00:00:00 |      11571 |         739 |  256205 |    17109 | True         |
| 83 | Brazil    | 2020-05-19 00:00:00 |      12280 |         830 |  268485 |    17939 | True         |
| 84 | Brazil    | 2020-05-20 00:00:00 |      13376 |         844 |  281861 |    18783 | True         |
| 85 | Brazil    | 2020-05-21 00:00:00 |      13637 |         879 |  295498 |    19662 | True         |
| 86 | Brazil    | 2020-05-22 00:00:00 |      14140 |         909 |  309638 |    20571 | True         |
| 87 | Brazil    | 2020-05-23 00:00:00 |      13888 |         876 |  323526 |    21447 | True         |
| 88 | Brazil    | 2020-05-24 00:00:00 |      13460 |         848 |  336986 |    22295 | True         |
| 89 | Brazil    | 2020-05-25 00:00:00 |      13908 |         880 |  350894 |    23175 | True         |
| 90 | Brazil    | 2020-05-26 00:00:00 |      14617 |         971 |  365511 |    24146 | True         |

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
|  81 | Brazil         | 2020-05-17 00:00:00 |      11123 |         708 |  244634 |    16370 | True         |
| 107 | Italy          | 2020-05-17 00:00:00 |       3470 |         500 |  228230 |    32263 | True         |
| 107 | United Kingdom | 2020-05-17 00:00:00 |       5713 |         683 |  247174 |    35229 | True         |
| 106 | Spain          | 2020-05-17 00:00:00 |       3813 |         463 |  244536 |    28026 | True         |
| 116 | US             | 2020-05-17 00:00:00 |      31780 |        1918 | 1499600 |    90672 | True         |
| 103 | Belgium        | 2020-05-17 00:00:00 |        753 |         184 |   55742 |     9189 | True         |
| 114 | France         | 2020-05-17 00:00:00 |       3194 |         455 |  182939 |    27987 | True         |

 **Para depois e amanhã** 
|     | country        | ds                  |   case_day |   death_day |   cases |   deaths | predicted?   |
|----:|:---------------|:--------------------|-----------:|------------:|--------:|---------:|:-------------|
|  82 | Brazil         | 2020-05-18 00:00:00 |      11571 |         739 |  256205 |    17109 | True         |
| 108 | Italy          | 2020-05-18 00:00:00 |       3100 |         522 |  231330 |    32785 | True         |
| 108 | United Kingdom | 2020-05-18 00:00:00 |       5452 |         689 |  252626 |    35918 | True         |
| 107 | Spain          | 2020-05-18 00:00:00 |       3854 |         473 |  248390 |    28499 | True         |
| 117 | US             | 2020-05-18 00:00:00 |      31285 |        2001 | 1530885 |    92673 | True         |
| 104 | Belgium        | 2020-05-18 00:00:00 |        602 |         177 |   56344 |     9366 | True         |
| 115 | France         | 2020-05-18 00:00:00 |       2277 |         536 |  185216 |    28523 | True         |