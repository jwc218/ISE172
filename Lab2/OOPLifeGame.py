#object oriented version of game of life
# make neccesary imports
__version__    = '1.0.0'
__author__     = 'G-Do (http://www.daniweb.com/members/G-Do/37720)'
__maintainer__ = 'Ted Ralphs'
__email__      = 'ted@lehigh.edu'
__url__        = 'http://coral.ie.lehigh.edu/~ted/files/ie172/code/life.py'
__title__      = 'The Game of Life'


from  sys import argv, exit
import random, pygame
from pygame.locals import *
from time import time
import cProfile, pstats
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

# GLOBALS
# The dimensions of each cell (in pixels)
CELL_DIMENSIONS = (10,10)
# The framerate of the game (in milliseconds)
FRAMERATE = 10
# The fraction (density) of the board occupied by cells when randomly generated
OCCUPANCY = 0.6
# Colors used to represent the cells
COLORS = { 0:(0,0,0), 1:(200,200,100) }
NEIGHBORS = [(0,1),   # up
             (0,-1),  # down
             (1,0),   # left
             (-1,0),  # right
             (1,1),   # upper left
             (-1,1),  # upper right
             (-1,-1), # lower right
             (1,-1),  # lower left
            ]
# Board marks
DEAD = 0
ALIVE = 1
WILL_BORN = 2
WILL_DIE = -1
#create object oriented game class
class OOPLifeGame:
    
    def life(self, iteration_limit):

        # Initialize pygame elements)
        self.screen
        self.clock
        self.bg
        self.interation_limit=10000
        # Create random board
        self.board = self.make_random_board()
        # Enter the game loop
        quit_game = False
        counter, timing = 0, 0
        while not quit_game and counter <= iteration_limit:
            # Slow things down to match the framerate
            self.clock.tick(FRAMERATE)
            # Update the board
            start = time()
            self.update_board(self.board)
            timing += time() - start
            # Draw the board on the background
            self.draw_board(self.board,self.bg)
            # Blit bg to the screen, flip display buffers
            self.screen.blit(self.bg, (0,0))
            pygame.display.flip()
            # Queue user input to catch QUIT signals
            for e in pygame.event.get():
                if e.type == QUIT: quit_game = True
            counter += 1
        return timing/counter
    
    def make_random_board(self):

        # Instantiate the board as a dictionary with a fraction occupied
        board = {}
        for x in range(self.dimx):
            for y in range(self.dimy):
                if random.random() < OCCUPANCY: board[(x,y)] = ALIVE
                else: board[(x,y)] = DEAD
        # Return the board
        return board

def update_board(self,board):
    '''
    Update the board according to the rules of the game
    Input:
        board: current board.
    Post:
        Updates board.
    '''
    # For every cell in the board...
    for cell in self.board:
        # How many occupied neighbors does this cell have?
        neighbors = self.count_neighbors(cell, board)
        # If the cell is empty and has 3 neighbors, mark it for occupation
        if self.board[cell] == DEAD and neighbors == 3:
            self.board[cell] = WILL_BORN
        # On the other hand, if the cell is occupied and doesn't have 2 or 3
        # neighbors, mark it for death
        elif self.board[cell] == ALIVE and not neighbors in [2, 3]:
            self.board[cell] = WILL_DIE

    # Now, go through it again, making all the approved changes
    for cell in self.board:
        if self.board[cell] == WILL_BORN: self.board[cell] = ALIVE
        if self.board[cell] == WILL_DIE: self.board[cell] = DEAD

def count_neighbors(self,cell):
    '''
    Return the number of occupied neighbors of cell.
    Inputs:
        cell: cell that we will count neighbors.
        board: game board.
    '''
    # For each potential neighbor, if the cell is occupied add one to the score
    score = 0
    for n in NEIGHBORS:
        # Is this a real neighbor, or is it out-of-bounds?
        if (cell[0] + n[0], cell[1] + n[1]) in self.board.keys():
            # Remember that neighbors which are marked for death count, too!
            if self.board[(cell[0] + n[0], cell[1] + n[1])] in [ALIVE, WILL_DIE]: 
                score += 1
    # Return the score
    return score

def draw_board(self, bg):
    '''
    Draw the board on the background.
    Inputs:
        board: game board.
        bg: background, pygame related object.
    '''
    # Grab hard-coded global values
    global CELL_DIMENSIONS
    # Draw every cell in the board as a rectangle on the screen
    for cell in self.board:
        rectangle = (cell[0]*CELL_DIMENSIONS[0],cell[1]*CELL_DIMENSIONS[1],
                     CELL_DIMENSIONS[0],CELL_DIMENSIONS[1])
        pygame.draw.rect(bg, COLORS[self.board[cell]], rectangle)
    
    def init(self,dimx, dimy):
        self.dimx=dimx
        self.dimy=dimy
        # Initialize the pygame modules
        pygame.init()
        # Determine and set the screen dimensions
        self.dimensions = (self.dimx*CELL_DIMENSIONS[0],
                  self.dimy*CELL_DIMENSIONS[1])
        self.screen = pygame.display.set_mode(self.dimensions)
        # Set the title string of the root window
        pygame.display.set_caption(__title__+" "+__version__)
        # Grab the background surface of the screen
        self.bg = self.screen.convert()
        # Grab the game clock
        self.clock = pygame.time.Clock()
        

game=OOPLifeGame(25,25)
game.life(10)      
        
