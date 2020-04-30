# **Predições**
Para experiência, estou fazendo predições simples sobre a quantidade de casos e mortes diárias. Como são séries temporais (*time-series*), estou usando [Facebook Prophet](https://facebook.github.io/prophet/docs/quick_start.html) que também é desenhado para este tipo de predição de uma maneira bem mais simples. Isso funciona muito bem na maioria das vezes; porém, algumas vezes há um grande salto entre os números que impactam no desempenho do modelo e leva um tempo (medições) para ser absorvido e compreendidos.

Essas predições foram feitas com os dados mundiais da pandemia Covid19 até **2020-04-29**.

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
| 59 | Brazil    | 2020-04-25 00:00:00 |       5281 |         353 |   59324 |     4057 | False        |
| 60 | Brazil    | 2020-04-26 00:00:00 |       3776 |         229 |   63100 |     4286 | False        |
| 61 | Brazil    | 2020-04-27 00:00:00 |       4346 |         317 |   67446 |     4603 | False        |
| 62 | Brazil    | 2020-04-28 00:00:00 |       5789 |         480 |   73235 |     5083 | False        |
| 63 | Brazil    | 2020-04-29 00:00:00 |       6450 |         430 |   79685 |     5513 | False        |
| 64 | Brazil    | 2020-04-30 00:00:00 |       4793 |         339 |   84478 |     5852 | True         |
| 65 | Brazil    | 2020-05-01 00:00:00 |       4909 |         332 |   89387 |     6184 | True         |
| 66 | Brazil    | 2020-05-02 00:00:00 |       5073 |         335 |   94460 |     6519 | True         |
| 67 | Brazil    | 2020-05-03 00:00:00 |       4872 |         313 |   99332 |     6832 | True         |
| 68 | Brazil    | 2020-05-04 00:00:00 |       4999 |         332 |  104331 |     7164 | True         |
| 69 | Brazil    | 2020-05-05 00:00:00 |       5506 |         374 |  109837 |     7538 | True         |
| 70 | Brazil    | 2020-05-06 00:00:00 |       5853 |         377 |  115690 |     7915 | True         |
| 71 | Brazil    | 2020-05-07 00:00:00 |       5844 |         401 |  121534 |     8316 | True         |
| 72 | Brazil    | 2020-05-08 00:00:00 |       5959 |         394 |  127493 |     8710 | True         |
| 73 | Brazil    | 2020-05-09 00:00:00 |       6124 |         396 |  133617 |     9106 | True         |

 #### As curvas acumuladas previstas para o Brasil
![](brazil_predictions.png)

 O Facebook Prophet gera automaticamente gráficos do comportamento sazonal dos dados, o que provê boas informações visuais. Aqui estão sobre as predições do Brasil:
### Casos
![](brazil_prophet_cases.png)

 ### Mortes
![](brazil_prophet_deaths.png)
#### Finalmente, as predições para os países selecionados para:
**Para amanhã**
|    | country        | ds                  |   case_day |   death_day |   cases |   deaths | predicted?   |
|---:|:---------------|:--------------------|-----------:|------------:|--------:|---------:|:-------------|
| 64 | Brazil         | 2020-04-30 00:00:00 |       4793 |         339 |   84478 |     5852 | True         |
| 90 | Italy          | 2020-04-30 00:00:00 |       4832 |         692 |  208423 |    28374 | True         |
| 90 | United Kingdom | 2020-04-30 00:00:00 |       5854 |        1037 |  172295 |    27203 | True         |
| 89 | Spain          | 2020-04-30 00:00:00 |       6801 |         695 |  243700 |    24970 | True         |
| 99 | US             | 2020-04-30 00:00:00 |      36737 |        2506 | 1076646 |    63473 | True         |
| 86 | Belgium        | 2020-04-30 00:00:00 |       1465 |         267 |   49324 |     7768 | True         |
| 97 | France         | 2020-04-30 00:00:00 |       4813 |         760 |  171356 |    24881 | True         |

 **Para depois e amanhã** 
|     | country        | ds                  |   case_day |   death_day |   cases |   deaths | predicted?   |
|----:|:---------------|:--------------------|-----------:|------------:|--------:|---------:|:-------------|
|  65 | Brazil         | 2020-05-01 00:00:00 |       4909 |         332 |   89387 |     6184 | True         |
|  91 | Italy          | 2020-05-01 00:00:00 |       5261 |         763 |  213684 |    29137 | True         |
|  91 | United Kingdom | 2020-05-01 00:00:00 |       6613 |        1087 |  178908 |    28290 | True         |
|  90 | Spain          | 2020-05-01 00:00:00 |       6889 |         697 |  250589 |    25667 | True         |
| 100 | US             | 2020-05-01 00:00:00 |      37573 |        2535 | 1114219 |    66008 | True         |
|  87 | Belgium        | 2020-05-01 00:00:00 |       1548 |         271 |   50872 |     8039 | True         |
|  98 | France         | 2020-05-01 00:00:00 |       4387 |         752 |  175743 |    25633 | True         |