'''
Make neccesary imports needed for game of life
this game is in OOP form
Graph be sized according to dimensions we input
Program will run according to an interation limit we input
'''


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

class OOPLifeGame:
    
    def life(self, iteration_limit):
        '''
        Arguments: takes in iteration_limit, max iteration number for program
        What it does:
        -adjust framerate
        -intitializes board and screen
        -initializes game time
        -randomizes board
        
        timing/counter refers to avg time to update the board
        '''
    
    def make_random_board(self):
            '''
            creates initial board
            random generators for x and y coordinates will go through empty board and create one ready for use
            '''
            
    def update_board(self,board):
        '''
        takes in board as its argument
        makes life/death adjustment based on rules of game
        returns modified board
        '''
    
    def count_neighbors(self,cell):
        '''
        takes in cell as argument
        returns number of cells surrounding that cell
        '''
    
    def draw_board(self, bg):
        '''
        takes in argument bg, an object that is part of the pygame package
        animates screeen appopriately to match presence of a cell
        '''
        
    def init(self,dimx, dimy):  
        '''
        takes in dimx and dimy as dimensions for the board
        initializes pygame module using init
        calls the objects methods so board is ready for input
        '''
'''
main method call to test program
'''
         