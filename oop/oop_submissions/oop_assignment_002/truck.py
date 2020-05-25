from oop_assignment_001.car import Car 
class Truck(Car):
    sound="Honk Honk"
    
    def __init__(self,color,max_speed,acceleration,tyre_friction,max_cargo_weight):
        self._max_cargo_weight=max_cargo_weight
        self._Load=0
        super().__init__(color,max_speed,acceleration,tyre_friction)
        
    @property
    def max_cargo_weight(self):
        return self._max_cargo_weight
    
    @property
    def Load(self):
        return self._Load
    
    def load(self,Load):
        if Load<0:
            raise ValueError("Invalid value for cargo_weight")
        if self._current_speed==0:
            if self._Load+Load<=self._max_cargo_weight and self._is_engine_started==False:
                self._max_cargo_weight+=self._Load
            else:
                print("Cannot load cargo more than max limit: {}".format(self._max_cargo_weight))
        else:
            print("Cannot load cargo during motion")
        
    
    def unload(self,Load):
        if Load<0:
            raise ValueError("Invalid value for cargo_weight")
        if self._current_speed==0:
            if self._Load+Load<=self._max_cargo_weight:
                self._max_cargo_weight-=self._Load
            else:
                print("Cannot unload cargo more than max limit: {}".format(self._max_cargo_weight))
        else:
            print("Cannot unload cargo during motion")
        

        
