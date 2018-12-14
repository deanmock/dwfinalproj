## tweets.py
# Dean Mock / Theo Stumpf
## Version 22 Nov 2018

from requests_oauthlib import OAuth2Session
from oauthlib.oauth2 import BackendApplicationClient
import json
import urllib
import main
from pprint import pprint

#open twitter keys
with open('keys.json', 'r') as f:
   keys = json.loads(f.read())['twitter']

twitter_key = keys['key']
twitter_secret = keys['secret']
client = BackendApplicationClient(client_id=twitter_key)
oauth = OAuth2Session(client=client)
token = oauth.fetch_token(token_url='https://api.twitter.com/oauth2/token',
                          client_id=twitter_key,
                          client_secret=twitter_secret)

# Base url needed for future queries
base_url = 'https://api.twitter.com/1.1/'

# specific page to append to
page = 'search/tweets.json'

#store movie title into variable
def getMovieTitle(mov):
  movie_title = mov['title']
  return movie_title

# function converting user input text to URL
def encodeTitle(movie_title):
	url_title = urllib.parse.urlencode(movie_title)
	#or just url_title = urllib.urlencode(movie_title)
	return url_title

def getURL(url_title):
	req_url = base_url + page + '?q=' + url_title + '&tweet_mode=extended&count=100'
	return req_url

# HTTP info request
def getResponse(req_url):
  response = oauth.get(req_url)
  return response
# Read the query results
def getResults(response):
  results = json.loads(response.content.decode('utf-8'))
  return results

## Process the results
def getStatuses(results):
  tweets = results['statuses']
  while True:
    if not ('next_results' in results['search_metadata']):
      break
    if len(tweets) > 10000:
      break
    next_search = base_url + page + results['search_metadata']['next_results'] + '&tweet_mode=extended'
    print(results['search_metadata']['next_results'])
    response = oauth.get(next_search)
    results = json.loads(response.content.decode('utf-8'))
    tweets.extend(results['statuses'])
    return tweets
###list comp
def tweetList(tweets):
  tweet_texts = [text['full_text'] for text in tweets]
  return tweet_texts




#def get_tweet_texts(tweet_texts):
 # for tweet_text in tweet_texts[0:9]:
  #  return tweet_text

def get_tweet_texts(tweet_texts):
  tweet_list = []
  for tweet_text in tweet_texts[0:9]:
    tweet_list.append(tweet_text)
  return tweet_list

def getTweets():
  title = getMovieTitle(mov)
  url = encodeTitle(title)
  req_url = getURL(url)
  response = getResponse(req_url)
  results = getResults(response)
  tweets = getStatuses(results)
  tweet_texts = tweetList(tweets)
  tweet_list = get_tweet_texts(tweet_texts)
  print(tweet_list)





## hashtags

#def get_hashtags(tweet):
#	hash_list = []
#	hashtags = tweet['entities']['hashtags']
#	for tag in hashtags:
#		hash_list.append(tag['text'])

#	return(hash_list)

#tags_per_tweet = [get_hashtags(tweet) for tweet in tweets]
