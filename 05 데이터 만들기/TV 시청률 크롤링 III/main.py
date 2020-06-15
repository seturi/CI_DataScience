import requests
from bs4 import BeautifulSoup

# 코드를 작성하세요.
rating_pages = []

for year in range(2010, 2019):
    for month in range(1, 13):
        for week in range(0, 5):
            url = "https://workey.codeit.kr/ratings/index?year={0}&month={1}&weekIndex={2}".format(year, month, week)
            response = requests.get(url)
            
            soup = BeautifulSoup(response.text, 'html.parser')
            row_tags = soup.select(".row")
            
            if len(row_tags) > 1:
                rating_pages.append(response.text)


# 테스트 코드
print(len(rating_pages)) # 가져온 총 페이지 수 
print(rating_pages[0]) # 첫 번째 페이지의 HTML 코드