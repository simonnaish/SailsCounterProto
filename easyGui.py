from databaseHandler import addSail, deleteSail,getAllSerials, checkSail, saveList, printList, sendMovementOfToday, getAllDates, sendMovementInDays, sendMovementOfDay
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
from Sail import Sail, checkNumber

#Main window
window = Tk()
window.title("Rene Egli equipment managment")
window.geometry('800x800')

#Add sail:
addLabel = Label(window, text="Add sail(i.g. FR44205):")
addLabel.grid(column=0, row=0)

addField = Entry(window, width=12)
addField.grid(column=1, row=0)

def addClick():
    if not checkNumber(addField.get()):
        messagebox.showerror('Serial Error', 'Number of Sail is not correct.')
        return
    elif checkNumber(addField.get()) and addSail(addField.get()):
        messagebox.showinfo("Success", 'Sail correctly added to database')
        refreshCombos()
    else:
        messagebox.showerror('Integrity error', 'Sail already exist in database')
addButton = Button(window, text="CONFIRM", command=addClick)
addButton.grid(column=2, row=0)

#DeleteSail:
delLabel = Label(window, text="Delete sail(i.g. FR44205 or choose):")
delLabel.grid(column=0, row=1)

delCombo = Combobox(window, width=11)
delCombo.grid(column=1, row=1)
delCombo['values']=getAllSerials()

def delClick():
    if not checkNumber(delCombo.get()):
        messagebox.showerror('Serial Error', 'Number of Sail is not correct.')
    elif checkNumber(delCombo.get()) and deleteSail(delCombo.get()):
        deleteSail(delCombo.get())
        messagebox.showinfo("Success", 'Sail correctly deleted from database')
        refreshCombos()
        delCombo.set('')
    else:
        messagebox.showerror('Integrity error', 'Sail does not exist in database')

delButton = Button(window, text="CONFIRM", command=delClick)
delButton.grid(column=2, row=1)

#Check sail:
checkLabel = Label(window, text="Check sail(i.g. FR44205 or choose):")
checkLabel.grid(column=0, row=2)

checkCombo = Combobox(window, width=11)
checkCombo.grid(column=1, row=2)
checkCombo['values']=getAllSerials()

def checkClick():
    if not checkNumber(checkCombo.get()):
        messagebox.showerror('Serial Error', 'Number of Sail is not correct.')
    elif checkSail(checkCombo.get())==[]:
        messagebox.showinfo("Sail not found", "No sail in database.")
    else:
        messagebox.showinfo(checkCombo.get(), Sail(checkCombo.get()).getStringDetails())

checkButton = Button(window, text="CONFIRM", command=checkClick)
checkButton.grid(column=2, row=2)

#Save to file:
toFileLabel=Label(window, text="Save to file")
toFileLabel.grid(column=0, row=3)

def saveToFile():
    saveList()
toFileButton = Button(window, text="CONFIRM", command=saveToFile)
toFileButton.grid(column=2, row=3)

#Print list of all sails:
printListLabel=Label(window, text="Print list of all sails")
printListLabel.grid(column=0, row=4)

printChoiceList=["FULL LIST", "SERIALS ONLY"]
i=1
toCheck=StringVar()
for x in printChoiceList:
    printRadio=Radiobutton(window, text=x, value=x, variable=toCheck)
    printRadio.grid(column=i, row=4)
    i += 1

def printAllSails():
    if toCheck.get() == "FULL LIST":            #Have to still work on formating text
        tempTk = Tk()
        tempTk.title('Full list of sails')
        txt = Label(tempTk, text=printList())
        txt.pack()
        tempTk.mainloop()
       #messagebox.showinfo('All sails', printList())
    elif toCheck.get() == "SERIALS ONLY":
        temp=getAllSerials()
        stemp=""
        for t in temp:
            stemp += t+'\n'
        tempTk=Tk()
        tempTk.title('Serial nubmers list')
        txt=Label(tempTk, text=stemp)
        txt.pack()
        tempTk.mainloop()
        #messagebox.showinfo('All serial numbers', stemp)
    else:
        messagebox.showerror('Error', 'You have to choose one of options.' )
printListButton=Button(window, text="CONFIRM", command=printAllSails)
printListButton.grid(column=3, row=4)

#Send daily movement:
def sendToday():
    if sendMovementOfToday():
        messagebox.showinfo('Success', "Report sent correctly")
    else:
        messagebox.showerror('Error', 'Can not send email. Check your internet connection.')
sendDayButton = Button(window, text="Send movement of today", command=sendToday)
sendDayButton.grid(column=0, row=5)

#Send movement on days
sendDaysLabel=Label(window, text="Send movement on day/days")
sendDaysLabel.grid(column=0, row=6)

sendCombo=Combobox(window, width=10)
sendCombo['values']=getAllDates()
sendCombo.grid(column=1, row=6)

checked=BooleanVar()

def disableField():
    if checked.get():
        sendCombo2.config(state="enabled")
    else:
        sendCombo2.config(state="disabled")
sendCheck=Checkbutton(window, text="Send raport from a period. ", var=checked, command=disableField)
sendCheck.grid(column=2, row=6)

sendCombo2=Combobox(window, width=10, state="disabled")
sendCombo2['values']=getAllDates()
sendCombo2.grid(column=3, row=6)

def sendDays():


    if checked.get():
        if sendCombo.get() > sendCombo2.get():
            messagebox.showerror('Error', 'Check dates. First date must happen earlier.')
            return 0
        elif sendMovementInDays(sendCombo.get(), sendCombo2.get()):
            messagebox.showinfo('Success', "Report sent correctly")
        else:
            messagebox.showerror('Error', 'Can not send email. Check your internet connection.')
    else:
        if not sendCombo.get():
            messagebox.showerror('Error', 'Date can not be empty!\nChose at least one date to send raport.')
        elif sendMovementOfDay(sendCombo.get()):
            messagebox.showinfo('Success', "Report sent correctly")
        else:
            messagebox.showerror('Error', 'Can not send email. Check your internet connection.')
sendDaysButton=Button(window, text="CONFIRM", command=sendDays)
sendDaysButton.grid(column=4, row=6)


def refreshCombos():
    checkCombo['values'] = getAllSerials()
    delCombo['values'] = getAllSerials()
    sendCombo['values'] = getAllDates()
    sendCombo2['values'] = getAllDates()


window.mainloop()
