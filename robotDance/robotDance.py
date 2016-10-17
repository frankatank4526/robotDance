from Myro import *
init ("sim")
def danceMove1():#movement right,comes back to origin
    forward(3,1)
    turnBy(180)
    forward(3,1)
    turnBy(180)
    
def danceMove2():#
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
    while x < 5:
        turnBy(2.45)
        forward(3,1)
        turnBy(4.9,1)
        turnBy(4.9,1)
        backward(3,1)
        
        x = x+1
        
def danceMove6():
    x = 1
    while x < 5:
        turnLeft(7.35,1)
        forward(3,1)
        turnBy(4.9,1)
        turnBy(4.9,1)
        backward(3,1)
        
        x = x+1

        
def danceMove7():
    x = 1
    while x < 9:
        turnLeft(1.3,1)
        forward(3,.5)
        turnLeft(4.9,1)
        turnLeft(4.9,1)
        backward(3,1)
        
        x = x+1
        
def danceMove8():
    x = 1
    while x < 9:
        turnRight(1.3,1)
        forward(3,.5)
        turnRight(4.9,1)
        turnRight(4.9,1)
        backward(3,1)
        
        x = x+1
        
danceMove7()