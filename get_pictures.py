#!/usr/bin/env python

import tweepy
from tweepy import OAuthHandler
import wget
import json
import argparse
import os

  
#consumer_key = '..............'
#consumer_secret = '.............'
#access_token = '..............'
#access_secret = '...............'


auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

def parse_arguments():
  parser = argparse.ArgumentParser(description='Download pictures from Twitter.')
  parser.add_argument('--username',type=str , help='the twitter screen name from the account we want to retrieve all the picture')
  parser.add_argument('--num', type=int, default=100, help='Maximum number of tweets to be returned.')
  parser.add_argument('--output', default='pictures/', type=str, help='folder where the pictures will be stored')
  args = parser.parse_args()
  return args


def create_folder(output_folder):
  if not os.path.exists(output_folder):
      os.makedirs(output_folder)

def parse(cls, api, raw):
    status = cls.first_parse(api, raw)
    setattr(status, 'json', json.dumps(raw))
    return status

def tweet_media_urls(tweet_status):
  media = tweet_status._json.get('extended_entities', {}).get('media', [])
  if (len(media) == 0):
    return []
  else:
    return [item['media_url'] for item in media]


def download_images_by_user(api, username, num_tweets, output_folder):
  status = tweepy.Cursor(api.user_timeline, screen_name=username, tweet_mode='extended').items()
  create_folder(output_folder)
  downloaded = 0
  file = open("image_list.txt", 'w')
  for tweet_status in status:
      if(downloaded >= num_tweets):
          break
      i = 0
      for media_url in tweet_media_urls(tweet_status):
          file_name = str(downloaded) + ".jpg"
          #file_name = os.path.split(media_url)[1]
          if True or (not os.path.exists(os.path.join(output_folder, file_name))):
              #wget.download(media_url +":orig", out=output_folder+'/'+file_name)
              wget.download(media_url, out=output_folder+'/'+file_name)
              downloaded += 1
              #print(media_url)
              file.write(str(media_url)+'\n')



arguments = parse_arguments()
username = arguments.username
num_tweets = arguments.num
output_folder = arguments.output
download_images_by_user(api, username, num_tweets, output_folder)

