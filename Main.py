import pygame
from tkinter import *
from tkinter import messagebox
from Boid import Boid

#Music player
pygame.mixer.init()
pygame.mixer.music.load("Music.mp3")
pygame.mixer.music.play()

#Boid Image
boidImg = pygame.image.load("Boid.png")
boidImg = pygame.transform.rotate(boidImg,-45)

#Screen dimensions
screenWidth = 1000
screenHeight = 563

#pygame initialization
pygame.init()
screen = pygame.display.set_mode((screenWidth,screenHeight))

pygame.display.set_caption("Flocking Simulation")
icon = pygame.image.load('Flocking Icon.jpg')
pygame.display.set_icon(icon)

#Flock creation
flocks = []

#Slider constants
margin = 100
barX1 = margin-30
barX2 = ((screenWidth-(margin*2))/6)+margin-30
barX3 = ((screenWidth-(margin*2))/6)*2+margin-30
barX4 = ((screenWidth-(margin*2))/6)*3+margin-30
barX5 = ((screenWidth-(margin*2))/6)*4+margin-30
barX6 = ((screenWidth-(margin*2))/6)*5+margin-30
barX7 = ((screenWidth-(margin*2))/6)*6+margin-30
barY = screenHeight-20

xScroll1 = barX1
xScroll2 = barX2
xScroll3 = barX3    
xScroll4 = barX4
xScroll5 = barX5
xScroll6 = barX6
xScroll7 = barX7

global boidPopulation, alignFactor, cohesionFactor, seperationFactor, maxForce, maxSpeed, perceptionRadius

root = Tk()

#Functions to create sliders & drawing buttons
def slider1(x,y,width,height,activeColor, action = None):
    global xScroll1
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + width > cur[0] > x and y + height + 40 > cur[1] > y - 40:
        pygame.draw.rect(screen,activeColor,(x,y,width,height))
        if click[0] == 1 and action != None:
            if action == "scroll1":
                xScroll1 = cur[0]
    else:
            pygame.draw.rect(screen,(120,120,120),(x,y,width,height))

def slider2(x,y,width,height,activeColor, action = None):
    global xScroll2
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + width > cur[0] > x and y + height + 40 > cur[1] > y - 40:
        pygame.draw.rect(screen,activeColor,(x,y,width,height))
        if click[0] == 1 and action != None:
            if action == "scroll1":
                xScroll2 = cur[0]
    else:
            pygame.draw.rect(screen,(120,120,120),(x,y,width,height))

def slider3(x,y,width,height,activeColor, action = None):
    global xScroll3
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + width > cur[0] > x and y + height + 40 > cur[1] > y - 40:
        pygame.draw.rect(screen,activeColor,(x,y,width,height))
        if click[0] == 1 and action != None:
            if action == "scroll1":
                xScroll3 = cur[0]
    else:
            pygame.draw.rect(screen,(120,120,120),(x,y,width,height))

def slider4(x,y,width,height,activeColor, action = None):
    global xScroll4
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + width > cur[0] > x and y + height + 40 > cur[1] > y - 40:
        pygame.draw.rect(screen,activeColor,(x,y,width,height))
        if click[0] == 1 and action != None:
            if action == "scroll1":
                xScroll4 = cur[0]
    else:
            pygame.draw.rect(screen,(120,120,120),(x,y,width,height))

def slider5(x,y,width,height,activeColor, action = None):
    global xScroll5
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + width > cur[0] > x and y + height + 40 > cur[1] > y - 40:
        pygame.draw.rect(screen,activeColor,(x,y,width,height))
        if click[0] == 1 and action != None:
            if action == "scroll1":
                xScroll5 = cur[0]
    else:
            pygame.draw.rect(screen,(120,120,120),(x,y,width,height))

def slider6(x,y,width,height,activeColor, action = None):
    global xScroll6
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + width > cur[0] > x and y + height + 40 > cur[1] > y - 40:
        pygame.draw.rect(screen,activeColor,(x,y,width,height))
        if click[0] == 1 and action != None:
            if action == "scroll1":
                xScroll6 = cur[0]
    else:
            pygame.draw.rect(screen,(120,120,120),(x,y,width,height))

def slider7(x,y,width,height,activeColor, action = None):
    global xScroll7
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + width > cur[0] > x and y + height + 40 > cur[1] > y - 40:
        pygame.draw.rect(screen,activeColor,(x,y,width,height))
        if click[0] == 1 and action != None:
            if action == "scroll1":
                xScroll7 = cur[0]
    else:
            pygame.draw.rect(screen,(120,120,120),(x,y,width,height))

#Draws "Help" button
def drawButton(window, x, y, width, height, color, text, action = None):
    if action:
        pygame.draw.rect(window,action,(x-2,y-2,width+4,height+4),0)
    pygame.draw.rect(window,color,(x,y,width,height),0)
    if text != "":
        font = pygame.font.SysFont("comicsans",32)
        text = font.render(text,1,(0,0,0))
        window.blit(text,(x+(width/2-text.get_width()/2),y+(height/2-text.get_height()/2)))

#Checks if "Help" button was clicked
def clicked(mousePos,x,y,width,height):
    if mousePos[0] > x and mousePos[0] < x + width:
        if mousePos[1] > y and mousePos[1] < y + height:
            return True
    return False

#Game Loop
running = True

while running:
    #Gets position of mouse and "Clicked" event
    pos = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    #Allows game loop to continue
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((75, 0, 130))

    #Slider creations:
    font = pygame.font.Font("freesansbold.ttf", 16)

    #Boid population
    text1 = font.render("Boids", True, (255, 255, 255))
    textRect1 = text1.get_rect()
    textRect1.center = (barX1 + 35, screenHeight - 50)
    slider1(barX1, barY, 75, 2, (120, 120, 120), action="scroll1")
    pygame.draw.rect(screen, (120, 120, 120), [xScroll1 - 5, barY - 12, 10, 24])
    boidPopulation = round((xScroll1 - (barX1+1))*(79/73)+1)

    #Alignment factor
    text2 = font.render("Alignment",True,(255,255,255))
    textRect2 = text2.get_rect()
    textRect2.center = (barX2+35,screenHeight-50)
    slider2(barX2,barY,75,2,(120,120,120),action="scroll1")
    pygame.draw.rect(screen,(120,120,120),[xScroll2-5,barY-12,10,24])
    alignFactor = (xScroll2 - (barX2+1))/70

    #Cohesion factor
    text3 = font.render("Cohesion", True, (255,255,255))
    textRect3 = text3.get_rect()
    textRect3.center = (barX3+35,screenHeight-50)
    slider3(barX3,barY,75,2,(120,120,120),action="scroll1")
    pygame.draw.rect(screen, (120, 120, 120), [xScroll3 - 5, barY - 12, 10, 24])
    cohesionFactor = (xScroll3 - (barX3+1))/70

    #Seperation factor
    text4 = font.render("Seperation", True, (255,255,255))
    textRect4 = text4.get_rect()
    textRect4.center = (barX4+35,screenHeight-50)
    slider4(barX4, barY, 75, 2, (120, 120, 120), action="scroll1")
    pygame.draw.rect(screen, (120, 120, 120), [xScroll4 - 5, barY - 12, 10, 24])
    seperationFactor = (xScroll4 - (barX4+1))/50

    #Max Force factor
    text5 = font.render("Max Force", True, (255,255,255))
    textRect5 = text5.get_rect()
    textRect5.center = (barX5 + 35, screenHeight - 50)
    slider5(barX5, barY, 75, 2, (120, 120, 120), action="scroll1")
    pygame.draw.rect(screen, (120, 120, 120), [xScroll5 - 5, barY - 12, 10, 24])
    maxForce = (xScroll5-(barX5+1))*(8/73)+1

    #Max Speed factor
    text6 = font.render("Max Speed", True, (255,255,255))
    textRect6 = text6.get_rect()
    textRect6.center = (barX6 + 35, screenHeight - 50)
    slider6(barX6, barY, 75, 2, (120, 120, 120), action="scroll1")
    pygame.draw.rect(screen, (120, 120, 120), [xScroll6 - 5, barY - 12, 10, 24])
    maxSpeed = (xScroll6 - (barX6 + 1)) * (8 / 73) + 1

    #Boid's viewing radius
    text7 = font.render("Perception Radius", True, (255,255,255))
    textRect7 = text7.get_rect()
    textRect7.center = (barX7 + 35, screenHeight - 50)
    slider7(barX7, barY, 75, 2, (120, 120, 120), action="scroll1")
    pygame.draw.rect(screen, (120, 120, 120), [xScroll7 - 5, barY - 12, 10, 24])
    perceptionRadius = (xScroll7 - (barX7 + 1)) * (499 / 73) + 1

    #Draw the "Help" button
    drawButton(screen, screenWidth-200, 20, 60, 20, (128,128,128), "Help", True)
    curr = pygame.mouse.get_pos()
    if clicked(curr,screenWidth-200,20,60,20):
        drawButton(screen, screenWidth-200, 20, 60, 20, (255, 0, 0), "Help", True)

    #"Help" button
    if event.type == pygame.MOUSEBUTTONDOWN:
        if clicked(curr,screenWidth-200,20,60,20):
            messagebox.showinfo("Flocking Simulation Guide","1. The first slider controls the population of boids (1-80 boids)"
                                                            "\n2. The 2nd, 3rd, and 4th sliders determine how much that factors vector is multiplied by (1-2)"
                                                            "\n3. The \"Max Force\" slider limits the magnitude of the steering force (1-10) (You won't see much difference)"
                                                            "\n4. The \"Max Speed\" slider sets the magnitude of the velocity vector (1-10)"
                                                            "\n5. The \"Perception Radius\" slider sets the radius that each boid can see (1-500) (Slide this slider a little bit to have maximum flocking effect)")
            root.destroy()
            root = Tk()
            root.withdraw()

    #Display all text on screen
    screen.blit(text1, textRect1)
    screen.blit(text2, textRect2)
    screen.blit(text3, textRect3)
    screen.blit(text4, textRect4)
    screen.blit(text5, textRect5)
    screen.blit(text6, textRect6)
    screen.blit(text7, textRect7)

    #Changes the boid population
    while boidPopulation != len(flocks):
        if boidPopulation > len(flocks):
            addedBoid = Boid()
            flocks.append(addedBoid)
        elif boidPopulation < len(flocks):
            flocks.pop()

    #Updates each invidivual boid in the flock
    for boid in flocks:
        boid.wrapAround()
        boid.flock(flocks)
        boid.update(alignFactor,cohesionFactor,seperationFactor,maxForce,maxSpeed,perceptionRadius)
        boid.show(screen)
    pygame.display.update()