import sqlite3
"""import pathlib
import sys
sys.path.append(pathlib.Path().parent.absolute())
from Sail import printDetails"""
import Sail
class databaseHandler:

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

def addSail(serial, category, model, size, year, firstDate):
    try:
        sqliteConnection=sqlite3.connect('SQLite_Python_ReneEgli.db')
        cursor=sqliteConnection.cursor()
        print('Connected to database')

        sqlite_insert_with_param= """INSERT INTO Sails
                                    (id, category, model, size, year, firstDate)
                                    VALUES(?,?,?,?,?,?);"""
        datatuble=(serial, category,model,size,year,firstDate)
        cursor.execute(sqlite_insert_with_param, datatuble)
        sqliteConnection.commit()
        print('Sail added correctly to database.')
        cursor.close()
    except sqlite3.IntegrityError:
        print('Sail already exist in database!')
    except sqlite3.Error as error:
        print('Ups! Something went wrong!')
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print('Connection to database closed.')

    def getSail(serial):
        sqlite_select_query="""SELECT id, category, model, size, year, firstDate from Sails where id=?"""
        cursor.execute(sqlite_select_query, (serial))
        records=cursor.fetchall()
        for row in records:
            tserial=row[0]
            tcategory=row[1]
            tmodel=row[2]
            tsize=row[3]
            tyear=row[4]
            tfirstDate=row[5]
        Sail.printDetails(tserial,tcategory,tmodel,tsize,tyear,tfirstDate)


"""try:
    sqliteConnection = sqlite3.connect('SQLite_Python.db')
    cursor = sqliteConnection.cursor()
    print("Database created and Successfully Connected to SQLite")

    sqlite_select_Query = "select sqlite_version();"
    cursor.execute(sqlite_select_Query)
    record = cursor.fetchall()
    print("SQLite Database Version is: ", record)
    cursor.close()

except sqlite3.Error as error:
    print("Error while connecting to sqlite", error)
finally:
    if (sqliteConnection):
        sqliteConnection.close()
        print("The SQLite connection is closed")"""