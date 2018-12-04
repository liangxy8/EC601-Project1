# EC601-Project1
## how to run this Project
1. Inpute your consumer_key, consumer_secret, access_key, access_secret in "get_pictures.py".  
2. run "run.sh" in the terminal and you will get a video combined with the images posted in tweets and the description of these images.  
3. remember to add json file and change the json file's storage path in "run.sh", when you run this code in your own computer.  
## some statements
1. The function of "get_pictures.py" is to download images from twitter feed.  
   The function of code 
'''python
ffmpeg -loglevel panic -framerate 0.4 -i images/%d.jpg -c:v libx264 -r 30 -s 800*600 -pix_fmt yuv420p video.mp4" 
'''
is to convert images to a video.  
   The function of "get_label_annotation.py" is to use Google Cloud APIs to describe the content of the images in the video.  
2. You can choose any user you like, any number of tweets you want to get by changing the input arguments of "get_pictures.py" in "run.sh". And you can also customize the folder where the images are stored. For Example, I use the following code to  get the latest 20 tweets of National Geographic:  
```python
       python tweepy --username NatGeo --num 20 --output './images/'
```
