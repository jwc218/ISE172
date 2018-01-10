'''
A basic stack implementation using a linked list
'''

__version__    = '1.0.0'
__author__     = 'Aykut Bulut, Ted Ralphs (ayb211@lehigh.edu,ted@lehigh.edu)'
__license__    = 'BSD'
__maintainer__ = 'Aykut Bulut'
__email__      = 'ayb211@lehigh.edu'
__url__        = None
__title__      = 'Maze class'



from coinor.blimpy import LinkedList

class Stack(object):
    '''
    classdocs
    '''
    count=0
    def __init__(self):
        self.items=[]
        self.count=0


    def isEmpty(self):
        return self.items==[]
        

    def push(self, item):
        self.count+=1
        self.items.insert(0,item)

    def pop(self):
        return self.items.pop(0)

    def peek(self):
        return self.items[0]

    def __len__(self):
        return len(self.items)
