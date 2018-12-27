import json
from twython import Twython
import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

APP_KEY ='CVALFM6NEB6DVAO57gSDGng2V'
APP_SECRET ='wJSYHO4RC1DXdVgYAAHfnQJLRemVfKLIi6Cc5XXQdPDwLdRZmu'
OAUTH_TOKEN ='2560618068-dbaSHbCDG8jwkQCLXZLaHT12tEMmCTcxSdRvLfF'
OAUTH_TOKEN_SECRET = '1VfrBi4CeYYJu9Ybt4vDwutu70tcpEasoOx8VjRpSkVOd'
twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)


##this is for veryfying the credentials
##real = twitter.verify_credentials()
##print(real)

##timeline = twitter.get_home_timeline()
##
##print(json.dumps(timeline))#this prints all the jason data on timeleine


user = 'realdonaldtrump'
start = datetime.datetime(2010, 1, 1)  
end = datetime.datetime(2016, 12, 7)


#data = twitter.search(q = 'from:narendramodi since:2018-04-05 until:2018-04-10', result_type='mixed', count=200)
data = twitter.search(q = 'from:narendramodi since:2018-03-01 until:2018-03-31' , result_type='mixed', count = 3000)

##print(json.dumps(data))
status = data['statuses']
##print ("the length of the data is",len(data['statuses']))
for tweet_data in status:
    print(tweet_data['created_at'])
    print("THE ABOVE IS A CREATED_AT")
    print(tweet_data['id_str']+ ' = ' + tweet_data['text'])
    
 
print("the end")
    
