import unittest
from unittest import TestCase
from selenium import webdriver
from pages.pages.ObjExtra import Extra

class TestPageExtra(TestCase):

    def setUp(self):
        self.driver=webdriver.Chrome()
        self.page_Extra=Extra(self.driver)
        self.driver.get('https://www.extra.com.br')

    def test_search(self):
        self.page_Extra.botao()
        assert 'JOÃO DIAS' in self.driver.title

    def tearDown(self):
        self.driver.close()

unittest.main()