# EC601-Project1
## how to run this Project
1. Inpute your consumer_key, consumer_secret, access_key, access_secret in "tweepy".  
2. run "run.sh" in the terminal and you will get a video combined with the images posted in tweets and the description of these images.  
3. remember to change the file's storage path in "google_vision", when you run this code in your own computer.  
## some statements
1. The function of "tweepy" is to download images from twitter feed.  
   The function of code "ffmpeg -i images/%d.jpg video.avi" is to convert images to a video.  
   The function of "google_vision" is to use Google Vision APIs to describe the content of the images.  
2. You can choose any user you like, any number of tweets you want to get by changing the input arguments of "tweepy" in "run.sh". And you can also customize the folder where the images are stored. For Example, I use the following code to  get the latest 20 tweets of National Geographic:  
```python
       python tweepy --username NatGeo --num 20 --output './images/'
```
