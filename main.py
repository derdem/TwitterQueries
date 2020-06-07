import tweepy
from twitterCredentials import consumer_key, consumer_secret, access_token, access_token_secret

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

trump_tweets = api.user_timeline("@realDonaldTrump")

for tweet in trump_tweets:
    print(tweet.text)