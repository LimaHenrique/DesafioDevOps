from selenium import webdriver
from pages.pages.ObjExtra import Extra
from selenium.webdriver.common.keys import Keys



def before_all(context):
	context.driver=webdriver.Chrome('driver/chromedriver.exe')
	context.Extra=Extra(context.driver)
	#context.page_Extra=Extra(context.driver)
	

def before_feature(context,feature):
    	pass
	
def before_scenario(context,scenario):
    	pass
	
def before_tag(context,tag):
    	pass
	
def after_tag(context,tag):
    	pass
	
def before_step(context,step):
    	pass
	
def after_step(context,step):
    	pass
	
def after_scenario(context,scenario):
    	pass
	
def after_feature(context,feature):
    	pass
	
def after_all(context):
    	context.driver.quit()
	


