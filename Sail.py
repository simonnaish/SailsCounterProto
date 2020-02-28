import SailsModelsAndCat
from datetime import date


class Sail:
    def __init__(
            self, serial
    ):  # , category, model, year, size, date-added to database)    # used, repaired):       #idea for future to  sign used/repaired sails?
        self.serial = serial  # UPDATE!!!#maybe bool "in repair?"? Keeping sail in database but hiden.
        prem = "premium"  # Or separated database for sails in repair and sails sent to shop.
        wc = "world cup"  # deleted when destroyed or  sold. :)

        if (str(serial[:3]).lower() in SailsModelsAndCat.premiumSet) | (
                str(serial[:2]).lower() in SailsModelsAndCat.exclusiveModels
        ):  # set category (WC/Prem)
            self.category = prem
        else:
            self.category = wc
        if (self.category is prem) & (
                str(serial[:2]).lower() not in SailsModelsAndCat.exclusiveModels
        ):
            ser = str(serial[:3]).lower()
        else:
            ser = str(serial[:2]).lower()
        self.model = SailsModelsAndCat.modelsMap[ser]  # set model full name
        if 9 == int(
                self.serial[-3]
        ):
            self.year = 2019
        else:
            self.year = 2020

        self.lastChange = date.today()

        self.size = (
                int(serial[len(ser): len(ser) + 2]) / 10
        )

    def printDetails(self):
        print(
            "Serial:%s\nCategory:%s\nModel:%s\nSize:%.1f\nYear:%d\nAdded to database:%s"
            % (self.serial, self.category, self.model, self.size, self.year, self.lastChange)
        )


    def getStringDetails(self):
        return "Serial:%s\nCategory:%s\nModel:%s\nSize:%.1f\nYear:%d\nAdded to database:%s" % (self.serial, self.category, self.model, self.size, self.year, self.lastChange)



    def getSail(self):
        return self.serial, self.category, self.model, self.size, self.year, self.lastChange
        """ self.category, self.model, self.size, self.year, self.firstDate)
        Need to include time of first time showing  up in database. 
        Could be used to check if  sail is new or came back from repaire or  looking for  mistakes.

        def deleteSail()print(s.category,s2.category)
        def sendToRepair()
        def sellSail()
        def createFileWithSails()


        def readQr()        #to come in summer2020


        PS Same classes for boards, masts and fins(imported to  boards-hashmap(board:fin)[special  situation for ignite!]
        """
def checkNumber(serial):      #FINISH FUNCTION, GET A SAIL DETAILS FROM LAST INDEX ([:-3] | [:-5] etc
    if (str(serial[0:2]).lower() in SailsModelsAndCat.premiumSet) and len(serial) ==7:
        if checkSize(serial[2:4], Sail(serial).model):
            return True
        else:
            return False
    elif (str(serial[0:3]).lower() in SailsModelsAndCat.premiumSet) and len(serial) ==8:
        if checkSize(serial[3:5], Sail(serial).model):
            return True
        else:
            return False
    elif str(serial[0:2]).lower() in set(SailsModelsAndCat.modelsMap.keys()) and len(serial) ==7:
        if checkSize(serial[2:4], Sail(serial).model):
            return True
        else:
            return False
    else:
        return False

def checkSize(size, model):
    if size in SailsModelsAndCat.modelToDict.get(model):
        return True
    else:
        return False

