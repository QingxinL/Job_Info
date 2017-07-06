from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
from pymongo import MongoClient

client = MongoClient()
db = client['Job_Info_Database']
HRT = db['Hudson_River_Trading_Collection']

HRT_dict = {}

# TODO: this url is the html within the iframe - didn't figure out how to get this link from the origin page
def job_Scraping(url):
    html = urlopen(url)
    bsObj = BeautifulSoup(html,'lxml')
    jobs = bsObj.findAll('a',{'data-mapped':'true'})
    for job in jobs:
        HRT_dict['Title']=job.text
        HRT_dict['Website']=job.get('href')
    locations = bsObj.findAll('span',class_='location')
    for loc in locations:
        HRT_dict['Location']=loc.text
    print(HRT_dict)
    HRT.update(spec=HRT_dict,document=HRT_dict,upsert=True)
    print('End of Program')

job_Scraping('https://boards.greenhouse.io/embed/job_board?for=wehrtyou&b=http://www.hudson-trading.com/careers/')