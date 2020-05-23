import pandas as pd

df = pd.read_csv('data/occupations.csv')

# 코드를 작성하세요.
occ_group = df.groupby('occupation')
occ_group.mean().sort_values(by='age')