'''
It is a ball except it's in green instead of blue 
'''

from ball import Ball

class Special(Ball): 
    def __init__(self, x, y):
        Ball.__init__(self, x, y) 
        
    def display(self, canvas):
        x, y = self.get_location() 
        canvas.create_oval(x+Ball.radius, y+Ball.radius, x-Ball.radius, y-Ball.radius, fill='green')
