from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
from pymongo import MongoClient

# Set up Database
client = MongoClient()
db = client['Job_Info_Database']
TS = db['Two_Sigma_Collection']  # Set up Two Sigma Collection

ts_dic = {} # dictionary store all the info

# TODO: Update the database (run the program) every day




def jobScraping(url):
    page =1
    while True:
        html = urlopen(url)
        soup = BeautifulSoup(html,'lxml')
        page+=1

        # General Info, include websites&job titles
        for link in soup.findAll('a',{'class':'mobileHide'}):
            href = link.get('href')
            href = href.replace('Dash', '')
            title = link.text
            html_individual = urlopen(href)
            soup_individual = BeautifulSoup(html_individual,'lxml')

            loc = getLocation(soup_individual)
            require = getRequirement(soup_individual)

            # Put data into dictionary (update each time through the loop)
            ts_dic['Title'] = title
            ts_dic['Website'] = href
            ts_dic['Location'] = loc
            ts_dic['Requirement'] = require
            #print(ts_dic)

            # TODO: Display the Requirement Data in the database better, with each line seperated

            TS.update(spec=ts_dic,document=ts_dic,upsert=True)



        if checkPageEnd(soup)==True:
            break

        #url = 'https://careers.twosigma.com/careers/SearchJobs/?jobOffset=' + str((page - 1) * 10)
        url = url[:(len(url)-1)] + str((page - 1) * 10)
        #url = 'https://careers.twosigma.com/careers/SearchJobs/?3_33_3=%5B%22897%22%5D&jobOffset=' + str((page - 1) * 10)


    print('End of Program')

def checkPageEnd(soup):
    for number in soup.findAll('a',{'class': 'paginationItem'}):
        if number.string=='Next >>':
            return False
    return True


def getRequirement(soup):

    if(soup.find(text='Requirements Include:')!=None):
        start = soup.find(text='Requirements Include:')
    else:
        start = soup.find(text=re.compile('[a-z]* qualifications')) #Handles other cases like 'Minimum Requirements'

    #print('Requirements Include: ')

    requirements = start.find_next('ul').findAll('li')
    text = ''
    for requirement in requirements:
        #print(requirement.text)
        text = text + requirement.text

    return text
    #print('\n')

def getLocation(soup):

    loc = soup.find('p',{'itemprop':'jobLocation'})
    return loc.text






