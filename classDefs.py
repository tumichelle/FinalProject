import pygame
from pygame.locals import *
import os
import sys
import math
import time
import random

class player(object):
    run = [pygame.image.load(os.path.join('Artwork','RunLeft.png')),
        pygame.image.load(os.path.join('Artwork','RunLeft.png')),
        pygame.image.load(os.path.join('Artwork','RunRight.png')),
        pygame.image.load(os.path.join('Artwork','RunRight.png')),]
    jump = pygame.image.load(os.path.join('Artwork','Jump.png'))
    slide = pygame.image.load(os.path.join('Artwork','Slide.png'))
    fall = pygame.image.load(os.path.join('Artwork','Fall.png'))
    jumpList = [30,30,30,0,0,0,0,0,0,0,0,0
                -30,-30,-30]
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
        self.hitbox = (x,y,width,height)
        self.fallCount = 0

    def draw(self, win):
        if self.falling:
            win.blit(self.fall, (self.x, self.y + 90))
            self.fallCount += 12
            if self.fallCount >= 70:
                self.fallCount = 0
                self.falling = False
        elif self.jumping:
            self.y -= self.jumpList[self.jumpCount] * 1.2
            win.blit(self.jump, (self.x,self.y))
            self.jumpCount += 1
            if self.jumpCount > 14:
                self.jumpCount = 0
                self.jumping = False
                self.runCount = 0
            self.hitbox = (self.x + 4, self.y, self.width + 10, self.height-20)
        elif self.sliding or self.slideUp:
            #if self.slideCount < 20:
                #self.y += 1
            if self.slideCount ==18:
                #self.y -= 19
                self.sliding = False
                #self.slideUp = True
            if self.slideCount < 18:
                self.hitbox = (self.x, self.y+60,111 , 51)
            if self.slideCount >= 18:
                self.slideCount = 0
                self.slideUp = False
                self.runCount = 0
                self.hitbox = (self.x, self.y+100, 60, 51)
            win.blit(self.slide, (self.x,(self.y+50)))
            self.slideCount += 1


        else:
            if self.runCount > 5:
                self.runCount = 1
            win.blit(self.run[self.runCount//2], (self.x,self.y))
            self.runCount += 1
            self.hitbox = (self.x+6, self.y+10, self.width, self.height)


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

    def collide(self, rect): #for ground objects
        if rect[0] + rect[2] > self.hitbox[0] and rect[0] < self.hitbox[0] + self.hitbox[2]:
            if rect[1] + rect[3] > self.hitbox[1]:
                return True
        return False

class firehydrant(bush1):
    img = (pygame.image.load(os.path.join('Artwork','FireHydrant.png')))

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = (x,y,width,height)

    def draw(self,win):
        win.blit(pygame.transform.scale(self.img, (44,44)), (self.x, self.y))
        self.hitbox = (self.x+2, self.y, self.width-10, self.height-10)

    def collide(self, rect): #for ground objects
        if rect[0] + rect[2] > self.hitbox[0] and rect[0] < self.hitbox[0] + self.hitbox[2]:
            if rect[1] + rect[3] > self.hitbox[1]:
                return True
        return False

class bush2(bush1):
    img = (pygame.image.load(os.path.join('Artwork','Bush2.png')))

    def draw(self,win):
        win.blit(pygame.transform.scale(self.img, (70,55)), (self.x,self.y))
        self.hitbox = (self.x + 5, self.y + 5, self.width - 10, self.height)

    def collide(self, rect): #for ground objects
        if rect[0] + rect[2] > self.hitbox[0] and rect[0] < self.hitbox[0] + self.hitbox[2]:
            if rect[1] + rect[3] > self.hitbox[1]:
                return True
        return False

class dog(bush1):
    img = (pygame.image.load(os.path.join('Artwork','Dog.png')))

    def draw(self,win):
        win.blit(pygame.transform.scale(self.img,(75,45)), (self.x,self.y))
        self.hitbox = (self.x + 5, self.y + 5, self.width - 10, self.height)

    def collide(self, rect): #for ground objects
        if rect[0] + rect[2] > self.hitbox[0] and rect[0] < self.hitbox[0] + self.hitbox[2]:
            if rect[1] + rect[3] > self.hitbox[1]:
                return True
        return False

class trashcan(bush1):
    img = (pygame.image.load(os.path.join('Artwork','TrashCan.png')))

    def draw(self,win):
        win.blit(pygame.transform.scale(self.img,(50,60)), (self.x,self.y))
        self.hitbox = (self.x + 5, self.y + 5, self.width - 10, self.height)

    def collide(self, rect): #for ground objects
        if rect[0] + rect[2] > self.hitbox[0] and rect[0] < self.hitbox[0] + self.hitbox[2]:
            if rect[1] + rect[3] > self.hitbox[1]:
                return True
        return False

class birds1(bush1):
    img = (pygame.image.load(os.path.join('Artwork','Birds1.png')))

    def draw(self,win):
        win.blit(self.img, (self.x,self.y))
        self.hitbox = (self.x + 5, self.y + 5, self.width - 10, self.height)

    def collide(self, rect):
        if rect[0] + rect[2] > self.hitbox[0] and rect[0] < self.hitbox[0] + self.hitbox[2]:
            if rect[1] < self.hitbox[1] + self.hitbox[3]:
                return True
        return False

class birds2(bush1):
    img = (pygame.image.load(os.path.join('Artwork','Birds2.png')))

    def draw(self,win):
        win.blit(self.img, (self.x,self.y))
        self.hitbox = (self.x + 5, self.y + 5, self.width - 10, self.height)

    def collide(self, rect):
        if rect[0] + rect[2] > self.hitbox[0] and rect[0] < self.hitbox[0] + self.hitbox[2]:
            if rect[1] < self.hitbox[3] + self.hitbox[1]:
                return True
        return False

class birds3(bush1):
    img = (pygame.image.load(os.path.join('Artwork','Birds3.png')))

    def draw(self,win):
        win.blit(self.img, (self.x,self.y))
        self.hitbox = (self.x + 5, self.y + 5, self.width - 10, self.height)

    def collide(self, rect):
        if rect[0] + rect[2] > self.hitbox[0] and rect[0] < self.hitbox[0] + self.hitbox[2]:
            if rect[1] < self.hitbox[3] + self.hitbox[1]:
                return True
        return False
