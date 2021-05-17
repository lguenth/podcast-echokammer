#!/usr/bin/env python3

import tweepy
from credentials import consumer_key, consumer_secret, access_token, access_token_secret
from datetime import datetime

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)

trends_at_place = api.trends_place(23424829)
for values in trends_at_place:
    for trend in values["trends"]:
        print(trend)

# keys in values: "trends", "as_of", "created_at", "locations"
# keys in trend: "name", "url", "promoted_content", "query", "tweet_volume"

user = api.get_user("pandemie_echo")
print(f"@-Name: {user.screen_name}")
print(f"Anzeigename: {user.name}")
print(f"Zahl der Follower: {user.followers_count}")

for friend in user.friends():
   print(friend.screen_name)

query = "Drosten"  # Kann auch Liste sein.

search_results = api.search(q=query, lang="de", tweet_mode="extended")
for result in search_results:
    print(result.full_text)

search_results = tweepy.Cursor(api.search, q=query, tweet_mode="extended", lang="de", since="2021-01-01").items(10)

corpus = []
corpus = [result.full_text for result in search_results if result not in corpus]

since_date = "2021-01-01" # String im Format YYYY-MM-DD
until_date = datetime.strptime("2021-01-06", "%Y-%m-%d")

search_results = tweepy.Cursor(api.search, q=query, tweet_mode="extended", lang="de", since=since_date, until=until_date).items(100)
