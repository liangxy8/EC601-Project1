#!/usr/bin/python

import io
import os

from google.cloud import vision
from google.cloud.vision import types

#Instantiates a client
client = vision.ImageAnnotatorClient()

#get all names of the image files to annotate and load these images into memory
for filename in os.listdir("/home/lxy/GitHub/EC601-Project1/images/"):
    print(filename+':')
    name = '/home/lxy/GitHub/EC601-Project1/images/'+filename
    with io.open(name, 'rb') as image:
        image_content = image.read()
    pictures = types.Image(content= image_content)
    
    #Performs label detection on the image file
    response = client.label_detection(image=pictures)
    labels = response.label_annotations

    print('Labels:')
    for label in labels:
        print(label.description)
    print('\n')



