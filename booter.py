import os
import bmp_converter
import screenshoter
import key
import Neural_Network
import math


def get_first_char(file):
    with open(file, 'r') as f:
            for line in f:
                return line[0]

def train(e):
    Answers = []
    for i in range(16):
        answer = [0,0,0]
        file = "TRAING_DATA/TRAIN_"+str(i+1)+".txt"
        x = get_first_char(file)
        if(x == "|"):
            answer = [0,0,1]
        if(x == "^"):
            answer = [1,0,0]
        if(x == "v"):
            answer = [0,1,0]
        Answers.append(answer)
    for i in range(16):
        file = "TRAING_DATA/TRAIN_" + str(i +1) + ".png"
        image_data = bmp_converter.get_data(file)
        
    #nn.fit(Training_data, Answers, learning_rate=0.3, epochs=e)



def boot():
    #os.system("open /Applications/Google\ Earth\ Pro.app")
    screenshoter.take_shot(0)
    w,h = screenshoter.get_dimensions('Shots/'+str(0)+'.bmp')
    net = [w*h*3, w*h*4, w*h*5,w*h*5,w*h*3,w*h*2,w*h*2,w*h,math.floor(1.5*w*h/2),math.floor(w*h/2),math.floor(w*h/2),400,400,300,200,150,90, 70, 60, 52, 46, 38, 33, 25, 11, 7, 4, 3]
    print("Net has: ", sum(net))
    print("Creating Net.. (This will take up to 5 minutes")
    nn = Neural_Network.NeuralNetwork(net)
    print("Done creating Net, Training...")
    train(1)
    print("Done Training")
    return 0
    
    
    
boot()
