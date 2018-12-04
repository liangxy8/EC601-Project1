#!/bin/sh

#download images from twitter feed, and you can choose any user you like, any number of twitter you want to get. And you can customize the folder where the images are stored.
python get_pictures.py --username NatGeo --num 20 --output './images/'

#convert images to a video
#ffmpeg -i images/%d.jpg video.avi
ffmpeg -loglevel panic -framerate 0.4 -i images/%d.jpg -c:v libx264 -r 30 -s 800*600 -pix_fmt yuv420p video.mp4

#setting environment variable
export GOOGLE_APPLICATION_CREDENTIALS="/home/lxy/EC601/EC601-Project3/mini-project3-6e29c4fa21eb.json"

#using Google_Vision APIs to describe the content of the images.
python get_label_annotation.py

