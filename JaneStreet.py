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



#job_Scraping('https://www.janestreet.com/join-jane-street/open-positions/')