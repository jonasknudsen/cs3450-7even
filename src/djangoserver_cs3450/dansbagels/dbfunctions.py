from dansbagels.models import *

# Change this variable to True if you want debug messages to print 
printDebugMessages = True

# Check to see if a given username/combination is valid.
# Return true if the username/password combination is in the database, false otherwise.
def verifyLogin(username, password):
    listOfUsers = []
    allPeople = Person.objects.all()
    for person in allPeople:
        listOfUsers.append((person.username_text, person.password_text))
    return (username, password) in listOfUsers


# Create an account given proper input parameters.
# Return true if account was created, false otherwise.
# An accountType object can be obtained by:
# AccountType.objects.get(pk=[1/2/3/4])
# All other parameters are strings.
def createAccount(firstName, lastName, username, password, email, phoneNumber, 
                  accountType, accountBalance=100.00):
    try:
        person = Person()
        person.firstName_text = firstName
        person.lastName_text = lastName
        person.username_text = username
        person.password_text = password
        person.email_email = email
        person.phoneNumber_text = phoneNumber
        person.accountBalance_decimal=accountBalance
        person.accountType = accountType
        person.save()
        printDebug("Account for " + firstName + " " + lastName + " created successfully")
        return True
    except Exception as e:
        printDebug("Failed to create account for " + firstName + " " + lastName)
        printDebug(str(e))
        return False


def printDebug(message):
    if printDebugMessages:
        print("[DEBUG] " + str(message))