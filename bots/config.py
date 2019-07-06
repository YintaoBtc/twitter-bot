# tweepy-bots/bots/config.py
import tweepy
import logging
import os
from dotenv import load_dotenv
load_dotenv()

logger = logging.getLogger()

def create_api():
    # Authenticate to Twitter
    auth = tweepy.OAuthHandler(os.getenv("CONSUMER_KEY"), os.getenv("CONSUMER_SECRET"))
    auth.set_access_token(os.getenv("ACCESS_TOKEN"), os.getenv("ACCESS_TOKEN_SECRET"))

    api = tweepy.API(auth)
    print (api)

    try:
        api.verify_credentials()
        print("Authentication OK")
    except:
        print("Error during authentication")
    return api