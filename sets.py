# lists -> ordenado, modificables, permite duplicados
# sets -> desordenados, no modificables, no duplicados
# diccionario ->desordenados, modificables, no dulicados
# tuple -> ordenado, no modificables, permite duplicados

setDeLaCompra={"manzana", "peras", "lentejas", True, 2.80, 1}
print(setDeLaCompra)

# acceso a los datos
# for itemShopLits in setDeLaCompra: 
#     print(itemShopLits)

# print ("manzana"in setDeLaCompra)

# añadir dato
# setDeLaCompra.add("naranjas")
# print(setDeLaCompra)

# añadir un set 
setDeLaCompra2 = {"pollo", "ternera"}
# setDeLaCompra.update(setDeLaCompra2)
# print(setDeLaCompra)

# eliminar un item de la lista

# setDeLaCompra.remove("naranjas")
# print(setDeLaCompra)

# limpiar lista
# setDeLaCompra.clear()
# print(setDeLaCompra)

# union
setDeLaCompra3= setDeLaCompra.union(setDeLaCompra2)
print(setDeLaCompra3)

# insertion
set1= {"cosas", 1}
set2= {"cosas", 2}
set3 =set1.intersection(set2)
print(set3)

# no dubplicates
set4 = set1.symmetric_difference(set2)
print(set4)

