class ObjLogin:
    
   def __init__(self,driver):
      self.driver=driver
      self.URL='https://www.extra.com.br/'
      self.BOTAO='//*[@id="lnkCadastreSe"]'
      self.INPUTEMAIL='//*[@id="Email"]'
      self.EMAIL='desafiodevops@gmail.com'
      self.INPUTSENHA='//*[@id="Senha"]'
      self.SENHA='indrabrasil123'
      self.BOTAOCONTINUAR='btnClienteLogin'

   def home_extra(self):
      self.driver.get(self.URL)

   def botao(self):
      self.driver.implicitly_wait(3)
      self.driver.find_element_by_xpath(self.BOTAO).click()


   def email(self):
      self.driver.implicitly_wait(3)
      self.driver.find_element_by_xpath(self.INPUTEMAIL).send_keys(self.EMAIL)
   
   def senha(self):
      self.driver.implicitly_wait(3)
      self.driver.find_element_by_xpath(self.INPUTSENHA).send_keys(self.SENHA)
      self.driver.implicitly_wait(20)

   def atraso(self):
      self.driver.find_element_by_xpath(self.INPUTEMAIL).click()
      self.driver.find_element_by_xpath(self.INPUTSENHA).click()
      self.driver.find_element_by_xpath(self.INPUTEMAIL).click()
      self.driver.find_element_by_xpath(self.INPUTSENHA).click()
      self.driver.find_element_by_xpath(self.INPUTEMAIL).click()
      self.driver.find_element_by_xpath(self.INPUTSENHA).click()
      self.driver.find_element_by_xpath(self.INPUTEMAIL).click()
      self.driver.find_element_by_xpath(self.INPUTSENHA).click()
      self.driver.find_element_by_xpath(self.INPUTEMAIL).click()
      self.driver.find_element_by_xpath(self.INPUTSENHA).click()
      self.driver.find_element_by_xpath(self.INPUTEMAIL).click()
      self.driver.find_element_by_xpath(self.INPUTSENHA).click()

   def botao_continuar(self):
      self.driver.implicitly_wait(30)
      self.driver.find_element_by_id(self.BOTAOCONTINUAR).click()

   def url_check(self):
      assert self.driver.title == 'Extra.com.br: o site da família e a maior loja de Informática do Brasil'
