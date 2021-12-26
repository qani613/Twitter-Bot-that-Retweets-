#IMPORT LIBRARIES 
import tweepy
import time

# INITIALIZATION 
api_key= "API KEY GOES IN HERE"
api_key_secret = "API SECRET KEY GOES IN HERE"
access_token = "ACCESS TOKEN GOES HERE"
access_token_secret = "SECRET ACCESS TOKEN GOES HERE"

auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token , access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)
#api = tweepy.API(auth)

#YOU CAN REPLACE THE HASHTAG WITH ANYTHING 
hashtag = "#AmisomOut"
tweet_number = 10

tweets = tweepy.Cursor(api.search, hashtag).items(tweet_number)
#IF YOU ARE USING TWEEPY V4.X THEN THE METHOD IS API.SEARCH_TWEETS. 

#IN THIS FUNCTION THE BOT IS LOOKING FOR THE TWEETS AND RETWEETING THEM
def searchBot():
    for tweet in tweets:
        try:
            tweet.retweet()
            print("retweet done!")
            time.sleep(2)
        except tweepy.TweepError as e:
            print(e.reason)
            time.sleep(15)

searchBot()
