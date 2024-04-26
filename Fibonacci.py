import sys,random
import math
import pygame
from pygame.locals import *

#
pygame.init()
WIDTH=700
HEIGHT=700
screen=pygame.display.set_mode((WIDTH,HEIGHT))
color=pygame.Color(0)

def colorHSV(v):
    color.hsva=(random.randint(0,360),30,v*100,100)
    return color

def drawSquare():
    xPos,yPos=0,0
    #nextFibo=fibo[-2]+fibo[-1]
    #scalar=WIDTH/nextFibo
    scalar=WIDTH/fibo[-1]

    for i in range(1,len(fibo)):
        pygame.draw.rect(screen,colorHSV(i/len(fibo)/2+0.5),(scalar*xPos,scalar*yPos,scalar*fibo[i]+1,scalar*fibo[i]+1))
        if i%2==1:
            xPos+=fibo[i]
            yPos-=fibo[i-1]
        else:
            xPos-=fibo[i-1]
            yPos+=fibo[i]

def drawSpiral():
    SGN=[-1,1,1,-1]
    xPos,yPos=0,0
    scalar=WIDTH/(2*fibo[-5])

    for i in range(1,len(fibo)-1):
        x,y,w,h=scalar*xPos,scalar*yPos,scalar*SGN[(i+1)%4]*fibo[i],scalar*SGN[i%4]*fibo[i]
        #w,hが負の数なら、変換
        if w<0:
            x+=w
            w=-w
        if h<0:
            y+=h
            h=-h
        pygame.draw.rect(screen,colorHSV(i/len(fibo)/2+0.5),(WIDTH/2+x,WIDTH/2+y,w+1,h+1))

        if i%2==1:
            xPos+=SGN[i%4]*(fibo[i]+fibo[i+1])
        else:
            yPos+=SGN[i%4]*(fibo[i]+fibo[i+1])
#
def main():
    screen.fill((0,0,0))
    #drawSquare()
    drawSpiral()
    #
    pygame.display.update()
    #
    while True:
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()

fibo=[0,1]
for i in range(16):
    fibo.append(fibo[-1]+fibo[-2])

if __name__=="__main__":
    print(fibo)
    main()