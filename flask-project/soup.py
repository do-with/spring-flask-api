import requests 
from bs4 import BeautifulSoup

def title_check():
    url = "https://www.foodbank1377.org/reference/notice.do" 
    res = requests.get(url) 
    res.raise_for_status() # 정상 200
    soup = BeautifulSoup(res.content, "html.parser")
    titleBox = soup.find_all('td', class_="title") # 전체 영역에서 'a' 태그를 찾지 않고 인기 급상승 영역으로 범위 제한4
    board_title = []
    for title in titleBox:
        board_title.append(title.get_text().strip().encode('utf-8'))
    return board_title
    

