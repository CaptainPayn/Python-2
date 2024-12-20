#importing module for encoding and decoding dictionary
import pickle

#creating dictionary for planet factors
dictPlanetFactor = {
       "Mercury" :0.38,
       "Venus"   :0.91, 
       "Moon"    :0.165, 
       "Mars"    :0.38, 
       "Jupiter" :2.34, 
       "Saturn"  :0.93, 
       "Uranus"  :0.92, 
       "Neptune" :1.12, 
       "Pluto"   :0.066
                     }

#inputvalidation
def validateInput(sPrompt):
    fNumber = 0
    while fNumber <= 0:
        # Attempt to convert user input to an integer
        try:
            fNumber = float(input(sPrompt))
            # If there is a problem converting to a float
            # monitor for the ValueError exception and inform
            # the user:
        except ValueError:
            print("Input must a numeric value")
    return fNumber

#initializing dictionary
dictPlanetHistory = dict()
#try to load the file and put into dictionary
try:
    with open("pyPlanetaryWeights.db", "rb") as file:
        dictPlanetHistory = pickle.load(file)
except:
    print("No file found")
#check if the dictionary is empty
#if it isn't ask if they want to see previous entries
if len(dictPlanetHistory) > 0:
    answer = input("Would you like to see the history? y/n: ").lower()
    if answer == "y":

        #nested loop to display name and planets with calculated weights
        for name, dictPlanetFactor in dictPlanetHistory.items():
            print(f"{name}, here are your weights on Solar System's planets")
            for planet, weight in dictPlanetFactor.items():
                print(f"Weight on {planet:10s} {weight:10,.2f}")

#defining main logic
def main():

    while True:
        #asking for input and using title to make it look nice
        sName = input("Enter name (Enter key to quit): ").title()
        #if enter key pressed breaks out of loop
        if sName == "":
            break

        #if name entered is already in history try again
        if sName in dictPlanetHistory:
            print(f"{sName} is already in the file. Enter a unique name.")
            continue
        #user input validation for their Earth weight
        fNumber = validateInput("Enter earth weight: ")
        print(f"{sName}, here are your weights on the solar systems planets")

        #initialize another dictionary for persons calculated weights
        dictPersonWeights =  dict()
        #iterate over dictionary and calculate persons weights
        for planet, factor in dictPlanetFactor.items():
            fWeight = fNumber * factor
            #put the calculations into another dictionary
            dictPersonWeights[planet] = fWeight
            print(f"Weight on {planet:10s}: {fWeight:>12.2f}")

        #pickle results to db file
        dictPlanetHistory[sName] = dictPersonWeights
        with open("pyPlanetaryWeights.db", "wb") as file:
            pickle.dump(dictPlanetHistory, file)

#start of program
main()

