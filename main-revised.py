
import multiprocessing
import TwoSigma
import HRT
import JaneStreet
import time
import datetime

from apscheduler.schedulers.blocking import BlockingScheduler


# Auto run the program / Update the Job_Info_Database every 12 hours
scheduler = BlockingScheduler()
@scheduler.scheduled_job('interval',hours=12)

def updateDatabase():
    print(datetime.datetime.now())
# Two Sigma:
    execution_trading ='https://careers.twosigma.com/careers/SearchJobs/?3_33_3=%5B%22897%22%5D&jobOffset=0'
    TwoSigma.jobScraping(execution_trading)

# Hudson River Trading:
    iframe_url = 'https://boards.greenhouse.io/embed/job_board?for=wehrtyou&b=http://www.hudson-trading.com/careers/'
    HRT.job_Scraping(iframe_url)

# Jane Street Capital:
    JaneStreet.jobScraping()

    print(datetime.datetime.now())
    print('Done')

scheduler.configure()
scheduler.start()



