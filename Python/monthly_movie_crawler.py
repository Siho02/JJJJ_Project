from selenium import webdriver

# option 버튼 선택하려고 추가함
from selenium.webdriver.support.select import Select
# alert 버튼 눌를려고 추가함
from selenium.webdriver.common.alert import Alert

#시간과 날짜를 받을 수 있는 모듈
from datetime import datetime
from datetime import date

import pandas as pd
import time
import os
import shutil

def crawl_data():
    #데이터를 가져올 사이트
    main_url = "https://www.kobis.or.kr/kobis/business/stat/boxs/findMonthlyBoxOfficeList.do"
    
    #크롬 드라이버 명명
    driver = webdriver.Chrome("c:/driver/chromedriver.exe")
    driver.get(main_url)
    
    time.sleep(3)
    driver.implicitly_wait(2)
    
    #엑셀 버튼 클릭   
    Lookup = driver.find_element_by_css_selector("#content > div.f_sch > div > a")
    Lookup.click()

    #엑섹 버튼 클릭 후 나오는 alert창에서 확인을 누름
    da = Alert(driver)
    da.accept()

    #대기 후 크롬드라이버 종료(자원 반환)
    time.sleep(3)
    driver.implicitly_wait(5)
    driver.close()

#크롤링하여 저장한 엑셀 데이터를 이름을 변경하여 저장하는 기능
def move_excel_change_name():
    date_now = datetime.now()
    filepath = 'C:/Users/xodlr_000/Downloads'
    filename = max([filepath + '/' + f for f in os.listdir(filepath)], key=os.path.getctime)

    #다운로드 디렉토리에서 오른쪽 주소의 디렉토리로 이동
    shutil.move(filename, 'C:/202105_lab/09.ELKStack/JJJJ_Project/Movie_CSV/month/')

    #현재 날짜의 월을 받아와 이름을 준비하기 위한 과정
    if date_now.month < 10:
        month_str = '0'+str(date_now.month)
    else:
        month_str = str(date_now.month)

    filepath = 'C:/202105_lab/09.ELKStack/JJJJ_Project/Movie_CSV/month'

    #가장 마지막에 생긴 파일명을 filename에 저장
    filename = max([filepath + '/' + f for f in os.listdir(filepath)], key=os.path.getctime)
    
    #파일의 경로와 이름을 합쳐서 src에 저장
    src = os.path.join(filepath, filename)
    #src의 경로와 파일명을 가진 파일을 오른쪽 2021_month.xls로 저장
    os.rename(src, filepath +'/2021'+ month_str+'.xls')

#python 파일이 실행되면 오늘 날짜가 1일인지 확인후 crawl_data()를 실행
if __name__=="__main__":
    if date.today().day == 1:
        crawl_data()
        move_excel_change_name()
    else :
        print("오늘은 1일이 아닙니다") 
        pass


