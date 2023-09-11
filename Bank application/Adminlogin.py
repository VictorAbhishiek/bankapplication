from tkinter import*
from tkinter import messagebox
from PIL import ImageTk, Image
import pymysql

conn=pymysql.connect(host="localhost",user="root",password="root",db="bank")
def cancel():
    top.destroy()
def Valid():
    uid=t1.get()
    pwd=t2.get()
    if(uid=="abcd" and pwd=="1234"):
        messagebox.showinfo("Conformation","Ok")
    else:
        messagebox.showinfo("Conformation","Invalid User id/Password")
        t1.delete(0,15)
        t2.delete(0,15)
        t1.focus()
        
top=Tk()
top.title("Admin Ligin")
top.geometry("900x500+300+150")
top.configure(bg="white")
#Create a canvas
canvas= Canvas(top, width=700, height= 475)
canvas.pack()

#Load an image in the script
img= (Image.open("logo.jpg"))

#Resize the Image using resize method
resized_image= img.resize((305,150))
new_image= ImageTk.PhotoImage(resized_image)

#Add image to the Canvas Items
canvas.create_image(180,25, anchor=NW, image=new_image)


l1=Label(top,text="Admin LogIn",font=("Times New Roman Bold",25),fg="white",bg="blue")
l1.place(x=350,y=225)
l2=Label(top,text="User ID",font=("Arial Bold",15),fg="white",bg="blue")
l2.place(x=275,y=300)

l3=Label(top,text="Password",font=("Arial Bold",15),fg="white",bg="blue")
l3.place(x=275,y=350)
t1=Entry(top,width=20)
t1.place(x=450,y=300)
t2=Entry(top,width=20)
t2.place(x=450,y=350)
b1=Button(top,text="Submit",width=17,bg="black",fg="white",command=Valid)
b1.place(x=275,y=420)
b2=Button(top,text="Cancel",width=17,bg="black",fg="white",command=cancel)
b2.place(x=450,y=420)
t1.focus()
top.mainloop()

