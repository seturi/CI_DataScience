import requests

# 코드를 작성하세요
page = requests.get("https://workey.codeit.kr/ratings/index")
rating_page = page.text

# 출력 코드
print(rating_page)
