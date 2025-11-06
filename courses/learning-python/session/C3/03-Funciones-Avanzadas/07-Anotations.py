# ##############################################
# Recursión ####
# ##############################################


def func2(a: 'spam', b: (1, 10), c: float) -> int:
    return a + b + c


print(func2(1, 2, 3))
print(func2.__annotations__)
