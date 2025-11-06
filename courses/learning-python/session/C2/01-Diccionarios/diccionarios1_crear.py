# ######################################
# Crear diccionario
# ######################################
F = {'clave1': 'valor1', 'clave2':'valor2', 'claven':'valorn'}

print(F['clave1'])
# ######################################
# Crear por asiganción
# ######################################
J = {}
J['clave1'] = 'valor1'
J['clave1'] = 'valor2'
print(F['clave1'])
# ######################################
# Crear mediante dict()
# ######################################

S = dict(clave1 = 'valor1', clave2 = 'valor2')
print(S['clave1'])
# ######################################
# Crear mediante dict() y zip
# ######################################

P = dict(zip(['clave1', 'clave2'], ['valor1', 'valor2']))
print(P['clave1'])

input()