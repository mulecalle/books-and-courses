# ##############################################
# Recursión ####
# ##############################################
def sumtree(L):
	tot = 0
	for x in L: # Para cada elemento del primer nivel
		if not isinstance(x, list):
			tot += x # agrega los números directamente
		else:
			tot += sumtree(x) # Recursión sobre la sublista
	return tot

L = [1, [2, [3, 4], 5], 6, [7, 8]]
print(sumtree(L))


input()