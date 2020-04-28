# **Predições**
Para experiência, estou fazendo predições simples sobre a quantidade de casos e mortes diárias. Como são séries temporais (*time-series*), estou usando [Facebook Prophet](https://facebook.github.io/prophet/docs/quick_start.html) que também é desenhado para este tipo de predição de uma maneira bem mais simples. Isso funciona muito bem na maioria das vezes; porém, algumas vezes há um grande salto entre os números que impactam no desempenho do modelo e leva um tempo (medições) para ser absorvido e compreendidos.

Essas predições foram feitas com os dados mundiais da pandemia Covid19 até **2020-04-27**.

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
| 57 | Brazil    | 2020-04-23 00:00:00 |       4279 |         425 |   50036 |     3331 | False        |
| 58 | Brazil    | 2020-04-24 00:00:00 |       4007 |         373 |   54043 |     3704 | False        |
| 59 | Brazil    | 2020-04-25 00:00:00 |       5281 |         353 |   59324 |     4057 | False        |
| 60 | Brazil    | 2020-04-26 00:00:00 |       3776 |         229 |   63100 |     4286 | False        |
| 61 | Brazil    | 2020-04-27 00:00:00 |       4346 |         317 |   67446 |     4603 | False        |
| 62 | Brazil    | 2020-04-28 00:00:00 |       3669 |         264 |   71115 |     4867 | True         |
| 63 | Brazil    | 2020-04-29 00:00:00 |       3957 |         274 |   75072 |     5141 | True         |
| 64 | Brazil    | 2020-04-30 00:00:00 |       4094 |         309 |   79166 |     5450 | True         |
| 65 | Brazil    | 2020-05-01 00:00:00 |       4172 |         302 |   83338 |     5752 | True         |
| 66 | Brazil    | 2020-05-02 00:00:00 |       4307 |         303 |   87645 |     6055 | True         |
| 67 | Brazil    | 2020-05-03 00:00:00 |       4067 |         280 |   91712 |     6335 | True         |
| 68 | Brazil    | 2020-05-04 00:00:00 |       4162 |         299 |   95874 |     6634 | True         |
| 69 | Brazil    | 2020-05-05 00:00:00 |       4401 |         317 |  100275 |     6951 | True         |
| 70 | Brazil    | 2020-05-06 00:00:00 |       4689 |         327 |  104964 |     7278 | True         |
| 71 | Brazil    | 2020-05-07 00:00:00 |       4826 |         362 |  109790 |     7640 | True         |

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
| 62 | Brazil         | 2020-04-28 00:00:00 |       3669 |         264 |   71115 |     4867 | True         |
| 88 | Italy          | 2020-04-28 00:00:00 |       4623 |         742 |  204037 |    27719 | True         |
| 88 | United Kingdom | 2020-04-28 00:00:00 |       5925 |         814 |  164273 |    21971 | True         |
| 87 | Spain          | 2020-04-28 00:00:00 |       6097 |         657 |  235519 |    24178 | True         |
| 97 | US             | 2020-04-28 00:00:00 |      35975 |        2597 | 1024172 |    58856 | True         |
| 84 | Belgium        | 2020-04-28 00:00:00 |       1339 |         282 |   48026 |     7489 | True         |
| 95 | France         | 2020-04-28 00:00:00 |       4744 |         737 |  170707 |    24064 | True         |

 **Para depois e amanhã** 
|    | country        | ds                  |   case_day |   death_day |   cases |   deaths | predicted?   |
|---:|:---------------|:--------------------|-----------:|------------:|--------:|---------:|:-------------|
| 63 | Brazil         | 2020-04-29 00:00:00 |       3957 |         274 |   75072 |     5141 | True         |
| 89 | Italy          | 2020-04-29 00:00:00 |       4957 |         726 |  208994 |    28445 | True         |
| 89 | United Kingdom | 2020-04-29 00:00:00 |       6217 |         837 |  170490 |    22808 | True         |
| 88 | Spain          | 2020-04-29 00:00:00 |       6877 |         726 |  242396 |    24904 | True         |
| 98 | US             | 2020-04-29 00:00:00 |      36745 |        2634 | 1060917 |    61490 | True         |
| 85 | Belgium        | 2020-04-29 00:00:00 |       1526 |         272 |   49552 |     7761 | True         |
| 96 | France         | 2020-04-29 00:00:00 |       4089 |         751 |  174796 |    24815 | True         |