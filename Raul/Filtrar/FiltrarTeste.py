import unittest
from unittest import TestCase
from selenium import webdriver

class TestPageExtra(TestCase):

    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.get('https://www.extra.com.br')
        assert 'Extra.com.br: o site da família e a maior loja de Informática do Brasil' in self.driver.title

    def teste_pesquisa(self):
       self.driver.find_element_by_xpath('//*[@id="ctl00_TopBar_PaginaSistemaArea1_ctl10_ctl00_txtBusca"]').send_keys('Celular')
       self.driver.find_element_by_xpath('//*[@id="ctl00_TopBar_PaginaSistemaArea1_ctl10_ctl00_btnOK"]').click()
       assert 'Celular no Extra.com.br' in self.driver.title

    def teste_filtros(self):
       self.driver.implicitly_wait(10)
       self.driver.find_element_by_xpath('//*[@id="neemu-search-filters"]/li[1]/ul/li[1]/ul/li[1]/ul/li[1]/a').click()
 # assert 'https://buscando2.extra.com.br/busca?q=Celular&common_filter[1]=144290' in self.driver.address


    def tearDown(self):
        self.driver.close()

unittest.main()