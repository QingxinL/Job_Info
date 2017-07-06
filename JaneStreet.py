from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
from pymongo import MongoClient

# Set up Microsoft Collection
client = MongoClient()
db = client['Job_Info_Database']
JSC = db['Jane_Street_Collection']

JSC_dict = {}

# https://www.janestreet.com/join-jane-street/open-positions/
# TODO: Need Selenium WebDriver - for the 'View Open Positions' button on the web
# Selenium does not interact with elements that have "display:none"
# Need execute_script() to set the value of the select - JavaScript
'''    
try:
    selenium.webdriver.support.ui.WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.ID, 'some_other_id_on_page')))
    selenium.execute_script("document.getElementById('some_id').style.display='inline-block';")
    element = selenium.webdriver.support.ui.WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.ID, 'some_id')))
    selenium.webdriver.support.ui.Select(element).select_by_value('1')
    except Exception as ex:
    print(ex)'''


#job_Scraping('https://www.janestreet.com/join-jane-street/open-positions/')