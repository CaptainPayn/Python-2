#author: Philip Yurovskiyh
from Numerology2 import Numerology


def main():
    
    while True:

        sName = input("Enter first and last name: ")

        #keeps looping if name is left blank
        if not sName:

            continue

        sDOB = input("Enter DOB(mm-dd-yyyy): ")

        #only breaks out of loop if all parameters are met
        #has to be 10 characters including dashes and/or slashes
        if sDOB[2] == "-" or sDOB[2] == "/" and \
                sDOB[5] == "-" or sDOB[5] == "/" and \
                len(sDOB) == 10:
                    break

    #instantiating class object
    myNumerologyObject = Numerology(sName, sDOB)

    #outputting results
    print(myNumerologyObject)

#program start
main()

