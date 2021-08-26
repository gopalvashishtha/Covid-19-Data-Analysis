
import pandas as pd
import requests

url = 'https://en.wikipedia.org/wiki/COVID-19_pandemic_by_country_and_territory'
req = requests.get(url)
data_list = pd.read_html(req.text)
target_df=data_list[8]

target_df.columns = ['Col0', 'Country Name', 'Total Cases', 'Total Deaths', 'Total Recoveries', 'Col5']

target_df=target_df[['Country Name', 'Total Cases', 'Total Deaths', 'Total Recoveries']]

last_idx=target_df.index[-1]
target_df=target_df.drop([last_idx, last_idx-1])

target_df['Country Name']=target_df['Country Name'].str.replace('\[.*\]', '')

target_df['Total Recoveries']=target_df['Total Recoveries'].str.replace('No data', '0')



target_df['Total Deaths']=target_df['Total Deaths'].replace(to_replace="60+",value=60)

target_df['Total Cases']=pd.to_numeric(target_df['Total Cases'])
target_df['Total Deaths']=pd.to_numeric(target_df['Total Deaths'])
target_df['Total Recoveries']=pd.to_numeric(target_df['Total Recoveries'])

target_df.to_excel(r'covid19_analysis.xlsx')

