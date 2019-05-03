class Extra:
    def __init__(self,driver):
        self.driver=driver
        self.URL='https://www.extra.com.br'
        self.PESQUISA='//*[@id="ctl00_TopBar_PaginaSistemaArea1_ctl10_ctl00_txtBusca"]'
        self.BUSCAR='//*[@id="ctl00_TopBar_PaginaSistemaArea1_ctl10_ctl00_btnOK"]'
        self.SMARTPHONE='//*[@id="nm-product-10941024"]/div/div[1]/a/img'
        self.LISTA='//*[@id="ctl00_Conteudo_ctl28_hplListaCasamento"]'

    def go_home(self):
        self.driver.get(self.URL)

    def go_pesquisa(self):
        element=self.driver.find_element_by_xpath(self.PESQUISA)
        element.send_keys('Xiaomi')
        element.click()

    def go_buscar(self):
        element=self.driver.find_element_by_xpath(self.BUSCAR)
        element.click()
        self.driver.implicitly_wait(2)

    def go_smartphone(self):
        element=self.driver.find_element_by_xpath(self.SMARTPHONE)
        element.click()
        self.driver.implicitly_wait(2)

    def go_lista(self):
        element=self.driver.find_element_by_xpath(self.LISTA)
        element.click() 