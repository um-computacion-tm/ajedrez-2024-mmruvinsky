import pygame as p
from chess import Chess
from board import Board

p.init

WIDTH = HEIGHT = 400

DIMENSIONS = 8

SQ_SIZE = HEIGHT // DIMENSIONS

MAX_FPS = 15

IMAGES = {

}

def loadimages(): 
    pieces = ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR",
              "wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load(f"images/{piece}.png"), (SQ_SIZE, SQ_SIZE))

def main():

    p.init()
    screen = p.display.set_mode((WIDTH, HEIGHT))
    loadimages()
    clock = p.time.Clock()
    chess = Chess()
    screen.fill(p.Color("cyan"))
    gs = Board()
    loadimages()
    running = True
    while running:

        for event in p.event.get():
            if event.type == p.QUIT:
                running = False
        drawGameState(screen, gs)
        clock.tick(MAX_FPS)
        p.display.flip()


def drawGameState(screen, gs):
    drawBoard(screen)


def drawBoard(screen):
    colors = [p.Color("white"), p.Color("black")]
    for i in range(DIMENSIONS):
        for j in range(DIMENSIONS):
            






































































