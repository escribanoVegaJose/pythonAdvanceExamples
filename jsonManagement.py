# importar librería json
import json
# ¿Qué es un json?

# creamos un json

jsonPerson= {'name':'jose', 'apellidos':'escribano', 'age':28, 'city':'Madrid'}

jsonPersonString= json.dumps(jsonPerson)

jsonPersonConver= json.loads(jsonPersonString)

print(jsonPersonConver['name']+ " "+ jsonPersonConver['apellidos'])