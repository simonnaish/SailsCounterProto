import sqlite3
from Sail import Sail


class DatabaseHandler:
   def __init__(self):
        try:
            sqliteConnection = sqlite3.connect('SQLite_Python_ReneEgli.db')
            sqlite_create_table_query = '''CREATE TABLE Sails (
                                           id TEXT  NOT NULL UNIQUE PRIMARY KEY,
                                           category TEXT NOT NULL,
                                           model TEXT NOT NULL ,

                      size REAL NOT NULL,
                                           year INTEGER NOT NULL,
                                           firstDate datetime);'''

            cursor = sqliteConnection.cursor()
            print("Successfully Connected to SQLite")
            cursor.execute(sqlite_create_table_query)
            sqliteConnection.commit()
            print("SQLite table created")

            cursor.close()

        except sqlite3.Error as error:
            print("Error while creating a sqlite table", error)
        finally:
            if (sqliteConnection):
                sqliteConnection.close()
                print("sqlite connection is closed")


def addSail(serial):#, category, model, size, year, firstDate):

    try:
        sqliteConnection = sqlite3.connect('SQLite_Python_ReneEgli.db')
        cursor = sqliteConnection.cursor()
        #print('Connected to database')

        sqlite_insert_with_param =  """INSERT INTO Sails 
                                    (id, category, model, size, year, firstDate)
                                    VALUES(?,?,?,?,?,?);"""
        datatuple = Sail(serial).getSail()#, category, model, size, year, firstDate)
        cursor.execute(sqlite_insert_with_param, datatuple)
        sqliteConnection.commit()
        print('Sail added correctly to database.')
        cursor.close()
    except sqlite3.IntegrityError:
        print('Sail %s already exist in database!'%serial)
    except sqlite3.Error as error:
        print('Ups! Something went wrong!')
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            #print('Connection to database closed.')


def deleteSail(serial):
    try:
        sqliteConnection = sqlite3.connect('SQLite_Python_ReneEgli.db')
        cursor = sqliteConnection.cursor()
        #print('Connected to database')

        if checkSail(serial) == []:
            print("Sail %s does not exist"%serial)
        else:
            sqlite_delete_query= """DELETE FROM Sails WHERE id = ? """
            cursor.execute(sqlite_delete_query, (serial,))
            sqliteConnection.commit()
            print('Sail %s deleted from database'%serial)
        cursor.close()
    except sqlite3.Error as error:
        print('Ups! Something went wrong!')
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            #print('Connection to database closed.')


def checkSail(serial):
    try:
        sqliteConnection = sqlite3.connect('SQLite_Python_ReneEgli.db')
        sqlite_check_query = """SELECT * FROM Sails WHERE id == ?"""
        cursor = sqliteConnection.cursor()
        cursor.execute(sqlite_check_query, (serial, ))
        records=cursor.fetchall()
        return records
    except sqlite3.Error as error:
        print('Ups! Something went wrong!')
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            #print('Connection to database closed')

def getSail(serial):

    records=checkSail(serial)
    if not records:
        print('Sail number %s does not exist in database.'%serial)
    else:
        printing(records)


#def saveList():         #TO DO: save to file



def printList():
    try:
        sqliteConnection = sqlite3.connect('SQLite_Python_ReneEgli.db')
        sqlite3_print_query = """SELECT * FROM Sails """
        cursor = sqliteConnection.cursor()
        cursor.execute(sqlite3_print_query)
        records=cursor.fetchall()
        if not records:
            print('No sails in database.')
        else:
            printing(records)

    except sqlite3.Error as error:
        print('Ups! Something went wrong!')
    finally:
        if (sqliteConnection):
            sqliteConnection.close()


def printDetails(ser, cat, mod, si, ye, fDate):  # print all details(I think quite goot for beginning)
    print("Serial:\t%s\nCategory:\t%s\nModel:\t%s\nSize:\t%.1f\nYear:\t%d\nAdded to database:\t%s"% (ser, cat, mod, si, ye, fDate))

def printing(records):
    for row in records:
        tserial = row[0]
        tcategory = row[1]
        tmodel = row[2]
        tsize = row[3]
        tyear = row[4]
        tfirstDate = row[5]
        print('chuj')

        printDetails(tserial, tcategory, tmodel, tsize, tyear, tfirstDate)
