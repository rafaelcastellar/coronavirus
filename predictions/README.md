# **Predições**
Para experiência, estou fazendo predições simples sobre a quantidade de casos e mortes diárias. Como são séries temporais (*time-series*), estou usando [Facebook Prophet](https://facebook.github.io/prophet/docs/quick_start.html) que também é desenhado para este tipo de predição de uma maneira bem mais simples. Isso funciona muito bem na maioria das vezes; porém, algumas vezes há um grande salto entre os números que impactam no desempenho do modelo e leva um tempo (medições) para ser absorvido e compreendidos.

Essas predições foram feitas com os dados da pandemia Covid19 no Brasil até **2020-04-29**.

Como há muitos estados para terem seus dados submetidos ao modelo de predição de uma só vez, selecionei alguns que estão em destaque neste momento:
['PI', 'CE', 'AM', 'RJ', 'SP', 'PR'].
***Dica**: você mesmo pode definir no notebook *[prediction.ipynb](../prediction.ipynb)* quais estados você prefere fazer a predição.*


## A predição
As predições estão sendo realizadas sobre os dados diários de casos e de mortes. Em seguida, os dados previstos são acumulados para que tenhamos a projeção acumulada. Estão sendo previstos os próximos 10 dias.
Ao ffim, é gerado o arquivo CSV contendo todas as previsões.

#### Os últimos 5 dias da pandemia em São Paulo e os próximos 10 dias previstos
*predicted? = True* significa que são dados de predição; *=False* significa que são dados reais.
|    | state   | ds                  |   case_day |   death_day |   cases |   deaths | predicted?   |
|---:|:--------|:--------------------|-----------:|------------:|--------:|---------:|:-------------|
| 59 | SP      | 2020-04-25 00:00:00 |       2178 |         155 |   20004 |     1667 | False        |
| 60 | SP      | 2020-04-26 00:00:00 |        711 |          33 |   20715 |     1700 | False        |
| 61 | SP      | 2020-04-27 00:00:00 |        981 |         125 |   21696 |     1825 | False        |
| 62 | SP      | 2020-04-28 00:00:00 |       2345 |         224 |   24041 |     2049 | False        |
| 63 | SP      | 2020-04-29 00:00:00 |       2117 |         198 |   26158 |     2247 | False        |
| 64 | SP      | 2020-04-30 00:00:00 |       1111 |         118 |   27269 |     2365 | True         |
| 65 | SP      | 2020-05-01 00:00:00 |       1227 |         111 |   28496 |     2476 | True         |
| 66 | SP      | 2020-05-02 00:00:00 |       1246 |         108 |   29742 |     2584 | True         |
| 67 | SP      | 2020-05-03 00:00:00 |        997 |          88 |   30739 |     2672 | True         |
| 68 | SP      | 2020-05-04 00:00:00 |        998 |          99 |   31737 |     2771 | True         |
| 69 | SP      | 2020-05-05 00:00:00 |       1383 |         127 |   33120 |     2898 | True         |
| 70 | SP      | 2020-05-06 00:00:00 |       1481 |         124 |   34601 |     3022 | True         |
| 71 | SP      | 2020-05-07 00:00:00 |       1269 |         133 |   35870 |     3155 | True         |
| 72 | SP      | 2020-05-08 00:00:00 |       1385 |         126 |   37255 |     3281 | True         |
| 73 | SP      | 2020-05-09 00:00:00 |       1404 |         123 |   38659 |     3404 | True         |

 #### As curvas acumuladas previstas para São Paulo
![](brazil_predictions.png)

 O Facebook Prophet gera automaticamente gráficos do comportamento sazonal dos dados, o que provê boas informações visuais. Aqui estão sobre as predições de São Paulo:
### Casos
![](brazil_prophet_cases.png)

 ### Mortes
![](brazil_prophet_deaths.png)
#### Finalmente, as predições para os demais estados selecionados para:
**Para amanhã**
|    | state   | ds                  |   case_day |   death_day |   cases |   deaths | predicted?   |
|---:|:--------|:--------------------|-----------:|------------:|--------:|---------:|:-------------|
| 41 | PI      | 2020-04-30 00:00:00 |         27 |           0 |     481 |       24 | True         |
| 44 | CE      | 2020-04-30 00:00:00 |        469 |          29 |    7736 |      470 | True         |
| 46 | AM      | 2020-04-30 00:00:00 |        296 |          24 |    5097 |      404 | True         |
| 56 | RJ      | 2020-04-30 00:00:00 |        450 |          42 |    9319 |      836 | True         |
| 64 | SP      | 2020-04-30 00:00:00 |       1111 |         118 |   27269 |     2365 | True         |
| 49 | PR      | 2020-04-30 00:00:00 |         53 |           4 |    1401 |       86 | True         |

 **Para depois e amanhã** 
|    | state   | ds                  |   case_day |   death_day |   cases |   deaths | predicted?   |
|---:|:--------|:--------------------|-----------:|------------:|--------:|---------:|:-------------|
| 42 | PI      | 2020-05-01 00:00:00 |         33 |           1 |     514 |       25 | True         |
| 45 | CE      | 2020-05-01 00:00:00 |        387 |          26 |    8123 |      496 | True         |
| 47 | AM      | 2020-05-01 00:00:00 |        265 |          24 |    5362 |      428 | True         |
| 57 | RJ      | 2020-05-01 00:00:00 |        403 |          42 |    9722 |      878 | True         |
| 65 | SP      | 2020-05-01 00:00:00 |       1227 |         111 |   28496 |     2476 | True         |
| 50 | PR      | 2020-05-01 00:00:00 |         53 |           4 |    1454 |       90 | True         |