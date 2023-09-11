from tkinter import*
from tkinter import messagebox
#from PIL import ImageTk, Image
#import pyodbc
import pymysql
#import Tkinter as tk



#conn=pyodbc.connect('Driver={SQL Server};'
#                   'Server=DESKTOP-A8AB9RO\SQLEXPRESS;'
#                   'Database=bankapp;'
#                   'Trusted-dbo.holder;')

conn=pymysql.connect(host="localhost",user="root",password="root",db="bank")
def main_form():
    def form1_del():
        form1.destroy()



    def new():
        t1.delete(0,'end')
        t2.delete(0,'end')
        t3.delete(0,'end')
        t4.delete(0,'end')
        t5.delete(0,'end')
        t6.delete(0,'end')
        t7.delete(0,'end')
        t8.delete(0,'end')
        t9.delete(0,'end')
        t10.delete(0,'end')
        t1.focus()
    def save():
        cur=conn.cursor()
        cur.execute("insert into holder values('" + t1.get() + "','" + t2.get() + "','" + t3.get() +"','" + t4.get() + "','" + t5.get() + "','" + t6.get() + "','" + t7.get() + "','" + t8.get() + "','" + t9.get() + "','" + t10.get() + "')")
        conn.commit()
        messagebox.showinfo("Conf","Saved")
        cur.close()

    
    form1=Tk()
    form1.title("Creation of New Account")
    form1.geometry("700x775+400+25")
    form1.configure(bg="white")
    #Create a canvas
    #canvas= Canvas(form1, width=600, height= 730)
    #canvas.pack()

    #Load an image in the script
    #img= (Image.open("heading.jpg"))

    #Resize the Image using resize method
    #resized_image= img.resize((450,125))
    #new_image= ImageTk.PhotoImage(resized_image)

    #Add image to the Canvas Items
    #canvas.create_image(145,5, anchor=NW, image=new_image)


    #img2= (Image.open("LOGO.png"))




    #resized__image= img2.resize((155,120))
    #new__image= ImageTk.PhotoImage(resized__image)

    #Add image to the Canvas Items
    #canvas.create_image(0,5, anchor=NW, image=new__image)

    l1=Label(form1,text="A/C NUMBER",font=("Arial Bold",15),fg="white",bg="blue")
    l1.place(x=75,y=175)
    l2=Label(form1,text="NAME OF A/C HOLDER",font=("Arial Bold",15),fg="white",bg="blue")
    l2.place(x=75,y=225)
    l3=Label(form1,text="DOB",font=("Arial Bold",15),fg="white",bg="blue")
    l3.place(x=75,y=275)
    l4=Label(form1,text="FATHER's NAME",font=("Arial Bold",15),fg="white",bg="blue")
    l4.place(x=75,y=325)
    l5=Label(form1,text="MOBILE NO",font=("Arial Bold",15),fg="white",bg="blue")
    l5.place(x=75,y=375)
    l6=Label(form1,text="ADDRESS",font=("Arial Bold",15),fg="white",bg="blue")
    l6.place(x=75,y=425)
    l7=Label(form1,text="AADHAR NO",font=("Arial Bold",15),fg="white",bg="blue")
    l7.place(x=75,y=475)
    l8=Label(form1,text="PAN",font=("Arial Bold",15),fg="white",bg="blue")
    l8.place(x=75,y=525)
    l9=Label(form1,text="OCCUPATION",font=("Arial Bold",15),fg="white",bg="blue")
    l9.place(x=75,y=575)
    l10=Label(form1,text="BALANCE",font=("Arial Bold",15),fg="white",bg="blue")
    l10.place(x=75,y=625)
    l11=Label(form1,text="ACCOUNT OPENING FORM",font=("Times New Roman",25),fg="white",bg="blue")
    l11.place(x=150,y=70)
    t1=Entry(form1,width=20,font=15)
    t1.place(x=400,y=175)
    t2=Entry(form1,width=20,font=15)
    t2.place(x=400,y=225)
    t3=Entry(form1,width=20,font=15)
    t3.place(x=400,y=275)
    t4=Entry(form1,width=20,font=15)
    t4.place(x=400,y=325)
    t5=Entry(form1,width=20,font=15)
    t5.place(x=400,y=375)
    t6=Entry(form1,width=20,font=15)
    t6.place(x=400,y=425)
    t7=Entry(form1,width=20,font=15)
    t7.place(x=400,y=475)
    t8=Entry(form1,width=20,font=15)
    t8.place(x=400,y=525)
    t9=Entry(form1,width=20,font=15)
    t9.place(x=400,y=575)
    t10=Entry(form1,width=20,font=15)
    t10.place(x=400,y=625)
    b1=Button(form1,text="Save",width=18,bg="black",fg="white",height=2,activebackground="white",command=save)
    b1.place(x=100,y=690)
    b2=Button(form1,text="Back",width=18,bg="black",fg="white",height=2,activebackground="white",command=form1_del)
    b2.place(x=450,y=690)
    b3=Button(form1,text="New",width=18,bg="black",fg="white",height=2,activebackground="white",command=new)
    b3.place(x=275,y=690)
    t1.focus()
    form1.mainloop()
main_form()





