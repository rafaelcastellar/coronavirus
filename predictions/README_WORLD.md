# **Predições**
Para experiência, estou fazendo predições simples sobre a quantidade de casos e mortes diárias. Como são séries temporais (*time-series*), estou usando [Facebook Prophet](https://facebook.github.io/prophet/docs/quick_start.html) que também é desenhado para este tipo de predição de uma maneira bem mais simples. Isso funciona muito bem na maioria das vezes; porém, algumas vezes há um grande salto entre os números que impactam no desempenho do modelo e leva um tempo (medições) para ser absorvido e compreendidos.

Essas predições foram feitas com os dados mundiais da pandemia Covid19 até **2020-04-17**.

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
| 47 | Brazil    | 2020-04-13 00:00:00 |       1238 |         105 |   23430 |     1328 | False        |
| 48 | Brazil    | 2020-04-14 00:00:00 |       1832 |         204 |   25262 |     1532 | False        |
| 49 | Brazil    | 2020-04-15 00:00:00 |       3058 |         204 |   28320 |     1736 | False        |
| 50 | Brazil    | 2020-04-16 00:00:00 |       2105 |         188 |   30425 |     1924 | False        |
| 51 | Brazil    | 2020-04-17 00:00:00 |       3257 |         217 |   33682 |     2141 | False        |
| 52 | Brazil    | 2020-04-18 00:00:00 |       2012 |         117 |   35694 |     2258 | True         |
| 53 | Brazil    | 2020-04-19 00:00:00 |       2035 |         117 |   37729 |     2375 | True         |
| 54 | Brazil    | 2020-04-20 00:00:00 |       2038 |         123 |   39767 |     2498 | True         |
| 55 | Brazil    | 2020-04-21 00:00:00 |       2381 |         146 |   42148 |     2644 | True         |
| 56 | Brazil    | 2020-04-22 00:00:00 |       2612 |         152 |   44760 |     2796 | True         |
| 57 | Brazil    | 2020-04-23 00:00:00 |       2537 |         157 |   47297 |     2953 | True         |
| 58 | Brazil    | 2020-04-24 00:00:00 |       2631 |         151 |   49928 |     3104 | True         |
| 59 | Brazil    | 2020-04-25 00:00:00 |       2473 |         140 |   52401 |     3244 | True         |
| 60 | Brazil    | 2020-04-26 00:00:00 |       2496 |         140 |   54897 |     3384 | True         |
| 61 | Brazil    | 2020-04-27 00:00:00 |       2499 |         146 |   57396 |     3530 | True         |

 #### As curvas acumuladas previstas para o Brasil
![](brazil_predictions.png)

 O Facebook Prophet gera automaticamente gráficos do comportamento sazonal dos dados, o que provê boas informações visuais. Aqui estão sobre as predições do Brasil:
### Casos
![](brazil_prophet_cases.png)

 ### Mortes
![](brazil_prophet_deaths.png)
#### Finalmente, as predições para os países selecionados:
**Para amanhã**
|    | country        | ds                  |   case_day |   death_day |   cases |   deaths | predicted?   |
|---:|:---------------|:--------------------|-----------:|------------:|--------:|---------:|:-------------|
| 52 | Brazil         | 2020-04-18 00:00:00 |       2012 |         117 |   35694 |     2258 | True         |
| 78 | Italy          | 2020-04-18 00:00:00 |       5845 |         795 |  178279 |    23540 | True         |
| 78 | United Kingdom | 2020-04-18 00:00:00 |       6106 |         996 |  115875 |    15603 | True         |
| 77 | Spain          | 2020-04-18 00:00:00 |       6872 |         746 |  197711 |    20748 | True         |
| 87 | US             | 2020-04-18 00:00:00 |      37153 |        2809 |  736859 |    39582 | True         |
| 74 | Belgium        | 2020-04-18 00:00:00 |       1698 |         343 |   37836 |     5506 | True         |
| 85 | France         | 2020-04-18 00:00:00 |       5165 |         921 |  154295 |    19624 | True         |

 **Para depois e amanhã** 
|    | country        | ds                  |   case_day |   death_day |   cases |   deaths | predicted?   |
|---:|:---------------|:--------------------|-----------:|------------:|--------:|---------:|:-------------|
| 53 | Brazil         | 2020-04-19 00:00:00 |       2035 |         117 |   37729 |     2375 | True         |
| 79 | Italy          | 2020-04-19 00:00:00 |       5651 |         765 |  183930 |    24305 | True         |
| 79 | United Kingdom | 2020-04-19 00:00:00 |       6331 |         984 |  122206 |    16587 | True         |
| 78 | Spain          | 2020-04-19 00:00:00 |       6481 |         755 |  204192 |    21503 | True         |
| 88 | US             | 2020-04-19 00:00:00 |      37275 |        2858 |  774134 |    42440 | True         |
| 75 | Belgium        | 2020-04-19 00:00:00 |       1687 |         343 |   39523 |     5849 | True         |
| 86 | France         | 2020-04-19 00:00:00 |       6698 |         879 |  160993 |    20503 | True         |