from Pyautomators.contrib.scenario_autoretry import scenario_retry
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pages.Filtrar import ObjFiltrar

def before_all(context):
	context.driver=webdriver.Chrome('driver/chromedriver.exe')
	context.ObjFiltrar=ObjFiltrar(context.driver)

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
	pass

