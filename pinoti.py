import os
import time
from tweepy import Client

"""
Wrapper to tweepy client. It will read auth keys from OS environment,
and establish a connection with twitter using Tweepy client.
make sure you have created a developer account with Twitter, and note
all the required auth tokens:
- Consumer Key (aka API Key)
- Consumer Secret (aka API Key Secret)
- Bearer Token (to access Twitter v2 API)
- Access Token
- Access Token Secret

For convenience, create a .env file and export all the environment variables.
Then you can simply: source .env; before running your program that instantiate this object

@author dsutedja
@version 1.0
"""
class Pinoti:
    def __init__(self):
        self.consumer_key = os.getenv('CONSUMER_KEY', '')
        self.consumer_secret = os.getenv('CONSUMER_SECRET', '')
        self.access_token = os.getenv('ACCESS_TOKEN', '')
        self.access_token_secret = os.getenv('ACCESS_TOKEN_SECRET', '')
        self.bearer_token = os.getenv('BEARER_TOKEN', '')
        self.__validate()

    def create_tweet(self, message):
        self.__client.create_tweet(text = message)

    def __validate(self):
        print("validating and establishing Twitter connection")
        
        if (self.consumer_key == '' or self.consumer_secret == '' or
            self.access_token == '' or self.access_token_secret == '' or
            self.bearer_token == ''):
            raise Exception("Cannot find auth info in the environment")

        self.__client = Client(bearer_token = self.bearer_token,
                             consumer_key = self.consumer_key,
                             consumer_secret = self.consumer_secret,
                             access_token = self.access_token,
                             access_token_secret = self.access_token_secret)
        
