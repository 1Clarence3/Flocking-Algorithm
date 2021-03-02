import math
import random

class Vector:
    x = 0
    y = 0
    def __init__(self):
        self.x = 0
        self.y = 0

    def initiatePosVector(self):
        self.x = random.uniform(0,1000)
        self.y = random.uniform(0,563)

    def randVector(self):
        self.x = random.uniform(-1,1)
        self.y = random.uniform(-1,1)

    def setX(self,x):
        self.x = x

    def setY(self,y):
        self.y = y

    def setMag(self,mag):
        currMag = math.sqrt(self.x**2 + self.y**2)
        self.x = (self.x/currMag)*mag
        self.y = (self.y/currMag)*mag

    def add(self,otherVec):
        self.x += otherVec.x
        self.y += otherVec.y

    def sub(self,otherVec):
        self.x -= otherVec.x
        self.y -= otherVec.y

    def div(self,otherVec):
        self.x /= otherVec.x
        self.y /= otherVec.y

    def mult(self,otherVec):
        self.x *= otherVec.x
        self.y *= otherVec.y

    def limit(self,force):
        currMag = math.sqrt(self.x ** 2 + self.y ** 2)
        if currMag > force:
            self.x = (self.x/currMag)*force
            self.y = (self.y/currMag)*force

    def dist(self,otherVec):
        return math.sqrt((otherVec.x - self.x)**2+(otherVec.y - self.y)**2)