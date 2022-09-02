# A Black_Hole is derived from a Simulton base; it updates by finding+removing
#   any objects (derived from a Prey base) whose center is crosses inside its
#   radius (and returns a set of all eaten simultons); it displays as a black
#   circle with a radius of 10 (e.g., a width/height 20).
# Calling get_dimension for the width/height (for containment and displaying)'
#   will facilitate inheritance in Pulsator and Hunter

from simulton import Simulton
from prey import Prey
import model 

class Black_Hole(Simulton):  
    radius = 10 
    
    def __init__(self, x, y):
        Simulton.__init__(self, x, y, 20, 20)
        
    def update(self):
        eaten_simultons = set() 
        for s in model.find(lambda x: isinstance(x, Prey)): 
            if self.contains(s.get_location()): 
                model.remove(s) 
                eaten_simultons.add(s) 
        return eaten_simultons 
    
    def display(self, canvas):
        x, y = self.get_location() 
        w, h = self.get_dimension() 
        canvas.create_oval(x+w/2, y+h/2, x-w/2, y-h/2, fill='black')
        
    def contains(self, xy): 
        return self.distance(xy) < self.get_dimension()[0]/2