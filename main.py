import tweepy
from .consumerData import consumer_key, consumer_secret

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)