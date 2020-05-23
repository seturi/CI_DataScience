%matplotlib inline
import pandas as pd

df = pd.read_csv('data/starbucks_drinks.csv')

# 코드를 작성하세요.
# df['Calories'].plot(kind='box')
df.plot(kind='box', y='Calories')