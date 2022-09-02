# A Hunter class is derived from a Pulsator and then Mobile_Simulton base.
#   It inherits updating+displaying from Pusator/Mobile_Simulton: it pursues
#   any close prey, or moves in a straight line (see Mobile_Simultion).


from prey  import Prey
from pulsator import Pulsator
from mobilesimulton import Mobile_Simulton
from math import atan2
import model 


class Hunter(Pulsator, Mobile_Simulton):  
    dis = 200 
    
    def __init__(self, x, y):
        self._angle = 1 
        self.randomize_angle() 
        Mobile_Simulton.__init__(self, x, y, 20, 20, self._angle, 5) 
        self.counter = 30 
        
    def update(self):
        Pulsator.update(self) 
        sdict = {Pulsator.distance(self, s.get_location()): s for s in model.find(lambda x: isinstance(x, Prey))}
        if len(sdict.keys()) != 0 and min(sdict.keys()) < Hunter.dis: 
            s = sdict[min(sdict.keys())] 
            x, y = s.get_location() 
            self.set_angle(atan2(y-self.get_location()[1], x-self.get_location()[0]))
        self.move() 
                
