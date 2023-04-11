#This is the main file of the program. It shows the main interactive menu of the program.

##-----------IMPORTS---------
import databaseConnect as db

##-------Global Variables------
global conn

##----------------firstMessage----------------------
print("\t----------Student Management-----------")
print("----------LOGIN-----------")



##------------------------------------------FUNCTIONS---------------

##-----------USER--------------------
def userLogin():
    print("\n\t----------USER LOGIN-----------\n")

    # Reading the username and password
    username = input("Enter the username: ")
    password = input("Enter your password: ")

    # Connecting to the database
    conn = db.oracleConnect(username, password)

    #Run till the user decides to exit the program
    while True:
        # Showing the actions to be performed
        print("\n---USER MENU---")
        print("1. Show Students")
        print("2. Exit")
        choice = input("Enter your choice: ")

        # Show Students Selected
        if choice == '1':
            # Execute the read statement and store the retrived values
            rows = db.readValues(conn)

            # for each row in data display as table
            # Format: [(sid, name, adderess, semester, faculty), ()]
            print("\nSTUDENT'S Details")
            print("SID\t\t\tNAME\t\t\tADDRESS\t\t\tSEMESTER\t\t\tFACULTY")
            for row in rows:
                sid,name,address,semester, faculty = row
                print(f"{sid}\t\t\t{name}\t\t\t{address}\t\t\t{semester}\t\t\t{faculty}")

        # Exit Selected
        if choice == '2':
            break 

        else:
            print("Please Select correct option.")
    db.oracleCommitClost(conn)
# -----------------------------------
    

    
#-----------ADMIN-------------------
def adminLogin():
    print("\n\t----------ADMIN LOGIN-----------\n")

    #Reading the username and password
    username = input("Enter the username: ")
    password = input("Enter your password: ")

    # Creating the connection
    conn = db.oracleConnect(username, password)
  
    # Show the menu till user decides to exit



    
# -----------------------------------
# ------------------------------------------------------------------

run = True #Setting this variable to read user input till user selects the correct option

# Continue reading user input till user selects something on menu
while run:
    # Main Menu
    print("-------Log In As------")
    print("1. User")
    print("2. Admin")
    print("3. Exit")

    choice = input("Enter your choice: ")

    #USER Login
    if choice == '1':
        run= False #Setting run to false as correct option is selected. 
        userLogin()
        

    #ADMIN login
    elif choice == '2':
        run= False #Setting run to false as correct option is selected. 
        adminLogin()
    
    # exit
    elif choice == '3':
        run=False
        exit()

    #If out of menu option selected
    else:
        print("\nPlease select a correct choice.")
        

