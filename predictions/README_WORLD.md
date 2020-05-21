# **Predições**
Para experiência, estou fazendo predições simples sobre a quantidade de casos e mortes diárias. Como são séries temporais (*time-series*), estou usando [Facebook Prophet](https://facebook.github.io/prophet/docs/quick_start.html) que também é desenhado para este tipo de predição de uma maneira bem mais simples. Isso funciona muito bem na maioria das vezes; porém, algumas vezes há um grande salto entre os números que impactam no desempenho do modelo e leva um tempo (medições) para ser absorvido e compreendidos.

Essas predições foram feitas com os dados mundiais da pandemia Covid19 até **2020-05-20**.

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
| 80 | Brazil    | 2020-05-16 00:00:00 |      13220 |         700 |  233511 |    15662 | False        |
| 81 | Brazil    | 2020-05-17 00:00:00 |       7569 |         456 |  241080 |    16118 | False        |
| 82 | Brazil    | 2020-05-18 00:00:00 |      14288 |         735 |  255368 |    16853 | False        |
| 83 | Brazil    | 2020-05-19 00:00:00 |      16517 |        1130 |  271885 |    17983 | False        |
| 84 | Brazil    | 2020-05-20 00:00:00 |      19694 |         876 |  291579 |    18859 | False        |
| 85 | Brazil    | 2020-05-21 00:00:00 |      14636 |         868 |  306215 |    19727 | True         |
| 86 | Brazil    | 2020-05-22 00:00:00 |      15171 |         897 |  321386 |    20624 | True         |
| 87 | Brazil    | 2020-05-23 00:00:00 |      14953 |         863 |  336339 |    21487 | True         |
| 88 | Brazil    | 2020-05-24 00:00:00 |      14262 |         813 |  350601 |    22300 | True         |
| 89 | Brazil    | 2020-05-25 00:00:00 |      15265 |         865 |  365866 |    23165 | True         |
| 90 | Brazil    | 2020-05-26 00:00:00 |      16130 |         981 |  381996 |    24146 | True         |
| 91 | Brazil    | 2020-05-27 00:00:00 |      17429 |         972 |  399425 |    25118 | True         |
| 92 | Brazil    | 2020-05-28 00:00:00 |      17312 |        1002 |  416737 |    26120 | True         |
| 93 | Brazil    | 2020-05-29 00:00:00 |      17847 |        1031 |  434584 |    27151 | True         |
| 94 | Brazil    | 2020-05-30 00:00:00 |      17628 |         997 |  452212 |    28148 | True         |

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
|  85 | Brazil         | 2020-05-21 00:00:00 |      14636 |         868 |  306215 |    19727 | True         |
| 111 | Italy          | 2020-05-21 00:00:00 |        849 |         236 |  228213 |    32566 | True         |
| 111 | United Kingdom | 2020-05-21 00:00:00 |       5245 |         792 |  255382 |    36578 | True         |
| 110 | Spain          | 2020-05-21 00:00:00 |       3552 |         485 |  246132 |    28373 | True         |
| 120 | US             | 2020-05-21 00:00:00 |      34115 |        2161 | 1585968 |    95600 | True         |
| 107 | Belgium        | 2020-05-21 00:00:00 |        498 |         186 |   56481 |     9336 | True         |
| 118 | France         | 2020-05-21 00:00:00 |       1445 |         551 |  183260 |    28686 | True         |

 **Para depois e amanhã** 
|     | country        | ds                  |   case_day |   death_day |   cases |   deaths | predicted?   |
|----:|:---------------|:--------------------|-----------:|------------:|--------:|---------:|:-------------|
|  86 | Brazil         | 2020-05-22 00:00:00 |      15171 |         897 |  321386 |    20624 | True         |
| 112 | Italy          | 2020-05-22 00:00:00 |       1147 |         282 |  229360 |    32848 | True         |
| 112 | United Kingdom | 2020-05-22 00:00:00 |       5790 |         830 |  261172 |    37408 | True         |
| 111 | Spain          | 2020-05-22 00:00:00 |       3262 |         464 |  249394 |    28837 | True         |
| 121 | US             | 2020-05-22 00:00:00 |      34678 |        2109 | 1620646 |    97709 | True         |
| 108 | Belgium        | 2020-05-22 00:00:00 |        533 |         192 |   57014 |     9528 | True         |
| 119 | France         | 2020-05-22 00:00:00 |       1002 |         518 |  184262 |    29204 | True         |