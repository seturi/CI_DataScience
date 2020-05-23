import pandas as pd

df = pd.read_csv('data/museum_1.csv')

# 코드를 작성하세요.
# df['분류']='일반'
# univ = df[df['시설명'].str.contains('대학')].index
# df.loc[univ, '분류'] = '대학'

is_university = df['시설명'].str.contains('대학교')
df.loc[is_university == True, '분류'] = '대학'
df.loc[is_university == False, '분류'] = '일반'
df