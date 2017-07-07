from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
from pymongo import MongoClient
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Set up Microsoft Collection
client = MongoClient()
db = client['Job_Info_Database']
JSC = db['Jane_Street_Collection']

JSC_dict = {}

# https://www.janestreet.com/join-jane-street/open-positions/
# Need Selenium WebDriver - for the 'View Open Positions' button on the web
# Selenium does not interact with elements that have "display:none"
# Need execute_script() to set the value of the select - JavaScript - Not needed
# Revised: Important! - when choosing XPath - Need to choose the most upper level one,
# which is the one started with '/html' - otherwise it will not find that


from selenium import webdriver
driver = webdriver.Chrome()
driver.get('https://www.janestreet.com/join-jane-street/open-positions/')
# driver.execute_script("document.getElementByXPath('/html/body/div[4]/div[5]/div/div/div/div[2]/div[2]').sty;e.display='block';")
wait = WebDriverWait(driver,10)

# button = wait.until(EC.presence_of_element_located((By.XPATH,buttonPath)))
# driver.execute_script('arguments[0].click();',button)
# button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME,'ult_exp_section_layer ult-adjust-bottom-margin  ')))
# button.click()

# Click the "Open Quantitative Trading Position Button"
trading_button_path="/html/body/div[4]/div[5]/div/div/div/div[2]"
trading_button = wait.until(EC.element_to_be_clickable((By.XPATH,trading_button_path)))
trading_button.click()

# "Open Software Development Positions & Open IT&NewWorking Position"
sd_button_path="/html/body/div[4]/div[7]/div/div/div/div[5]"
it_button_path="/html/body/div[4]/div[7]/div/div/div/div[7]"
sd_button = wait.until(EC.element_to_be_clickable((By.XPATH,sd_button_path)))
sd_button.click() # Error: Element is not clickable

it_button = wait.until(EC.element_to_be_clickable((By.XPATH,it_button_path)))
it_button.click()

# "Open Quantitative Research Position"
research_button_path = "/html/body/div[4]/div[9]/div/div/div/div[5]"
research_button = wait.until(EC.element_to_be_clickable((By.XPATH,research_button_path)))
research_button.click()


