from tkinter import*
from tkinter import messagebox
from PIL import ImageTk, Image
import pymysql
import pyodbc

#conn=pyodbc.connect('Driver={SQL Server};'
#                    'Server=DESKTOP-A8AB9RO\SQLEXPRESS;'
#                    'Database=bankapp;'
#                    'Trusted-dbo.holder;')

conn=pymysql.connect(host="localhost",user="root",password="root",db="bank")
def main_form():
    
    def form8_del():
        form8.destroy()
        
    def new():
        t1.delete(0,'end')
        t2.delete(0,'end')
        t3.delete(0,'end')
        t4.delete(0,'end')
        t1.focus()
        
    def ACDetails():
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
            
    def Deposit():
        cur= conn.cursor()
        cur.execute("select * from holder where ACNo='" + t1.get() + "'")
        r=cur.fetchall()
        r[0][0]
        r[0][9]
        ACB=float(r[0][9])
        Amount= float(t4.get())
        
        
        
        
        ACB=ACB+Amount
        cur1=conn.cursor()
        ACB = str(ACB)
            
        cur1.execute("update holder set ACBalance='" + ACB + "' where ACNo ='" + t1.get() + "'")
        conn.commit()
        messagebox.showinfo("conf","Debited Successfully ")
        

        
    
            
            



    form8=Tk()
    form8.title("Deposit")
    form8.geometry("900x600+300+100")
    form8.configure(bg="white")
    #Create a canvas
    canvas= Canvas(form8, width=850, height= 550)
    canvas.pack()

    #Load an image in the script
    #img= (Image.open("withdraw.png"))

    #Resize the Image using resize method
    #resized_image= img.resize((250,225))
    #new_image= ImageTk.PhotoImage(resized_image)

    #Add image to the Canvas Items
    #canvas.create_image(225,5, anchor=NW, image=new_image)


    l1=Label(form8,text="Deposit Amount",font=("Times New Roman Bold",30),fg="white",bg="blue")
    l1.place(x=510,y=75)
    l2=Label(form8,text="Account Number",font=("Arial Bold",15),fg="white",bg="blue")
    l2.place(x=478,y=200)
    l3=Label(form8,text="Holder Name",font=("Arial Bold",15),fg="white",bg="blue")
    l3.place(x=478,y=300)
    l4=Label(form8,text="Date of Birth",font=("Arial Bold",15),fg="white",bg="blue")
    l4.place(x=475,y=350)
    l5=Label(form8,text="Enter Amount",font=("Arial Bold",15),fg="white",bg="blue")
    l5.place(x=475,y=425)


    t1=Entry(form8,width=13,font=("Arial Bold",15))
    t1.place(x=680,y=200)
    t2=Entry(form8,width=13,font=("Arial Bold",15))
    t2.place(x=680,y=300)
    t3=Entry(form8,width=13,font=("Arial Bold",15))
    t3.place(x=680,y=350)
    t4=Entry(form8,width=13,font=("Arial Bold",15))
    t4.place(x=680,y=425)

    b1=Button(form8,text="SHOW DETAILS",width=13,bg="black",fg="white",font=("Arial Bold",8),command=ACDetails)
    b1.place(x=600,y=250)
    b2=Button(form8,text="DEBIT",width=12,bg="black",fg="white",font=("Arial Bold",8),command=Deposit)
    b2.place(x=475,y=500)
    b3=Button(form8,text="NEW",width=12,bg="black",fg="white",font=("Arial Bold",8),command=new)
    b3.place(x=600,y=500)
    b4=Button(form8,text="BACK",width=12,bg="black",fg="white",font=("Arial Bold",8),command=form8_del)
    b4.place(x=730,y=500)


    t1.focus()
    form8.mainloop()
main_form()
