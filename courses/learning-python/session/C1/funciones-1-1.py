import copy
nombre = "asignacion dinamica"

F1 = 2
F2 = F1
print(F1)
print(F2)

F1 = 4
print(str(F1) + '/' +  str(F2))


F1 = [2,1,2]
print(F2)

F1 = [0,1,2]
F2 = copy.copy(F1)

F1[0] = 4
print(str(F1) + '/' +  str(F2))


F1[0] = 4
print(F2)
print(F1)