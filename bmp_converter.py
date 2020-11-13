import os
import imageio
import screenshoter



def get_data(number):
    screenshoter.take_shot(number)
    path = "Shots/"+str(number)+".bmp"
    image = imageio.imread(path)
    return image




