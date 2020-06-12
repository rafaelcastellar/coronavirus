# **Predições**
Para experiência, estou fazendo predições simples sobre a quantidade de casos e mortes diárias. Como são séries temporais (*time-series*), estou usando [Facebook Prophet](https://facebook.github.io/prophet/docs/quick_start.html) que também é desenhado para este tipo de predição de uma maneira bem mais simples. Isso funciona muito bem na maioria das vezes; porém, algumas vezes há um grande salto entre os números que impactam no desempenho do modelo e leva um tempo (medições) para ser absorvido e compreendidos.

Essas predições foram feitas com os dados mundiais da pandemia Covid19 até **2020-06-11**.

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
| 102 | Brazil    | 2020-06-07 00:00:00 |      18912 |         525 |  691758 |    36455 | False        |
| 103 | Brazil    | 2020-06-08 00:00:00 |      15654 |         679 |  707412 |    37134 | False        |
| 104 | Brazil    | 2020-06-09 00:00:00 |      32091 |        1272 |  739503 |    38406 | False        |
| 105 | Brazil    | 2020-06-10 00:00:00 |      32913 |        1274 |  772416 |    39680 | False        |
| 106 | Brazil    | 2020-06-11 00:00:00 |      30412 |        1239 |  802828 |    40919 | False        |
| 107 | Brazil    | 2020-06-12 00:00:00 |      30105 |        1225 |  832933 |    42144 | True         |
| 108 | Brazil    | 2020-06-13 00:00:00 |      29908 |        1175 |  862841 |    43319 | True         |
| 109 | Brazil    | 2020-06-14 00:00:00 |      27718 |        1055 |  890559 |    44374 | True         |
| 110 | Brazil    | 2020-06-15 00:00:00 |      27795 |        1124 |  918354 |    45498 | True         |
| 111 | Brazil    | 2020-06-16 00:00:00 |      31153 |        1312 |  949507 |    46810 | True         |
| 112 | Brazil    | 2020-06-17 00:00:00 |      32658 |        1315 |  982165 |    48125 | True         |
| 113 | Brazil    | 2020-06-18 00:00:00 |      33261 |        1367 | 1015426 |    49492 | True         |
| 114 | Brazil    | 2020-06-19 00:00:00 |      33921 |        1344 | 1049347 |    50836 | True         |
| 115 | Brazil    | 2020-06-20 00:00:00 |      33723 |        1294 | 1083070 |    52130 | True         |
| 116 | Brazil    | 2020-06-21 00:00:00 |      31534 |        1174 | 1114604 |    53304 | True         |

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
| 107 | Brazil         | 2020-06-12 00:00:00 |      30105 |        1225 |  832933 |    42144 | True         |
| 133 | Italy          | 2020-06-12 00:00:00 |       -232 |          12 |  235910 |    34179 | True         |
| 133 | United Kingdom | 2020-06-12 00:00:00 |       2106 |         384 |  295381 |    41748 | True         |
| 132 | Spain          | 2020-06-12 00:00:00 |       1672 |         -23 |  244742 |    27113 | True         |
| 142 | US             | 2020-06-12 00:00:00 |      27261 |        1778 | 2050608 |   115598 | True         |
| 129 | Belgium        | 2020-06-12 00:00:00 |         84 |          28 |   59795 |     9664 | True         |
| 140 | France         | 2020-06-12 00:00:00 |         52 |          77 |  195256 |    29426 | True         |

 **Para depois e amanhã** 
|     | country        | ds                  |   case_day |   death_day |   cases |   deaths | predicted?   |
|----:|:---------------|:--------------------|-----------:|------------:|--------:|---------:|:-------------|
| 108 | Brazil         | 2020-06-13 00:00:00 |      29908 |        1175 |  862841 |    43319 | True         |
| 134 | Italy          | 2020-06-13 00:00:00 |       -201 |           1 |  235709 |    34180 | True         |
| 134 | United Kingdom | 2020-06-13 00:00:00 |       1572 |         331 |  296953 |    42079 | True         |
| 133 | Spain          | 2020-06-13 00:00:00 |       1305 |         -73 |  246047 |    27040 | True         |
| 143 | US             | 2020-06-13 00:00:00 |      26167 |        1714 | 2076775 |   117312 | True         |
| 130 | Belgium        | 2020-06-13 00:00:00 |         57 |          11 |   59852 |     9675 | True         |
| 141 | France         | 2020-06-13 00:00:00 |       -144 |          19 |  195112 |    29445 | True         |