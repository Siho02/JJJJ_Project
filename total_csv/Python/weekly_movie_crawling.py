from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import time
import re
# option 버튼 선택하려고 추가함
from selenium.webdriver.support.select import Select
# alert 버튼 눌를려고 추가함
# from selenium.webdriver.common.alert import Alert


def weekly_movie():

    main_url = "https://www.kobis.or.kr/kobis/business/stat/boxs/findWeeklyBoxOfficeList.do"
    results = []
    total_revenu = 0
    total_attendance = 0

    driver = webdriver.Chrome("c:/driver/chromedriver.exe")
    driver.get(main_url)
    time.sleep(3)
    driver.implicitly_wait(2)


    # option버튼 눌러서 선택지 고르는법
    comboBox = Select(driver.find_element_by_css_selector("#sWeekGb"))
    comboBox.select_by_index(0)
    time.sleep(1)

    # 조회버튼
    Lookup = driver.find_element_by_css_selector("#searchForm > div > div.wrap_btn > button")
    Lookup.click()
    time.sleep(4)

    # 데이터를 전부 크롤링 하기위해서 더보기 버튼을 끝까지 누르게 하는 코드 (마지막에 더보기 대신에 닫기가나옴)
    plus_btn = driver.find_element_by_css_selector("#btn_0").text 
    while plus_btn == "더보기":
        Lookup = driver.find_element_by_css_selector("#btn_0")
        Lookup.click()
        time.sleep(1)
        plus_btn = driver.find_element_by_css_selector("#btn_0").text


    soup = BeautifulSoup(driver.page_source, "lxml")

    naljja = soup.select("#content > div.rst_sch > div:nth-child(2) > h4")[0].text
    naljja = re.findall("\d+", naljja)
    naljja = naljja[0]
    print(naljja)

    boxitem = soup.select("tbody#tbody_0 > tr")
    time.sleep(3)

    try:
        for item in boxitem:
            revenu = item.select("tr > td:nth-child(4)")[0].text
            attendance = item.select("tr > td:nth-child(8)")[0].text
            
            # 특수문자 제거후 공백제거
            pattern = re.compile(r'\s+')
            revenu = re.sub(pattern, '', revenu)
            attendance = re.sub(pattern, '', attendance)

            # "제거
            revenu = re.sub('"', '', revenu)
            attendance = re.sub('"', '', attendance)

            # ,제거
            revenu = re.sub(',', '', revenu)
            attendance = re.sub(',', '', attendance)

            # str -> float 형태로 
            revenu = float(revenu)
            attendance = float(attendance)

            # 값들 더해주기
            total_revenu += revenu
            total_attendance += attendance

    except Exception as e:
            print("페이지 파싱 에러", e)

    finally:
        time.sleep(3)
        print("크롤링을 종료합니다.")

        data = [total_revenu,0, total_attendance,0 ,"2021_"+naljja]
        results.append(data)

        df = pd.DataFrame(results)
        df.columns = ['매출액','매출액증감', '관객수','관객수증감' ,'연도주차']
        df['매출액'] = df['매출액'] / 1000000
        df['관객수'] = df['관객수'] / 1000000


        df.to_csv(f'./new_csv/2021_{naljja}.csv', index = False)
        data = "크롤링완료"
        driver.close()

if __name__=='__main__':
    weekly_movie()
