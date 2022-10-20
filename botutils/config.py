import tweepy
from . import utils

logger = utils.get_logger()

def get_api():
    try:
        __API_KEY = "jall74fWCw9VdxBKM728MPqHx"
        __API_SECRET_KEY = "vZk2NiS3WyRj5CsGntOSFlEe0rRv3XytwfZjAMh0WUbcELOY0A"
        __ACCESS_TOKEN = "1582154646789001217-0AJheDFr3f66BxVsBl6yEmo11JjaPD"
        __ACCESS_TOKEN_SECRET = "phz1z8parmx9FawTnwAKmaGni0k9zmD8fqPIeWheuPBIr"

        auth = tweepy.OAuthHandler(__API_KEY, __API_SECRET_KEY)
        auth.set_access_token(__ACCESS_TOKEN, __ACCESS_TOKEN_SECRET)
        api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
        api.verify_credentials()
        logger.info('Authentication successful')
    except KeyError:
        logger.error('Twitter credentials not supplied.')
    except Exception as e:
        logger.error(e)
    return api
