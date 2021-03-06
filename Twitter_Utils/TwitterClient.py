from Eternal_Utils.CommonUtils import CommonUtils
import tweepy


class TwitterClient:
    def __init__(self):
        """
        Initializes API keys and sets up Auth with Twitter API
        """
        self.APP_KEY = CommonUtils.get_environ_variable('SPORTS_CANARY_APP_KEY')
        self.APP_SECRET = CommonUtils.get_environ_variable('SPORTS_CANARY_APP_KEY_SECRET')
        self.OAUTH_TOKEN = CommonUtils.get_environ_variable('SPORTS_CANARY_OAUTH_TOKEN')
        self.OAUTH_TOKEN_SECRET = CommonUtils.get_environ_variable('SPORTS_CANARY_OAUTH_TOKEN_SECRET')
        self.auth = tweepy.OAuthHandler(self.APP_KEY, self.APP_SECRET)
        self.auth.set_access_token(self.OAUTH_TOKEN, self.OAUTH_TOKEN_SECRET)
        self.api = tweepy.API(self.auth)

    def tweet(self, tweet):
        """
        Tweets out content
        :param tweet: message to be tweeted
        """
        self.api.update_status(tweet)

    def delete_latest_tweet(self):
        timeline = self.api.user_timeline(count=1)
        for t in timeline:
            self.api.destroy_status(t.id)
