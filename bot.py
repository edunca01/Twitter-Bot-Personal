import sys
import multiprocessing
import json
import re
import time

import tweepy
import pandas as pd


# Create a stream listener
class StreamListener(tweepy.StreamListener):
    def on_status(self, status):
        # Check if the tweet is from Elon Musk
        if status.user.screen_name == "elonmusk":
            # Like the tweet
            api.create_favorite(status.id)
            print(f"Liked tweet: {status.text}")

if __name__ == '__main__':
    print('Starting Twitter Bot')
    api_info = json.load(open('credentials.json', 'r'))

    try:
        __API_KEY = api_info['API_KEY']
        __API_SECRET_KEY = api_info['API_SECRET_KEY']
        __ACCESS_TOKEN = api_info['ACCESS_TOKEN']
        __ACCESS_TOKEN_SECRET = api_info['ACCESS_TOKEN_SECRET']

        auth = tweepy.OAuthHandler(__API_KEY, __API_SECRET_KEY)
        auth.set_access_token(__ACCESS_TOKEN, __ACCESS_TOKEN_SECRET)
        api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
        api.verify_credentials()
        print('Authentication successful')
    except KeyError as e:
        print('Twitter credentials not supplied.',e)
    except Exception as e:
        print(e)
    print('Finished Initialization')

    

    # Get Tweets from timeline
    public_tweets = api.home_timeline()

    #Create Dataframe
    column = ['Tweet', 'Time']
    data = []

    for tweet in public_tweets:
        data.append([tweet.text, tweet.created_at])

    df = pd.DataFrame(data,columns=column)
    # Remove hyperlinks included in tweets
    df['Tweet'] = df['Tweet'].apply(lambda x: re.sub(r'http\S+', '', x)) #Remove hyperlinks
    df['Tweet'] = df['Tweet'].str.replace('[^\w\s]','') #Remove special characters
    df.to_csv('tweets.csv')
    #print(public_tweets)
