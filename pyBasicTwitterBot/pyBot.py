import sys 
from twython import Twython 

CONSUMER_KEY = ''#Add your data here
CONSUMER_SECRET = '' #Add your data here
ACCESS_KEY = ''#Add your data here
ACCESS_SECRET = ''#Add your data here

api = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET)
photo = open('img.jpg', 'rb')
api.update_status_with_media(media=photo, status="Whatever you'd like to say")

