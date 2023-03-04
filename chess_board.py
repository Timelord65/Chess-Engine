from time import sleep
import os
from copy import deepcopy
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import sys
import chess

pygame.init()

dw = 800    #Stands for display width
dh = 600    #Stands for display height

red = (255, 0, 0)
green = (1, 50, 32)
blue = (0, 0, 255)
black = (0, 0, 0)
white = (255, 255, 255)

P_assets = "./assets"

def disp_Blackking(x, y):
    piece_name = "black king"
    path = P_assets + "/Pieces/" + piece_name + ".png"
    img = pygame.image.load(path)
    gameDisplay.blit(img, (x, y))
    return

def disp_Blackqueen(x, y):
    piece_name = "black queen"
    path = P_assets + "/Pieces/" + piece_name + ".png"
    img = pygame.image.load(path)
    gameDisplay.blit(img, (x, y))
    return

def disp_Blackbishop(x, y):
    piece_name = "black bishop"
    path = P_assets + "/Pieces/" + piece_name + ".png"
    img = pygame.image.load(path)
    gameDisplay.blit(img, (x, y))
    return


def disp_Blackknight(x, y):
    piece_name = "black knight"
    path = P_assets + "/Pieces/" + piece_name + ".png"
    img = pygame.image.load(path)
    gameDisplay.blit(img, (x, y))
    return

def disp_Blackrook(x, y):
    piece_name = "black rook"
    path = P_assets + "/Pieces/" + piece_name + ".png"
    img = pygame.image.load(path)
    gameDisplay.blit(img, (x, y))
    return

def disp_Blackpawn(x, y):
    piece_name = "black pawn"
    path = P_assets + "/Pieces/" + piece_name + ".png"
    img = pygame.image.load(path)
    gameDisplay.blit(img, (x, y))
    return


def disp_Whiteking(x, y):
    piece_name = "white king"
    path = P_assets + "/Pieces/" + piece_name + ".png"
    img = pygame.image.load(path)
    gameDisplay.blit(img, (x, y))
    return

def disp_Whitequeen(x, y):
    piece_name = "white queen"
    path = P_assets + "/Pieces/" + piece_name + ".png"
    img = pygame.image.load(path)
    gameDisplay.blit(img, (x, y))
    return

def disp_Whitebishop(x, y):
    piece_name = "white bishop"
    path = P_assets + "/Pieces/" + piece_name + ".png"
    img = pygame.image.load(path)
    gameDisplay.blit(img, (x, y))
    return


def disp_Whiteknight(x, y):
    piece_name = "white knight"
    path = P_assets + "/Pieces/" + piece_name + ".png"
    img = pygame.image.load(path)
    gameDisplay.blit(img, (x, y))
    return

def disp_Whiterook(x, y):
    piece_name = "white rook"
    path = P_assets + "/Pieces/" + piece_name + ".png"
    img = pygame.image.load(path)
    gameDisplay.blit(img, (x, y))
    return

def disp_Whitepawn(x, y):
    piece_name = "white pawn"
    path = P_assets + "/Pieces/" + piece_name + ".png"
    img = pygame.image.load(path)
    gameDisplay.blit(img, (x, y))
    return

def drawBackground(): #Function to draw the background chess board. 
    boundaryRect = pygame.Rect((200, 100), (400, 400))
    pygame.draw.rect(gameDisplay, pygame.Color(green), boundaryRect)
    prev_color = white

    for i in range(0, 8):
        if prev_color == white:
            prev_color = green
        else:
            prev_color = white
        for j in range(0, 8):

            if prev_color == white:
                    current = green
                    prev_color = green
            
            else:
                current = white
                prev_color = white

            tile = pygame.Rect((200 + (50*i), 100 + (50*j)), (50, 50))
            pygame.draw.rect(gameDisplay, pygame.Color(current), tile)
            
            #print("Current i: %d, Current j: %d, Current: %s, prev: %s" %(i, j, current, prev_color))

def drawBoard(board): #Function to display the pychess board on the GUI. 
    pass


    
gameDisplay = pygame.display.set_mode((dw, dh))
pygame.display.set_caption('Chess Game')

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    drawBackground()
    #gameDisplay.fill(white)
    disp_Whiteknight(200, 200)

    pygame.display.update()

pygame.quit()
quit()