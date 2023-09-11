from tkinter import*
from tkinter import messagebox
from PIL import ImageTk, Image
import pyodbc
import pymysql

#conn=pyodbc.connect('Driver={SQL Server};'
#                    'Server=DESKTOP-A8AB9RO\SQLEXPRESS;'
#                    'Database=bank;'
#                    'Trusted-dbo.holder;')

conn=pymysql.connect(host="localhost",user="root",password="root",db="bank")
def main_form():
    def form5_del():
        form5.destroy()
    #def change():
        #cur= conn.cursor()
        #cur2= conn.cursor()
        #cur3= conn.cursor()
        #cur4= conn.cursor()
        #cur5= conn.cursor()
        #cur6= conn.cursor()
        #cur7= conn.cursor()
        #cur8= conn.cursor()
        #cur9= conn.cursor()
        #cur.execute("select * from holder where ACNo='" + t1.get() + "'")

        #r=cur.fetchall()
        #ACNo=r[0][0]
        #ACName=r[0][1]
        #DAteOfBirth=r[0][2]
        #FatherName=r[0][3]
        #MobileNo=r[0][4]
        #AccountAddress=r[0][5]
        #AadharNo=r[0][6]
        #Pan=r[0][7]
        #Occupation=r[0][8]
        

        
        #cur2.execute("update holder set ACName=" + r[0][1] + "where ACNo=" t2.get() )
        #cur2.execute("update holder set ACName=" + r[0][1] + " where ACNo=" + t2.get())
        #cur3.execute("update holder set DateOfBirth=" + r[0][2] + " where ACNo=" + t2.get())
        #cur4.execute("update holder set FatherName=" + r[0][3] + " where ACNo=" + t2.get())
        #cur5.execute("update holder set MobileNo=" + r[0][4] + " where ACNo=" + t2.get())
        #cur6.execute("update holder set AccountAddress=" + r[0][5] + " where ACNo=" + t2.get())
        #cur7.execute("update holder set AadharNo=" + r[0][6] + " where ACNo=" + t2.get())
        #cur8.execute("update holder set Pan=" + r[0][7] + " where ACNo=" + t2.get())
        #cur9.execute("update holder set Occupation=" + r[0][8] + " where ACNo=" + t2.get())
        
        #conn.commit()
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
        t1.focus()
    def edit1(): 
        cur= conn.cursor()
        cur.execute("update holder set ACName='" + t2.get() + "' where ACNo='" + t1.get() + "'")
        conn.commit()
        messagebox.showinfo("Conf","Updated")
    def edit2(): 
        cur= conn.cursor()
        cur.execute("update holder set DateOfBirth='" + t3.get() + "' where ACNo='" + t1.get() + "'")
        conn.commit()
        messagebox.showinfo("Conf","Updated")
    def edit3(): 
        cur= conn.cursor()
        cur.execute("update holder set FatherName='" + t4.get() + "' where ACNo='" + t1.get() + "'")
        conn.commit()
        messagebox.showinfo("Conf","Updated")
    def edit4(): 
        cur= conn.cursor()
        cur.execute("update holder set MobileNo='" + t5.get() + "' where ACNo='" + t1.get() + "'")
        conn.commit()
        messagebox.showinfo("Conf","Updated")
    def edit5(): 
        cur= conn.cursor()
        cur.execute("update holder set AccountAddress='" + t6.get() + "' where ACNo='" + t1.get() + "'")
        conn.commit()
        messagebox.showinfo("Conf","Updated")
    def edit6(): 
        cur= conn.cursor()
        cur.execute("update holder set AadharNo='" + t7.get() + "' where ACNo='" + t1.get() + "'")
        conn.commit()
        messagebox.showinfo("Conf","Updated")
    def edit7(): 
        cur= conn.cursor()
        cur.execute("update holder set Pan='" + t8.get() + "' where ACNo='" + t1.get() + "'")
        conn.commit()
        messagebox.showinfo("Conf","Updated")
    def edit8(): 
        cur= conn.cursor()
        cur.execute("update holder set Occupation='" + t9.get() + "' where ACNo='" + t1.get() + "'")
        conn.commit()
        messagebox.showinfo("Conf","Updated")
    def cancel():
        form5.destroy()
        
    form5=Tk()
    form5.title("Edit Form")
    form5.geometry("700x750+400+25")
    form5.configure(bg="white")
    #Create a canvas
    canvas= Canvas(form5, width=600, height= 735)
    canvas.pack()

    #Load an image in the script
    #img= (Image.open("sbitext.jpg"))

    #Resize the Image using resize method
    #resized_image= img.resize((380,90))
    #new_image= ImageTk.PhotoImage(resized_image)

    #Add image to the Canvas Items
    #canvas.create_image(115,5, anchor=NW, image=new_image)

    l1=Label(form5,text="A/C NUMBER",font=("Arial Bold",15),fg="white",bg="blue")
    l1.place(x=75,y=175)
    l2=Label(form5,text="NAME OF A/C HOLDER",font=("Arial Bold",15),fg="white",bg="blue")
    l2.place(x=75,y=225)
    l3=Label(form5,text="DOB",font=("Arial Bold",15),fg="white",bg="blue")
    l3.place(x=75,y=275)
    l4=Label(form5,text="FATHER's NAME",font=("Arial Bold",15),fg="white",bg="blue")
    l4.place(x=75,y=325)
    l5=Label(form5,text="MOBILE NO",font=("Arial Bold",15),fg="white",bg="blue")
    l5.place(x=75,y=375)
    l6=Label(form5,text="ADDRESS",font=("Arial Bold",15),fg="white",bg="blue")
    l6.place(x=75,y=425)
    l7=Label(form5,text="AADHAR NO",font=("Arial Bold",15),fg="white",bg="blue")
    l7.place(x=75,y=475)
    l8=Label(form5,text="PAN",font=("Arial Bold",15),fg="white",bg="blue")
    l8.place(x=75,y=525)
    l9=Label(form5,text="OCCUPATION",font=("Arial Bold",15),fg="white",bg="blue")
    l9.place(x=75,y=575)
    l10=Label(form5,text="EDIT ACCOUNT DETAILS",font=("Times New Roman",25),fg="white",bg="blue")
    l10.place(x=150,y=70)
    t1=Entry(form5,width=15,font=15)
    t1.place(x=340,y=175)
    t2=Entry(form5,width=15,font=15)
    t2.place(x=340,y=225)
    t3=Entry(form5,width=15,font=15)
    t3.place(x=340,y=275)
    t4=Entry(form5,width=15,font=15)
    t4.place(x=340,y=325)
    t5=Entry(form5,width=15,font=15)
    t5.place(x=340,y=375)
    t6=Entry(form5,width=15,font=15)
    t6.place(x=340,y=425)
    t7=Entry(form5,width=15,font=15)
    t7.place(x=340,y=475)
    t8=Entry(form5,width=15,font=15)
    t8.place(x=340,y=525)
    t9=Entry(form5,width=15,font=15)
    t9.place(x=340,y=575)
    
    
    b1=Button(form5,text="EDIT",width=12,bg="blue",fg="white",height=1,activebackground="white",command=edit1)
    b1.place(x=540,y=225)
    b2=Button(form5,text="EDIT",width=12,bg="blue",fg="white",height=1,activebackground="white",command=edit2)
    b2.place(x=540,y=275)
    b3=Button(form5,text="EDIT",width=12,bg="blue",fg="white",height=1,activebackground="white",command=edit3)
    b3.place(x=540,y=325)
    b4=Button(form5,text="EDIT",width=12,bg="blue",fg="white",height=1,activebackground="white",command=edit4)
    b4.place(x=540,y=375)
    b5=Button(form5,text="EDIT",width=12,bg="blue",fg="white",height=1,activebackground="white",command=edit5)
    b5.place(x=540,y=425)
    b6=Button(form5,text="EDIT",width=12,bg="blue",fg="white",height=1,activebackground="white",command=edit6)
    b6.place(x=540,y=475)
    b7=Button(form5,text="EDIT",width=12,bg="blue",fg="white",height=1,activebackground="white",command=edit7)
    b7.place(x=540,y=525)
    b8=Button(form5,text="EDIT",width=12,bg="blue",fg="white",height=1,activebackground="white",command=edit8)
    b8.place(x=540,y=575)
    b9=Button(form5,text="BACK",width=18,bg="black",fg="white",height=2,activebackground="white",command=form5_del)
    b9.place(x=350,y=640)
    b10=Button(form5,text="NEW",width=18,bg="black",fg="white",height=2,activebackground="white",command=new)
    b10.place(x=180,y=640)
    
    t1.focus()
    form5.mainloop()

main_form()




