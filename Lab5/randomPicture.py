from turtle import *

class randomImages(object):
    
    def __init__(self):
        self.turtle = Turtle()



    def randomShape(self):
        self.myWin = self.turtle.getscreen()
        self.turtle.speed(10)
        
        self.turtle.color('red')
        #create star shape
        for i in range(20):
            self.turtle.forward(i * 10)
            self.turtle.right(144)
         
        self.turtle.left(100)   
        self.turtle.color('blue')
        token=0
        # create turtle star
        while token<75:
            self.turtle.forward(200)
            self.turtle.left(170)
            token+=1
            if abs(self.turtle.pos()) < 1:
                break
    
        self.myWin.exitonclick()
        
if __name__ == "__main__":
    r = randomImages()
    r.randomShape()