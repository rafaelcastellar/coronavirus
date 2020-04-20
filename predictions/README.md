# **Predições**
Para experiência, estou fazendo predições simples sobre a quantidade de casos e mortes diárias. Como são séries temporais (*time-series*), estou usando [Facebook Prophet](https://facebook.github.io/prophet/docs/quick_start.html) que também é desenhado para este tipo de predição de uma maneira bem mais simples. Isso funciona muito bem na maioria das vezes; porém, algumas vezes há um grande salto entre os números que impactam no desempenho do modelo e leva um tempo (medições) para ser absorvido e compreendidos.

Essas predições foram feitas com os dados da pandemia Covid19 no Brasil até **2020-12-04**.

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
| 49 | SP      | 2020-04-15 00:00:00 |       1672 |          83 |   11043 |      778 | False        |
| 50 | SP      | 2020-04-16 00:00:00 |        525 |          75 |   11568 |      853 | False        |
| 51 | SP      | 2020-04-17 00:00:00 |       1273 |          75 |   12841 |      928 | False        |
| 52 | SP      | 2020-04-18 00:00:00 |       1053 |          63 |   13894 |      991 | False        |
| 53 | SP      | 2020-04-19 00:00:00 |        373 |          24 |   14267 |     1015 | False        |
| 54 | SP      | 2020-12-05 00:00:00 |        455 |          34 |   14722 |     1049 | True         |
| 55 | SP      | 2020-12-06 00:00:00 |        327 |          24 |   15049 |     1073 | True         |
| 56 | SP      | 2020-12-07 00:00:00 |        174 |          18 |   15223 |     1091 | True         |
| 57 | SP      | 2020-12-08 00:00:00 |        463 |          34 |   15686 |     1125 | True         |
| 58 | SP      | 2020-12-09 00:00:00 |        461 |          30 |   16147 |     1155 | True         |
| 59 | SP      | 2020-12-10 00:00:00 |        229 |          24 |   16376 |     1179 | True         |
| 60 | SP      | 2020-12-11 00:00:00 |        363 |          27 |   16739 |     1206 | True         |
| 61 | SP      | 2020-12-12 00:00:00 |        458 |          34 |   17197 |     1240 | True         |
| 62 | SP      | 2020-12-13 00:00:00 |        330 |          24 |   17527 |     1264 | True         |
| 63 | SP      | 2020-12-14 00:00:00 |        177 |          18 |   17704 |     1282 | True         |

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
| 31 | PI      | 2020-12-05 00:00:00 |          4 |           0 |     149 |       10 | True         |
| 34 | CE      | 2020-12-05 00:00:00 |        158 |           9 |    3410 |      195 | True         |
| 43 | MG      | 2020-12-05 00:00:00 |         24 |           1 |    1178 |       40 | True         |
| 46 | RJ      | 2020-12-05 00:00:00 |        132 |          11 |    4897 |      413 | True         |
| 54 | SP      | 2020-12-05 00:00:00 |        455 |          34 |   14722 |     1049 | True         |
| 39 | PR      | 2020-12-05 00:00:00 |         65 |           3 |    1052 |       51 | True         |

 **Para depois e amanhã** 
|    | state   | ds                  |   case_day |   death_day |   cases |   deaths | predicted?   |
|---:|:--------|:--------------------|-----------:|------------:|--------:|---------:|:-------------|
| 32 | PI      | 2020-12-06 00:00:00 |          6 |           0 |     155 |       10 | True         |
| 35 | CE      | 2020-12-06 00:00:00 |        135 |           7 |    3545 |      202 | True         |
| 44 | MG      | 2020-12-06 00:00:00 |         39 |           0 |    1217 |       40 | True         |
| 47 | RJ      | 2020-12-06 00:00:00 |        127 |           8 |    5024 |      421 | True         |
| 55 | SP      | 2020-12-06 00:00:00 |        327 |          24 |   15049 |     1073 | True         |
| 40 | PR      | 2020-12-06 00:00:00 |         41 |           3 |    1093 |       54 | True         |