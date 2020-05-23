# **Predições**
Para experiência, estou fazendo predições simples sobre a quantidade de casos e mortes diárias. Como são séries temporais (*time-series*), estou usando [Facebook Prophet](https://facebook.github.io/prophet/docs/quick_start.html) que também é desenhado para este tipo de predição de uma maneira bem mais simples. Isso funciona muito bem na maioria das vezes; porém, algumas vezes há um grande salto entre os números que impactam no desempenho do modelo e leva um tempo (medições) para ser absorvido e compreendidos.

Essas predições foram feitas com os dados mundiais da pandemia Covid19 até **2020-05-22**.

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
| 82 | Brazil    | 2020-05-18 00:00:00 |      14288 |         735 |  255368 |    16853 | False        |
| 83 | Brazil    | 2020-05-19 00:00:00 |      16517 |        1130 |  271885 |    17983 | False        |
| 84 | Brazil    | 2020-05-20 00:00:00 |      19694 |         876 |  291579 |    18859 | False        |
| 85 | Brazil    | 2020-05-21 00:00:00 |      18508 |        1188 |  310087 |    20047 | False        |
| 86 | Brazil    | 2020-05-22 00:00:00 |      20803 |        1001 |  330890 |    21048 | False        |
| 87 | Brazil    | 2020-05-23 00:00:00 |      16027 |         906 |  346917 |    21954 | True         |
| 88 | Brazil    | 2020-05-24 00:00:00 |      15374 |         858 |  362291 |    22812 | True         |
| 89 | Brazil    | 2020-05-25 00:00:00 |      16422 |         910 |  378713 |    23722 | True         |
| 90 | Brazil    | 2020-05-26 00:00:00 |      17326 |        1027 |  396039 |    24749 | True         |
| 91 | Brazil    | 2020-05-27 00:00:00 |      18677 |        1020 |  414716 |    25769 | True         |
| 92 | Brazil    | 2020-05-28 00:00:00 |      18915 |        1077 |  433631 |    26846 | True         |
| 93 | Brazil    | 2020-05-29 00:00:00 |      19624 |        1091 |  453255 |    27937 | True         |
| 94 | Brazil    | 2020-05-30 00:00:00 |      19091 |        1054 |  472346 |    28991 | True         |
| 95 | Brazil    | 2020-05-31 00:00:00 |      18438 |        1006 |  490784 |    29997 | True         |
| 96 | Brazil    | 2020-06-01 00:00:00 |      19485 |        1059 |  510269 |    31056 | True         |

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
|  87 | Brazil         | 2020-05-23 00:00:00 |      16027 |         906 |  346917 |    21954 | True         |
| 113 | Italy          | 2020-05-23 00:00:00 |        904 |         209 |  229562 |    32825 | True         |
| 113 | United Kingdom | 2020-05-23 00:00:00 |       5088 |         777 |  261047 |    37252 | True         |
| 112 | Spain          | 2020-05-23 00:00:00 |       2866 |         418 |  247715 |    29046 | True         |
| 122 | US             | 2020-05-23 00:00:00 |      33701 |        2022 | 1634638 |    98001 | True         |
| 109 | Belgium        | 2020-05-23 00:00:00 |        456 |         159 |   56967 |     9371 | True         |
| 120 | France         | 2020-05-23 00:00:00 |        782 |         418 |  182912 |    28636 | True         |

 **Para depois e amanhã** 
|     | country        | ds                  |   case_day |   death_day |   cases |   deaths | predicted?   |
|----:|:---------------|:--------------------|-----------:|------------:|--------:|---------:|:-------------|
|  88 | Brazil         | 2020-05-24 00:00:00 |      15374 |         858 |  362291 |    22812 | True         |
| 114 | Italy          | 2020-05-24 00:00:00 |        594 |         144 |  230156 |    32969 | True         |
| 114 | United Kingdom | 2020-05-24 00:00:00 |       5135 |         647 |  266182 |    37899 | True         |
| 113 | Spain          | 2020-05-24 00:00:00 |       2836 |         406 |  250551 |    29452 | True         |
| 123 | US             | 2020-05-24 00:00:00 |      31761 |        1795 | 1666399 |    99796 | True         |
| 110 | Belgium        | 2020-05-24 00:00:00 |        405 |         149 |   57372 |     9520 | True         |
| 121 | France         | 2020-05-24 00:00:00 |       1970 |         388 |  184882 |    29024 | True         |