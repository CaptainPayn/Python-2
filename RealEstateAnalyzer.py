import csv

#median function takes in list
def getMedian(lstList1):

    #sorting list and getting length
    lstList1.sort()
    iListLength = len(lstList1)

    #modulus division to determine odd or even
    if iListLength % 2 == 0:
        fMedianRight = lstList1[iListLength // 2]
        fMedianLeft = lstList1[(iListLength // 2) - 1]

        fMedian = (fMedianLeft + fMedianRight) / 2
    else:
        #if even simply divide by 2
        fMedian = lstList1[iListLength // 2]

    return fMedian

#using csv reader to get input from file
def getDataInput(sFileName):
    try:
        #reading file in with csv reader
        with open(sFileName, "r") as file:
            reader = csv.reader(file)
            
            #bypass heading
            next(reader)
            
            #creating list for data
            inputData = []

            #iterating over contents in file and 
            #appending to list
            for row in reader:
                inputData.append(row)

        return inputData 
    except FileNotFoundError:
        print(f"File {sFileName} not found!")
        raise SystemExit

def main():
    #inputting actual file to be processed
    lstData = getDataInput("RealEstateData.csv")

    #creating lists
    lstCitys = []
    lstPropertyTypes = []
    lstPrices = []

    #creating dictionaries
    dictPropertyType = {}
    dictCity = {}
    dictZip = {}

    for row in lstData:
        #indexing the different types of data
        sCity = row[1]
        sPropertyType = row[7]
        fPrice = float(row[8])
        sZip = row[2]

        #checking if city is in list; adding if not
        if sCity not in lstCitys: lstCitys.append(sCity)

        #checking if property type is in list; adding if not
        if sPropertyType not in lstPropertyTypes: lstPropertyTypes.append(sPropertyType)

        #adding price based on property type
        if sPropertyType in dictPropertyType:
            dictPropertyType[sPropertyType] += fPrice
        else:
            dictPropertyType[sPropertyType] = fPrice


        #adding price based on city
        if sCity in dictCity:
            dictCity[sCity] += fPrice
        else:
            dictCity[sCity] = fPrice
            
        #adding price based on zip code
        if sZip in dictZip:
            dictZip[sZip] += fPrice
        else:
            dictZip[sZip] = fPrice

        #adding prices to list
        lstPrices.append(fPrice)

    #sorting list
    lstPrices.sort()

    #calling median func
    fMedian = getMedian(lstPrices)
        
    #iterating over dictionaries and outputting with formatting
    print("\nSummary by property type:")
    for propertyType, fTotal in dictPropertyType.items():
        print(f"{propertyType:20s}{fTotal:15,.2f}")
       
    print("\nSummary by city:")
    for sCity, fTotal in dictCity.items():
        print(f"{sCity.title():20s}{fTotal:15,.2f}")
        
    print("\nSummary by zip code:")
    for sZip, fTotal in dictZip.items():
        print(f"{sZip:20s}{fTotal:15,.2f}")
        
        
    #outputting formatted calculations
    print("\nCalculated prices:")
    print(f"Minimum {min(lstPrices):>27,.2f}")
    print(f"Maximum {max(lstPrices):>27,.2f}")
    print(f"Sum     {sum(lstPrices):>27,.2f}")
    print(f"Avg     {sum(lstPrices)/len(lstPrices):>27,.2f}")
    print(f"Median  {fMedian:>27,.2f}")

main()
