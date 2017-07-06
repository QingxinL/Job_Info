from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
from pymongo import MongoClient
from selenium import webdriver

client = MongoClient()
db = client['Job_Info_Database']
HRT = db['Hudson_River_Trading_Collection']

HRT_dict = {}

# TODO: this url is the html within the iframe - didn't figure out how to get this link from the origin page
# Need Selenium to deal with iframe - for the requirement

def job_Scraping(url):
    html = urlopen(url)
    bsObj = BeautifulSoup(html,'lxml')
    jobs = bsObj.findAll('div',class_='opening')

    for job in jobs:
        HRT_dict['Title']=job.find('a',{'data-mapped':'true'}).text
        web=job.find('a',{'data-mapped':'true'}).get('href')
        HRT_dict['Website']=web
        HRT_dict['Location'] = job.find('span',class_='location').text
        # get the requirement within each url (web)
        require = getRequirement(web)
        HRT_dict['Requirement'] = require

        HRT.update(spec=HRT_dict,document=HRT_dict,upsert=True)
    print('End of Program')
#
# //*[@id="content"]/ul[2]/li[1]/span
# //*[@id="content"]/ul[2]/li[2]/span/text()


def getRequirement(web):
    driver = webdriver.Chrome()
    driver.get(web)
    element = driver.find_element_by_xpath('//*[@id="grnhse_iframe"]').get_attribute('src')
    newhtml = urlopen(element)
    new_soup = BeautifulSoup(newhtml,'lxml')
    skills = new_soup.findAll('ul')[1].findAll('span')
    require = ''
    for skill in skills:
        require+=skill.text
    driver.close()
    return require




job_Scraping('https://boards.greenhouse.io/embed/job_board?for=wehrtyou&b=http://www.hudson-trading.com/careers/')
