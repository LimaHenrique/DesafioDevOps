class Extra:
    def __init__(self,driver):
        self.driver=driver
        self.ITEM='//*[@id="ctl00_TopBar_PaginaSistemaArea1_ctl10_ctl00_txtBusca"]'
        self.PESQUISA='//*[@id="ctl00_TopBar_PaginaSistemaArea1_ctl10_ctl00_btnOK"]'
        self.JOGO='//*[@id="nm-product-11133458"]/div/div[1]/a/img'
        self.FRETE='//*[@id="ctl00_Conteudo_ctl36_txtCep"]'
        self.CALCULA='//*[@id="btnCalculoFrete"]'
        self.URL='https://www.extra.com.br'

    def home(self):
        self.driver.get(self.URL)

    def search(self):
        element=self.driver.find_element_by_xpath(self.ITEM)
        element.send_keys('PS4 jogos')
        element.click()

    def search_2(self):
        element=self.driver.find_element_by_xpath(self.PESQUISA)
        element.click()

    def search_3(self):
        element=self.driver.find_element_by_xpath(self.JOGO)
        element.click()
        self.driver.implicitly_wait(2)

    def search_4(self):
        element=self.driver.find_element_by_xpath(self.FRETE)
        element.send_keys('05802-140')
        element.click()
        self.driver.implicitly_wait(2)

    def search_5(self):
        element=self.driver.find_element_by_xpath(self.CALCULA)
        element.click()
        self.driver.implicitly_wait(2)