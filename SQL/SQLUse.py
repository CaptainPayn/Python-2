
import sqlite3
import csv


#creating database file and cursor
dbConnection = sqlite3.connect("myDatabase.db")
dbCursor = dbConnection.cursor()

#try and except to create tables 
try:
    sCreateTable = "CREATE TABLE Employee(EmployeeID int, Name text)"
    dbConnection.execute(sCreateTable)
    #print(sCreateTable)

    sCreateTable = "CREATE TABLE Pay(EmployeeID int, year int, Earnings real)"
    dbConnection.execute(sCreateTable)
    #print(sCreateTable)

    sCreateTable = "CREATE TABLE SocialSecurityMinimum(Year int, Minimum real)"
    dbConnection.execute(sCreateTable)
    #print(sCreateTable)

    #save game
    dbConnection.commit()

except sqlite3.OperationalError: print("Could not create table")



#setting up query of inserting into pay table
sInsertPay = "INSERT INTO Pay(EmployeeID, year, Earnings) VALUES("

#setting up reset variable to use to reset each iterating
sInsertPayReset = sInsertPay

#reading pay text file
with open("Pay.txt", "r") as file:

    iRows = 0

    #setting up csv reader
    reader = csv.reader(file)

    #skipping heading
    next(reader)

    #iterating over each row
    for row in reader:
        #print(row)

        sInsertPay += f"{row[0]}, {row[1]}, {row[2]})"
        #print(sInsertPay)

        #executing the insert pay with the data from pay text file
        try:
            dbConnection.execute(sInsertPay)
            iRows += 1

        except sqlite3.OperationalError:
            print("Could not insert")

        #resetting insert pay after each row
        sInsertPay = sInsertPayReset

    #saving the data and outputting number of rows
    dbConnection.commit()
    print(f"Rows loaded into Pay table: {iRows}")


#setting up query of inserting into social security table
sInsertSocialSecurityMinimum = "INSERT INTO SocialSecurityMinimum(Year, Minimum) VALUES("

#setting up reset variable
sInsertSocialSecurityMinimumReset = sInsertSocialSecurityMinimum

#reading text file
with open("SocialSecurityMin.txt", "r") as file:

    iRows = 0

    reader = csv.reader(file)

    #skipping header
    next(reader)

    #iterating over each row in text file
    for row in reader:
        #print(row)

        sInsertSocialSecurityMinimum += f"{row[0]}, {row[1]})"
        #print(sInsertSocialSecurityMinimum)

        #execute insert
        try:
            dbConnection.execute(sInsertSocialSecurityMinimum)
            iRows += 1

        except sqlite3.OperationalError: print("Could not insert")

        #resetting for each row
        sInsertSocialSecurityMinimum = sInsertSocialSecurityMinimumReset

    #saving data and outputting rows loaded
    dbConnection.commit()
    print(f"Rows loaded into Social Security table: {iRows}")


#setting up employee query
sInsertEmployee = "INSERT INTO Employee(EmployeeID, Name) VALUES("
#setting up reset
sInsertEmployeeReset = sInsertEmployee

#reading file
with open("Employee.txt", "r") as file:

    iRows = 0

    reader = csv.reader(file)

    #skip heading
    next(reader)

    for row in reader:
        #print(row)

        sInsertEmployee += f"{row[0]}, '{row[1]}')"
        #print(sInsertEmployee)

        #execute insert
        try:
            dbConnection.execute(sInsertEmployee)
            iRows += 1

        except sqlite3.OperationalError: print("Could not insert")

        #resetting after each row
        sInsertEmployee = sInsertEmployeeReset

    dbConnection.commit()
    print(f"Rows loaded into Employee table: {iRows}")



#selecting specific things to be outputted from each table (thanks mikey and scott)
dbCursor.execute("""
    SELECT a.Name, b.Year, b.Earnings, c.Minimum
    FROM Employee AS a
    JOIN Pay AS b
    JOIN SocialSecurityMinimum AS c
    ON c.Year = b.Year;
""")

#outputting hard coded headings
print(f"{'Employee Name':<20} {'Year':<5} {'Earnings':>15} {'Min':>15} {'Include':>15}")

#iterating over selected data from all tables
for row in dbCursor.fetchall():

    fResult = ""

    #logic if else to output include answer for social security
    if row[2] >= row[-1]: fResult = "Yes"

    else: fResult = "No"

    
    #outputting each row of chosen data with formatting
    print(f"{row[0]:<20} {row[1]:<5} {row[2]:>15,.2f} {row[3]:>15,.2f} {fResult:>15}")

