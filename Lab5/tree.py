'''
Brief description:
Contains Tree class which draws a random tree using turtle graphics

Detailed description:
Classes contained:
Tree:
    attributes:
        turtle:        turtle object, more info can be found on official
                       Python documentation 
                       type: turtle.Turtle
        meanBranchLength:
                       mean branch Length in pixels
                       type: int
        drawMode:      changes draw mode, either RECURSIVE or NONRECURSIVE, if
                       it is RECURSIVE, draw_r() method is used, if
                       NONRECURSIVE, draw_nr() method is used.
                       type: string
        myWin:         turtle graphics screen
                       type: TurtleScreen
    methods:
        __init__(self, drawMode = RECURSIVE, meanBranchLength = 100,
                 randomSeed = 0):
                       sets drawMode, meanBranchLength, uses randomSeed as
                       seed input for random module creates turtle instance
        draw(self, meanBanchLen):
                       draws tree by calling either draw_r() or draw_nr()
                       method
        draw_r(self, meanBranchLength):
                       recursive function that draws random tree given mean
                       branch length
        draw_nr(self):
                       draws random tree using stack data structure 
'''

__version__    = '1.0.0'
__author__     = 'Aykut Bulut, Ted Ralphs (ayb211@lehigh.edu,ted@lehigh.edu)'
__license__    = 'BSD'
__maintainer__ = 'Aykut Bulut'
__email__      = 'ayb211@lehigh.edu'
__title__      = 'Recursive Tree'


from turtle import *
from coinor.blimpy import Stack, Queue
# use seed and randint for creating random branch length etc.
from random import seed, randint

#global constants
EPS = 0.000000001
RECURSIVE = 'recursive'
NONRECURSIVE = 'nonrecursive'
#global variables
counts = {}

def counter(func):
    counts[func.func_name] = 0
    def wrapper(*arg):
        counts[func.func_name] += 1
        res = func(*arg)
        return res
    return wrapper


class Tree(object):
    '''
    Tree class which draws a random tree using turtle graphics.
    '''
    def __init__(self, drawMode = RECURSIVE, meanBranchLength = 100,
                 randomSeed = 0):
        '''
        Sets drawMode, meanBranchLength, uses randomSeed as seed input for
        random module creates turtle instance.
        Inputs:
            drawMode:
            meanBranchLength:
            randomSeed:
        Post: Sets drawMode and meanBranchLength. Calls seed(randomSeed)
        '''
        seed(randomSeed)
        self.turtle = Turtle()
        self.meanBranchLength = meanBranchLength
        self.drawMode = drawMode
        

    def draw(self, meanBranchLen = None):
        '''
        Draws tree by calling either draw_r() or draw_nr() method.
        Inputs:
            meanBanchLen:
        Post: myWin and turtle are initialized.
        '''
        if meanBranchLen == None:
            meanBranchLen = self.meanBranchLength 
        self.myWin = self.turtle.getscreen()
        self.turtle.left(90)
        self.turtle.up()
        self.turtle.backward(300)
        self.turtle.down()
        self.turtle.color('green')
        self.turtle.speed(50)
        if self.drawMode == RECURSIVE:
            self.draw_r(meanBranchLen)
        elif self.drawMode == NONRECURSIVE:
            self.draw_nr(meanBranchLen)
        else:
            raise Exception, "Unknown drawing mode"
        self.myWin.exitonclick()

    @counter
    def draw_r(self, branchLen):
        '''
        Recursive function that draws random tree given mean branch length.
        Post: turtle updated.
        '''
        if branchLen > 5:
            self.turtle.forward(branchLen)
            self.turtle.right(20)
            self.draw_r(branchLen-15)
            self.turtle.left(40)
            self.draw_r(branchLen-10)
            self.turtle.right(20)
            self.turtle.backward(branchLen)

    def draw_nr(self, branchLen):
        '''
        Draws random tree using stack data structure.
        Post: turtle is changed.
        '''
        s = Queue()
 #       s = Stack()        
        while True:
            self.turtle.pensize(branchLen/10)
            minus= randint(5,15)
            if branchLen > 5:
                self.turtle.forward(branchLen)
                self.turtle.left(20)
                s.enqueue((branchLen-minus,
                        self.turtle.position(),
                        self.turtle.heading()))
                self.turtle.right(40)
                s.enqueue((branchLen-minus, 
                        self.turtle.position(), 
                        self.turtle.heading()))
                self.turtle.left(20)
            if s.isEmpty():
                break
            branchLen, p, h = s.dequeue()
            self.turtle.setheading(h)
            self.turtle.penup()
            self.turtle.goto(p)
            self.turtle.pendown()

if __name__ == "__main__":
    t = Tree(NONRECURSIVE)
    t.draw(100)
    for k in counts:
        print k, counts[k]
