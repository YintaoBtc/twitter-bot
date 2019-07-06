import tweepy
import os
from dotenv import load_dotenv
load_dotenv()
import logging
from config import create_api
import time, random
from one_time import *

#logging.basicConfig(level=logging.INFO)
logging.basicConfig(filename='app.log', filemode='a', format='%(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger()

def follow_followers(api):
    logger.info("Retrieving and following followers")
    for follower in tweepy.Cursor(api.followers).items():
        if not follower.following:
            logger.info(f"Following {follower.name}")
            follower.follow()

            api.update_status(f"Following {follower.name}")



def favorite(api):
    userID="CrownPlatform"
    tweets = api.user_timeline(screen_name=userID, 
                            # 200 is the maximum allowed count
                            count=5,
                            include_rts = False,
                            # Necessary to keep full_text 
                            # otherwise only the first 140 words are extracted
                            tweet_mode = 'extended'
                            )
                    
    for tweet in tweets:
        print(f"Processing tweet id {tweet.id}:{tweet.full_text}")

        try:
            tweet.favorite()
            tweet.retweet()
        except Exception as e:
            logger.error("Error on fav and retweet", exc_info=True)



def search(api):
    # For loop to iterate over tweets with #CrownPlatform, limit to 10
    for tweet in tweepy.Cursor(api.search,
                            q='#CrownPlatform',                           
                            #since='2019-06-25',
                            ).items(10):

         # Print out usernames of the last 10 people to use #CrownPlatform
        try:

            # Follow the user who tweeted
            if not tweet.user.following:
                try: 
                    tweet.user.follow()
                    print('Followed the user')
                except tweepy.TweepError as e:
                    print(e.reason)
                    
            print('Tweet by: @' + tweet.user.screen_name)
            tweet.retweet()
            print('Retweeted the tweet')

            # Favorite the tweet
            tweet.favorite()
            print('Favorited the tweet')





        except tweepy.TweepError as e:
            print(e.reason)

        except StopIteration:
            break





def main():
    api = create_api()
    while True:
        favorite(api)
        follow_followers(api)
        search(api)
        logger.info("Waiting...")
        time.sleep(60)

if __name__ == "__main__":
    api = create_api()

    bender_talk(api)
    price_crw(api)
    main()
    