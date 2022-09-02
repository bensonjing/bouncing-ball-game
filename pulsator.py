# A Pulsator is a Black_Hole; it updates as a Black_Hole
#   does, but also by growing/shrinking depending on
#   whether or not it eats Prey (and removing itself from
#   the simulation if its dimension becomes 0), and displays
#   as a Black_Hole but with varying dimensions 


from blackhole import Black_Hole
from prey import Prey
import model 


class Pulsator(Black_Hole): 
    def __init__(self, x, y):
        Black_Hole.__init__(self, x, y) 
        self.counter = 30 
        
    def update(self):
        eaten = Black_Hole.update(self) 
        if len(eaten) != 0: 
            self.change_dimension(len(eaten), len(eaten))   
            self.counter = 30 
        else: 
            self.counter -= 1 
            if self.counter == 0: 
                self.change_dimension(-1, -1) 
                self.counter = 30 
                    
        w, h = self.get_dimension()
        if w == 0 and h == 0: 
            model.remove(self) 
        return eaten