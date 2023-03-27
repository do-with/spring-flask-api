import requests 
from bs4 import BeautifulSoup

def notice_check():
    url = "https://www.foodbank1377.org/reference/promote.do" 
    res = requests.get(url) 
    res.raise_for_status() # 정상 200
    soup = BeautifulSoup(res.content, "html.parser")
    titleBox = soup.find_all('li', class_="grid-item") # 전체 영역에서 'a' 태그를 찾지 않고 인기 급상승 영역으로 범위 제한4
    notice_title = []
    for title in titleBox:
        notice_title.append(title.get_text().strip().encode('utf-8'))
    return notice_title

def notice_link():
    url = "https://www.foodbank1377.org/reference/promote.do" 
    res = requests.get(url) 
    res.raise_for_status() # 정상 200
    soup = BeautifulSoup(res.content, "html.parser")
    #titleBox = soup.find_all('div',class_='bd-contents') # 전체 영역에서 'a' 태그를 찾지 않고 인기 급상승 영역으로 범위 제한4
    titleBox = soup.find_all('em') # 전체 영역에서 'a' 태그를 찾지 않고 인기 급상승 영역으로 범위 제한4
    notice_link = []
    for title in titleBox:
        notice_link.append(title.get_text().strip())
    return notice_link
    

