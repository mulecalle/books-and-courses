# #################################################
# Datos
# #################################################
Juan = {'identificacion': {'nombre': 'Juan', 'apellido': 'Garcia'},'edad': 24,'sueldo': 5000,'profesion': 'Pintor'}
Susana = {'identificacion': {'nombre': 'Susana', 'apellido': 'Gomez'},'edad': 25,'sueldo': 6000,'profesion': 'Empleada'}
# #################################################
# Base de datos
# #################################################
db = {}
db['Juan'] = Juan
db['Susana'] = Susana
# #################################################
# Evaluar solo al correr script
# #################################################

if __name__ == '__main__':
    for key in db:
        print(key, '=>\n', db[key])
