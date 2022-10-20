import sys
import multiprocessing

from botutils import config
from botutils import fetch_data

if __name__ == '__main__':
    print('Starting Twitter Bot')
    api = config.get_api()
    print('Finished Initialization')

    #dataframe
    column = [Tweet, Time]

    #public_tweets = api.home_timeline()
    #print(public_tweets)
