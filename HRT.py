from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
from pymongo import MongoClient

client = MongoClient()
db = client['Job_Info_Database']
HRT = db['Hudson_River_Trading_Collection']

HRT_dict = {}

html = urlopen('http://www.hudson-trading.com/careers/').read()
soup = BeautifulSoup(html,'lxml')

# Need to deal with iframe
