import pandas as pd

df = pd.read_csv('data/enrolment_2.csv')

# 코드를 작성하세요.
df['room assignment'] = 'not assigned'
students = df['course name'].value_counts()

auditorium = list((students[students >= 80]).index)
large = list(students[(students >= 40) & (students < 80)].index)
medium =list(students[(students >= 15) & (students < 40)].index)
small = list(students[(students >= 5) & (students < 15)].index)

for i in auditorium:
    df.loc[df['course name'] == i, 'room assignment'] = 'Auditorium'

for i in large:
    df.loc[df['course name'] == i, 'room assignment'] = 'Large room'

for i in medium:
    df.loc[df['course name'] == i, 'room assignment'] = 'Medium room'

for i in small:
    df.loc[df['course name'] == i, 'room assignment'] = 'Small room'

df.loc[df['status'] == 'not allowed', 'room assignment'] = 'not assigned'

# 정답 출력
df