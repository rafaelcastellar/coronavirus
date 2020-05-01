# **Predições**
Para experiência, estou fazendo predições simples sobre a quantidade de casos e mortes diárias. Como são séries temporais (*time-series*), estou usando [Facebook Prophet](https://facebook.github.io/prophet/docs/quick_start.html) que também é desenhado para este tipo de predição de uma maneira bem mais simples. Isso funciona muito bem na maioria das vezes; porém, algumas vezes há um grande salto entre os números que impactam no desempenho do modelo e leva um tempo (medições) para ser absorvido e compreendidos.

Essas predições foram feitas com os dados mundiais da pandemia Covid19 até **2020-04-30**.

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
| 60 | Brazil    | 2020-04-26 00:00:00 |       3776 |         229 |   63100 |     4286 | False        |
| 61 | Brazil    | 2020-04-27 00:00:00 |       4346 |         317 |   67446 |     4603 | False        |
| 62 | Brazil    | 2020-04-28 00:00:00 |       5789 |         480 |   73235 |     5083 | False        |
| 63 | Brazil    | 2020-04-29 00:00:00 |       6450 |         430 |   79685 |     5513 | False        |
| 64 | Brazil    | 2020-04-30 00:00:00 |       7502 |         493 |   87187 |     6006 | False        |
| 65 | Brazil    | 2020-05-01 00:00:00 |       5411 |         361 |   92598 |     6367 | True         |
| 66 | Brazil    | 2020-05-02 00:00:00 |       5611 |         365 |   98209 |     6732 | True         |
| 67 | Brazil    | 2020-05-03 00:00:00 |       5431 |         345 |  103640 |     7077 | True         |
| 68 | Brazil    | 2020-05-04 00:00:00 |       5586 |         365 |  109226 |     7442 | True         |
| 69 | Brazil    | 2020-05-05 00:00:00 |       6122 |         409 |  115348 |     7851 | True         |
| 70 | Brazil    | 2020-05-06 00:00:00 |       6503 |         414 |  121851 |     8265 | True         |
| 71 | Brazil    | 2020-05-07 00:00:00 |       6793 |         454 |  128644 |     8719 | True         |
| 72 | Brazil    | 2020-05-08 00:00:00 |       6713 |         436 |  135357 |     9155 | True         |
| 73 | Brazil    | 2020-05-09 00:00:00 |       6913 |         440 |  142270 |     9595 | True         |
| 74 | Brazil    | 2020-05-10 00:00:00 |       6733 |         419 |  149003 |    10014 | True         |

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
|  65 | Brazil         | 2020-05-01 00:00:00 |       5411 |         361 |   92598 |     6367 | True         |
|  91 | Italy          | 2020-05-01 00:00:00 |       5168 |         750 |  210631 |    28717 | True         |
|  91 | United Kingdom | 2020-05-01 00:00:00 |       6636 |         957 |  179117 |    27799 | True         |
|  90 | Spain          | 2020-05-01 00:00:00 |       4552 |         683 |  217987 |    25226 | True         |
| 100 | US             | 2020-05-01 00:00:00 |      35563 |        2461 | 1104987 |    65457 | True         |
|  87 | Belgium        | 2020-05-01 00:00:00 |       1520 |         266 |   50039 |     7860 | True         |
|  98 | France         | 2020-05-01 00:00:00 |       4253 |         738 |  171552 |    25148 | True         |

 **Para depois e amanhã** 
|     | country        | ds                  |   case_day |   death_day |   cases |   deaths | predicted?   |
|----:|:---------------|:--------------------|-----------:|------------:|--------:|---------:|:-------------|
|  66 | Brazil         | 2020-05-02 00:00:00 |       5611 |         365 |   98209 |     6732 | True         |
|  92 | Italy          | 2020-05-02 00:00:00 |       5147 |         729 |  215778 |    29446 | True         |
|  92 | United Kingdom | 2020-05-02 00:00:00 |       6256 |         943 |  185373 |    28742 | True         |
|  91 | Spain          | 2020-05-02 00:00:00 |       5229 |         638 |  223216 |    25864 | True         |
| 101 | US             | 2020-05-02 00:00:00 |      35513 |        2510 | 1140500 |    67967 | True         |
|  88 | Belgium        | 2020-05-02 00:00:00 |       1515 |         256 |   51554 |     8116 | True         |
|  99 | France         | 2020-05-02 00:00:00 |       3972 |         691 |  175524 |    25839 | True         |