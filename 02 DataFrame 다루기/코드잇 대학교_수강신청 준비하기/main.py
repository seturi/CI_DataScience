import pandas as pd

df = pd.read_csv('data/enrolment_1.csv')

# 코드를 작성하세요.
df['status'] = 'allowed'
case1 = (df['course name'] == 'information technology') & (df['year'] == 1 )
df.loc[case1, 'status'] = 'not allowed'
case2 = (df['course name'] == 'commerce') & (df['year'] == 4)
df.loc[case2, 'status'] = 'not allowed'
case3 = df['course name'].value_counts() < 5
lists = list(case3[case3].index)
for i in lists:
    df.loc[df['course name'] == i, 'status'] = 'not allowed'


# 정답 출력
df