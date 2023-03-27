# selenium의 webdriver를 사용하기 위한 import
from selenium import webdriver

# selenium으로 무엇인가 입력하기 위한 import
from selenium.webdriver.common.keys import Keys

# 페이지 로딩을 기다리는데에 사용할 time 모듈 import
import time

# 크롬드라이버 실행  (경로 예: '/Users/Roy/Downloads/chromedriver')
driver = webdriver.Chrome("C:\chromedriver.exe") 

#크롬 드라이버에 url 주소 넣고 실행
driver.get('https://www.foodbank1377.org/reference/promote.do')

# 페이지가 완전히 로딩되도록 3초동안 기다림
time.sleep(3)
search_box = driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/ul/li[1]/a/span')

# click 함수는 ()안에 아무것도 넣지 않으면 좌클릭을 수행
search_box.click()
