from sys import argv # example client code

def getOpts(argv):

    opts = []

    iterList = iter(argv)

    for arg in iterList:

        if arg[0][0] == '-': # find "-i value" pairs

            item= next(iterList)
            opts.append(item)


    return opts

if __name__ == '__main__':

    print('argv received: ', argv)

    myArgs = getOpts(argv)

    for arg in myArgs:
        print(arg)
