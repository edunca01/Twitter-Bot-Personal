import tweepy

class StreamListener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        self.me = api.me()

    def on_status(self, tweet):
        #Check if tweet mentions someone
        #if check_mentions(tweet.user.id):
        #    print(f'Tweet is from {tweet.user.name}')
        #    return
        print(f'{tweet.user.id}')
        #Check if tweet is a reply
        if tweet.in_reply_to_status_id is not None:
            print('Tweet is a reply')
            return
        #Like and Retweet
        if not tweet.favorited:
            try:
                tweet.favorited()
                print(f'Tweet liked: tweet user {tweet.user.name} , tweet text {tweet.text}')
            except Exception as e:
                print(f'{e}')
        if not tweet.retweeted:
            try:
                tweet.retweet()
                print(f'Tweet retweeted: tweet user {tweet.user.name} , tweet text {tweet.text}')
            except Exception as e:
                print(f'{e}')
    def on_error(self, status_code):
         print('Error detected in stream listener')

twitter_ids = [
    '702590808965316608',   # Abhi_indian
    '44196397',             # elonmusk
    '92708272',             # msdhoni
    # '445921112',          # TechieAman
]
def check_mentions(user_id):
    if str(user_id) in twitter_ids:
        return False
    return True

def run_streamer(api, mode='follow', keywords=[], twitter_ids=twitter_ids):
    print("Getting API")
    _api = api
    tweet_listener = StreamListener(_api)
    stream = tweepy.Stream(_api.auth, tweet_listener)
    if mode == 'follow':
        stream.filter(follow=twitter_ids, languages=['en'], is_async=False)
    elif mode == 'track':
        stream.filter(track=keywords, languages=["en"], is_async=True)
    else:
        print('Please supply proper mode (follow/track)')
