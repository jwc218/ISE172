'''
Created on April 1, 2014

@author: Ted Ralphs
'''

class PriorityQueue(object):
    def __init__(self, aList = None):
        self.aList={}

    def isEmpty(self):
        if len(self.aList)==0:
            return True
        

    def pop(self, key = None):
         min=1000
         for a in self.aList:
            if self.aList[a]<=min:
                min=self.aList[a]
                key=a
         del self.aList[key]
         return key
    
    def peek(self, key = None):
        min=1000
        for a in self.aList:
            if self.aList[a]<=min:
                min=self.aList[a]
                key=a
        return key
            

    def get_priority(self, key):
        return self.aList[key]
    
    def push(self, key, priority = 0):
        self.aList[key]=priority
    
    def remove(self, key):
        if key in self.aList:
            del self.aList[key]
        else:
            raise KeyError('Key not in list')
