import pygame
import math
import random
from Vector import Vector

#Boid Image
boidImg = pygame.image.load("Boid.png")
boidImg = pygame.transform.rotate(boidImg,-45)

#Screen dimensions
screenWidth = 1000
screenHeight = 563

class Boid:
    pos = Vector()
    velocity = Vector()
    acceleration = Vector()
    ownBoidImg = boidImg
    alignFactor = 1
    cohesionFactor = 1
    seperationFactor = 1
    maxForce = 1
    maxSpeed = 4
    radius = 80

    def __init__(self):
        self.pos = Vector()
        self.velocity = Vector()
        self.acceleration = Vector()
        self.pos.initiatePosVector()
        self.velocity.randVector()
        self.velocity.setMag(random.uniform(2,4))
        self.alignFactor = 1
        self.cohesionFactor = 1
        self.seperationFactor = 1
        self.maxForce = 1
        self.maxSpeed = 4
        self.radius = 80

    #Displays boid on screen
    def show(self,screen):
        rad = math.atan2(self.velocity.y,self.velocity.x)
        deg = -1*math.degrees(rad)
        image = pygame.transform.rotate(self.ownBoidImg, deg)
        screen.blit(image,(self.pos.x,self.pos.y))

    #Updates the position, velocity, acceleration, and forces on the boid
    def update(self, align, cohesion, seperation, force, speed, radius):
        self.alignFactor = align
        self.cohesionFactor = cohesion
        self.seperationFactor = seperation
        self.maxForce = force
        self.maxSpeed = speed
        self.radius = radius
        self.pos.add(self.velocity)
        self.velocity.add(self.acceleration)
        self.velocity.limit(self.maxSpeed)
        self.acceleration.x *= 0
        self.acceleration.y *= 0

    #Creates steering force for alignment
    def align(self,boids):
        steering = Vector()
        tot = 0
        for other in boids:
            dist = self.pos.dist(other.pos)
            if self.pos.x != other.pos.x and self.pos.y != other.pos.y and dist < self.radius:
                steering.add(other.velocity)
                tot = tot+1
        if tot > 0:
            steering.x /= tot
            steering.y /= tot
            steering.setMag(self.maxSpeed)
            steering.sub(self.velocity)
            steering.limit(self.maxForce)
        return steering

    # Creates steering force for cohesion
    def cohesion(self,boids):
        steering = Vector()
        tot = 0
        for other in boids:
            dist = self.pos.dist(other.pos)
            if self.pos.x != other.pos.x and self.pos.y != other.pos.y and dist < self.radius:
                steering.add(other.pos)
                tot = tot + 1
        if tot > 0:
            steering.x /= tot
            steering.y /= tot
            steering.sub(self.pos)
            steering.setMag(self.maxSpeed)
            steering.sub(self.velocity)
            steering.limit(self.maxForce)
        return steering

    # Creates steering force for seperation
    def seperation(self,boids):
        steering = Vector()
        tot = 0
        for other in boids:
            dist = self.pos.dist(other.pos)
            if self.pos.x != other.pos.x and self.pos.y != other.pos.y and dist < self.radius:
                distVector = Vector()
                distVector.setX(self.pos.x - other.pos.x)
                distVector.setY(self.pos.y - other.pos.y)
                distVector.x /= dist**2
                distVector.y /= dist**2
                steering.add(distVector)
                tot += 1
        if tot > 0:
            steering.x /= tot
            steering.y /= tot
            steering.setMag(self.maxSpeed)
            steering.sub(self.velocity)
            steering.limit(self.maxForce)
        return steering

    #Adds alignment, cohesion, and seperation factors to acceleration vector
    def flock(self,boids):
        #only for align
        alignment = self.align(boids)
        alignment.x *= self.alignFactor
        alignment.y *= self.alignFactor
        self.acceleration.add(alignment)

        #only for cohesion
        cohesion = self.cohesion((boids))
        cohesion.x *= self.cohesionFactor
        cohesion.y *= self.cohesionFactor
        self.acceleration.add(cohesion)

        #only for seperation
        seperation = self.seperation(boids)
        seperation.x *= self.seperationFactor
        seperation.y *= self.seperationFactor
        self.acceleration.add(seperation)

    #Allows boid to teleport across the edges of the screen
    def wrapAround(self):
        if self.pos.x > screenWidth:
            self.pos.setX(0)
        elif self.pos.x < 0:
            self.pos.setX(screenWidth)
        if self.pos.y > screenHeight:
            self.pos.setY(0)
        elif self.pos.y < 0:
            self.pos.setY(screenHeight)