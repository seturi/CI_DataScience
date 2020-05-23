import pandas as pd

df = pd.read_csv('data/occupations.csv')

# 코드를 작성하세요.
df.loc[df['gender'] == 'M', 'gender'] = 0
df.loc[df['gender'] == 'F', 'gender'] = 1

gender = df.groupby('occupation').mean()
gender['gender'].sort_values(ascending=False)