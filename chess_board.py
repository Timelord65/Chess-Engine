#!c:/Python/python.exe
from time import sleep
import os
from copy import deepcopy
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import sys

pygame.init()

dw = 800    #Stands for display width
dh = 600    #Stands for display height

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)



gameDisplay = pygame.display.set_mode((dw, dh))
pygame.display.set_caption('Chess Game')

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    gameDisplay.fill(red)