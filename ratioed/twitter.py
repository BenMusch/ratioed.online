import os

import tweepy


consumer_key = os.environ['TWITTER_API_KEY']
consumer_secret = os.environ['TWITTER_API_SECRET_KEY']
access_token = os.environ['TWITTER_ACCESS_TOKEN']
access_token_secret = os.environ['TWITTER_ACCESS_TOKEN_SECRET']

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

def get_tweets_by_ids(tweet_ids):
    return api.statuses_lookup(tweet_ids)

def get_recent_tweets(username, until_id=None):
    if until_id:
        return api.user_timeline(username, since_id=until_id, count=1000)
    else:
        return api.user_timeline(username, count=1000)
