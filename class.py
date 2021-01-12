# ¿Qué es un clase y un objeto?

# Ejemplo básico
class Gato: 
    # variable
    life= 100
    damage= 150
    # constructor
    def __init__(self, name, age, velocity): 
        self.name= name
        self.age=age
        self.velocity=velocity
    # métodos 
    def takingDamage(self, dmgRecieve): 
        self.life -= dmgRecieve

# main
# puntero del objeto que apunta a la clase Gato 
gatoObjeto = Gato("Espiga", 3, 50)
print("nombre= "+gatoObjeto.name)
print("edad= "+str(gatoObjeto.age))
print("vida= "+str(gatoObjeto.life))

# vamos hacer daño al gato, utilizabdo un método del objeto
gatoObjeto.takingDamage(10)
print("vida_actual="+str(gatoObjeto.life))

# modificando una propiedad directamente 
gatoObjeto.age= 11
gatoObjeto.life= 20 

print("edad= "+str(gatoObjeto.age), "vida= "+ str(gatoObjeto.life))