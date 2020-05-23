%matplotlib inline
import pandas as pd

df = pd.read_csv('data/silicon_valley_details.csv')

# 코드를 작성하세요.
adobe = (df['company'] == 'Adobe')
zero = (df['count'] != 0)
job = (df['job_category'] != 'Totals') & (df['job_category'] !='Previous_totals')
race = (df['race'] == 'Overall_totals')

people = df[ adobe & zero & job & race]
people.set_index('job_category', inplace=True)
people.plot(kind='pie', y='count')