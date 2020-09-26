import tweepy


auth = tweepy.OAuthHandler('API key', 'API sceret key')
auth.set_access_token('Consumer key', 'Consumer second key')

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

user = api.me()


def main():
    search = ("Python")

    numberofTweets = 5
    for tweet in tweepy.Cursor(api.search, search).items(numberofTweets):
        try:
            tweet.retweet()
            print("Tweet Retweeted")
        except tweepy.TweepError as e:
            print(e.reason)
        except StopIteration:
            break


main()