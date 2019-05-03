class ObjFiltrar:
    
   def __init__(self,driver):
      self.driver=driver
      self.URL='https://www.extra.com.br/'
      self.INPUTSEARCH='//*[@id="ctl00_TopBar_PaginaSistemaArea1_ctl10_ctl00_txtBusca"]'
      self.BOTAO='//*[@id="ctl00_TopBar_PaginaSistemaArea1_ctl10_ctl00_btnOK"]'
      self.PESQUISA='Celular'    
      self.FILTRAR1='//*[@id="neemu-search-filters"]/li[1]/ul/li[1]/ul/li[1]/ul/li[1]/a/span[1]'
      self.FILTRAR2='//*[@id="neemu-search-filters"]/li[2]/ul/li[2]/a/span[1]'
      self.FILTRAR3='//*[@id="neemu-search-filters"]/li[4]/ul/li[1]/a/span[1]'

   def home_extra(self):
       self.driver.get(self.URL)

   def pesquisar(self):
       self.driver.find_element_by_xpath(self.INPUTSEARCH).send_keys(self.PESQUISA)
       self.driver.find_element_by_xpath(self.BOTAO).click()

   def filtrar1(self):
       self.driver.implicitly_wait(10)
       self.driver.find_element_by_xpath(self.FILTRAR1).click()
       self.driver.implicitly_wait(10)

   def filtrar2(self):
       self.driver.implicitly_wait(10)
       self.driver.find_element_by_xpath(self.FILTRAR2).click()
       self.driver.implicitly_wait(10)

   def filtrar3(self):
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath(self.FILTRAR3).click()
        self.driver.implicitly_wait(10)
    