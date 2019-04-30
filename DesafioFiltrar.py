from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
browser=webdriver.Chrome()
browser.get('https://www.extra.com.br/')
element=browser.find_element_by_xpath('//*[@id="ctl00_TopBar_PaginaSistemaArea1_ctl10_ctl00_txtBusca"]')
element.send_keys('Celular')
element.send_keys(u'\ue007')
time.sleep(1)
browser.implicitly_wait(5)
element2=browser.find_element_by_xpath('//*[@id="neemu-search-filters"]/li[1]/ul/li[1]/ul/li[1]/ul/li[1]/a/span[1]')
element2.click()
element3=browser.find_element_by_xpath('//*[@id="neemu-search-filters"]/li[2]/ul/li[2]/a/span[1]')
element3.click()