from Myro import *
init ("sim")
def danceMove1():#movement right,comes back to origin
    forward(3,1)
    turnBy(180)
    forward(3,1)
    turnBy(180)
    
def danceMove2():#movement left
    turnBy(180)
    forward(3,1)
    turnBy(180)
    forward(3,1)
    
def danceMove3():#upward,sprins turns back
    turnBy(90)
    forward(3,1)
    turnBy(180)
    forward(3,1)
    turnBy(270)

def danceMove4():#downward, spins turns back
    turnBy(270)
    forward(3,1)
    turnBy(180)
    forward(3,1)
    turnBy(90)

def danceMove5():#upward spin turnback leftward spin turnback etc.
    x = 0
    for x in range(5):
        turnBy(2.45)
        forward(1,.5)
        turnLeft(4.9,1)
        turnLeft(4.9,1)
        backward(1,.5)
        
        x = x+1
        
def danceMove6():#dancemove5, but opposite direction
    x = 0
    for x in range(5):
        turnLeft(7.35,1)
        forward(3,1)
        turnRight(4.9,1)
        turnRight(4.9,1)
        backward(3,1)
        
        x = x+1

        
def danceMove7():#diagonal variation
    x = 0
    for x in range(4):
        turnLeft(1.3,1)
        forward(3,.5)
        turnLeft(4.9,1)
        turnLeft(4.9,1)
        backward(3,1)
        x = x+1
        
def danceMove8():#opposite of move7
    x = 0
    for x in range(5):
        turnRight(1.3,1)
        forward(3,.5)
        turnRight(4.9,1)
        turnRight(4.9,1)
        backward(3,1)
        x = x+1
        
#HOLY MOLY ITS ACTUAL MOVEMENTS IN ACTION NOW


turnLeft(4.9,.5)
wait(.5)
turnRight(4.9,.5)#1 second of build up
wait(.5)
turnRight(4.9,.5)
turnLeft(4.9,5)
danceMove5()
danceMove7()
danceMove5()
wait(1)
danceMove4()
danceMove6()
danceMove8()
danceMove6()
wait(1)