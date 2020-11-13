import os
import bmp_converter
import screenshoter
import key
import Neural_Network
import math


def boot():
    os.system("open /Applications/Google\ Earth\ Pro.app")
    screenshoter.take_shot(0)
    w,h = screenshoter.get_dimensions('Shots/'+str(0)+'.bmp')
    net = [w*h*3, w*h*4, w*h*5,w*h*5,w*h*3,w*h*2,w*h*2,w*h,math.floor(1.5*w*h/2),400,400,300,200,150,90, 70, 60, 52, 46, 38, 33, 25, 11, 7, 4, 1]
    print("Net has: ", sum(net))
    nn = Neural_Network.NeuralNetwork(net)
    
    
boot()
