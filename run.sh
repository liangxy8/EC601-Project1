#!/bin/sh

#download images from twitter feed, and you can choose any user you like, any number of twitter you want to get. And you can customize the folder where the images are stored.
python tweepy --username NatGeo --num 20 --output './images/'

#convert images to a video
ffmpeg -i images/%d.jpg video.avi

#setting environment variable
export GOOGLE_APPLICATION_CREDENTIALS="/home/lxy/GitHub/EC601-Project1/My First Project-4e5403450a58.json"

#using Google_Vision APIs to describe the content of the images.
python google_vision

