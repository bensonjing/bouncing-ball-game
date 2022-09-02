# A Floater is Prey; it updates by moving mostly in
#   a straight line, but with random changes to its
#   angle and speed, and displays as ufo.gif (whose
#   dimensions (width and height) are computed by
#   calling .width()/.height() on the PhotoImage 


from PIL.ImageTk import PhotoImage
from prey import Prey
from random import random


class Floater(Prey): 
    radius = 5 
    
    def __init__(self, x, y): 
        self._angle = 1 
        self.randomize_angle()
        Prey.__init__(self, x, y, 10, 10, self._angle, 5)
        self._image = PhotoImage(file='ufo.gif')
        
    def update(self):
        i = random() 
        if i <= 0.3:
            j = random()-0.5 
            self.set_angle(self.get_angle()+j)
            if not self.get_speed() + j < 3 or self.get_speed() + j > 7: 
                self.set_speed(self.get_speed()+j) 
        self.move() 
        
    def display(self, canvas):
        canvas.create_image(*self.get_location(), image=self._image)
    
