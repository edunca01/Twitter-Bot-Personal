import tweepy
import os

def get_api():
    try:
        __API_KEY = os.environ['API_KEY']
        __API_SECRET_KEY = os.environ['API_SECRET_KEY']
        __ACCESS_TOKEN = os.environ['ACCESS_TOKEN']
        __ACCESS_TOKEN_SECRET = os.environ['ACCESS_TOKEN_SECRET']

        auth = tweepy.OAuthHandler(__API_KEY, __API_SECRET_KEY)
        auth.set_access_token(__ACCESS_TOKEN, __ACCESS_TOKEN_SECRET)
        api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
        api.verify_credentials()
        print('Authentication successful')
    except KeyError as e:
        print('Twitter credentials not supplied.',e)
    except Exception as e:
        print(e)
    return api
