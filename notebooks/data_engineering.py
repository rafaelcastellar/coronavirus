#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from pandas.io.json import json_normalize
import json, requests


# #### Fetching worldwide data

# In[2]:


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

# In[3]:


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

# In[4]:


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
        cases_million = (df[df.country == country]['case_day'] / million).round(1)
        deaths_million = (df[df.country == country]['death_day'] / million).round(1)
        recoveries_million = (df[df.country == country]['recovery_day'] / million).round(1)
    else:
        cases_million = 0
        deaths_million = 0
        recoveries_million = 0
        
    df.loc[df.country == country, 'cases_million'] = cases_million
    df.loc[df.country == country, 'deaths_million'] = deaths_million
    df.loc[df.country == country, 'recoveries_million'] = recoveries_million
    
    # moving averages (from last 7 days)
    df.loc[df.country == country, 'avg7_cases'] = df[df.country == country]['case_day'].rolling(window=7).mean().replace([np.inf, -np.inf], 0).replace([np.nan], 0).astype('int')
    df.loc[df.country == country, 'avg7_deaths'] = df[df.country == country]['death_day'].rolling(window=7).mean().replace([np.inf, -np.inf], 0).replace([np.nan], 0).astype('int')
    df.loc[df.country == country, 'avg7_recoveries'] = df[df.country == country]['recovery_day'].rolling(window=7).mean().replace([np.inf, -np.inf], 0).replace([np.nan], 0).astype('int')
    
    df.loc[df.country == country, 'avg7_cases_million'] = df[df.country == country]['cases_million'].rolling(window=7).mean().replace([np.inf, -np.inf], 0).replace([np.nan], 0).astype('int')
    df.loc[df.country == country, 'avg7_deaths_million'] = df[df.country == country]['deaths_million'].rolling(window=7).mean().replace([np.inf, -np.inf], 0).replace([np.nan], 0).astype('int')
    df.loc[df.country == country, 'avg7_recoveries_million'] = df[df.country == country]['recoveries_million'].rolling(window=7).mean().replace([np.inf, -np.inf], 0).replace([np.nan], 0).astype('int')
    

df['perc_death'] = (df['deaths']/df['cases'] * 100).round(2)
df['perc_recovery'] = (df['recoveries']/df['cases'] * 100).round(2)
df['active_cases'] = df['cases'] - df['recoveries'] - df['deaths']

df.fillna(0, inplace=True)

df['day'] = df['day'].astype('int')
df['case_day'] = df['case_day'].astype('int')
df['death_day'] = df['death_day'].astype('int')
df['recovery_day'] = df['recovery_day'].astype('int')

df.tail()


# #### Gravando CSV

# In[5]:


df.to_csv('../data/corona19_world_data.csv', index = False)


# In[6]:


df[df['country']=='Brazil'].tail()


# #### countries not located in UN dataset

# In[7]:


for country in countries:
    if df_countries[df_countries['country']==country]['PopTotal'].empty:
        print(country)
# df[df['pais'] == pais].tail()
# df_countries[df_countries['Location']==pais]['PopTotal']


# In[ ]:



