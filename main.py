'''Initial Idea:
build a web crawler to collect the job information from big companies
(without multiple domains involved)
call the function each companies collected [like: getJobs(companyUrl)
put the urls into a dictionary with keys being the company name and values being the urls '''

'''Revised Idea:
Collect job information from companies' websites and put them into files
each company with two files:
one file with general information like Title and Websites 
another file with specific requirements'''

'''Second Revised Idea: Use Database not files - MongoDB'''

# TODO: AUTOMATIC RUN THE SCRIPT ON DAILY BASIS - USE Launchd
# TODO: Update the database (run the program) every day



import TwoSigma
import HRT
import JaneStreet

# Two Sigma:
execution_trading ='https://careers.twosigma.com/careers/SearchJobs/?3_33_3=%5B%22897%22%5D&jobOffset=0'
TwoSigma.jobScraping(execution_trading)

# Hudson River Trading:
iframe_url = 'https://boards.greenhouse.io/embed/job_board?for=wehrtyou&b=http://www.hudson-trading.com/careers/'
HRT.job_Scraping(iframe_url)

JaneStreet.jobScraping()

