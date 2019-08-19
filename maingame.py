import pygame
from pygame.locals import *
import os
import sys
import math
import time
import random

pygame.init()

W, H = 700, 391
win = pygame.display.set_mode((W,H))
pygame.display.set_caption('Escape from Unemployment')

bg = pygame.image.load('pixil-frame-0-4.png').convert()
bgX = 0
bgX2 = bg.get_width()
clock = pygame.time.Clock()

class player(object):
    run = [pygame.image.load(os.path.join('Artwork','RunLeft.png')),
        pygame.image.load(os.path.join('Artwork','RunLeft.png')),
        pygame.image.load(os.path.join('Artwork','RunRight.png')),
        pygame.image.load(os.path.join('Artwork','RunRight.png')),]
    jump = pygame.image.load(os.path.join('Artwork','Jump.png'))
    slide = pygame.image.load(os.path.join('Artwork','Slide.png'))
    jumpList = [12,12,12,12,12,12,0,0,0,0,0
                -12,-12,-12,-12,-12,-12]
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.jumping = False
        self.sliding = False
        self.slideCount = 0
        self.jumpCount = 0
        self.runCount = 0
        self.slideUp = False
        self.falling = False

    def draw(self, win):
        if self.jumping:
            self.y -= self.jumpList[self.jumpCount] * 1.2
            win.blit(self.jump, (self.x,self.y))
            self.jumpCount += 1
            if self.jumpCount > 15:
                self.jumpCount = 0
                self.jumping = False
                self.runCount = 0
            self.hitbox = (self.x + 4, self.y, self.width-24, self.height-10)
        elif self.sliding or self.slideUp:
            #if self.slideCount < 20:
                #self.y += 1
            if self.slideCount ==18:
                #self.y -= 19
                self.sliding = False
                #self.slideUp = True
            if self.slideCount < 18:
                self.hitbox = (self.x, self.y+3, self.width-8, self.height-35)
            if self.slideCount >= 18:
                self.slideCount = 0
                self.slideUp = False
                self.runCount = 0
            win.blit(self.slide, (self.x,(self.y+50)))
            self.hitbox = (self.x+4, self.y, self.width-24, self.height-10)
            self.slideCount += 1

        elif self.falling:
            win.blit(fall, (self.x, self.y + 30))

        else:
            if self.runCount > 5:
                self.runCount = 1
            win.blit(self.run[self.runCount//2], (self.x,self.y))
            self.runCount += 1
            self.hitbox = (self.x+4, self.y, self.width-24, self.height-13)


class bush1(object):
    img = (pygame.image.load(os.path.join('Artwork','Bush1.png')))

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = (x,y,width,height)

    def draw(self,win):
        win.blit(pygame.transform.scale(self.img, (44,44)), (self.x, self.y))
        self.hitbox = (self.x+2, self.y, self.width+10, self.height-10)
        pygame.draw.rect(win, (255,0,0), self.hitbox, 2)

class bush2(bush1):
    img = (pygame.image.load(os.path.join('Artwork','Bush2.png')))

    def draw(self,win):
        win.blit(pygame.transform.scale(self.img, (70,55)), (self.x,self.y))
        self.hitbox = (self.x + 5, self.y + 5, self.width - 10, self.height)
        pygame.draw.rect(win, (255,0,0), self.hitbox, 2)

class dog(bush1):
    img = (pygame.image.load(os.path.join('Artwork','Dog.png')))

    def draw(self,win):
        win.blit(pygame.transform.scale(self.img,(75,45)), (self.x,self.y))
        self.hitbox = (self.x + 5, self.y + 5, self.width - 10, self.height)
        pygame.draw.rect(win, (255,0,0), self.hitbox, 2)

class trashcan(bush1):
    img = (pygame.image.load(os.path.join('Artwork','TrashCan.png')))

    def draw(self,win):
        win.blit(pygame.transform.scale(self.img,(50,60)), (self.x,self.y))
        self.hitbox = (self.x + 5, self.y + 5, self.width - 10, self.height)
        pygame.draw.rect(win, (255,0,0), self.hitbox, 2)

class birds1(bush1):
    img = (pygame.image.load(os.path.join('Artwork','Birds1.png')))

    def draw(self,win):
        win.blit(self.img, (self.x,self.y))
        self.hitbox = (self.x + 5, self.y + 5, self.width - 10, self.height)
        pygame.draw.rect(win, (255,0,0), self.hitbox, 2)

class birds2(bush1):
    img = (pygame.image.load(os.path.join('Artwork','Birds2.png')))

    def draw(self,win):
        win.blit(self.img, (self.x,self.y))
        self.hitbox = (self.x + 5, self.y + 5, self.width - 10, self.height)
        pygame.draw.rect(win, (255,0,0), self.hitbox, 2)

class birds3(bush1):
    img = (pygame.image.load(os.path.join('Artwork','Birds3.png')))

    def draw(self,win):
        win.blit(self.img, (self.x,self.y))
        self.hitbox = (self.x + 5, self.y + 5, self.width - 10, self.height)
        pygame.draw.rect(win, (255,0,0), self.hitbox, 2)

def redrawWindow():
    win.blit(bg, (bgX, 0))
    win.blit(bg, (bgX2,0))
    runner.draw(win)
    for x in objects:
            x.draw(win)
    pygame.display.update()

flyind = random.randint(0,2)
groundind = random.randint(0,3)
runner = player(200, 160, 10, 17)
pygame.time.set_timer(USEREVENT+1, 500)
pygame.time.set_timer(USEREVENT+2, random.randrange(2000,3500)) #can change this to make level harder
speed = 30
run = True

objects = []

while run:
    redrawWindow()

    for objectt in objects:
        objectt.x -= 12
        if objectt.x < objectt.width * -1:
            objects.pop(objects.index(objectt))

    bgX -= 13
    bgX2 -= 13
    if bgX < bg.get_width() * -1:
        bgX = bg.get_width()
    if bgX2 < bg.get_width() * -1:
        bgX2 = bg.get_width()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            quit()
        if event.type == USEREVENT+1:
            speed += 1
        if event.type == USEREVENT+2:
            r = random.randint(1,7)
            if r == 1:
                objects.append(bush1(710,230,44,64))
            elif r == 2:
                objects.append(bush2(710,232,60,75))
            elif r == 3:
                objects.append(trashcan(710,220,50,60))
            elif r == 4:
                objects.append(dog(710,240,75,45))
            elif r == 5:
                objects.append(birds1(710,150,120,50))
            elif r == 6:
                objects.append(birds2(710,150,120,50))
            elif r == 7:
                objects.append(birds3(710,150,120,50))



    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE] or keys[pygame.K_UP]:
        if not (runner.jumping):
            runner.jumping = True

    if keys[pygame.K_DOWN]:
        if not (runner.sliding):
            runner.sliding = True

    clock.tick(speed)
