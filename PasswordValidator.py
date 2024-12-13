#setting characters to be checked
specialCharacters = set("!@#$%^")
lowerCase = set("abcdefghijklmnopqrstuvwxyz")
upperCase = set("ABCDEFGHIJKLMNOPQRSTUVYXYZ")
numbers = set("0123456789")

def characterOccurence(password):
    #initialize dictionary
    dictCharacterOccurence = {i:0 for i in password}
    occurences = list()

    #iterate over the password
    for i in password:
        dictCharacterOccurence[i] += 1

    #checking if a character is appearing more than once (courtesy of tim)
    for key, value in dictCharacterOccurence.items():
        if value > 1:
             occurences.append(f"{key} appeared {value} times") 

    #returns list of occurences if > 1
    return occurences

def lengthCorrect(password):
    #returns true if length is incorrect
    if len(password) > 12 or len(password) < 8:
        return "Password must be between 8 and 12 characters" 
    else:
        return "" 

def containsPass(password):
    #returns true if "Pass" is present (case insensitive)
    if password.startswith("PASS"):
        return "Password cannot start with Pass"
    else:
        return "" 

def checkLower(password):
    #returns true if no lower case present
    if not any(char in lowerCase for char in password):
            return "Password must contain at least one lower case (a-z)"
    else:
        return ""

def checkUpper(password):
    #returns true if no upper case present
    if not any(char in upperCase for char in password):
            return "Password must contain at least one upper case (A-Z)"
    else:
        return ""

def checkSpecial(password):
    #returns true if no special characters present
    if not any(char in specialCharacters for char in password):
        return "Password must contain at least one of these ! @ # $ % ^"
    else:
        return ""

def checkNum(password):
    #returns true if no number present
    if not any(char in numbers for char in password):
        return "Password must contain at least one number(0-9)"
    else:
        return ""

def checkInitials(initials,password):
    #returns true if initials are present case (insensitive)
    if initials.upper() in password:
        return 'Password must not contain user initials'
    else:
        return ""


def main():

    #asking name and extracting initials
    sName = input("Enter full name such as John Smith: ")
    sInitials = sName[0] + sName[sName.find(" ") + 1]

    while True:

        #initialize list and empty it if not first time going through loop
        listValid = []
        #getting input
        sPassword = input("Enter Password: ")
        #using a capitalized version of password to use in checks
        sPassword2 = sPassword.upper()

        occursMore = characterOccurence(sPassword2)


        for character in occursMore:
            print(character)


        listValid.append(lengthCorrect(sPassword))

        listValid.append(containsPass(sPassword2))

        listValid.append(checkLower(sPassword))

        listValid.append(checkUpper(sPassword))

        listValid.append(checkSpecial(sPassword))
            
        listValid.append(checkNum(sPassword))

        listValid.append(checkInitials(sInitials, sPassword2))

        #if list is empty strings password is valid
        if listValid == ['', '', '', '', '', '', '']:
            print("Password is valid and OK to use")
            break

        #iterating over list of messages appended
        for element in(listValid):
            if element == "":
                pass
            else:
                print(element)

main()

