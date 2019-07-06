import tweepy
import os
from dotenv import load_dotenv
load_dotenv()

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

