from tkinter import*
from tkinter import messagebox
from PIL import ImageTk, Image
#import pyodbc
import pymysql

#conn=pyodbc.connect('Driver={SQL Server};'
#                   'Server=DESKTOP-A8AB9RO\SQLEXPRESS;'
#                   'Database=bank;'
#                   'Trusted-dbo.holder;')
conn=pymysql.connect(host="localhost",user="root",password="root",db="bank")
def main_form():
    def form4_del():
        form4.destroy()
    def new():
        t1.delete(0,'end')
        t2.delete(0,'end')
        t3.delete(0,'end')
        t4.delete(0,'end')
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
            t4.insert(0,r[0][9])

        except Exception as err:
            messagebox.showinfo("Error","Number Not Found ")
        finally :
            cur.close()




    form4=Tk()
    form4.title("Account Balance")
    form4.geometry("900x600+300+100")
    form4.configure(bg="white")
    #Create a canvas
    canvas= Canvas(form4, width=850, height= 550)
    canvas.pack()

    #Load an image in the script
    img= (Image.open("balance.jpg"))

    #Resize the Image using resize method
    #resized_image= img.resize((250,200))
    #new_image= ImageTk.PhotoImage(resized_image)

    #Add image to the Canvas Items
    #canvas.create_image(225,25, anchor=NW, image=new_image)


    l1=Label(form4,text="Account Balance",font=("Times New Roman Bold",25),fg="white",bg="blue")
    l1.place(x=520,y=75)
    l2=Label(form4,text="Account Number",font=("Arial Bold",15),fg="white",bg="blue")
    l2.place(x=475,y=200)
    l3=Label(form4,text="Holder Name",font=("Arial Bold",15),fg="white",bg="blue")
    l3.place(x=475,y=250)
    l4=Label(form4,text="Date of Birth",font=("Arial Bold",15),fg="white",bg="blue")
    l4.place(x=475,y=300)
    l5=Label(form4,text="A/C Balance",font=("Arial Bold",15),fg="white",bg="blue")
    l5.place(x=475,y=350)
    
    t1=Entry(form4,width=12,font=("Arial Bold",15))
    t1.place(x=680,y=200)
    t2=Entry(form4,width=12,font=("Arial Bold",15))
    t2.place(x=680,y=250)
    t3=Entry(form4,width=12,font=("Arial Bold",15))
    t3.place(x=680,y=300)
    t4=Entry(form4,width=12,font=("Arial Bold",15))
    t4.place(x=680,y=350)
    
    b1=Button(form4,text="BALANCE",width=12,bg="black",fg="white",font=("Arial Bold",8),command=find)
    b1.place(x=475,y=450)
    b2=Button(form4,text="NEW",width=12,bg="black",fg="white",font=("Arial Bold",8),command=new)
    b2.place(x=600,y=450)
    b3=Button(form4,text="BACK",width=12,bg="black",fg="white",font=("Arial Bold",8),command=form4_del)
    b3.place(x=730,y=450)
    t1.focus()
    form4.mainloop()
main_form()
