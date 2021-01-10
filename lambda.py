# función rápida y anonima

# estructura -> lambda parámetro1, param2 : sentencia 

# ejemplo 1 
res = lambda firstParam , secParam : firstParam * secParam

# def res (firstParam , secParam):
#     return firstParam * secParam
print(res(2, "-las cosas de la vida-"))


# ejemplo 2 lambda dentro de una función 
def funclambda (text): 
    return lambda param : param + text

res2 = funclambda('cola')
print(res2("colita igual viene la "))