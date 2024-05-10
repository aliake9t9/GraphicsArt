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

def colorHSV():
    color.hsva=(random.randint(0,360),20,100,100)
    return color

#正方形の分割
def divSquare(xPos,yPos,wd):
    itr=0
    xEndPos=xPos+wd
    yEndPos=yPos+wd
    #正方形を塗りつぶす
    pygame.draw.rect(screen,colorHSV(),(xPos,yPos,wd,wd))
    pygame.draw.rect(screen,(127,127,127),(xPos,yPos,wd+1,wd+1),1)
    #
    while wd>thr:
        itr+=1
        if itr%2==1:
            while xPos+wd*ratio<xEndPos+0.1:
                #pygame.draw.rect(screen,colorHSV(),(xPos,yPos,wd*ratio,wd))
                #pygame.draw.rect(screen,(127,127,127),(xPos,yPos,wd*ratio+1,wd+1),1)
                divRect(xPos,yPos,wd*ratio)
                xPos+=wd*ratio
            wd=xEndPos-xPos
        else:
            while yPos+wd/ratio<yEndPos+0.1:
                #pygame.draw.rect(screen,colorHSV(),(xPos,yPos,wd,wd/ratio))
                #pygame.draw.rect(screen,(127,127,127),(xPos,yPos,wd+1,wd/ratio+1),1)
                divRect(xPos,yPos,wd/ratio)
                yPos+=wd/ratio
            wd=yEndPos-yPos

#長方形の分割
def divRect(xPos,yPos,wd):
    itr=0
    xEndPos=xPos+wd
    yEndPos=yPos+wd/ratio
    #塗りつぶす
    pygame.draw.rect(screen,colorHSV(),(xPos,yPos,wd,wd/ratio))
    pygame.draw.rect(screen,(127,127,127),(xPos,yPos,wd+1,wd/ratio+1),1)
    #
    while wd>thr:
        itr+=1
        if itr%2==0:
            while xPos+wd<xEndPos+0.1:
                divSquare(xPos,yPos,wd)
                xPos+=wd
            wd=xEndPos-xPos
        else:
            while yPos+wd<yEndPos+0.1:
                divSquare(xPos,yPos,wd)
                yPos+=wd
            wd=yEndPos-yPos
#
def main():
    #
    screen.fill((0,0,0))
    divSquare(0,0,WIDTH)
    #
    pygame.display.update()
    #
    while True:
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()

#長方形の縦横比
#これによって、描かれる模様が変化する
ratio=math.sqrt(2)
if ratio>1:
    ratio=1/ratio
thr=20

if __name__=="__main__":
    main()