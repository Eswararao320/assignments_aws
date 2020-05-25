class Car:
    sound="Beep Beep"
    def __init__(self,color,max_speed,acceleration,tyre_friction):
        self._color=color
        self._max_speed=max_speed
        
        if self._max_speed<0:
            raise ValueError("Invalid value for max_speed")
            
        self._acceleration=acceleration
        if self._acceleration<0:
            raise ValueError("Invalid value for acceleration")
        
        self._tyre_friction=tyre_friction
        if self._tyre_friction<0:
            raise ValueError("Invalid value for tyre_friction")
        
        self._is_engine_started=False
        self._current_speed=0
        
    @property
    def color(self):
        return self._color
        
    @property
    def tyre_friction(self):
        return self._tyre_friction
        
    @property
    def acceleration(self):
        return self._acceleration
    
    @property
    def max_speed(self):
        return self._max_speed
        
    @property
    def is_engine_started(self):
        return self._is_engine_started
        
    @property
    def current_speed(self):
        return self._current_speed
    
    def start_engine(self): #instane maethod
        self._is_engine_started=True
     
    def accelerate(self): #instance method
        if self._is_engine_started==True:
            if (self._current_speed+self._acceleration)<=self._max_speed:
                self._current_speed+=self._acceleration
            else:
                self._current_speed = self._max_speed
                
        else:
            print("Start the engine to accelerate")
    
    def apply_brakes(self):#instance method
        if self._current_speed>=self._tyre_friction:
            self._current_speed-=self._tyre_friction
        else:
            self._current_speed=0
    
    def sound_horn(self):#instance method
        if self._is_engine_started==True:
            print(self.sound)# class attribute ni class lo , instance method lo kuda self to call chesi vadukovachu
        else:
            print("Start the engine to sound_horn")
    
    def stop_engine(self):#instance method
        self._is_engine_started=False
        
'''car = Car(color="Red", max_speed=250, acceleration=240, tyre_friction=3)
car.start_engine()
car.accelerate()
car.accelerate()
print(car.current_speed)'''



