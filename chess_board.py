import chess
import sys
import pygame
from time import sleep
import os
from copy import deepcopy
from main import *
INF = 1000000
from typing import Final
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

board = chess.Board()
pygame.init()
turn = 1

dw = 800  # Stands for display width
dh = 600  # Stands for display height

red = (255, 0, 0)
green = (1, 50, 32)
blue = (0, 0, 255)
black = (0, 0, 0)
white = (255, 255, 255)

P_assets = "./assets"

depth: Final = 8

def disp_Blackking(x, y, gameDisplay):
    piece_name = "black king"
    path = P_assets + "/Pieces/" + piece_name + ".png"
    img = pygame.image.load(path)
    gameDisplay.blit(img, (x, y))
    return


def disp_Blackqueen(x, y, gameDisplay):
    piece_name = "black queen"
    path = P_assets + "/Pieces/" + piece_name + ".png"
    img = pygame.image.load(path)
    gameDisplay.blit(img, (x, y))
    return


def disp_Blackbishop(x, y, gameDisplay):
    piece_name = "black bishop"
    path = P_assets + "/Pieces/" + piece_name + ".png"
    img = pygame.image.load(path)
    gameDisplay.blit(img, (x, y))
    return


def disp_Blackknight(x, y, gameDisplay):
    piece_name = "black knight"
    path = P_assets + "/Pieces/" + piece_name + ".png"
    img = pygame.image.load(path)
    gameDisplay.blit(img, (x, y))
    return


def disp_Blackrook(x, y, gameDisplay):
    piece_name = "black rook"
    path = P_assets + "/Pieces/" + piece_name + ".png"
    img = pygame.image.load(path)
    gameDisplay.blit(img, (x, y))
    return


def disp_Blackpawn(x, y, gameDisplay):
    piece_name = "black pawn"
    path = P_assets + "/Pieces/" + piece_name + ".png"
    img = pygame.image.load(path)
    gameDisplay.blit(img, (x, y))
    return


def disp_Whiteking(x, y, gameDisplay):
    piece_name = "white king"
    path = P_assets + "/Pieces/" + piece_name + ".png"
    img = pygame.image.load(path)
    gameDisplay.blit(img, (x, y))
    return


def disp_Whitequeen(x, y, gameDisplay):
    piece_name = "white queen"
    path = P_assets + "/Pieces/" + piece_name + ".png"
    img = pygame.image.load(path)
    gameDisplay.blit(img, (x, y))
    return


def disp_Whitebishop(x, y, gameDisplay):
    piece_name = "white bishop"
    path = P_assets + "/Pieces/" + piece_name + ".png"
    img = pygame.image.load(path)
    gameDisplay.blit(img, (x, y))
    return


def disp_Whiteknight(x, y, gameDisplay):
    piece_name = "white knight"
    path = P_assets + "/Pieces/" + piece_name + ".png"
    img = pygame.image.load(path)
    gameDisplay.blit(img, (x, y))
    return


def disp_Whiterook(x, y, gameDisplay):
    piece_name = "white rook"
    path = P_assets + "/Pieces/" + piece_name + ".png"
    img = pygame.image.load(path)
    gameDisplay.blit(img, (x, y))
    return


def disp_Whitepawn(x, y, gameDisplay):
    piece_name = "white pawn"
    path = P_assets + "/Pieces/" + piece_name + ".png"
    img = pygame.image.load(path)
    gameDisplay.blit(img, (x, y))
    return


def getSquare(pos):
    x, y = pos
    x = (x-200)//50
    y = (y-100)//50
    sq = x + (7-y)*8
    return chess.SQUARE_NAMES[sq]




def pieceSelection(turn, buffer, selection, pos, gameDisplay):
    square = getSquare(pos)
    buffer += square

    if selection == False: #Meaning selection is done. We have to get the legality from the previous square and present position square.
        chess_move = chess.Move.from_uci(buffer)
        legal = chess_move in board.legal_moves
        buffer = ""

        if legal:
            board.push(chess_move)
            assert(turn==1)
            turn = 0
            print("It's legal to do so!!")
        else:
            print("FBI OPEN UP!!")

    return buffer, turn



# Function to draw the background chess board.
def drawBackground(gameDisplay):
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

            # print("Current i: %d, Current j: %d, Current: %s, prev: %s" %(i, j, current, prev_color))


def drawBoard(board, gameDisplay):  # Function to display the pychess board on the GUI. Translate the fenstring from pychess board to positions on the chess_board
    char_piece_map = {
        'k': disp_Blackking,
        'q': disp_Blackqueen,
        'b': disp_Blackbishop,
        'n': disp_Blackknight,
        'r': disp_Blackrook,
        'p': disp_Blackpawn,
        'K': disp_Whiteking,
        'Q': disp_Whitequeen,
        'B': disp_Whitebishop,
        'N': disp_Whiteknight,
        'R': disp_Whiterook,
        'P': disp_Whitepawn
    }

    # tile = 0
    fenString = board.fen()
    #fenString = "r1bkr/p2pBpNp/n4n2/1p1NP2P/6P1/3P4/P1P1K3/q5b1"
    fen = fenString.split(' ')[0]
    for i in range(8):
        row = fen.split('/')[i]
        j = 0
        for c in row:

            if c.isalpha():
                char_piece_map[c](200 + 50*j, 100 + 50*i, gameDisplay)
                j += 1
            else:
                j += ord(c) - 48


if __name__=="__main__":
    selection = False
    buffer = ""
    gameDisplay = pygame.display.set_mode((dw, dh))
    pygame.display.set_caption('Chess Game')

    running = True

    while running:
        if turn == 0:
            print("Computer is thinking...")
            evaluation, best_move = MinMax(board, depth, -INF, INF, turn)
            if best_move is not None:
                board.push(best_move)
                print(f"Computer played: {best_move}")
            turn = 1
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                selection = not (selection)
                pos = pygame.mouse.get_pos()
                assert(turn==1)
                buffer, turn = pieceSelection(turn, buffer, selection, pos, gameDisplay)
                print("Turn after pieceSelection: " + (str(turn)))
            if event.type == pygame.QUIT:
                running = False
            # if event.type == pygame.KEYDOWN:
            #     if event.key == pygame.K_SPACE:
            #         print(board.outcome().winner)
            #         print(board.outcome().termination)

        if board.is_checkmate():
            print("The game ended. Someone won!!")
            running = False
        drawBackground(gameDisplay)
        drawBoard(board, gameDisplay)
        # gameDisplay.fill(white)

        pygame.display.update()

    pygame.quit()
    quit()
