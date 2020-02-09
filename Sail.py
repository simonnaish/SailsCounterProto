import SailsModelsAndCat
import sqlite3

class Sail:
    def __init__(
        self, serial
    ):  # , category, model, year, size, used, repaired):       #idea for future to  sign used/repaired sails?
        self.serial = serial
        prem = "premium"
        wc = "world cup"

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
        if 1 == int(
            self.serial[-3]
        ):  # set year   #len(ser)+1:len(ser)+2 !!!!!!!!!!!!!!! DOESN'T WORK!!!!!!
            self.year = 2019
        else:
            self.year = 2020
        """tempSize=serial[len(ser):len(ser)+2]
        strSize=''
        for x in tempSize: strSize=strSize+','+x
        """
        self.size = (
            int(serial[len(ser) : len(ser) + 2]) / 10
        )  # set size...a bit freestyle?

    def printDetails(self):  # print all details(I think quite goot for beginning)
        print(
            "Serial:\t%s\nCategory:\t%s\nModel:\t%s\nSize:\t%.1f\nYear:\t%d"
            % (self.serial, self.category, self.model, self.size, self.year)
        )

    def addSailtoSQLite(self):  #adding sail to SQLite user:reneeglic1; pass:fuckLagoon




        """
        Need to include time of first time showing  up in database. 
        Could be used to check if  sail is new or came back from repare or  looking for  mistakes.
        
        def deleteSail()
        def sendToRepair()
        def sellSail()
        def createFileWithSails()
        
        
        def readQr()        #to come in summer2020
        
        
        PS Same classes for boards, masts and fins(imported to  boards-hashmap(board:fin)[special  situation for ignite!]
        """


"""ail('BL45201')
s2=Sail('BLP2010')

print(s.category,s2.category)
s.printDetails()
"""
