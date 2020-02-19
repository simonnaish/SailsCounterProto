from databaseHandler import addSail, deleteSail,getAllSerials, checkSail
from tkinter import *
from tkinter.ttk import *
from Sail import Sail

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
    addSail(addField.get())
    refreshCombos()
addButton = Button(window, text="CONFIRM", command=addClick)
addButton.grid(column=2, row=0)

#DeleteSail:
delLabel = Label(window, text="Delete sail(i.g. FR44205 or choose):")
delLabel.grid(column=0, row=1)

delCombo = Combobox(window, width=11)
delCombo.grid(column=1, row=1)
delCombo['values']=getAllSerials()

# delField = Entry(window, width=12)
# delField.grid(column=1, row=1)

def delClick():
    deleteSail(delCombo.get())
    refreshCombos()
delButton = Button(window, text="CONFIRM", command=delClick)
delButton.grid(column=2, row=1)

#Check sail:
checkLabel = Label(window, text="Check sail(i.g. FR44205 or choose):")
checkLabel.grid(column=0, row=2)

checkCombo = Combobox(window, width=11)
checkCombo.grid(column=1, row=2)
checkCombo['values']=getAllSerials()
# delField = Entry(window, width=12)
# delField.grid(column=1, row=2)

def checkClick():
    if checkSail(checkCombo.get())==[]:
        print("No sail in database.")
    else:
        Sail(checkCombo.get()).printDetails()
checkButton = Button(window, text="CONFIRM", command=checkClick)
checkButton.grid(column=2, row=2)

def refreshCombos():
    checkCombo['values'] = getAllSerials()
    delCombo['values'] = getAllSerials()


window.mainloop()
