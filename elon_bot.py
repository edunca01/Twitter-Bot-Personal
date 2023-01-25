import json
import time

import tweepy

    
    
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
    
    prev_elon_tweet = api.user_timeline(screen_name='elonmusk', count=1)

    while True:
        # Get the latest tweet from Elon Musk
        elon_tweet = api.user_timeline(screen_name='elonmusk', count=1)

        # Check if the latest tweet is different from the previous tweet
        if elon_tweet[0].id != prev_elon_tweet[0].id:
            # Update the latest tweet
            prev_elon_tweet = elon_tweet

            # Like the tweet
            api.create_favorite(elon_tweet[0].id)
            print(f"Liked tweet: {elon_tweet[0].text}")
        else:
            time.sleep(300)