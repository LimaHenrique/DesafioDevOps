import unittest
from unittest import TestCase
from selenium import webdriver
from pages.pages.Extra_page import Extra

class TestePageExtra(TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome('driver\chromedriver')
        self.pesquisa_extra=Extra(self.driver)
        self.driver.get('https://www.extra.com.br')

    def test_xiaomi(self):
        #o nome da função de teste tem que ser test_alguma_coisa
        self.pesquisa_extra.go_pesquisa()
        self.pesquisa_extra.go_buscar()
        self.pesquisa_extra.go_smartphone()
        self.pesquisa_extra.go_lista()

    def tearDown(self):
        self.driver.close()

unittest.main()