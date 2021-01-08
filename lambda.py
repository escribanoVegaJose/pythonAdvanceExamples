# función rápida

# estructura -> lambda parámetros : sentencia 

# ejemplo 1 
res = lambda firstParam , secParam : firstParam * secParam
print(res(2,"-Las cosas de la vida-"))

# ejemplo 2 lambda dentro de una función 
def funclambda (text): 
    return lambda param : param + text

res2 = funclambda('cola')
print(res2("colita igual viene la "))