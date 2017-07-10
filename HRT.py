from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
from pymongo import MongoClient
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


client = MongoClient()
db = client['Job_Info_Database']
HRT = db['Hudson_River_Trading_Collection']

HRT_dict = {}


# Need Selenium to deal with iframe - for the requirement

driver = webdriver.PhantomJS()
#driver = webdriver.Chrome()
wait = WebDriverWait(driver,10)






def job_Scraping(url):
    html = urlopen(url)
    bsObj = BeautifulSoup(html,'lxml')
    jobs = bsObj.findAll('div',class_='opening')

    for job in jobs:
        HRT_dict['Title']=job.find('a',{'data-mapped':'true'}).text
        web=job.find('a',{'data-mapped':'true'}).get('href')
        HRT_dict['Website']=web
        HRT_dict['Location'] = job.find('span',class_='location').text
        # TODO: get the requirement within each url (web)
        require = getRequirement(driver,web)
        HRT_dict['Requirement']=require

        HRT.update(spec=HRT_dict,document=HRT_dict,upsert=True)
    print('End of Program')
# TODO: Get the requirements is not finished - each individual job website is differently structured

# def getRequirement(web):
#     driver = webdriver.PhantomJS() # Not actually open the browser
#     driver.get(web)
#     element = driver.find_element_by_xpath('//*[@id="grnhse_iframe"]').get_attribute('src')
#     # TODO: Need to scrape not only the skills, but the profile, need to find by text
#
#     newhtml = urlopen(element)
#     new_soup = BeautifulSoup(newhtml,'lxml')
#
#     require = ''
#
#     # Deal with "Responsibilities"
#     start = new_soup.find(text='Responsibilities')
#     require += getRequire_breakdown(start,require)
#     # Deal with "The skills" & "Skills"
#     start = new_soup.find(text=re.compile('[a-z]* Skills',re.IGNORECASE))
#     require += getRequire_breakdown(start,require)
#
#     # Deal with "The Profile"
#     start = new_soup.find(text=re.compile('[a-z]* profile', re.IGNORECASE))
#     require += getRequire_breakdown(start,require)
#
#     print(require)
#     driver.close()
#     return require

# def getRequire_breakdown(start,require):
#     if start!=None:
#         skills = start.find_all('li')
#         if skills == None:
#             skills = start.find_all('span')
#         for skill in skills:
#             require+=skill.text



#job_Scraping('https://boards.greenhouse.io/embed/job_board?for=wehrtyou&b=http://www.hudson-trading.com/careers/')


# get the text inside iframe - selenium driver switch frame and find elements, get attribute by text content
def getRequirement(driver,url):
    driver.get(url)
    iframe = driver.find_element_by_tag_name('iframe')
    driver.switch_to_frame(iframe)

    requirement = ''  # a string contain all the requirement for a certain job (on a certain web)
    requirements = driver.find_element_by_id('content')
    requirements = requirements.find_elements_by_tag_name('ul')  # get the 'ul' tag under id 'content'
    for require in requirements:
        require = require.get_attribute('textContent').strip()
        requirement+=require
        # print(require)

    return requirement


#job_Scraping('https://boards.greenhouse.io/embed/job_board?for=wehrtyou&b=http://www.hudson-trading.com/careers/')