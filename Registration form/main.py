from tkinter import *
root = Tk()
root.geometry("500x300")
def getvals():
    print("Accepted")
#Heading
Label(root,text="Python registration form", font="arial 15 bold").grid(row=0,column=3)


#Field name
name = Label(root,text="name")
phone = Label(root,text="Phone")
gender = Label(root,text="Gender")
payment = Label(root,text="Payment mode")

#Packing fields
name.grid(row=1,column=2)
phone.grid(row=2,column=2)
gender.grid(row=3,column=2)
payment.grid(row=4,column=2)

#Value for storing data
namevalue = StringVar
phonevalue = StringVar
gendervalue = StringVar
paymentvalue = StringVar
checkvalue = IntVar

#Creaiting entry fields
nameentry = Entry(root,textvariable=namevalue)
phoneentry = Entry(root,textvariable=phonevalue)
genderentry = Entry(root,textvariable=gendervalue)
paymententry = Entry(root,textvariable=paymentvalue)

#Packing entry firlds
nameentry.grid(row=1,column=3)
phoneentry.grid(row=2,column=3)
genderentry.grid(row=3,column=3)
paymententry.grid(row=4,column=3)

#Creating check box
checkbtn = Checkbutton(text="rememeber me?",variable=checkvalue)
checkbtn.grid(row=5,column=3)

#Creating button
Button(text="Submit",command=getvals).grid(row = 6,column=3)

root.mainloop()





