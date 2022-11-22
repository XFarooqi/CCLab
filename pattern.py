from tkinter import *

def phFun():
    phoneNum = phValue.get()
    if len(phoneNum) ==11:
        print(f"Phone number is Valid")
    else:
        print(f"Phone number is InValid")

def emFun():
    EmailVal = emValue.get()
    if "@" in EmailVal:
        print(f"Email number is Valid")
    else:
        print(f"Email number is InValid")


root = Tk()
root.geometry("444x344")

Label(root, text="Pattern Matching", font="comicsansms 13 bold", pady=15).grid(row=0, column=3)

phone = Label(root, text="Enter phone number :")
phone.grid(row=1, column=3)
phValue = StringVar()
phEntry = Entry(root, textvariable=phValue)
phEntry.grid(row=1, pady=5, column=4)
Button(text="Submit Number", command=phFun).grid(row=10, pady=10, column=4)

email = Label(root, text="Enter Email number :")
email.grid(row=15, column=3)
emValue = StringVar()
emEntry = Entry(root, textvariable=emValue)
emEntry.grid(row=15, pady=5, column=4)
Button(text="Submit Email", command=emFun).grid(row=20, pady=10, column=4)

root.mainloop()
