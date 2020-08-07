import tweepy
import time
import os
from os import environ

CONSUMER_KEY=environ['CONSUMER_KEY']
CONSUMER_SECRET=environ['CONSUMER_SECRET']
ACCESS_KEY=environ['ACCESS_KEY']
ACCESS_SECRET=environ['ACCESS_SECRET']

auth=tweepy.OAuthHandler(CONSUMER_KEY , CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY , ACCESS_SECRET)
api=tweepy.API(auth)

FILE_NAME='last_seen_id.txt'

def retrive_last_seen_id(file_name):
    f_read=open(file_name,'r')
    last_seen_id=int(f_read.read().strip())
    f_read.close()
    return last_seen_id

def store_last_seen_id(last_seen_id, file_name):
    f_write=open(file_name,'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return 

def like_tweets():
    print("Liking tweets...")
    last_seen_id=retrive_last_seen_id(FILE_NAME)
    mentions = api.mentions_timeline(
        last_seen_id,
        tweet_mode='extended'
    )

    for mention in reversed(mentions):
        print( str(mention.id) + " -- " + mention.full_text)
        last_seen_id=mention.id
        store_last_seen_id(last_seen_id,FILE_NAME)
        if '#customtag' in mention.full_text.lower():
            print("Found CUSTOMTAG !!!")
            print("Responding back....")
            mention.favorite()

while True:
    like_tweets()
    time.sleep(10)
