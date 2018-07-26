import tweepy
from textblob import TextBlob

# these are retrieved from the twitter app
consumer_key = "your consumer key"
consumer_secret = "your consumer secret"

access_token = "your access token"
access_token_secret = "your access token secret"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Apple')

for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    print()
