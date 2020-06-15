import requests
from bs4 import BeautifulSoup

# 코드를 작성하세요
response = requests.get("https://workey.codeit.kr/music/index")
soup = BeautifulSoup(response.text, 'html.parser')
rank_tags = soup.select(".rank__order li")

search_ranks = []
for rank in rank_tags:
    artist = rank.text.strip().split(" ")[2]
    search_ranks.append(artist)

# 결과 출력
print(search_ranks)