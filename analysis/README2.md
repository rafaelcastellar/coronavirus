# **Analysis and monitoring**
These analysis are related to the Covid19 pandemic data upto @@@@@ 

As we have a big number of countries around ther world to have all of their data ploted togheter, will select a few of them and Brazil to be compared with: []
Some countries are not in UN dataset, so we can not analise them by population. They can be found at the end of the *[data_engineering.ipynb](../data_engineering.ipynb)*.
*Tip: you can set yourself at the analysis notebook which countries you prefer to compare*

First, I would like to present two rankings. Each of them are driven by the moving average of the last 7 days for daily cases and daily death, respectively:

## Top 5 deadliest countries + Brazil
@@@@@@@@@

## Top 5 most transmissible countries + Brazil
@@@@@@@@@@

----------------------
## World analysis
### Cases and deaths 
![](world_cases_deaths.png)

### Cases and deaths per million
Million of population normalizes the features so they can me better compareble among the selected countries. As we can see, the first charts shows us how agressive the pandemic is in Italy, Spain and somehow in France.
![](world_cases_deaths_million.png)

### Active cases, world overview, % recoveries and lethality
![](world_active_cases_percentages.png)

----------------------
## Brazil analysis
### Cases, deaths and recoveries
![](brazil_number_million_variation.png)

### Moving averages (last 7 days)
![](brazil_movingAvg.png)