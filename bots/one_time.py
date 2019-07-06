import tweepy
import os
import logging
from config import create_api
import time, random
import requests, json

#logging.basicConfig(level=logging.INFO)
logging.basicConfig(filename='app.log', filemode='a', format='%(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger()


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
        if i == number:
            try:
                print(line)
                #api.update_status(line)
            except tweepy.TweepError as e:
                print(e.reason)



def price_crw(api):
    #Check info from coinmarketcap for CRW
    url = "https://api.coinmarketcap.com/v2/ticker/720/?convert=EUR"
    headers = {'content-type': "application/json", 'cache-control': "no-cache"}
    response = requests.request("GET", url, headers=headers)
    result = json.loads(response.text)

    #Work with data
    data = result["data"]
    name = data["name"]
    percent_change_24h = data["quotes"]["EUR"]["percent_change_24h"]
    eur = data["quotes"]["EUR"]["price"]
    format_eur = format(eur, ".2f")
    message =  f"Moneda: {name}\nPrecio: {format_eur} €\n24h: {percent_change_24h}%" 
    print(message)
    #api.update_status(message)

def search(api):
    # For loop to iterate over tweets with #CrownPlatform, limit to 10
    for tweet in tweepy.Cursor(api.search,
                            q='#CrownPlatform',                           
                            since='2019-06-25',
                            ).items(10):

         # Print out usernames of the last 10 people to use #CrownPlatform
        try:
            print('Tweet by: @' + tweet.user.screen_name)
            #tweet.retweet()
            print('Retweeted the tweet')

            # Favorite the tweet
            #tweet.favorite()
            print('Favorited the tweet')

            # Follow the user who tweeted
            if not tweet.user.following:
                #tweet.user.follow()
                print('Followed the user')

        except tweepy.TweepError as e:
            print(e.reason)

        except StopIteration:
            break






api = create_api()
search(api)
bender_talk(api)
price_crw(api)
        
        

    