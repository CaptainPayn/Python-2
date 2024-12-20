
class Numerology:

    #intitializing class object
    def __init__(self, sName:str, sDOB:str)->object:

        self.__sName = sName
        self.__sDOB = sDOB
        #removing dashes and/or slashes to use for calcs
        self.__nDOB = sDOB.replace("-", "").replace("/", "") #take out dashes or slashes

        #creating dictionary for conversions
        self.__myCharacters = { "A":1, "J":1, "S": 1, 
                                "B":2, "K":2, "T": 2, 
                                "C":3, "L":3, "U": 3, 
                                "D":4, "M":4, "V": 4, 
                                "E":5, "N":5, "W": 5, 
                                "F":6, "O":6, "X": 6, 
                                "G":7, "P":7, "Y": 7, 
                                "H":8, "Q":8, "Z": 8, 
                                "I":9, "R":9}

    #name getter
    def getName(self):
        return self.__sName
    
    #DOB getter
    def getDOB(self):
        return self.__sDOB
    
    #courtesy of mikey
    #decorator to reduce number if greater than 9
    def _reduceNumberDecorator(func):
        def wrapper(self):
            iNumber = func(self)
            while iNumber >= 10:
                sNumber = str(iNumber)
                iNumber = int(sNumber[0]) + int(sNumber[1])
            return iNumber
        return wrapper

    @_reduceNumberDecorator
    def getLifePath(self):

        iTotal = 0

        #iterating over DOB and returning total
        for sNumber in self.__nDOB:

            iTotal += int(sNumber)

        return iTotal

    @_reduceNumberDecorator
    def getBirthdayNumber(self):

        #indexing the day of birth
        return int(self.__nDOB[2:4]) #08161998
    
    @_reduceNumberDecorator
    def getAttitude(self):

        #indexing month and day
        sDOBAttitude = self.__nDOB[:4] #08161998

        iTotal = 0

        #iterating over month and day and adding together
        for sNumber in sDOBAttitude:

            iTotal += int(sNumber)

        return iTotal
    
    @_reduceNumberDecorator
    def getSoul(self):

        iTotal = 0

        #iterating over vowels in name
        for sLetter in self.getName().upper():

            if sLetter in "AEIOU":

                #thanks mikey
                iTotal += self.__myCharacters.get(sLetter, 0)

        return iTotal
    
    @_reduceNumberDecorator
    def getPersonality(self):

        iTotal = 0

        #iterating over consonants in name
        for sLetter in self.getName().upper():

            if sLetter not in "AEIOU":

                iTotal += self.__myCharacters.get(sLetter, 0)

        return iTotal
    
    @_reduceNumberDecorator
    def getPower(self):

        #returning the sum of soul and personality numbers
        return self.getSoul() + self.getPersonality()
    
    #courtesy of mikey
    #this cleaned up my USE code quite a bit
    #allowed me to print everything at once using the object
    def __str__(self)->str:
        return f"Name: {self.getName()}\
        \nDOB: {self.getDOB()}\
        \nLife Path: {self.getLifePath()}\
        \nBirthday: {self.getBirthdayNumber()}\
        \nAttitude: {self.getAttitude()}\
        \nPersonality: {self.getPersonality()}\
        \nSoul: {self.getSoul()}\
        \nPower: {self.getPower()}"

