# **Predições**
Para experiência, estou fazendo predições simples sobre a quantidade de casos e mortes diárias. Como são séries temporais (*time-series*), estou usando [Facebook Prophet](https://facebook.github.io/prophet/docs/quick_start.html) que também é desenhado para este tipo de predição de uma maneira bem mais simples. Isso funciona muito bem na maioria das vezes; porém, algumas vezes há um grande salto entre os números que impactam no desempenho do modelo e leva um tempo (medições) para ser absorvido e compreendidos.

Essas predições foram feitas com os dados da pandemia Covid19 no Brasil até **2020-04-25**.

Como há muitos estados para terem seus dados submetidos ao modelo de predição de uma só vez, selecionei alguns que estão em destaque neste momento:
['PI', 'CE', 'MG', 'RJ', 'SP', 'PR'].
***Dica**: você mesmo pode definir no notebook *[prediction.ipynb](../prediction.ipynb)* quais estados você prefere fazer a predição.*


## A predição
As predições estão sendo realizadas sobre os dados diários de casos e de mortes. Em seguida, os dados previstos são acumulados para que tenhamos a projeção acumulada. Estão sendo previstos os próximos 10 dias.
Ao ffim, é gerado o arquivo CSV contendo todas as previsões.

#### Os últimos 5 dias da pandemia em São Paulo e os próximos 10 dias previstos
*predicted? = True* significa que são dados de predição; *=False* significa que são dados reais.
|    | state   | ds                  |   case_day |   death_day |   cases |   deaths | predicted?   |
|---:|:--------|:--------------------|-----------:|------------:|--------:|---------:|:-------------|
| 55 | SP      | 2020-04-21 00:00:00 |        805 |          56 |   15385 |     1093 | False        |
| 56 | SP      | 2020-04-22 00:00:00 |        529 |          41 |   15914 |     1134 | False        |
| 57 | SP      | 2020-04-23 00:00:00 |        826 |         211 |   16740 |     1345 | False        |
| 58 | SP      | 2020-04-24 00:00:00 |       1086 |         167 |   17826 |     1512 | False        |
| 59 | SP      | 2020-04-25 00:00:00 |       2178 |         155 |   20004 |     1667 | False        |
| 60 | SP      | 2020-04-26 00:00:00 |        744 |          66 |   20748 |     1733 | True         |
| 61 | SP      | 2020-04-27 00:00:00 |        711 |          67 |   21459 |     1800 | True         |
| 62 | SP      | 2020-04-28 00:00:00 |        974 |          86 |   22433 |     1886 | True         |
| 63 | SP      | 2020-04-29 00:00:00 |       1112 |          86 |   23545 |     1972 | True         |
| 64 | SP      | 2020-04-30 00:00:00 |        988 |         105 |   24533 |     2077 | True         |
| 65 | SP      | 2020-05-01 00:00:00 |       1104 |          99 |   25637 |     2176 | True         |
| 66 | SP      | 2020-05-02 00:00:00 |       1123 |          95 |   26760 |     2271 | True         |
| 67 | SP      | 2020-05-03 00:00:00 |        877 |          79 |   27637 |     2350 | True         |
| 68 | SP      | 2020-05-04 00:00:00 |        845 |          80 |   28482 |     2430 | True         |
| 69 | SP      | 2020-05-05 00:00:00 |       1108 |          98 |   29590 |     2528 | True         |

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
| 37 | PI      | 2020-04-26 00:00:00 |         21 |           0 |     318 |       17 | True         |
| 40 | CE      | 2020-04-26 00:00:00 |        299 |          17 |    5720 |      327 | True         |
| 49 | MG      | 2020-04-26 00:00:00 |         78 |           2 |    1559 |       60 | True         |
| 52 | RJ      | 2020-04-26 00:00:00 |        324 |          29 |    7152 |      644 | True         |
| 60 | SP      | 2020-04-26 00:00:00 |        744 |          66 |   20748 |     1733 | True         |
| 45 | PR      | 2020-04-26 00:00:00 |         49 |           3 |    1189 |       72 | True         |

 **Para depois e amanhã** 
|    | state   | ds                  |   case_day |   death_day |   cases |   deaths | predicted?   |
|---:|:--------|:--------------------|-----------:|------------:|--------:|---------:|:-------------|
| 38 | PI      | 2020-04-27 00:00:00 |         20 |           1 |     338 |       18 | True         |
| 41 | CE      | 2020-04-27 00:00:00 |        326 |          19 |    6046 |      346 | True         |
| 50 | MG      | 2020-04-27 00:00:00 |         61 |           3 |    1620 |       63 | True         |
| 53 | RJ      | 2020-04-27 00:00:00 |        318 |          30 |    7470 |      674 | True         |
| 61 | SP      | 2020-04-27 00:00:00 |        711 |          67 |   21459 |     1800 | True         |
| 46 | PR      | 2020-04-27 00:00:00 |         33 |           3 |    1222 |       75 | True         |