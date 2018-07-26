import tweepy
from textblob import TextBlob

# these are retrieved from the twitter app
consumer_key = "HePKq1HpTDJ7C8MXjS5jfoYu8"
consumer_secret = "hjcNk73Rtw0Q1DSyUwgHGog8mpPxmwq6kMmDmdBSLyw34TPJkq"

access_token = "2169050092-bGYBxjXfoJ0NJAzBZnxm4H2ciVPzUHGIrkdGmnD"
access_token_secret = "KIQ1MhQjJO9dCkqfvVMPVJwWPfi1TWT3aLwtMkxqwqVUI"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Apple')

for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    print()