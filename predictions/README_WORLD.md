# **Predições**
Para experiência, estou fazendo predições simples sobre a quantidade de casos e mortes diárias. Como são séries temporais (*time-series*), estou usando [Facebook Prophet](https://facebook.github.io/prophet/docs/quick_start.html) que também é desenhado para este tipo de predição de uma maneira bem mais simples. Isso funciona muito bem na maioria das vezes; porém, algumas vezes há um grande salto entre os números que impactam no desempenho do modelo e leva um tempo (medições) para ser absorvido e compreendidos.

Essas predições foram feitas com os dados mundiais da pandemia Covid19 até **2020-05-18**.

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
| 78 | Brazil    | 2020-05-14 00:00:00 |      13028 |         759 |  203165 |    13999 | False        |
| 79 | Brazil    | 2020-05-15 00:00:00 |      17126 |         963 |  220291 |    14962 | False        |
| 80 | Brazil    | 2020-05-16 00:00:00 |      13220 |         700 |  233511 |    15662 | False        |
| 81 | Brazil    | 2020-05-17 00:00:00 |       7569 |         456 |  241080 |    16118 | False        |
| 82 | Brazil    | 2020-05-18 00:00:00 |      14288 |         735 |  255368 |    16853 | False        |
| 83 | Brazil    | 2020-05-19 00:00:00 |      12060 |         784 |  267428 |    17637 | True         |
| 84 | Brazil    | 2020-05-20 00:00:00 |      13159 |         796 |  280587 |    18433 | True         |
| 85 | Brazil    | 2020-05-21 00:00:00 |      13417 |         829 |  294004 |    19262 | True         |
| 86 | Brazil    | 2020-05-22 00:00:00 |      13907 |         857 |  307911 |    20119 | True         |
| 87 | Brazil    | 2020-05-23 00:00:00 |      13644 |         822 |  321555 |    20941 | True         |
| 88 | Brazil    | 2020-05-24 00:00:00 |      12908 |         771 |  334463 |    21712 | True         |
| 89 | Brazil    | 2020-05-25 00:00:00 |      13872 |         821 |  348335 |    22533 | True         |
| 90 | Brazil    | 2020-05-26 00:00:00 |      14316 |         907 |  362651 |    23440 | True         |
| 91 | Brazil    | 2020-05-27 00:00:00 |      15415 |         919 |  378066 |    24359 | True         |
| 92 | Brazil    | 2020-05-28 00:00:00 |      15673 |         951 |  393739 |    25310 | True         |

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
|  83 | Brazil         | 2020-05-19 00:00:00 |      12060 |         784 |  267428 |    17637 | True         |
| 109 | Italy          | 2020-05-19 00:00:00 |        762 |         522 |  226648 |    32529 | True         |
| 109 | United Kingdom | 2020-05-19 00:00:00 |       5148 |         848 |  252857 |    35724 | True         |
| 108 | Spain          | 2020-05-19 00:00:00 |       3629 |         467 |  245260 |    28176 | True         |
| 118 | US             | 2020-05-19 00:00:00 |      31645 |        2188 | 1539953 |    92535 | True         |
| 105 | Belgium        | 2020-05-19 00:00:00 |        866 |         200 |   56425 |     9280 | True         |
| 116 | France         | 2020-05-19 00:00:00 |       2197 |         567 |  182363 |    28809 | True         |

 **Para depois e amanhã** 
|     | country        | ds                  |   case_day |   death_day |   cases |   deaths | predicted?   |
|----:|:---------------|:--------------------|-----------:|------------:|--------:|---------:|:-------------|
|  84 | Brazil         | 2020-05-20 00:00:00 |      13159 |         796 |  280587 |    18433 | True         |
| 110 | Italy          | 2020-05-20 00:00:00 |        928 |         515 |  227576 |    33044 | True         |
| 110 | United Kingdom | 2020-05-20 00:00:00 |       5453 |         815 |  258310 |    36539 | True         |
| 109 | Spain          | 2020-05-20 00:00:00 |       4276 |         530 |  249536 |    28706 | True         |
| 119 | US             | 2020-05-20 00:00:00 |      32486 |        2245 | 1572439 |    94780 | True         |
| 106 | Belgium        | 2020-05-20 00:00:00 |       1001 |         212 |   57426 |     9492 | True         |
| 117 | France         | 2020-05-20 00:00:00 |       1376 |         563 |  183739 |    29372 | True         |