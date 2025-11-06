# ##################################
# Ejemplo 1
# ##################################
y=22
x = y // 2   # la // trunca el resultado de dividir y entre 2
print(x)
print('')
while x > 1:

	print(x)

	if y % x == 0:
		print(y, 'has factor', x)
		break
		x-=1
	else:
		print(y, 'is prime')
