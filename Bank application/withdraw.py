from tkinter import*
from tkinter import messagebox
from PIL import ImageTk, Image
import pymysql
#import pyodbc

#conn=pyodbc.connect('Driver={SQL Server};'
#                   'Server=DESKTOP-A8AB9RO\SQLEXPRESS;'
#                   'Database=bankapp;'
#                   'Trusted-dbo.holder;')


conn=pymysql.connect(host="localhost",user="root",password="root",db="bank")


def main_form():
    
    def form7_del():
        form7.destroy()
        
    def new():
        t1.delete(0,'end')
        t2.delete(0,'end')
        t3.delete(0,'end')
        t4.delete(0,'end')
        t1.focus()
        
    def FindDetails():
        try:
            cur= conn.cursor()
            n=t1.get()
            cur.execute("select * from holder where ACNo=" + n)
            r=cur.fetchall()
            t2.insert(0,r[0][1])
            t3.insert(0,r[0][2])
        except Exception as err:
            messagebox.showinfo("Error","Number Not Found ")
        finally :
            cur.close()
        

        
    def withdraw():
        
        cur= conn.cursor()
        cur.execute("select * from holder where ACNo='" + t1.get() + "'")
        r=cur.fetchall()
        r[0][0]
        r[0][9]
        ACB=float(r[0][9])
        Amount= float(t4.get())
        
        if (Amount > ACB):
            messagebox.showinfo("conf","Insufficient Balance")
        
        else:
            ACB=ACB-Amount
            cur1=conn.cursor()
            ACB = str(ACB)
            
            cur1.execute("update holder set ACBalance='" + ACB + "' where ACNo ='" + t1.get() + "'")
            conn.commit()
            messagebox.showinfo("conf","Credited Successfully ")
            
            



    form7=Tk()
    form7.title("Withdraw")
    form7.geometry("900x600+300+100")
    form7.configure(bg="white")
    #Create a canvas
    canvas= Canvas(form7, width=850, height= 550)
    canvas.pack()

    #Load an image in the script
    img= (Image.open("withdraw.png"))

    #Resize the Image using resize method
    #resized_image= img.resize((250,225))
    #new_image= ImageTk.PhotoImage(resized_image)

    #Add image to the Canvas Items
    #canvas.create_image(225,5, anchor=NW, image=new_image)


    l1=Label(form7,text="Withdraw Amount",font=("Times New Roman Bold",30),fg="white",bg="blue")
    l1.place(x=485,y=75)
    l2=Label(form7,text="Account Number",font=("Arial Bold",15),fg="white",bg="blue")
    l2.place(x=475,y=200)
    l3=Label(form7,text="Holder Name",font=("Arial Bold",15),fg="white",bg="blue")
    l3.place(x=475,y=300)
    l4=Label(form7,text="Date of Birth",font=("Arial Bold",15),fg="white",bg="blue")
    l4.place(x=475,y=350)
    l5=Label(form7,text="Enter Amount",font=("Arial Bold",15),fg="white",bg="blue")
    l5.place(x=475,y=425)


    t1=Entry(form7,width=13,font=("Arial Bold",15))
    t1.place(x=680,y=200)
    t2=Entry(form7,width=13,font=("Arial Bold",15))
    t2.place(x=680,y=300)
    t3=Entry(form7,width=13,font=("Arial Bold",15))
    t3.place(x=680,y=350)
    t4=Entry(form7,width=13,font=("Arial Bold",15))
    t4.place(x=680,y=425)

    b1=Button(form7,text="SHOW DETAILS",width=13,bg="black",fg="white",font=("Arial Bold",8),command=FindDetails)
    b1.place(x=600,y=250)
    b2=Button(form7,text="CREDIT",width=12,bg="black",fg="white",font=("Arial Bold",8),command=withdraw)
    b2.place(x=475,y=500)
    b3=Button(form7,text="NEW",width=12,bg="black",fg="white",font=("Arial Bold",8),command=new)
    b3.place(x=600,y=500)
    b4=Button(form7,text="BACK",width=12,bg="black",fg="white",font=("Arial Bold",8),command=form7_del)
    b4.place(x=730,y=500)


    t1.focus()
    form7.mainloop()
main_form()
