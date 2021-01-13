# Herencia clase que hereda propiedades de la clase padre

# clase animal -Padre-
class Animal:
    # variables
    food = 50  # 0 esta hambriento y 100 esta no hambriento
    # constructor con propiedades

    def __init__(self, name, age, velocity, acuatic):
        self.name = name
        self.age = age
        self.velocity = velocity
        self.acuatic = acuatic

    # métodos
    def __isHungry(self):
        return self.food < 50

    def pasandoHambre(self, food):
        self.food -= food

    def eat(self):
        if self.__isHungry():
            self.food += 10

    def defend(self):
        print(self.name+" se esta defendiendo del enemigo")


# Hijos
# caso más simple hereda todas las características sin aportar nada.
class Amorfo(Animal):
    pass
# Mamifero
class Mamifero (Animal): 

    # constructor
    def __init__(self, name, age, velocity, acuatic, milk):
        super().__init__(name, age, velocity, acuatic)
        self.milk= milk
    # métodos
    def amamantar(self): 
        print ("amamatando")

# main
amorfo = Amorfo("caracol", 1, 5, True)
amorfo.defend()

mamifero = Mamifero("Oso",356,45,True, 80)
print(mamifero.milk)
mamifero.amamantar()

animal= Animal("Perro", 45, 40, True)
