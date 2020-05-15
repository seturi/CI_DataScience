import pandas as pd

# 코드를 작성하세요.
list = [
    {'name': 'Taylor Swift', 'birthday':'December 13, 1989', 'occupation':'Singer-songwriter'},
    {'name': 'Aaron Sorkin', 'birthday':'June 9, 1961', 'occupation':'Screenwriter'},
    {'name': 'Harry Potter', 'birthday':'July 31, 1980', 'occupation':'Wizard'},
    {'name': 'Ji-Sung Park', 'birthday':'February 25, 1981', 'occupation':'Footballer'}
]
df = pd.DataFrame(list, columns=['name', 'birthday', 'occupation'])

# 정답 출력
df