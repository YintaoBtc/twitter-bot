import tweepy
import os
from dotenv import load_dotenv
load_dotenv()
import logging
from config import create_api
import time, random

#logging.basicConfig(level=logging.INFO)
logging.basicConfig(filename='app.log', filemode='a', format='%(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger()




def follow_followers(api):
    logger.info("Retrieving and following followers")
    for follower in tweepy.Cursor(api.followers).items():
        if not follower.following:
            logger.info(f"Following {follower.name}")
            follower.follow()

            api.update_status(f"Following @{follower.name}")


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


def bender_talk(api):
    # Open text file verne.txt (or your chosen file) for reading
    my_file = open('bender_phrases.txt', 'r')

    # Read lines one by one from my_file and assign to file_lines variable
    file_lines = my_file.readlines()

    # Close file
    my_file.close()

    total = len(file_lines)

    number = random.randint(0,total)
    print(number)
    i = 0

    # Create a for loop to iterate over file_lines
    for line in file_lines:
        i += 1
        print(i)
        if i == number:
            print (line)

            api.update_status(line)





def main():
    api = create_api()
    while True:
        bender_talk(api)
        favorite(api)
        follow_followers(api)
        logger.info("Waiting...")
        time.sleep(60)

if __name__ == "__main__":
    main()
    