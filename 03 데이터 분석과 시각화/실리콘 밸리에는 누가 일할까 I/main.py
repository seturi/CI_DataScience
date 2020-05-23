%matplotlib inline
import pandas as pd

df = pd.read_csv('data/silicon_valley_summary.csv')

# 코드를 작성하세요.
people = df[(df['job_category'] == 'Managers') & (df['gender'] == 'Male') & (df['race_ethnicity'] != 'All')] 
people.plot(kind='bar', x='race_ethnicity', y='count')