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

bg = pygame.image.load('pixil-frame-0-3.png').convert()
bgX = 0
bgX2 = bg.get_width()

# def blit_alpha(target,source,location,opacity):
#     x = location[0]
#     y = location[1]
#     temp = pygame.Surface((source.get_width))

clock = pygame.time.Clock()

class player(object):
    run = [pygame.image.load(os.path.join('Artwork','RunLeft.png')),
            pygame.image.load(os.path.join('Artwork','RunRight.png'))]
    jump = pygame.image.load(os.path.join('Artwork','Jump.png'))
    slide = pygame.image.load(os.path.join('Artwork','Slide.png'))
    jumpList = [1,1,2,2,2,2,3,3,3,3,4,4,4,4,0,0,0,0,-1,-1,-1,
                -2,-2,-2,-2,-3,-3,-3,-3,-4,-4,-4,-4,-4]
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

    def draw(self, win):
        if self.jumping:
            self.y -= self.jumpList[self.jumpCount] * 1.2
            win.blit(self.jump, (self.x,self.y))
            self.jumpCount += 1
            if self.jumpCount > 32:
                self.jumpCount = 0
                self.jumping = False
                self.runCount = 0
        elif self.sliding or self.slideUp:
            #if self.slideCount < 20:
                #self.y += 1
            if self.slideCount ==25:
                #self.y -= 19
                self.sliding = False
                #self.slideUp = True
            if self.slideCount >= 25:
                self.slideCount = 0
                self.slideUp = False
                self.runCount = 0
            win.blit(self.slide, (self.x,(self.y+50)))
            self.slideCount += 1

        else:
            if self.runCount > 2:
                self.runCount = 1
            win.blit(self.run[self.runCount//2], (self.x,self.y))
            self.runCount += 1
            time.sleep(0.1)

class ground(object):
    img = [pygame.image.load(os.path.join('Artwork','Bush1.png')),
            pygame.image.load(os.path.join('Artwork','Bush2.png')),
            pygame.image.load(os.path.join('Artwork','FireHydrant.png')),
            pygame.image.load(os.path.join('Artwork','TrashCan.png')),
            pygame.image.load(os.path.join('Artwork','Dog.png'))]

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = (x,y,width,height)

    def draw(self,win,groundind):
        win.blit(self.img[groundind], (self.x, self.y))
        self.hitbox = (self.x+2, self.y, self.width+10, self.height-10)
        pygame.draw.rect(win, (255,0,0), self.hitbox, 2)

class fly(ground):
    img = [pygame.image.load(os.path.join('Artwork','Birds1.png')),
            pygame.image.load(os.path.join('Artwork','Birds2.png')),
            pygame.image.load(os.path.join('Artwork','Birds3.png'))]

    def draw(self,win,flyind):
        win.blit(self.img[flyind], (self.x,self.y))
        self.hitbox = (self.x + 5, self.y + 5, self.width - 10, self.height)
        pygame.draw.rect(win, (255,0,0), self.hitbox, 2)


def redrawWindow():
    win.blit(bg, (bgX, 0))
    win.blit(bg, (bgX2,0))
    runner.draw(win)
    flyy.draw(win,flyind)
    groundd.draw(win,groundind)
    pygame.display.update()

flyind = random.randint(0,2)
groundind = random.randint(0,4)
flyy = fly(300,0,64,64)

if groundind == 0: #darkbush
    groundd = ground(300,230,64,64)
elif groundind == 1: #lightbush
    groundd = ground(300,242,35,45)
elif groundind == 2: #firehydrant
    groundd = ground(300,240,20,52)
elif groundind == 3: #trash can
    groundd = ground(300,240,20,52)
runner = player(200, 170, 10, 17)
pygame.time.set_timer(USEREVENT+1, 500)
speed = 30
run = True


while run:
    redrawWindow()
    bgX -= 1.4
    bgX2 -= 1.4
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

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE] or keys[pygame.K_UP]:
        if not (runner.jumping):
            runner.jumping = True

    if keys[pygame.K_DOWN]:
        if not (runner.sliding):
            runner.sliding = True

    clock.tick(speed)
