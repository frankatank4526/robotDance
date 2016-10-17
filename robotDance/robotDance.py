from Myro import *
init ("sim")
def danceMove1():
    forward(3,1)
    turnBy(180)
    forward(3,1)
    turnBy(180)
    
def danceMove2():
    turnBy(180)
    forward(3,1)
    turnBy(180)
    forward(3,1)

def danceMove3():
    turnBy(90)
    forward(3,1)
    turnBy(180)
    forward(3,1)
    turnBy(270)

def danceMove4():
    turnBy(270)
    forward(3,1)
    turnBy(180)
    forward(3,1)
    turnBy(90)

def danceMove5():
    x = 1
    while x < 4:
        turnBy(90)
        forward(3,1)
        turnBy(180)
        turnBy(180)
        backward(3,1)
        
        x = x+1
danceMove5()