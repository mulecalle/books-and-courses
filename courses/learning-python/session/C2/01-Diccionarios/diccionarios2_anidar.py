# ######################################
# Encadenamiento
# ######################################
F = {'nombre': {'primero':'Juan', 'segundo':'Marcelo'},
     'trabajo':['profesor','ingeniero']
    }
print(F)
print('nombre')
print(F['nombre']['primero'])
# ######################################
# Agregar elementos
# ######################################
F['trabajo'].append('pintor')
print(F)
input()