import unittest
from unittest import TestCase
from selenium import webdriver
from pages.pages.extra_pesquisa import Extra

class TestPageExtra(TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome('driver/chromedriver')
        self.extra_pesquisa=Extra(self.driver)
        self.driver.get('https://www.extra.com.br')

    def test_search(self):
        self.extra_pesquisa.search()
        self.extra_pesquisa.search_2()
        self.extra_pesquisa.search_3()
        self.extra_pesquisa.search_4()
        self.extra_pesquisa.search_5()

    def tearDown(self):
        self.driver.close()

unittest.main()