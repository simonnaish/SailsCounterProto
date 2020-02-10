import SailsModelsAndCat
import databaseHandler
from datetime import date
import sqlite3


class Sail:
    def __init__(
        self, serial
    ):  # , category, model, year, size, date-added to database)    # used, repaired):       #idea for future to  sign used/repaired sails?
        self.serial = serial                                   #UPDATE!!!#maybe bool "in repair?"? Keeping sail in database but hided.
        prem = "premium"                                                 #Or separated database for sails in repair and sails sent to shop.
        wc = "world cup"                                                 #deleted when destroyed or  sold. :)

        if (str(serial[:3]).lower() in SailsModelsAndCat.premiumSet) | (
            str(serial[:2]).lower() in SailsModelsAndCat.exclusiveModels
        ):  # set category (WC/Prem)
            self.category = prem
        else:
            self.category = wc
        if (self.category is prem) & (
            str(serial[:2]).lower() not in SailsModelsAndCat.exclusiveModels
        ):  # set string for model code
            ser = str(serial[:3]).lower()
        else:
            ser = str(serial[:2]).lower()
        self.model = SailsModelsAndCat.modelsMap[ser]  # set model full name
        if 9 == int(
            self.serial[-3]
        ):  # set year   #len(ser)+1:len(ser)+2 !!!!!!!!!!!!!!! DOESN'T WORK!!!!!!
            self.year = 2019
        else:
            self.year = 2020

        self.firstDate=date.today()

        self.size = (
            int(serial[len(ser) : len(ser) + 2]) / 10
        )  # set size...a bit freestyle?


    def printDetails(self):  # print all details(I think quite goot for beginning)
        print(
            "Serial:\t%s\nCategory:\t%s\nModel:\t%s\nSize:\t%.1f\nYear:\t%d\nAdded to database:\t%s"
            % (self.serial, self.category, self.model, self.size, self.year, self.firstDate)
        )

    """def addSailtoSQLite(self):      #How to make  it directly in databaseHandler.py ????
        databaseHandler.addSail(self.serial, self.category, self.model, self.size, self.year, self.firstDate)
"""             #DONE!!!!!!!!!!!!!!

    def getSail(self):
        return self.serial, self.category, self.model, self.size, self.year, self.firstDate
        """ self.category, self.model, self.size, self.year, self.firstDate)

        Need to include time of first time showing  up in database. 
        Could be used to check if  sail is new or came back from repare or  looking for  mistakes.
        
        def deleteSail()print(s.category,s2.category)

        def sendToRepair()
        def sellSail()
        def createFileWithSails()
        
        
        def readQr()        #to come in summer2020
        
        
        PS Same classes for boards, masts and fins(imported to  boards-hashmap(board:fin)[special  situation for ignite!]
        """


s=Sail('BL45201')
s2=Sail('BLP47210')
s3=Sail('GT57211')

"""s.printDetails()
s2.printDetails()
s.addSailtoSQLite()
s2.addSailtoSQLite()
s3.printDetails()
s3.addSailtoSQLite()"""