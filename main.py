import tweepy
from time import sleep

auth = tweepy.OAuthHandler(
    "ba66VbTbYAVfb7xd9Mk3iz0hY",
    "XvGqFT2BUieHNyfjdMYBA7yHXVOHgsaAXufqho8nZGEvMyf1V8")
auth.set_access_token("4911328633-7cubR0QaKRTDUmZEREHof96YEqznuRTzB10ZzCS",
                      "WzeeTD3ADFvbOpn3JGLjJ4AHP7dO9KmGRPSCzMB08V8dM")

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

tweets_modi = api.user_timeline(
    screen_name="narendramodi", tweet_mode="extended", count=50)

texts_modi = []
for t in tweets_modi:
    temp = t.full_text
    if (temp[0] != '@'):
        if (temp[0:2] != "RT"):
            texts_modi.append(temp)

texts_modi.reverse()

print("Modi tweets: {}".format(len(texts_modi)))

modi_tweets = open("./ModiTweets.txt", "w+")
for i in texts_modi:
    modi_tweets.write("{}\n\n\n".format(i))
modi_tweets.close()

sleep(120)

tweets_trump = api.user_timeline(
    screen_name="realDonaldTrump", tweet_mode="extended", count=50)

texts_trump = []
for t in tweets_trump:
    temp = t.full_text
    if (temp[0] != '@'):
        if (temp[0:2] != "RT"):
            texts_trump.append(temp)

texts_trump.reverse()

print("Trump tweets: {}".format(len(texts_trump)))

trump_tweets = open("./TrumpTweets.txt", "w+")
for i in texts_trump:
    trump_tweets.write("{}\n\n\n".format(i))
trump_tweets.close()
