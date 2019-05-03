from selenium.webdriver.support.ui import Select

class Extra:

    def __init__(self,driver):
        self.driver=driver
        self.LOCAL='//*[@id="ulServicos"]/li[4]/a' 
        self.ESTADOSP = '//*[@id="state"]'
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

        self.driver.maximize_window()

        self.driver.switch_to_window(self.driver.window_handles[1])
        self.driver.implicitly_wait(3)
        
        self.driver.implicitly_wait(7)
        
        Select(self.driver.find_element_by_xpath(self.ESTADOSP)).select_by_value('São Paulo')
        self.driver.implicitly_wait(3)

        Select(self.driver.find_element_by_xpath(self.CIDADE)).select_by_value('São Paulo')
        self.driver.implicitly_wait(3)

        Select(self.driver.find_element_by_xpath(self.BAIRRO)).select_by_value('Jardim São Luís')
        self.driver.implicitly_wait(3)

    def pesquisar(self):
        self.driver.find_element_by_xpath(self.BOTAO).click()



