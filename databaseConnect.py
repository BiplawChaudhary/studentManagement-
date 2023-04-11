# This file connects to the database and returns the connection to the caller
##--------------IMPORTS---------
import cx_Oracle

# Function to connect to oracleDB 
def oracleConnect(username, password, hostname='localhost', sid='xe'):
    connectionString = username + '/' + password +'@//' + hostname + ':1521/' + sid

    try:
        #Creating the connection
        conn = cx_Oracle.connect(connectionString)
        # If connection is successful return the connection
        return conn
    # Else Show the connection error
    except Exception as err:
        print("\nConnection Error.")
        print(f"Error Cause: \n {err}")
        exit()



#Function to just close the connection without commiting it to the database
def oracleDisconnect(conn):
    conn.close()
    print("Connection Closed")



#Function to commit the changes to the database and close the connection
def oracleCommitClost(conn):
    conn.commit()
    conn.close()
    print("Changes Committed and Connection Closed")



# Function to insert the values into STUDENT table
def insertValues(sid, name, address, semester, faculty, conn):
    # Creating the insertQuery
    query = """
        INSERT INTO student VALUES(:1,:2,:3,:4,:5)
    """

    # Creating the cursor to execute query
    cur = conn.cursor()
    #Executing the query.
    try:
        cur.execute(query,[sid, name, address, semester, faculty])
        # return true if execution successful
        return True
    # If query is not executed successfully
    except Exception as err:
        print("\nConnection Error.")
        print(f"Error Cause: \n {err}") 
        #Return false as the execution is unsuccessful.
        return False
    # Closing the cursor
    cur.close()



# Function to read values from table
def readValues(conn):
    query = """
        SELECT * FROM student ORDER BY sid
    """
    # Creating the cursor to execute query
    cur = conn.cursor()
    #Executing the query.
    try:
        cur.execute(query)
        # getting the rows
        rows= cur.fetchall()
        # return true if execution successful
        cur.close()
        return rows
    # If query is not executed successfully
    except Exception as err:
        print("\nConnection Error.")
        print(f"Error Cause: \n {err}") 
        #Return -1 if no data returned from the table.
        return -1
    # Closing the cursor
    
       

    
def getSID(conn):
    query = """
        SELECT s_id FROM counter
    """

    try:
        #Creating the cursor to execute query
        cur = conn.cursor()
        cur.execute(query)
        sidCount = cur.fetchone()
        cur.close()
        return sidCount
    except Exception as err:
        print("\nConnection Error.")
        print(f"Error Cause: \n {err}") 

    