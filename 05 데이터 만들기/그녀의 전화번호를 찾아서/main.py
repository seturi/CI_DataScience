import requests
from bs4 import BeautifulSoup

# 코드를 작성하세요
response = requests.get("https://workey.codeit.kr/orangebottle/index")
soup = BeautifulSoup(response.text, 'html.parser')
num_tags = soup.select(".phoneNum")

phone_numbers = []
for num in num_tags:
    phone_numbers.append(num.text)

# 결과 출력
print(phone_numbers)