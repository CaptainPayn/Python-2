#Author:Philip

from NumerologyLifePathDetails import NumerologyExtended

def main():
    while True:

        sName = input("Enter first and last name: ")
        #sName = "Philip Yurovskiyh"

        #keeps looping if name is left blank
        if not sName:

            continue

        sDOB = input("Enter DOB(mm-dd-yyyy): ")
        #sDOB = "08-16-1998"

        #only breaks out of loop if all parameters are met
        #has to be 10 characters including dashes and/or slashes
        if sDOB[2] == "-" or sDOB[2] == "/" and \
                sDOB[5] == "-" or sDOB[5] == "/" and \
                len(sDOB) == 10:
                    break

    #putting object to variable so it can be printed
    myObject = NumerologyExtended(sName, sDOB)
    print(myObject)

main()
