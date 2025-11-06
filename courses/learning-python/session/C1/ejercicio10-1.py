# #################################################
# Definir listas
# #################################################
Juan = ['Juan Garcia', 24, 5000, 'Pintor']
Susana = ['Susana Gomez', 25, 6000, 'Empleada']
print(Juan[0])
# #################################################
# Definir lista como Base de datos
# #################################################
personas = [Juan, Susana]
# #################################################
# Imprimo elementos de la lista de base de datos
# #################################################
for x in personas:
    print(x)
print('------------------------------')
# #################################################
# Imprimo los apellidos y les doy aumento del 20%
# #################################################
for x in personas:
    print((x[0].split()[-1]))
    x[2] *= 1.20
for x in personas:
    print(x)
print('------------------------------')
# #################################################
# Agregamos un registro a la lista de base de datos
# #################################################
personas.append(['Pedro', 37, 7000, 'Plomero'])
for x in personas:
    print(x)
print('------------------------------')
+eval(input())