import pandas as pd

df = pd.read_csv('data/enrolment_3.csv')

# 코드를 작성하세요.
df.rename(columns={'room assignment':"room number"}, inplace=True)

aud = sorted(list(df.loc[df['room number'] == 'Auditorium', 'course name'].value_counts().index))
large = sorted(list(df.loc[df['room number'] == 'Large room', 'course name'].value_counts().index))
medium = sorted(list(df.loc[df['room number'] == 'Medium room', 'course name'].value_counts().index))
small = sorted(list(df.loc[df['room number'] == 'Small room', 'course name'].value_counts().index))

for i in range(len(aud)):
    audNum = "Auditorium-" + str(i + 1)
    df.loc[df['course name'] == aud[i], 'room number'] = audNum

for i in range(len(large)):
    larNum = "Large-" + str(i + 1)
    df.loc[df['course name'] == large[i], 'room number'] = larNum

for i in range(len(medium)):
    medNum = "Medium-" + str(i + 1)
    df.loc[df['course name'] == medium[i], 'room number'] = medNum
    
for i in range(len(small)):
    smaNum = "Small-" + str(i + 1)
    df.loc[df['course name'] == small[i], 'room number'] = smaNum
    
df.loc[df['status'] == 'not allowed', 'room number'] = 'not assigned'

# 정답 출력
df