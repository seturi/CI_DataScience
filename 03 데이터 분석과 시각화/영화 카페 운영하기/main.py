%matplotlib inline
import pandas as pd
import seaborn as sns

df = pd.read_csv('data/survey.csv')

# 코드를 작성하세요.
movie = df.loc[:,"Horror":"Action"]
corr = movie.corr()
sns.clustermap(corr)