from Myro import *
init ("sim")
def moveRight():#movement right,comes back to origin
    forward(3,1)
    turnBy(180)
    forward(3,1)
    turnBy(180)
    
def moveLeft():#movement left
    turnBy(180)
    forward(3,1)
    turnBy(180)
    forward(3,1)
    
def moveUp():#upward,sprins turns back
    turnBy(90)
    forward(3,1)
    turnBy(180)
    forward(3,1)
    turnBy(270)

def moveDown():#downward, spins turns back
    turnBy(270)
    forward(3,1)
    turnBy(180)
    forward(3,1)
    turnBy(90)

def upLoop():#upward spin turnback leftward spin turnback etc.
    x = 0
    for x in range(4):
        turnBy(2.45)
        forward(1,.5)
        turnLeft(4.9,1)
        turnLeft(4.9,1)
        backward(1,.5)
        
        x = x+1

        
def downLoop():#dancemove5, but opposite direction
    x = 0
    for x in range(4):
        turnLeft(7.35,1)
        forward(2,1)
        turnRight(4.9,1)
        turnRight(4.9,1)
        backward(2,1)
        
        x = x+1

        
def diagonalLoop1():#diagonal variation
    x = 0
    for x in range(4):
        turnLeft(1.3,1)
        forward(2,.5)
        turnLeft(4.9,1)
        turnLeft(4.9,1)
        backward(2,1)
        
        x = x+1
        
def diagonalLoop2():#opposite of move7
    x = 0
    for x in range(4):
        turnRight(1.3,1)
        forward(2,.5)
        turnRight(4.9,1)
        turnRight(4.9,1)
        backward(2,1)
        x = x+1
        
#HOLY MOLY ITS ACTUAL MOVEMENTS IN ACTION NOW



turnLeft(4.9,.5)
wait(.5)
turnRight(4.9,.5)#1 second of build up
wait(.5)
turnRight(4.9,.5)
turnLeft(4.9,5)
wait(1)
upLoop()
diagonalLoop1()
upLoop()
wait(1)
moveDown()
downLoop()
diagonalLoop2()
downLoop()
    
