class Animal:
    # constructor
    def __init__(self, name, age, velocity): 
        self.name = name 
        self.age = age
        self.velocity= velocity
    # métodos 
    def takingdamage(self, dmgrecieve): 
        self.life -= dmgrecieve



    