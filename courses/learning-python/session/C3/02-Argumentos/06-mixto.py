


def f(a, *pargs, **kargs):
    print(a)
    print(pargs)
    print(kargs)


f(1, 2, x=1, y=2)

