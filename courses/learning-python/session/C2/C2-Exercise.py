
asd = [1, None, 'asd',[1,'asd',3],True]

for x in asd:

    if isinstance(x,str):
        print('string')
    elif isinstance(x,list):
        print('list')
    elif type(x) is bool:
        print('bool')
    elif isinstance(x, int):
        print('int')
    elif x is None:
        print('null')

