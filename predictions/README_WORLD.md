# **Predições**
Para experiência, estou fazendo predições simples sobre a quantidade de casos e mortes diárias. Como são séries temporais (*time-series*), estou usando [Facebook Prophet](https://facebook.github.io/prophet/docs/quick_start.html) que também é desenhado para este tipo de predição de uma maneira bem mais simples. Isso funciona muito bem na maioria das vezes; porém, algumas vezes há um grande salto entre os números que impactam no desempenho do modelo e leva um tempo (medições) para ser absorvido e compreendidos.

Essas predições foram feitas com os dados mundiais da pandemia Covid19 até **2020-06-01**.

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
|  92 | Brazil    | 2020-05-28 00:00:00 |      26417 |        1156 |  438238 |    26754 | False        |
|  93 | Brazil    | 2020-05-29 00:00:00 |      26928 |        1124 |  465166 |    27878 | False        |
|  94 | Brazil    | 2020-05-30 00:00:00 |      33274 |         956 |  498440 |    28834 | False        |
|  95 | Brazil    | 2020-05-31 00:00:00 |      16409 |         480 |  514849 |    29314 | False        |
|  96 | Brazil    | 2020-06-01 00:00:00 |      11598 |         623 |  526447 |    29937 | False        |
|  97 | Brazil    | 2020-06-02 00:00:00 |      21040 |        1074 |  547487 |    31011 | True         |
|  98 | Brazil    | 2020-06-03 00:00:00 |      22660 |        1070 |  570147 |    32081 | True         |
|  99 | Brazil    | 2020-06-04 00:00:00 |      23308 |        1124 |  593455 |    33205 | True         |
| 100 | Brazil    | 2020-06-05 00:00:00 |      24030 |        1132 |  617485 |    34337 | True         |
| 101 | Brazil    | 2020-06-06 00:00:00 |      24027 |        1087 |  641512 |    35424 | True         |
| 102 | Brazil    | 2020-06-07 00:00:00 |      22218 |         987 |  663730 |    36411 | True         |
| 103 | Brazil    | 2020-06-08 00:00:00 |      22482 |        1051 |  686212 |    37462 | True         |
| 104 | Brazil    | 2020-06-09 00:00:00 |      24274 |        1197 |  710486 |    38659 | True         |
| 105 | Brazil    | 2020-06-10 00:00:00 |      25895 |        1193 |  736381 |    39852 | True         |
| 106 | Brazil    | 2020-06-11 00:00:00 |      26543 |        1247 |  762924 |    41099 | True         |

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
|  97 | Brazil         | 2020-06-02 00:00:00 |      21040 |        1074 |  547487 |    31011 | True         |
| 123 | Italy          | 2020-06-02 00:00:00 |       -333 |          68 |  232864 |    33543 | True         |
| 123 | United Kingdom | 2020-06-02 00:00:00 |       2696 |         712 |  280847 |    39839 | True         |
| 122 | Spain          | 2020-06-02 00:00:00 |       1856 |          -3 |  241857 |    27124 | True         |
| 132 | US             | 2020-06-02 00:00:00 |      30110 |        2002 | 1841470 |   107167 | True         |
| 119 | Belgium        | 2020-06-02 00:00:00 |         13 |          53 |   58530 |     9539 | True         |
| 130 | France         | 2020-06-02 00:00:00 |        494 |         170 |  190012 |    29006 | True         |

 **Para depois e amanhã** 
|     | country        | ds                  |   case_day |   death_day |   cases |   deaths | predicted?   |
|----:|:---------------|:--------------------|-----------:|------------:|--------:|---------:|:-------------|
|  98 | Brazil         | 2020-06-03 00:00:00 |      22660 |        1070 |  570147 |    32081 | True         |
| 124 | Italy          | 2020-06-03 00:00:00 |       -185 |          53 |  232679 |    33596 | True         |
| 124 | United Kingdom | 2020-06-03 00:00:00 |       2630 |         689 |  283477 |    40528 | True         |
| 123 | Spain          | 2020-06-03 00:00:00 |       2395 |          32 |  244252 |    27156 | True         |
| 133 | US             | 2020-06-03 00:00:00 |      30976 |        2086 | 1872446 |   109253 | True         |
| 120 | Belgium        | 2020-06-03 00:00:00 |        108 |          61 |   58638 |     9600 | True         |
| 131 | France         | 2020-06-03 00:00:00 |       -245 |         176 |  189767 |    29182 | True         |