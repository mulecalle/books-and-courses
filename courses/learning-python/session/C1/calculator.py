import sys

def add():
    nFirstNumber = askForNumber("+")
    nSecondNumber = askForNumber("+")
    nResult = (float(nFirstNumber) + float(nSecondNumber)).__str__()
    print ("Result: " + nResult)
    sys.exit(0)

def sub():
    nFirstNumber = askForNumber("-")
    nSecondNumber = askForNumber("-")
    nResult = (float(nFirstNumber) - float(nSecondNumber)).__str__()
    print ("Result: " + nResult)
    sys.exit(0)

def div():
    nFirstNumber = askForNumber("/")
    nSecondNumber = askForNumber("/")
    nResult = (float(nFirstNumber) / float(nSecondNumber)).__str__()
    print ("Result: " + nResult)
    sys.exit(0)

def mult():
    nFirstNumber = askForNumber("*")
    nSecondNumber = askForNumber("*")
    nResult = (float(nFirstNumber) * float(nSecondNumber)).__str__()
    print ("Result: " + nResult)
    sys.exit(0)

def askForNumber(sOperation):

    bValidNumber = False
    while not bValidNumber:

        nNum = float(raw_input("enter number: "))
        bValidNumber = isThisAValidNumber(nNum, sOperation)

    return nNum

def isThisAValidNumber(nNum, sOp):

    if sOp == "+":
        return isPositive(nNum)
    elif sOp == "-":
        return isPositive(nNum)
    elif sOp == "*":
        return True
    elif sOp == "/":
        return notZero(nNum)

def isPositive(nNum):

    if nNum >= 0:
        return True
    else:
        print("Number not valid")
        return False

def notZero(nNum):

    if nNum == 0:
        print("Number not valid")
        return False
    else:
        return True

def calc():

    sOp = raw_input("enter operator (+,-,*,/): ")

    if (sOp == "+"):
        add()
    elif (sOp == "-"):
        sub()
    elif (sOp == "*"):
        mult()
    elif (sOp == "/"):
        div()
    else:
        print("operator not valid.")


calc()