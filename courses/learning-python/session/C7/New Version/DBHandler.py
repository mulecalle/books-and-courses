import shelve

def grabDataFromDB(userID):

    db = shelve.open('persona')

    IDToLook = userID.get()

    try:

        userDetails = db[IDToLook]
        db.close()

        return userDetails

    except:

        return ("Cannot find that user ID")

def deleteUser(userID):

    db = shelve.open('persona')

    IDToLook = userID.get()

    try:

        del db[IDToLook]
        db.close()

        return ("The userId " + IDToLook + " was successfully deleted.")

    except:

        return ("userId doesnt exist.")

def userExist(userID):

    db = shelve.open('persona')

    IDToLook = userID.get()

    try:

        bool = IDToLook in db
        db.close()

        return bool

    except:

        return False

def DBModify(values, aUser):

    db = shelve.open('persona')

    person = db[aUser.get()]

    #print(values)

    person.setNombre(values[0])
    person.setEdad(values[1])
    person.setSueldo(values[2])
    person.setTrabajo(values[3])

    print(person)

    try:
        db[aUser.get()] = person
        db.close()

    except:

        print("Cannot update the person")
