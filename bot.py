import sys
import multiprocessing
import pandas as pd
import re
import tweepy
from botutils import config
from botutils import fetch_data
import json

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

    
    public_tweets = api.home_timeline()

    #dataframe
    column = ['Tweet', 'Time']
    data = []

    for tweet in public_tweets:
        data.append([tweet.text, tweet.created_at])

    df = pd.DataFrame(data,columns=column)
    # Remove hyperlinks included in tweets
    df['Tweet'] = df['Tweet'].apply(lambda x: re.sub(r'http\S+', '', x)) #Remove hyperlinks
    df['text'] = df['text'].str.replace('[^\w\s]','') #Remove special characters
    df.to_csv('tweets.csv')
    #print(public_tweets)
