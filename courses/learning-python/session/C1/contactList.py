dict = {}

class Employee:
    def __init__(self, sName, sAddress, sNum):
        self.sName = sName
        self.sAddress = sAddress
        self.sNum = sNum

    def setAddress(self, sNewAddress):
        self.sAddress = sNewAddress

    def setNum(self, sNewNum):
        self.sNum = sNewNum

    def printMe(self):
        print ("*********")
        print("Name: " + str(self.sName))
        print("Address: " + str(self.sAddress))
        print("Num: " + str(self.sNum))


def promptName():
    return input("Enter name: ")


def promptAddress():
    return input("Enter address: ")


def promptMobileNum():
    return input("Enter mobile number: ")


def promptEditName():
    return input("Enter the name of the one whom will be edited: ")


def promptDeleteName():
    return input("Enter the name of the one whom will be deleted: ")


def add():

    sName = promptName()
    sAddr = promptAddress()
    sNum = promptMobileNum()

    emp = Employee(sName, sAddr, sNum)

    dict[sName] = emp

    print "add successfully completed"


def edit():

    sName = promptEditName()

    if isKeyValid(sName):
        sAddr = promptAddress()
        sNum = promptMobileNum()

        emp = dict.get(sName)
        emp.setAddress(sAddr)
        emp.setNum(sNum)


def remove():

    sName = promptDeleteName()

    if isKeyValid(sName):
        dict.__delitem__(sName)


def display():

    for the_key, the_value in dict.iteritems():
        the_value.printMe()


def isKeyValid(sName):

    if not (dict.has_key(sName)):
        print("user not found.")
        return False
    else:
        return True


def register():

    while 1:

        sOp = raw_input("enter an operator (add, edit, remove, display, exit): ")
        if sOp == "add":
            add()
        elif sOp == "edit":
            edit()
        elif sOp == "remove":
            remove()
        elif sOp == "display":
            display()
        elif sOp == "exit":
            return
        else:
            print("operator not valid.")


register()