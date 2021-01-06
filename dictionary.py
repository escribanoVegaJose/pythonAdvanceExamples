# Estructura de datos clave valor. 
# nombre_dictionary= {"clave": valor, "clave":valor}

# Ejemplo
car = {"brand": "bmw", "potencia":158, "precio":34000}
car2= {"brand": "porsche", "potencia":215, "precio":48000}
carsToBuy={"coches":[car,car2]}

# Acceso al dato
print (carsToBuy["coches"])
print (car["brand"])

print("..................")

for value in car.values():
  print(value)
print("..................")

for key in car.keys():
  print(key)
print("..................")
  
for itemKey, itemValue in car.items():
  print(itemKey,itemValue)
print("..................")

# modificación del dato
car["brand"]="ferrari"
# Añadir nuevo elemento
car["nuevo"]=True
print(car)

# borrar key, se puede utilizar del o pop de la misma forma
del car["brand"]
car.pop("potencia")
print(car)

# limpiar diccionario
car.clear()


