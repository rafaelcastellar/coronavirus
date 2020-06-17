#!/usr/bin/env python
# coding: utf-8

# In[310]:


print('Initializing data engineering!')
import pandas as pd
import numpy as np
import datetime
from pandas.io.json import json_normalize
import json, requests, gzip


# ### World data engineering
# #### Fetching worldwide data

# In[311]:


# df = pd.read_json('https://pomber.github.io/covid19/timeseries.json')
# df = pd.read_json('https://covidapi.info/api/v1/country/BRA')
# df = pd.read_json('https://api.covid19api.com/dayone/country/brazil/status/confirmed')
#https://documenter.getpostman.com/view/10808728/SzS8rjbc?version=latest#cc76052f-6601-4645-80e5-ca7aaa36f8ef
df_countries = pd.read_csv('../data/world_countries_2019.csv')

df = pd.DataFrame()
url = "https://pomber.github.io/covid19/timeseries.json"
req = requests.get(url)
# r = r.json()
j = json.loads(req.text)


# #### Fetching countries's pandemic data from Pomber's JSON to a dataframe 

# In[312]:


# Loading countries names to dict
countries = []
df = pd.DataFrame()
for country in j:
    countries.append(country)

df['country'] = pd.Series(countries)

# Loading countries data do dict then to dataframe
dic = []
for country in countries:
    i = 0
    while i < len(j[country]):
        if j[country][i]['confirmed'] == 0:
            i += 1
            continue
        row = {'country': country, 'date': j[country][i]['date'], 'cases':j[country][i]['confirmed'],
               'deaths':j[country][i]['deaths'], 'recoveries':j[country][i]['recovered']}
        dic.append(row)
        i += 1 
df = pd.DataFrame.from_dict(dic)
df[df['country']=='Brazil'].tail()


# #### Feature engineering

# In[ ]:


for country in countries:
    qtdeDays = len(df[df.country == country])+1
    df.loc[df.country == country, 'day'] = (np.arange(1,qtdeDays,1))
#     df.drop(df[case].index, inplace=True)
    # valores diários
    df.loc[df.country == country, 'case_day'] = df[df.country == country]['cases'].diff()    
    df.loc[df.country == country, 'death_day'] = df[df.country == country]['deaths'].diff()
    df.loc[df.country == country, 'recovery_day'] = df[df.country == country]['recoveries'].diff()

    # % daily variations
    df.loc[df.country == country, '%var_case_day'] = ((df[df.country == country]['case_day'] - df[df.country == country]['case_day'].shift()) / df[df.country == country]['case_day'].shift()*100).replace([np.inf, -np.inf], 0).replace([np.nan], 0).round(2)
    df.loc[df.country == country, '%var_death_day'] = ((df[df.country == country]['death_day'] - df[df.country == country]['death_day'].shift()) / df[df.country == country]['death_day'].shift()*100).replace([np.inf, -np.inf], 0).replace([np.nan], 0).round(2)
    df.loc[df.country == country, '%var_recovery_day'] = ((df[df.country == country]['recovery_day'] - df[df.country == country]['recovery_day'].shift()) / df[df.country == country]['recovery_day'].shift()*100).replace([np.inf, -np.inf], 0).replace([np.nan], 0).round(2)
    
    # Igualo o valor da primeira linha igual ao primeiro número do acumulado, pois se o acumulado começa em 1 o primeiro diff fica igual a 0
    df.loc[(df.country == country) & (df.day == 1), 'case_day']= df.loc[(df.country == country) & (df.day==1), 'cases']
    df.loc[(df.country == country) & (df.day == 1), 'death_day']= df.loc[(df.country == country) & (df.day==1), 'deaths']
    df.loc[(df.country == country) & (df.day == 1), 'recovery_day']= df.loc[(df.country == country) & (df.day==1), 'recoveries']
    
    # Buscando a população do país e calculado os indicador per milhão
    if not df_countries[df_countries['country']==country].empty:
        million = df_countries[df_countries['country']==country]['PopTotal'].values[0] / 1000
        cases_million = (df[df.country == country]['cases'] / million).round(1)
        deaths_million = (df[df.country == country]['deaths'] / million).round(1)
        recoveries_million = (df[df.country == country]['recoveries'] / million).round(1)
        case_day_million = (df[df.country == country]['case_day'] / million).round(1)
        death_day_million = (df[df.country == country]['death_day'] / million).round(1)
        recovery_day_million = (df[df.country == country]['recovery_day'] / million).round(1)
        
    else:
        cases_million = 0
        deaths_million = 0
        recoveries_million = 0
        case_day_million = 0
        death_day_million = 0
        recovery_day_million = 0
    
    df.loc[df.country == country, 'cases_million'] = cases_million
    df.loc[df.country == country, 'deaths_million'] = deaths_million
    df.loc[df.country == country, 'recoveries_million'] = recoveries_million
    df.loc[df.country == country, 'case_day_million'] = case_day_million
    df.loc[df.country == country, 'death_day_million'] = death_day_million
    df.loc[df.country == country, 'recovery_day_million'] = recovery_day_million
    
    # moving averages (from last 7 days)
    df.loc[df.country == country, 'avg7_cases'] = df[df.country == country]['case_day'].rolling(window=7).mean().replace([np.inf, -np.inf], 0).replace([np.nan], 0).astype('int')
    df.loc[df.country == country, 'avg7_deaths'] = df[df.country == country]['death_day'].rolling(window=7).mean().replace([np.inf, -np.inf], 0).replace([np.nan], 0).astype('int')
    df.loc[df.country == country, 'avg7_recoveries'] = df[df.country == country]['recovery_day'].rolling(window=7).mean().replace([np.inf, -np.inf], 0).replace([np.nan], 0).astype('int')
    
    df.loc[df.country == country, 'avg7_case_day_million'] = df[df.country == country]['case_day_million'].rolling(window=7).mean().replace([np.nan], 0).round(3)
    df.loc[df.country == country, 'avg7_death_day_million'] = df[df.country == country]['death_day_million'].rolling(window=7).mean().replace([np.nan], 0).round(3)
    df.loc[df.country == country, 'avg7_recovery_day_million'] = df[df.country == country]['recovery_day_million'].rolling(window=7).mean().replace([np.nan], 0).round(3)
    

df['perc_death'] = (df['deaths']/df['cases'] * 100).round(2)
df['perc_recovery'] = (df['recoveries']/df['cases'] * 100).round(2)
df['active_cases'] = df['cases'] - df['recoveries'] - df['deaths']

df.fillna(0, inplace=True)

df['day'] = df['day'].astype('int')
df['case_day'] = df['case_day'].astype('int')
df['death_day'] = df['death_day'].astype('int')
df['recovery_day'] = df['recovery_day'].astype('int')

df.tail()


# In[ ]:


#Adjusting wrong negative variations (wrong number from the source)
# df.loc[df.case_day < 0, ['cases']] = df[df.case_day < 0].shift().cases#, ['cases']]
df.loc[df.case_day < 0, ['case_day']] = df[df.case_day < 0].shift().case_day#, ['cases']]
df.loc[df.cases_million < 0, ['cases_million']] = 0#df[df.cases_million < 0].cases_million.shift()#, ['cases']]


# In[ ]:


df.to_csv('../data/world_corona19_data.csv', index = False)


# #### countries not located in UN dataset

# In[ ]:


# for country in countries:
#     if df_countries[df_countries['country']==country]['PopTotal'].empty:
#         print(country)


# ### Brazil data engineering

# In[ ]:


url = 'https://data.brasil.io/dataset/covid19/caso.csv.gz'
response = requests.get(url)
# response.content
with open('/home/rafael/tmp/caso.csv.gz', 'wb') as f:
    f.write(response.content)
    
with gzip.open('/home/rafael/tmp/caso.csv.gz') as f:
    df = pd.read_csv(f)


# In[ ]:


df.rename(columns={'confirmed': 'cases', 'estimated_population_2019':'population', 'order_for_place':'day'}, inplace= True)
df['date'] = df['date'].astype('datetime64[ns]')

df = df[(df['city']!='Importados/Indefinidos')]

df.population.fillna(0, inplace=True)
df.city_ibge_code.fillna(0, inplace=True)

df.population = df.population.astype('int')
df.city_ibge_code = df.city_ibge_code.astype('int')

df.drop(columns=['confirmed_per_100k_inhabitants'], inplace=True)
df.fillna('-', inplace=True)

df.sort_values(['state','city','date'], inplace = True)
df.reset_index(inplace = True, drop=True)

df.tail()


# #### Feature engineering

# In[ ]:


print('Iniciando feature engieering Brasil')
inicio = datetime.datetime.now()

states = df.state.unique()
# states = ['SP']
df.drop(df[df['cases'] == 0 ].index, axis=0, inplace= True)

df['perc_death'] = (df['deaths']/df['cases'] * 100).round(2)
df.rename(columns={'order_for_place': 'day'}, inplace= True)

for state in states:
    cities = df[df['state']==state].city.unique()
#     cities = ['Santa Gertrudes']
    print(datetime.datetime.now().time(), state)
    for city in cities:
        indexes = (df['state']==state) & (df.city == city)
        # valores diários
        df.loc[indexes, 'case_day'] = df[indexes]['cases'].diff()    
        df.loc[indexes, 'death_day'] = df[indexes]['deaths'].diff()

        # Igualo o valor da primeira linha igual ao primeiro número do acumulado, pois se o acumulado começa em 1 o primeiro diff fica igual a 0
        df.loc[(indexes) & (df.day == 1), 'case_day']= df.loc[(indexes) & (df.day==1), 'cases']
        df.loc[(indexes) & (df.day == 1), 'death_day']= df.loc[(indexes) & (df.day==1), 'deaths']

#         % daily variations
        df.loc[indexes, 'var_case_day'] = ((df[indexes]['case_day'].diff())) #/ df[indexes]['case_day'].shift()*100).replace([np.inf, -np.inf], 0).replace([np.nan], 0).round(2)
        df.loc[indexes, 'var_death_day'] = ((df[indexes]['death_day'].diff())) #/ df[indexes]['death_day'].shift()*100).replace([np.inf, -np.inf], 0).replace([np.nan], 0).round(2)

        # Buscando a população do estado/cidade e calculado os indicador per milhar
        if not df[indexes].population.empty:
            thousand = df[indexes]['population'] / 1000
            cases_thousand = (df[indexes]['cases'] / thousand)
            deaths_thousand = (df[indexes]['deaths'] / thousand)
            case_day_thousand = (df[indexes]['case_day'] / thousand)
            death_day_thousand = (df[indexes]['death_day'] / thousand)
        else:
            cases_thousand = 0
            deaths_thousand = 0
            case_day_thousand = 0
            death_day_thousand = 0
            
        df.loc[indexes, 'cases_thousand'] = cases_thousand
        df.loc[indexes, 'deaths_thousand'] = deaths_thousand
        df.loc[indexes, 'case_day_thousand'] = case_day_thousand
        df.loc[indexes, 'death_day_thousand'] = death_day_thousand
        
        # moving averages (from last 7 days)
        df.loc[indexes, 'avg7_cases'] = df[indexes]['case_day'].rolling(window=7).mean()
        df.loc[indexes, 'avg7_deaths'] = df[indexes]['death_day'].rolling(window=7).mean()
        df.loc[indexes, 'avg7_perc_death'] = df[indexes]['perc_death'].rolling(window=7).mean()
        df.loc[indexes, 'avg7_case_day_thousand'] = df[indexes]['case_day_thousand'].rolling(window=7).mean()
        df.loc[indexes, 'avg7_death_day_thousand'] = df[indexes]['death_day_thousand'].rolling(window=7).mean()
    

df.fillna(0, inplace=True)

df['day'] = df['day'].astype('int')
df['case_day'] = df['case_day'].astype('int')
df['death_day'] = df['death_day'].astype('int')


df['cases_thousand'] = df['cases_thousand'].round(3)
df['deaths_thousand'] = df['deaths_thousand'].round(3)
df['case_day_thousand'] = df['case_day_thousand'].round(3)
df['death_day_thousand'] = df['death_day_thousand'].round(3)


df['avg7_cases'] = df['avg7_cases'].replace([np.inf, -np.inf], 0).replace([np.nan], 0).astype('int')
df['avg7_deaths'] = df['avg7_deaths'].replace([np.inf, -np.inf], 0).replace([np.nan], 0).astype('int')
df['avg7_perc_death'] = df['avg7_perc_death'].replace([np.inf, -np.inf], 0).replace([np.nan], 0).round(2)
df['avg7_case_day_thousand'] = df['avg7_case_day_thousand'].replace([np.nan], 0).round(3)
df['avg7_death_day_thousand'] = df['avg7_death_day_thousand'].replace([np.nan], 0).round(3)


termino = datetime.datetime.now()
print('finalizado em ', termino-inicio)
df[indexes].tail()


# In[ ]:


df.to_csv('../data/brazil_corona19_data.csv', index = False)


# In[ ]:


# df[df.city=='Rio Claro'][['population','case_day','death_day','cases_thousand','deaths_thousand','active_cases']]


# In[ ]:


# df[df['country']=='Belgium']
print('Data engineering done!')


# In[ ]:




