import sqlite3
import pathlib
import smtplib
import ssl
from datetime import datetime, date, timedelta
from time import mktime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from Sail import Sail, checkNumber

class DatabaseHandler:
   def __init__(self):
       createBase()


def createBase():
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


def addSail(serial):#, category, model, size, year, firstDate): #GUI done
    if not checkNumber(serial):
        print("Serial number wrong.")
        return
    try:
        sqliteConnection = sqlite3.connect('SQLite_Python_ReneEgli.db')
        cursor = sqliteConnection.cursor()
        sqlite_insert_with_param =  """INSERT INTO Sails 
                                    (id, category, model, size, year, firstDate)
                                    VALUES(?,?,?,?,?,?);"""
        datatuple = Sail(serial).getSail()
        cursor.execute(sqlite_insert_with_param, datatuple)
        sqliteConnection.commit()
        print('Sail added correctly to database.')
        cursor.close()
        return True
    except sqlite3.IntegrityError:
        print('Sail %s already exist in database!'%serial)
    except sqlite3.Error as error:
        print('Ups! Something went wrong!')
    finally:
        if (sqliteConnection):
            sqliteConnection.close()


def deleteSail(serial):     #GUI done
    if not checkNumber(serial):
        print("Serial number wrong.")
        return
    try:
        sqliteConnection = sqlite3.connect('SQLite_Python_ReneEgli.db')
        cursor = sqliteConnection.cursor()
        #print('Connected to database')

        if checkSail(serial) == []:
            print("Sail %s does not exist"%serial)
            if (sqliteConnection):
                sqliteConnection.close()
            return False
        else:
            sqlite_delete_query= """DELETE FROM Sails WHERE id = ? """
            cursor.execute(sqlite_delete_query, (serial,))
            sqliteConnection.commit()
            print('Sail %s deleted from database'%serial)
        cursor.close()
        return True
    except sqlite3.Error as error:
        print('Ups! Something went wrong!')
    finally:
        if (sqliteConnection):
            sqliteConnection.close()


def checkSail(serial):      #GUI done
    if not checkNumber(serial):
        print("Serial number wrong.")
        return
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


def saveList():     #GUI done
    try:
        sqliteConnection = sqlite3.connect('SQLite_Python_ReneEgli.db')
        sqlite3_print_query = """SELECT * FROM Sails """
        cursor = sqliteConnection.cursor()
        cursor.execute(sqlite3_print_query)
        records = cursor.fetchall()
        if not records:
            print('No sails in database.')
        else:
            f=open('SailsCenter1.txt','w')
            line='Serial\tCategory\tModel\tSize\tYear\tFirst time in database\n'
            f.write(line)
            for row in records:
                line=str(row[0])+'\t'+row[1]+'\t'+row[2]+'\t'+str(row[3])+'\t'+str(row[4])+'\t'+str(row[5])+'\n'
                f.write(line)

            f.close()
        currentPath=str(pathlib.Path().absolute())
        print('File saved in: %s'%currentPath)

    except sqlite3.Error as error:
        print('Ups! Something went wrong!')
    finally:
        if (sqliteConnection):
            sqliteConnection.close()


def printList():        #GUI done
    try:
        sqliteConnection = sqlite3.connect('SQLite_Python_ReneEgli.db')
        sqlite3_print_query = """SELECT * FROM Sails """
        cursor = sqliteConnection.cursor()
        cursor.execute(sqlite3_print_query)
        records=cursor.fetchall()
        if not records:
            return 'No sails in database.'
        else:
            return stringFullList(records)

    except sqlite3.Error as error:
        print('Ups! Something went wrong!')
    finally:
        if (sqliteConnection):
            sqliteConnection.close()


def getAllSerials():        #for gui deleting/searching list    #GUI done
    try:
        sqliteConnection = sqlite3.connect('SQLite_Python_ReneEgli.db')
        sqlite3_print_query = """SELECT id FROM Sails """
        cursor = sqliteConnection.cursor()
        cursor.execute(sqlite3_print_query)
        records=cursor.fetchall()
        if not records:
            print('No sails in database.')
        else:
            #printing(records)
            a=[]
            for x in records:
                a.append(str(x)[2:-3])
            # print(a)
            return a

    except sqlite3.Error as error:
        print('Ups! Something went wrong!')
    finally:
        if (sqliteConnection):
            sqliteConnection.close()


def printDetails(ser, cat, mod, si, ye, fDate):  # print all details(I think quite goot for beginning)
    print("Serial:\t%s\nCategory:\t%s\nModel:\t%s\nSize:\t%.1f\nYear:\t%d\nAdded to database:\t%s"% (ser, cat, mod, si, ye, fDate))


def sendListSsl(list, date, lastDate = 0 ):
    try:
        gmailServer = "smtp.gmail.com"
        port = 465
        login = 'surfdeveloper@gmail.com'
        password = 'vyynzusvjmexilvz'
        reciever = 'surfdeveloper@gmail.com'

        message = MIMEMultipart('alternative')
        message['From'] = 'Windsurfing Center 1 Rene Egli'
        message['To'] = 'Megastore Rene Egli'
        if lastDate == 0:
            message['Subject'] = 'List of the day ' + (date.strftime("%A, %d. %B %Y"))
        else:
            message['Subject'] = 'List from ' + (date.strftime("%A, %d. %B %Y")) + 'until ' + (lastDate.strftime("%A, %d. %B %Y"))

        part1 = MIMEText(list, 'plain') #list >>>text
        message.attach(part1)
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(gmailServer, port, context=context) as server:
            server.login(login, password)
            server.sendmail(login, reciever, message.as_string())
            server.close()
        return True
    except Exception as e:
        print(e)
        return False

def sendFullListFromFile():
    fileName = 'SailsCenter1.txt'
    f = open(fileName, 'r')
    converted = f.read()
    sendListSsl(converted, datetime.now())


def sendMovementOfToday():      #GUI done
    today=date.today()
    list = movementOfDay(today.strftime('%Y-%m-%d'))
    if sendListSsl(list, datetime.now()):
        return True


def getAllDates():
    try:
        sqliteConnection = sqlite3.connect('SQLite_Python_ReneEgli.db')
        sqlite3_print_query = """SELECT firstDate FROM Sails """
        cursor = sqliteConnection.cursor()
        cursor.execute(sqlite3_print_query)
        records = cursor.fetchall()
        dateDict = set()
        dateList=[]
        if not records:
            print('No movements in database.')
        else:
            dateDict.update(records)
            for x in dateDict:
                dateList.append(str(x)[2:-3])

        return dateList

    except sqlite3.Error as error:
        print('Ups! Something went wrong!')
    finally:
        if (sqliteConnection):
            sqliteConnection.close()


def sendMovementOfDay(date):
    list = movementOfDay(date)
    if sendListSsl(list, datetime.strptime(date, '%Y-%m-%d')):
        return True


def sendMovementInDays(fromDate, toDate):
    fromDateObj = datetime.strptime(fromDate, '%Y-%m-%d')
    toDateObj = datetime.strptime(toDate, '%Y-%m-%d')
    list = ""
    for dt in daterange(fromDateObj, toDateObj):
        dailyList = movementOfDay(dt.strftime('%Y-%m-%d'))
        if dailyList == None:
            return print("No database")
        list += dailyList
    if sendListSsl(list, fromDateObj, toDateObj):
        return True

    #print(list)


def daterange(fromD, toD):
        for n in range(int((toD-fromD).days)+1):
            print('range'+str(n))
            yield fromD + timedelta(n)


def movementOfDay(date):    #date %Y-%m-%d
    dateObj = datetime.strptime(date, '%Y-%m-%d')
    unixDate = mktime(dateObj.timetuple())
    try:
        sqliteConnection = sqlite3.connect('SQLite_Python_ReneEgli.db')
        sqlite3_print_query = """SELECT * FROM Sails WHERE firstDate = date( ? , 'unixepoch');"""
        cursor = sqliteConnection.cursor()
        cursor.execute(sqlite3_print_query, (unixDate,))
        records = cursor.fetchall()
        list = ''
        if not records:
            list += ('No movements on day %s\n.' % date)
            print('No movements on day %s.' % date)
        else:
            line='Serial\tCategory\tModel\tSize\tYear\tAdded to database\n'
            list += line
            for row in records:
                line=str(row[0])+'\t'+row[1]+'\t'+row[2]+'\t'+str(row[3])+'\t'+str(row[4])+'\t'+str(row[5])+'\n'
                list += line
        return list
        #sendListSsl(list, dateObj)
    except sqlite3.Error as error:
        print('Ups! Something went wrong!')
    finally:
        if (sqliteConnection):
            sqliteConnection.close()

def stringFullList(records):
    line = 'Serial\tCategory\tModel\tSize\tYear\tFirst time in database\n'

    for row in records:
        line += str(row[0]) + ' ' + row[1] + ' ' + row[2] + ' ' + str(row[3]) + ' ' + str(row[4]) + ' ' + str(
            row[5]) + '\n'
    return line

def printing(records):
    for row in records:
        tserial = row[0]
        tcategory = row[1]
        tmodel = row[2]
        tsize = row[3]
        tyear = row[4]
        tLastChange = row[5]

        printDetails(tserial, tcategory, tmodel, tsize, tyear, tLastChange)
