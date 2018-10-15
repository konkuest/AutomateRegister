#-*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common import action_chains
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import xlrd
from collections import OrderedDict

from register_ssobing import *

'''
#참고사항
- 지금까지의 모든 거래 기록을 2017-01-01 부터 현재 날짜까지 다운로드 (변경가능)
- 다운로드 경로는 브라우저가 기본으로 설정된 다운로드 위치 (Download 폴더)
'''

#1 Login 이후 주문 리스트로 이동
id = '#id'
pw = '#pw'

ssobing_login(id, pw)
driver.get("http://www.ssobing.com/selleradmin/order/catalog")
driver.maximize_window()

#가능하면 다운로드 받는 폴더 Path 지정 가능하게 세팅하면 좋을 듯

#2 정보 세팅
def download_setting():
    selectall_btn = driver.find_elements_by_xpath("//span[@class='icon-check hand all-check']")

    start = '2018-09-01'
    end = '2018-10-01'

    #시작일을 2017-01-01로 설정, 마감일은 수집하는 날짜로 서버가 자동설정 해줌
    #input에 .send_keys가 아니라 value 값을 바꾸는 javascript를 실행해야 함
    collecting_date = driver.find_elements_by_xpath("//input[@name='regist_date[]']")
    driver.execute_script("arguments[0].setAttribute('value','2017-01-01')", collecting_date[0]) #변경가능

    selectall_btn[0].click() #Before 출고
    selectall_btn[1].click() #After 출고 이후

    start_collect_btn = driver.find_elements_by_xpath("//button[@type='submit']")
    start_collect_btn[0].click()


def download_action():
    sleep(3)

    #전체선택
    select_ops = driver.find_elements_by_xpath("//span[@class='custom-select-box-btn btn drop_multi_main']")
    select_ops[0].click()
    sleep(2)

    #양식선택
    select_form = driver.find_element_by_xpath("//select[@id='select_down_35']")
    sleep(2)
    select_btn = driver.find_element_by_xpath("//span[@class='custom-select-box-btn btn drop']")
    select_btn.click()
    sleep(3)
    select_basic = driver.find_elements_by_xpath("//span[contains(text(), '기본양식_파인애플')]")
    select_basic[0].click()

    #Download
    down_btn = driver.find_element_by_xpath("//button[@name='excel_down']")
    down_btn.click()

    #Delivery
    deliv_methods = driver.find_elements_by_xpath("//input[@name='excel_search_shipping_method[]']")
    for i in deliv_methods:
        i.click()

    #final_download
    final_down = driver.find_element_by_xpath("//span[@class='btn large gray']")
    final_down.click()

download_setting()
download_action()