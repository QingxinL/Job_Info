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

# https://www.janestreet.com/join-jane-street/open-positions/#job-2017-1319
# Need Selenium WebDriver - for the 'View Open Positions' button on the web
# Selenium does not interact with elements that have "display:none"
# Need execute_script() to set the value of the select - JavaScript - Not needed
# Revised: Important! - when choosing XPath - Need to choose the most upper level one,
# which is the one started with '/html' - otherwise it will not find that


from selenium import webdriver
#driver = webdriver.Chrome()
def getClicked(xpath,wait):
    button = wait.until(EC.element_to_be_clickable((By.XPATH,xpath)))
    button.click()

def open_positions(driver):
    wait = WebDriverWait(driver,10)


# Click the "Open Quantitative Trading Position Button"
    trading_button_path="/html/body/div[4]/div[5]/div/div/div/div[2]"
    getClicked(trading_button_path,wait)



# "Open Software Development Positions & Open IT&NewWorking Position"
    sd_button_path="/html/body/div[4]/div[7]/div/div/div/div[5]"
    it_button_path="/html/body/div[4]/div[7]/div/div/div/div[7]"
    # TODO: Error: Element is not clickable in Chrome, but no error with PhantomJS

    getClicked(sd_button_path,wait)
    getClicked(it_button_path,wait)


# "Open Quantitative Research Position"
    research_button_path = "/html/body/div[4]/div[9]/div/div/div/div[5]"
    getClicked(research_button_path,wait)


    return driver.page_source


def jobScraping():
    driver = webdriver.PhantomJS()
    driver.get('https://www.janestreet.com/join-jane-street/open-positions/')

    html = open_positions(driver)
    soup = BeautifulSoup(html,'lxml')

    # Get the job titles & locations
    jobs = soup.findAll('h4',class_='job-title')
    for job in jobs:
        job = job.find('a',class_='launch-job')
        JSC_dict['Title']=job.text
        loc = job.find_next('span',class_=re.compile('job-post-[a-z]'))
        JSC_dict['Location']=loc.text

        # TODO: UODATE THE DICT FOR EACH JOB 
        getWebsite(driver) # the same with the below
        getRequirement(driver)
        # Website is also display:none, details (requirements) is hidden
        # use element.get_attribute('textContent')
        # - not actually click on the button, but only get the text inside the element



    print(JSC_dict)

def getRequirement(driver):
    requirements = driver.find_elements_by_class_name('job-candidate')
    for requirement in requirements:
        require = requirement.get_attribute('textContent')
        require = re.sub(pattern=r"<.*?>",repl="",string=require)
        JSC_dict['Requirement']=require


def getWebsite(driver):
    webs = driver.find_elements_by_class_name('arrow-link-normal')
    for web in webs:
        website = web.get_attribute('href')
        JSC_dict['Website']=website




jobScraping()
