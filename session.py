import json
import base64
import tweepy


def read_file(filename, encrypt=False):
    if encrypt:
        with open(filename, 'rb') as file:
            return base64.b64decode(file.read()).decode('utf-8')
    else:
        with open(filename, 'r') as file:
            return file.read()


def query_token(token_id):
    return read_file(f'token_{token_id}', True)


def get_session():
    twitter_token = json.loads(query_token('twitter'))
    token_auth = tweepy.OAuthHandler(twitter_token['consumer_key'], twitter_token['consumer_secret'])
    token_auth.set_access_token(twitter_token['access_token'], twitter_token['access_token_secret'])
    return tweepy.API(token_auth, wait_on_rate_limit=True)


print('  Getting session...')
kuma = get_session()
