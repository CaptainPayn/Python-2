#Author:Philip

class Numerology:

    def __init__(self, sName:str, sDOB:str)->object:

        self.__sName = sName
        self.__sDOB = sDOB
        self.__nDOB = sDOB.replace("-", "").replace("/", "")

        #could not get your isalpha code to work so went back
        #to the original way
        self.__myCharacters = { "A":1, "J":1, "S": 1, 
                                "B":2, "K":2, "T": 2, 
                                "C":3, "L":3, "U": 3, 
                                "D":4, "M":4, "V": 4, 
                                "E":5, "N":5, "W": 5, 
                                "F":6, "O":6, "X": 6, 
                                "G":7, "P":7, "Y": 7, 
                                "H":8, "Q":8, "Z": 8, 
                                "I":9, "R":9}

        #setting up variables
        self.__iLifePath = 0
        self.__iBirthday = 0
        self.__iAttitude = 0
        self.__iPower = 0
        self.__iPersonality = 0
        self.__iSoul = 0


        #doing all computing in __init__
        #to be more efficient
        for sNumber in self.__nDOB:
            self.__iLifePath += int(sNumber)
        self.__iLifePath = self._reduceNumber(self.__iLifePath)
    

        self.__iBirthday += int(self.__nDOB[2:4])
        self.__iBirthday = self._reduceNumber(self.__iBirthday)


        sDOBAttitude = self.__nDOB[:4]
        for sNumber in sDOBAttitude:
            self.__iAttitude += int(sNumber)
        self.__iAttitude = self._reduceNumber(self.__iAttitude)


        #checking vowels; else consonants
        #for soul and personality nums
        for sLetter in self.Name.upper():

            if sLetter in "AEIOU":

                self.__iSoul += self.__myCharacters.get(sLetter, 0)

            else:

                self.__iPersonality += self.__myCharacters.get(sLetter, 0)

        self.__iSoul = self._reduceNumber(self.__iSoul)
        self.__iPersonality = self._reduceNumber(self.__iPersonality)

        #self.__iPower += self.Personality + self.Soul
        self.__iPower = self._reduceNumber(self.Personality + self.Soul)

    
    #stole from Prof C.
    def _reduceNumber(self, iNumber)->int:
        while len(str(iNumber)) > 1:
            iNumber = (iNumber % 10) + (iNumber // 10)
        return iNumber

    #def _reduceNumber(self, iNumber):
    #    while iNumber >= 10:
    #        sNumber = str(iNumber)
    #        iNumber = int(sNumber[0]) + int(sNumber[1])
    #    return iNumber


    #using properties so the "get" is no longer needed
    @property
    def Name(self)->str:
        return self.__sName
    
    @property
    def DOB(self)->str:
        return self.__sDOB
    
    @property
    def LifePath(self)->int:
        return self.__iLifePath

    @property
    def Birthday(self)->int:
        return self.__iBirthday

    @property
    def Attitude(self)->int:
        return self.__iAttitude

    @property
    def Power(self)->int:
        return self.__iPower

    @property
    def Personality(self)->int:
        return self.__iPersonality

    @property
    def Soul(self)->int:
        return self.__iSoul


    def __str__(self)->str:
        return f"Name: {self.Name}\
        \nDOB: {self.DOB}\
        \nLife Path: {self.LifePath}\
        \nBirthday: {self.Birthday}\
        \nAttitude: {self.Attitude}\
        \nPersonality: {self.Personality}\
        \nSoul: {self.Soul}\
        \nPower: {self.Power}"


#inheriting from Numerology class
class NumerologyExtended(Numerology):

    def __init__(self, sName, sDOB):

        #pulling name and DOB from original class
        Numerology.__init__(self, sName, sDOB)

        #dictionary with description for each number
        self.__lifePathDescriptions = {

            1: "The Independent: Wants to work/think for themselves",
            2: "The Mediator: Avoids conflict and wants love and harmony",
            3: "The Performer: Likes music, art and to perform or get attention",
            4: "The Teacher/Truth Seeker: Is meant to be a teacher or mentor and is truthful",
            5: "The Adventurer: Likes to travel and meet others, often a extrovert",
            6: "The Inner Child: Is meant to be a parent and/or one that is young at heart",
            7: "The Naturalist: Enjoy nature and water and alternative life paths, open to spirituality",
            8: "The Executive: Gravitates to money and power",
            9: "The Humanitarian: Helps others and/or experiences pain and learns the hard way"}
        
    #using get to return the description according to the life path num
    @property
    def LifePathDescription(self)->str:
        return self.__lifePathDescriptions.get(self.LifePath)
    
    #using __str__ from original class and adding life path description
    def __str__(self)->str: return \
        f"{Numerology.__str__(self)}\
        \n{'Life Path Description: ':20s}{self.LifePathDescription}"

