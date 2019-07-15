# from selenium import webdriver
#
# driver = webdriver.Chrome()  # Optional argument, if not specified will search path.
# driver.get('https://www.baidu.com') # 获取百度页面
#
# input = driver.find_element_by_id('kw')
# search = driver.find_element_by_id('su')
# input.send_keys("你好我是你爹")
# search.click()
# import os
# os.chdir(r'E:\a small program every day\selenium')
# from selenium import webdriver
# from selenium.webdriver.support.wait import WebDriverWait # 用于实例化一个Driver的显式等待
# from selenium.webdriver.common.by import By # 内置定位器策略集
# from selenium.webdriver.support import expected_conditions as EC # 内置预期条件函数，具体API请参考此小节后API链接
#
# driver = webdriver.Chrome()
# driver.get('https://www.bilibili.com/v/game/esports/?spm_id_from=333.334.primary_menu.35#/9222')
# try:
#     WebDriverWait(driver, 20, 0.5).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'vd-list'))) #使用expected_conditions自带验证函数
#     for doctorName in driver.find_elements_by_css_selector('.vd-list li'):
#         print(doctorName.find_element_by_css_selector('.r > a').text)
# finally:
#     driver.close()


import time
from  selenium import webdriver


drive = webdriver.Chrome()

drive.get("https://www.bilibili.com")
time.sleep(5)
with open('a.txt', 'w+', encoding='utf-8') as f:
    f.write(drive.page_source)
#print(drive.page_source)
drive.close()
