from selenium import webdriver
from bs4 import BeautifulSoup
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re

def create_browser(url):
    # headless, user-agent
    options = webdriver.ChromeOptions()
    options.headless = True
    options.add_argument("window-size=1920x1080")
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36")

    # browser 생성
    browser = webdriver.Chrome(options=options)
    browser.get(url)

    return browser

def scrape_reproduct_data(browser, casnum):
    
    # 카스번호 검색
    elem = browser.find_element_by_id("searchKeyword")
    elem.send_keys(casnum)
    elem.send_keys(Keys.ENTER)
    
    
    elem = browser.find_element_by_xpath("//*[@id='Container']/div[2]/div[5]/table/tbody")
    print (elem.text)
    if "71-43-2" in elem.text:
        elem = elem.find_element_by_partial_link_text("71-43-2")

        print("a 태그", elem.text)
        elem.click()
    else :
        return("자료없음")

    try:
        elem = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='Title11']")))
    except:
        print("로딩이 깁니다. 브라우저를 끕니다.")
        browser.quit()

    # 독성에 관한 정보 클릭
    elem = browser.find_element_by_id("Title11")
    elem.click()

    # 생식독성 data 가져오기
    elem = browser.find_element_by_xpath("//*[@id='Contents11']/ul/li[2]/dl/dd[13]")
    return elem.text


