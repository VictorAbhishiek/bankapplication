from tkinter import*
from tkinter import messagebox
from PIL import ImageTk, Image
#import pyodbc
import pymysql
#conn=pyodbc.connect('Driver={SQL Server};'
#                   'Server=DESKTOP-A8AB9RO\SQLEXPRESS;'
#                    'Database=bank;'
#                    'Trusted-dbo.holder;')

conn=pymysql.connect(host="localhost",user="root",password="root",db="bank")
def main_form():
    def form6_del():
        form6.destroy()

    def FindDetails():
        try:
            cur= conn.cursor()
            n=t1.get()
            cur.execute("select * from holder where ACNo=" + n)
            r=cur.fetchall()
            #t1.insert(0,r[0][0])
            t2.insert(0,r[0][1])
            t3.insert(0,r[0][2])
        except Exception as err:
            messagebox.showinfo("Error","Number Not Found ")
        finally :
            cur.close()
    

    
    def delete():
        
        cur= conn.cursor()
        cur.execute("delete from holder where ACNo='" + t1.get() + "'")
        #cur.execute("delete from holder where DateOfBirth='" + t2.get() + "'")
        conn.commit()
        messagebox.showinfo("Conf","Deleted")
        
    form6=Tk()
    form6.title("Account close")
    form6.geometry("900x600+300+100")
    form6.configure(bg="white")
    
    #Create a canvas
    canvas= Canvas(form6, width=850, height= 550)
    canvas.pack()

    #Load an image in the script
    img1= (Image.open("close.png"))

    #Resize the Image using resize method
    resized_image1= img1.resize((300,275))
    new_image1= ImageTk.PhotoImage(resized_image1)

    #Add image to the Canvas Items
    canvas.create_image(75,75, anchor=NW, image=new_image1)


    #frame=Frame(form6, width=850,height=550)
    #frame.pack()
    #frame.place(anchor=NW, relx=0.5, rely=0.5)
    #img1= (Image.open("close.png"))

    #Resize the Image using resize method
    #resized_image1= img1.resize((300,275))
    #new_image1= ImageTk.PhotoImage(resized_image1)

    #label=Label(frame,image=new_image1)
    
    



    l1=Label(form6,text="Account Close",font=("Times New Roman Bold",30),fg="white",bg="blue")
    l1.place(x=485,y=75)
    l2=Label(form6,text="Account Number",font=("Arial Bold",15),fg="white",bg="blue")
    l2.place(x=450,y=200)
    l3=Label(form6,text="Holder Name",font=("Arial Bold",15),fg="white",bg="blue")
    l3.place(x=450,y=300)
    l4=Label(form6,text="Date of Birth",font=("Arial Bold",15),fg="white",bg="blue")
    l4.place(x=450,y=350)


    t1=Entry(form6,width=12,font=("Arial Bold",15))
    t1.place(x=630,y=200)
    t2=Entry(form6,width=12,font=("Arial Bold",15))
    t2.place(x=630,y=300)
    t3=Entry(form6,width=12,font=("Arial Bold",15))
    t3.place(x=630,y=350)

    b1=Button(form6,text="CLOSE A/C",width=17,bg="black",fg="white",font=("Arial Bold",8),command=delete)
    b1.place(x=450,y=400)
    b2=Button(form6,text="BACK",width=17,bg="black",fg="white",font=("Arial Bold",8),command=form6_del)
    b2.place(x=630,y=400)
    b3=Button(form6,text="SHOW DETAILS",width=17,bg="black",fg="white",font=("Arial Bold",8),command=FindDetails)
    b3.place(x=550,y=250)

    t1.focus()
    form6.mainloop()
main_form()
