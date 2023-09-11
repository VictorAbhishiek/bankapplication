from tkinter import*
from tkinter import messagebox
from PIL import ImageTk, Image
import pymysql
import pyodbc

#conn=pyodbc.connect('Driver={SQL Server};'
#                   'Server=DESKTOP-A8AB9RO\SQLEXPRESS;'
#                   'Database=bankapp;'
#                   'Trusted-dbo.holder;')

conn=pymysql.connect(host="localhost",user="root",password="root",db="bank")
def main_form():
    def form3_del():
        form3.destroy()


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

    def find():
        try:
            cur= conn.cursor()
            n=t1.get()
            cur.execute("select * from holder where ACNo=" + n)
            r=cur.fetchall()
            #t1.insert(0,r[0][0])
            t2.insert(0,r[0][1])
            t3.insert(0,r[0][2])
            t4.insert(0,r[0][3])
            t5.insert(0,r[0][4])
            t6.insert(0,r[0][5])
            t7.insert(0,r[0][6])
            t8.insert(0,r[0][7])
            t9.insert(0,r[0][8])
            t10.insert(0,r[0][9])
        except Exception as err:
            messagebox.showinfo("Error","Number Not Found ")
        finally :
            cur.close()
            


    form3=Tk()
    form3.title("Account Details")
    form3.geometry("700x760+400+25")
    form3.configure(bg="white")
    #Create a canvas
    canvas= Canvas(form3, width=600, height= 735)
    canvas.pack()

    #Load an image in the script
    #img= (Image.open("sbitext.jpg"))

    #Resize the Image using resize method
    #resized_image= img.resize((380,90))
    #new_image= ImageTk.PhotoImage(resized_image)

    #Add image to the Canvas Items
    #canvas.create_image(115,5, anchor=NW, image=new_image)

    l1=Label(form3,text="ENTER A/C NUMBER",font=("Arial Bold",15),fg="white",bg="blue")
    l1.place(x=75,y=125)
    l2=Label(form3,text="NAME OF A/C HOLDER",font=("Arial Bold",15),fg="white",bg="blue")
    l2.place(x=75,y=225)
    l3=Label(form3,text="DOB",font=("Arial Bold",15),fg="white",bg="blue")
    l3.place(x=75,y=275)
    l4=Label(form3,text="FATHER's NAME",font=("Arial Bold",15),fg="white",bg="blue")
    l4.place(x=75,y=325)
    l5=Label(form3,text="MOBILE NO",font=("Arial Bold",15),fg="white",bg="blue")
    l5.place(x=75,y=375)
    l6=Label(form3,text="ADDRESS",font=("Arial Bold",15),fg="white",bg="blue")
    l6.place(x=75,y=425)
    l7=Label(form3,text="AADHAR NO",font=("Arial Bold",15),fg="white",bg="blue")
    l7.place(x=75,y=475)
    l8=Label(form3,text="PAN",font=("Arial Bold",15),fg="white",bg="blue")
    l8.place(x=75,y=525)
    l9=Label(form3,text="OCCUPATION",font=("Arial Bold",15),fg="white",bg="blue")
    l9.place(x=75,y=575)
    l10=Label(form3,text="BALANCE",font=("Arial Bold",15),fg="white",bg="blue")
    l10.place(x=75,y=625)
    l11=Label(form3,text="ACCOUNT DETAILS",font=("Times New Roman",25),fg="white",bg="blue")
    l11.place(x=195,y=40)
    t1=Entry(form3,width=20,font=15)
    t1.place(x=400,y=125)
    t2=Entry(form3,width=20,font=15)
    t2.place(x=400,y=225)
    t3=Entry(form3,width=20,font=15)
    t3.place(x=400,y=275)
    t4=Entry(form3,width=20,font=15)
    t4.place(x=400,y=325)
    t5=Entry(form3,width=20,font=15)
    t5.place(x=400,y=375)
    t6=Entry(form3,width=20,font=15)
    t6.place(x=400,y=425)
    t7=Entry(form3,width=20,font=15)
    t7.place(x=400,y=475)
    t8=Entry(form3,width=20,font=15)
    t8.place(x=400,y=525)
    t9=Entry(form3,width=20,font=15)
    t9.place(x=400,y=575)
    t10=Entry(form3,width=20,font=15)
    t10.place(x=400,y=625)
    b1=Button(form3,text="SHOW DETAILS",width=18,bg="black",fg="white",height=1,font=("Arial Bold",9),activebackground="white",command=find)
    b1.place(x=280,y=175)
    b2=Button(form3,text="NEW",width=18,bg="black",fg="white",height=1,font=("Arial Bold",9),activebackground="white",command=new)
    b2.place(x=180,y=680)
    b3=Button(form3,text="BACK",width=18,bg="black",fg="white",height=1,font=("Arial Bold",9),activebackground="white",command=form3_del)
    b3.place(x=400,y=680)

    t1.focus()
    form3.mainloop()
main_form()





