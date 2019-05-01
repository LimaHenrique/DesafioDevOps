class Extra:

    def __init__(self,driver):
        self.driver=driver
        self.LOCAL='//*[@id="ulServicos"]/li[4]/a'
        self.ESTADO='//*[@id="state"]'
        self.ESTADOSP = '//*[@id="state"]/option[17]'
        self.CIDADE='//*[@id="city"]'
        self.BAIRRO='//*[@id="neighborhood"]'
        self.SP='São Paulo'
        self.JDSL='Jardim São Luis'
        self.BOTAO='/html/body/div/div/div/div[2]/div[2]/div[2]/a'
        self.URL= "https://www.extra.com.br/"

    def home_extra(self):
        self.driver.get(self.URL)

    def botao(self):
        self.driver.implicitly_wait(3)
        self.driver.find_element_by_xpath(self.LOCAL).click()

    def localizacao(self):

        self.driver.find_element_by_xpath(self.ESTADO).click().send_keys(self.SP).click()
        self.driver.implicitly_wait(3)

        self.driver.find_element_by_xpath(self.CIDADE).click().send_keys(self.SP).click()
        self.driver.implicitly_wait(3)

        self.driver.find_element_by_xpath(self.BAIRRO).click().send_keys(self.JDSL).click()
        self.driver.implicitly_wait(3)

    def pesquisar(self):
        self.driver.find_element_by_xpath(self.BOTAO).click()
