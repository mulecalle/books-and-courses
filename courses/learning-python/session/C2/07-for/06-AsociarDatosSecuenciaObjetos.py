# ##############################################
# Ejemplo 1 - Asociar Datos ####################
# ##############################################
A = ["Hay", 2323 , (1,2)]
B = [(1,2) , 545]
for b in B:
	if b in A:
		print("Se encontro coincidencia", b)
	else:
		print("No se encontro coincidencia", b)	
input()