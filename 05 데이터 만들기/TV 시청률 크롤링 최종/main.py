import pandas as pd
import requests
from bs4 import BeautifulSoup

# 코드를 작성하세요.

# 기간 지정
years = list(range(2010, 2019))
months = list(range(1, 13))
weeks = list(range(0, 5))

# 페이지를 담는 빈 리스트 생성
rating_pages = []

for year in years:
    for month in months:
        for week in weeks:
            # HTML 코드 받아오기
            url = "https://workey.codeit.kr/ratings/index?year={0}&month={1}&weekIndex={2}".format(year, month, week)
            response = requests.get(url)

            # BeautifulSoup 타입으로 변환하기
            soup = BeautifulSoup(response.text, 'html.parser')

            # "row" 클래스가 1개를 넘는 경우만 페이지를 리스트에 추가
            if len(soup.select('.row')) > 1:
                rating_pages.append(soup)

# 레코드를 담는 빈 리스트 만들기
records = []

# 각 페이지 파싱해서 정보 얻기
for page in rating_pages:
    date = page.select('option[selected=selected]')[2]
    rank = page.select('.row .rank')[1:]
    channel = page.select('.row .channel')[1:]
    program = page.select('.row .program')[1:]
    percent = page.select('.row .percent')[1:]

    # 페이지에 있는 10개의 레코드를 리스트에 추가
    for i in range(10):
        record = []
        record.append(date.text)
        record.append(rank[i].text)
        record.append(channel[i].text)
        record.append(program[i].text)
        record.append(percent[i].text)
        records.append(record)

# DataFrame 만들기
df = pd.DataFrame(data=records, columns=['period', 'rank', 'channel', 'program', 'rating'])

# 결과 출력
df.head()