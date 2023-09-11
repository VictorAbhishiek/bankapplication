from tkinter import*
from tkinter import messagebox
from PIL import ImageTk, Image
import pymysql
#import Tkinter as tk

import CreationOfAccount
import Accountdetails
import edit
import Close
import withdraw
import deposit
import Balance

conn=pymysql.connect(host="localhost",user="root",password="root",db="bank")


def exit():
    form2.destroy()

form2=Tk()   
form2.title("Menu")
form2.geometry("900x600+300+100")
form2.configure(bg="white")
#Create a canvas
canvas= Canvas(form2, width=850, height= 550)
canvas.pack()

#Load an image in the script
img= (Image.open("sbitext.jpg"))

#Resize the Image using resize method
resized_image= img.resize((405,100))
new_image= ImageTk.PhotoImage(resized_image)

#Add image to the Canvas Items
canvas.create_image(225,25, anchor=NW, image=new_image)


b1=Button(form2,text="CREATE NEW A/C",width=22,height=1,font=0.9,bg="black",fg="white",command=CreationOfAccount.main_form)
b1.place(x=150,y=175)
b2=Button(form2,text="A/C INFO",width=22,height=1,font=0.9,bg="black",fg="white",command=Accountdetails.main_form)
b2.place(x=150,y=250)
b3=Button(form2,text="A/C UPDATION",width=22,height=1,font=0.9,bg="black",fg="white",command=edit.main_form)
b3.place(x=150,y=325)
b4=Button(form2,text="CLOSE A/C",width=22,height=1,font=0.9,bg="black",fg="white",command=Close.main_form)
b4.place(x=150,y=400)
b5=Button(form2,text="WITHDRAW",width=22,height=1,font=0.9,bg="black",fg="white",command=withdraw.main_form)
b5.place(x=480,y=175)
b6=Button(form2,text="DEPOSIT",width=22,height=1,font=0.9,bg="black",fg="white",command=deposit.main_form)
b6.place(x=480,y=250)
b7=Button(form2,text="ALL A/C DETAILS",width=22,height=1,font=0.9,bg="black",fg="white")
b7.place(x=480,y=325)
b8=Button(form2,text="A/C BALANCE",width=22,height=1,font=0.9,bg="black",fg="white",command=Balance.main_form)
b8.place(x=480,y=400)
b9=Button(form2,text="EXIT",width=22,height=1,font=0.9,bg="black",fg="white",command=exit)
b9.place(x=320,y=475)


form2.mainloop()

