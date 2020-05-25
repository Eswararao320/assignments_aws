class Pokemon:
    Run=""
    Swim=""
    Fly=""
    Make_sound=""
    def __init__(self,name,level):
        if name=='':
            raise ValueError("name cannot be empty")
        else:
            self._name=name
        
        if level<=0:
            raise ValueError("level should be > 0")
        else:
            self._level=level
        self._c=0

    
    @property
    def name(self):
        return self._name
        
    @property        
    def level(self):
        return self._level
        
    @property        
    def c(self):
        return self._c
    
    @classmethod
    def make_sound(cls):
        print(cls.Make_sound)
        
    @classmethod
    def run(cls):
        print(cls.Run)

    @classmethod
    def swim(cls):
        print(cls.Swim)
        
    @classmethod
    def fly(cls):
        print(cls.Fly)


class Pikachu(Pokemon):
    Make_sound="Pika Pika"
    Run="Pikachu running..."
    
    def __str__(self):
        return ('{} - Level {}'.format(self._name,self._level))
        
    def attack(self):
        if self._c==0:
            self._c=1
            print ("Electric attack with {} damage".format(self._level*10))
        else:
            self._level+=1
            print ("Electric attack with {} damage".format(self._level*10))
    

class Squirtle(Pokemon):
    Make_sound="Squirtle...Squirtle"
    Run="Squirtle running..."
    Swim="Squirtle swimming..."
    def __str__(self):
        return ('{} - Level {}'.format(self._name,self._level))
        
        
    def attack(self):
        if self._c==0:
            self._c=1
            print ("Water attack with {} damage".format(self._level*9))
        else:
            self._level+=1
            print ("Water attack with {} damage".format(self._level*9))

class Pidgey(Pokemon):
    Make_sound="Pidgey...Pidgey"
    Fly="Pidgey flying..."
    Swim="Squirtle swimming..."
    def __str__(self):
        return ('{} - Level {}'.format(self._name,self._level))
        
    def attack(self):
        if self._c==0:
            self._c=1
            print ("Air attack with {} damage".format(self._level*5))
        else:
            self._level+=1
            print ("Air attack with {} damage".format(self._level*5))

class Swanna(Pokemon):
    Make_sound="Swanna...Swanna"
    Fly="Swanna flying..."
    Swim="Swanna swimming..."
    
    def __str__(self):
        return ('{} - Level {}'.format(self._name,self._level))
        
    def attack(self):
        if self._c==0:
            self._c=1
            print ("Water attack with {} damage".format(self._level*9))
            print ("Air attack with {} damage".format(self._level*5))
        else:
            self._level+=1
            print ("Water attack with {} damage".format(self._level*9))
            print ("Air attack with {} damage".format(self._level*5))

class Zapdos(Pokemon):
    Make_sound="Zap...Zap"
    Fly="Zapdos flying..."
    
    def __str__(self):
        return ('{} - Level {}'.format(self._name,self._level))
        
        
    def attack(self):
        if self._c==0:
            self._c=1
            print ("Electric attack with {} damage".format(self._level*10))
            print ("Air attack with {} damage".format(self._level*5))
        else:
            self._level+=1
            print ("Electric attack with {} damage".format(self._level*10))
            print ("Air attack with {} damage".format(self._level*5))


class Island:
    island_list=[]
    def __init__(self,name,max_no_of_pokemon,total_food_available_in_kgs):
        self._name=name
        self._max_no_of_pokemon=max_no_of_pokemon
        self._total_food_available_in_kgs=total_food_available_in_kgs
        self._pokemon_left_to_catch=0
        self.island_pokemon_list=[]
        self.island_list.append(self)
    @property
    def name(self):
        return self._name
        
    @property
    def max_no_of_pokemon(self):
        return self._max_no_of_pokemon
    
    @property
    def total_food_available_in_kgs(self):
        return self._total_food_available_in_kgs
        
    @property
    def pokemon_left_to_catch(self):
        return self._pokemon_left_to_catch
    
    @classmethod
    def get_all_islands(cls):
        return cls.island_list
    
    def __str__(self):
        return ('{} - {} pokemon - {} food'.format(self._name,self._pokemon_left_to_catch,self._total_food_available_in_kgs))
    
    def add_pokemon(self,other):
        if self._max_no_of_pokemon>=self._pokemon_left_to_catch:
            self._pokemon_left_to_catch+=1
            return self._pokemon_left_to_catch
        else:
            print("Island at its max pokemon capacity")
    
    
class Trainer:
    def __init__(self,name):
        self._name=name
        self._experience=100
        self._max_food_in_bag=self._experience*10
        self._food_in_bag=0
        self._current_island=""
        self._move_island=0
        self.pokemon_list=[]
    @property
    def name(self):
        return self._name
    
    @property
    def experience(self):
        return self._experience
    
    @property
    def max_food_in_bag(self):
        return self._max_food_in_bag
        
    @property
    def food_in_bag(self):
        return self._food_in_bag

    @property
    def current_island(self):
        return self._current_island

    @property
    def move_island(self):
        return self._move_island
        
    def move_to_island(self,island):
        self._move_island+=1
        self._current_island=island
        
    def collect_food(self):
        if self.move_island !=0 and self._food_in_bag==0:
            if self._current_island._total_food_available_in_kgs>self._max_food_in_bag:
                self._food_in_bag=self._max_food_in_bag
            else:
                self._food_in_bag=self._current_island._total_food_available_in_kgs
                self._current_island._total_food_available_in_kgs=0
        else:
            print("Move to an island to collect food")
            
    
    def catch(self,pokemon):
        if self._experience>=100*pokemon.level:
            self._experience+=pokemon.level*20
            self.pokemon_list.append(pokemon)
            pokemon._master=self
            print("You caught {}".format(pokemon.name))
        else:
            print("You need more experience to catch {}".format(pokemon.name))
            
    def get_my_pokemon(self):
        return self.pokemon_list
        
    def __str__(self):
        return self._name
            