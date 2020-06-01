# **Predições**
Para experiência, estou fazendo predições simples sobre a quantidade de casos e mortes diárias. Como são séries temporais (*time-series*), estou usando [Facebook Prophet](https://facebook.github.io/prophet/docs/quick_start.html) que também é desenhado para este tipo de predição de uma maneira bem mais simples. Isso funciona muito bem na maioria das vezes; porém, algumas vezes há um grande salto entre os números que impactam no desempenho do modelo e leva um tempo (medições) para ser absorvido e compreendidos.

Essas predições foram feitas com os dados mundiais da pandemia Covid19 até **2020-05-31**.

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
|  91 | Brazil    | 2020-05-27 00:00:00 |      20599 |        1086 |  411821 |    25598 | False        |
|  92 | Brazil    | 2020-05-28 00:00:00 |      26417 |        1156 |  438238 |    26754 | False        |
|  93 | Brazil    | 2020-05-29 00:00:00 |      26928 |        1124 |  465166 |    27878 | False        |
|  94 | Brazil    | 2020-05-30 00:00:00 |      33274 |         956 |  498440 |    28834 | False        |
|  95 | Brazil    | 2020-05-31 00:00:00 |      16409 |         480 |  514849 |    29314 | False        |
|  96 | Brazil    | 2020-06-01 00:00:00 |      21174 |         982 |  536023 |    30296 | True         |
|  97 | Brazil    | 2020-06-02 00:00:00 |      22433 |        1106 |  558456 |    31402 | True         |
|  98 | Brazil    | 2020-06-03 00:00:00 |      24101 |        1102 |  582557 |    32504 | True         |
|  99 | Brazil    | 2020-06-04 00:00:00 |      24790 |        1158 |  607347 |    33662 | True         |
| 100 | Brazil    | 2020-06-05 00:00:00 |      25553 |        1167 |  632900 |    34829 | True         |
| 101 | Brazil    | 2020-06-06 00:00:00 |      25609 |        1123 |  658509 |    35952 | True         |
| 102 | Brazil    | 2020-06-07 00:00:00 |      23859 |        1023 |  682368 |    36975 | True         |
| 103 | Brazil    | 2020-06-08 00:00:00 |      24867 |        1113 |  707235 |    38088 | True         |
| 104 | Brazil    | 2020-06-09 00:00:00 |      26126 |        1237 |  733361 |    39325 | True         |
| 105 | Brazil    | 2020-06-10 00:00:00 |      27794 |        1233 |  761155 |    40558 | True         |

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
|  96 | Brazil         | 2020-06-01 00:00:00 |      21174 |         982 |  536023 |    30296 | True         |
| 122 | Italy          | 2020-06-01 00:00:00 |       -319 |          74 |  232678 |    33489 | True         |
| 122 | United Kingdom | 2020-06-01 00:00:00 |       2802 |         534 |  279373 |    39105 | True         |
| 121 | Spain          | 2020-06-01 00:00:00 |       1581 |        -100 |  241423 |    27027 | True         |
| 131 | US             | 2020-06-01 00:00:00 |      29978 |        1717 | 1820150 |   106098 | True         |
| 118 | Belgium        | 2020-06-01 00:00:00 |         56 |          36 |   58437 |     9503 | True         |
| 129 | France         | 2020-06-01 00:00:00 |        623 |         177 |  189802 |    28982 | True         |

 **Para depois e amanhã** 
|     | country        | ds                  |   case_day |   death_day |   cases |   deaths | predicted?   |
|----:|:---------------|:--------------------|-----------:|------------:|--------:|---------:|:-------------|
|  97 | Brazil         | 2020-06-02 00:00:00 |      22433 |        1106 |  558456 |    31402 | True         |
| 123 | Italy          | 2020-06-02 00:00:00 |       -334 |          90 |  232344 |    33579 | True         |
| 123 | United Kingdom | 2020-06-02 00:00:00 |       2911 |         725 |  282284 |    39830 | True         |
| 122 | Spain          | 2020-06-02 00:00:00 |       2074 |           0 |  243497 |    27027 | True         |
| 132 | US             | 2020-06-02 00:00:00 |      30744 |        2031 | 1850894 |   108129 | True         |
| 119 | Belgium        | 2020-06-02 00:00:00 |          0 |          58 |   58437 |     9561 | True         |
| 130 | France         | 2020-06-02 00:00:00 |        725 |         198 |  190527 |    29180 | True         |