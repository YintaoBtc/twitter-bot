import tweepy
import os
from dotenv import load_dotenv
load_dotenv()

# Authenticate to Twitter
auth = tweepy.OAuthHandler(os.getenv("CONSUMER_KEY"), os.getenv("CONSUMER_SECRET"))
auth.set_access_token(os.getenv("ACCESS_TOKEN"), os.getenv("ACCESS_TOKEN_SECRET"))

api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")


# Create API object
api = tweepy.API(auth, wait_on_rate_limit=True,
    wait_on_rate_limit_notify=True)

#Coge todos los tweet del timeline de un usuario
timeline = api.home_timeline()
for tweet in timeline:
    print(f"{tweet.user.name} said {tweet.text}")

# Publica tweet con texto
api.update_status("Test tweet from Tweepy Python")


# Metodos de usuarios
user = api.get_user("MikezGarcia")

print("User details:")
print(user.name)
print(user.description)
print(user.location)

print("Last 20 Followers:")
for follower in user.followers():
    print(follower.name)



#Sigue a un usuario
api.create_friendship("realpython")

#Updatea la biografia del perfil
api.update_profile(description="I like Python")

# Da like al ultimo post de nuestro timeline
tweets = api.home_timeline(count=1)
tweet = tweets[0]
print(f"Liking tweet {tweet.id} of {tweet.author.name}")
api.create_favorite(tweet.id)

# Metodo para buscar en twitter
# q = query
for tweet in api.search(q="Python", lang="en", rpp=10):
    print(f"{tweet.user.name}:{tweet.text}")


# Busca trends de este momento en un pais
# place(1) = todo el mundo 
trends_result = api.trends_place(1)
for trend in trends_result[0]["trends"]:
    print(trend["name"])

#Lista de paises
api.trends_available()

# Fetch every tweet in which you are mentioned, and then mark each tweet as Liked and follow its author
tweets = api.mentions_timeline()
for tweet in tweets:
    tweet.favorite()
    tweet.user.follow()