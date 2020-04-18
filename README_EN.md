# **Coronavirus analysis from a brazilian perspective**

[<img src="https://raw.githubusercontent.com/NovelCOVID/API/master/assets/flags/br.png" width="40"  />
Versão em português](README.md)

Since the virus had arrived here in Brazil, I started some analysis over the contamination, death and recoveries data of the pandemic around the world, in order to understand, compare and even predict the its behaviour here in Brazil.

As this content content may be useful for someone else than me and my friends, I decided to share it here. If so, I'll be glad to help.
I will update it in a daily base around 7am in Brazil (or 4am UTC).

------------------

## Brasil's analysis
[<img src="analysis/BrazilMap.png" width="80"  /> <br>Click here for updated map](analysis/BrazilMap.html)

[The analysis over pandemic data Brazil can be found here](analysis/README_EN.md).

## World's analysis
[The analysis over pandemic data over some countries and Brazil can be found here](analysis/README_WORLD_EN.md).

## Brazil's prediction (under construction)
[The detailed pandemic prediction for the states of Brazil can be found here](predictions/README_EN.md).

## World's prediction
[The detailed pandemic prediction for Brazil and overall of some countries can be found here](predictions/README_WORLD_EN.md).

------------------------------------

## About this study

I would like to thank Pomber [https://github.com/pomber/covid19](https://github.com/pomber/covid1) who provides an updated JSON with worldwide covid-19 data from [CSSEGISandData/COVID-19](https://github.com/CSSEGISandData/COVID-19), which is the principal incoming data for this content from. I also would like to thank the [ebwinters](https://github.com/NovelCOVID/API/commits?author=ebwinters) and the guys from [https://github.com/novelcovid/api](https://github.com/novelcovid/api) project, which provides GEO-data from all the contries.
I encourge you to visit his project to get known about this data.

Bellow are the detailed information about this study as well as its jupyter-notebooks:

#### Incoming data
These are data fetched to produce the datasets used by this analisys:
* Pomber's JSON [Pomber](https://github.com/pomber/covid19): worldwide whole convid-19 pandemic data by contries
* ebwinter's [API] (https://github.com/novelcovid/api): contries geo-data
* UN Population [dataset](#https://population.un.org/wpp/Download/Standard/CSV/): total population of each country (not all) provided by United Nations
* [brasil-estados.json](data/brasil-estados.json): a JSON file cotaining all geographic data from all brazilian states from [IBGE's API](https://servicodados.ibge.gov.br/api/v2/malhas/?formato=application/vnd.geo+json&resolucao=2). These data are used to draw the states over the map of Brazil.
* [brazilian_states.csv](data/brazilian_states.csv): descriptive data from all the braizlian states from [IBGE's API](https://servicodados.ibge.gov.br/api/v1/localidades/estados/)
* [gov_brazil_corona19_data.csv](data/gov_brazil_corona19_data.csv): updated pandemic data in Brazil provied by brazilian [Ministery of Health](https://covid.saude.gov.br/).

### Dataset
* **[world_countries_2019.csv](data/world_countries_2019.csv)**: a consolidated dataset from ebinters and UN data, which is used to normalize some pandemic indicadors by countries total population
* **[world_corona19_data.csv](data/world_corona19_data.csv)**: the main dataset used by this study. It is made from Pomber's JSON and enriched with the following features which are derivate to cases, deaths and recoveries, although, to simplify I will use just *case's* :
    * *day*: number of the day since the first case of contamination
    * *cases*: cumulative number of cases since day 0
    * *case_day*: number of the cases recorded in a specific day
    * *%var_case_day*: daily variation of cases from the previous day (in percent)
    * *cases_million*: number of daily cases per one million of population of a coumtry. It is better comparable along the countries
    * *avg7_cases*: moving average of the daily cases among the last 7 days 
    * *avg7_cases_million*: moving average of the daily cases per one million among the last 7 days 
    * *perc_death*: percentage of deaths over the cases of the country
* **[brazil_corona19_data.csv](data/brazil_corona19_data.csv)**: a previous-like dataset, but with brazilian pandemic data over its states. 

### Notebooks
Here are my jupyter-notebooks used to build this study:

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/rafaelcastellar/coronavirus/blob/master/notebooks/countries_data_aggregator.ipynb) *[countries_data_aggregator.ipynb](notebooks/countries_data_aggregator.ipynb)*: the aggregator of all countries data.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/rafaelcastellar/coronavirus/blob/master/notebooks/data_engineering.ipynb) *[data_engineering.ipynb](notebooks/data_engineering.ipynb)*: data and feature engineering for the main dataset.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/rafaelcastellar/coronavirus/blob/master/notebooks/analysis.ipynb) *[analysis.ipynb](notebooks/analysis.ipynb)*: all the analises and charts about the world and brazilian pandemic.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/rafaelcastellar/coronavirus/blob/master/notebooks/brazil_analysis.ipynb) *[brazil_analysis.ipynb](notebooks/brazil_analysis.ipynb)*: all the analises and charts about the brazilian pandemic.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/rafaelcastellar/coronavirus/blob/master/notebooks/prediction.ipynb) *[prediction.ipynb](notebooks/prediction.ipynb)*: all prediction of world and brazilian pandemic using [Facebook-Prophet](https://facebook.github.io/prophet/docs/quick_start.html).

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/rafaelcastellar/coronavirus/blob/master/notebooks/brazilian_prediction.ipynb) *[brazilian_prediction.ipynb](notebooks/brazilian_prediction.ipynb)*: all prediction of brazilian pandemic among its states using [Facebook-Prophet](https://facebook.github.io/prophet/docs/quick_start.html).