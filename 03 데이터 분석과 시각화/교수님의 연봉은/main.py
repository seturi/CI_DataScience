%matplotlib inline
import pandas as pd
import seaborn as sns

df = pd.read_csv('data/salaries.csv')

# 코드를 작성하세요.
sns.violinplot(df['salary'])