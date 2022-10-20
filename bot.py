import sys
import multiprocessing
import pandas as pd
from botutils import config
from botutils import fetch_data

if __name__ == '__main__':
    print('Starting Twitter Bot')
    api = config.get_api()
    print('Finished Initialization')
    public_tweets = api.home_timeline()

    #dataframe
    column = ['Tweet', 'Time']
    data = []

    for tweet in public_tweets:
        data.append([tweet.text, tweet.created_at])

    df = pd.DataFrame(data,columns=column)
    df.to_csv('tweets.csv')
    #print(public_tweets)
