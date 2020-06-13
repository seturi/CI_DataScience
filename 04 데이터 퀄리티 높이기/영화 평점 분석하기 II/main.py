%matplotlib inline
import pandas as pd

df = pd.read_csv('data/movie_metadata.csv')

# 코드를 작성하세요.
top15 = df['budget'].sort_values(ascending=False).head(15)
df.drop(top15.index, inplace=True)
df.plot(kind='scatter', x='budget', y='imdb_score')