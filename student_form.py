from tkinter import *
from tkinter import messagebox
import mysql.connector

mycon=mysql.connector.connect(host="localhost",user="root",password="",database="stdform")
cur=mycon.cursor()

window = Tk()
window.geometry("600x350")

e1=StringVar()
e2=StringVar()
e3=StringVar()
e4=StringVar()
e5=StringVar()
e6=StringVar()
e7=StringVar()
e8=StringVar()
def register():
    dbid=""
    StudentID=e1.get()
    select="select StudentID from detail where StudentID='%s'"%(StudentID)
    cur.execute(select)
    result=cur.fetchall()
    for i in result:
        dbid=i[0]
    if(StudentID==dbid):
        messagebox.askokcancel("Information","record Already exists")
    else:
        Insert=" Insert into detail(StudentID,StudentName,HomeAddress,ContactNumber,SubjectTakencode,SubjectTaken,ParentName,ParentContact) values(%s,%s,%s,%s,%s,%s,%s,%s)"
        StudentName=e2.get()
        HomeAddress=e3.get()
        ContactNumber=e4.get()
        SubjectTakencode=e5.get()
        SubjectTaken=e6.get()
        ParentName=e7.get()
        ParentContact=e8.get()

        if(StudentName!="" and HomeAddress!="" and ContactNumber!="" and SubjectTakencode!="" and SubjectTaken!="" and ParentName!="" and ParentContact!=""):
            values=(id,StudentName,HomeAddress,ContactNumber,SubjectTakencode,SubjectTaken,ParentName,ParentContact)
            cur.execute(Insert,values)
            mycon.commit()
            messagebox.askokcancel("Information","Record inserted")
            e1.set("")
            e2.set("")
            e3.set("")
            e4.set("")
            e5.set("")
            e6.set("")
            e7.set("")
            e8.set("")
        else:
            messagebox.askokcancel("Information","Some feilds left blank")
            
    
'''
def check():
    id=e1.get()
    num=e4.get()
    
    code=e6.get()
    if id.isdigit():
        if len(id)==0:
            messagebox.showinfo("info","Please Fill Student ID")
            #print("Fill all the Information")
        if len(e2.get())==0:
            messagebox.showinfo("info","Please Fill Student Name")
        if len(e3.get())==0:
            messagebox.showinfo("Info","Please Fill Address")
        if num.isdigit():
            pass
        else:
            messagebox.showerror("Error","only give your 10 digit number")
        if code.isdigit():
            pass
        else:
            messagebox.showerror("Error","Code contain both letters and numbers")
        if len(e7.get())==0:
            messagebox.showinfo("Info","Please Parent Name")
        if len(e8.get())==0:
            messagebox.showinfo("Info","Please parent contact")
    else:
        messagebox.showerror("Error","Student ID contain only digit")
        
    #if len(e2.get())==0:
     #   messagebox.showinfo("info","Please Fill Student Name")
'''
label1 = Label(window,text="NEW STUDENT REGISTRATION").place(x=200,y=5)
label2=Label(window,text="Student ID").place(x=20,y=50)
entry1=Entry(window,textvariable=e1).place(x=210,y=50)
label3=Label(window,text="Student Name").place(x=20,y=80)
entry2=Entry(window,textvariable=e2).place(x=210,y=80)
label4=Label(window,text="Home Address").place(x=20,y=110)
entry3=Entry(window,textvariable=e3).place(x=210,y=110)
label5=Label(window,text="Contact Number").place(x=20,y=140)
entry4=Entry(window,textvariable=e4).place(x=210,y=140)
label6=Label(window,text="Subject Taken(Code)").place(x=20,y=170)
entry5=Entry(window,textvariable=e5).place(x=210,y=170)
label7=Label(window,text="Subject Taken(Name)").place(x=20,y=200)
entry6=Entry(window,textvariable=e6).place(x=210,y=200)
label8=Label(window,text="Parent Name").place(x=20,y=230)
entry7=Entry(window,textvariable=e7).place(x=210,y=230)
label9=Label(window,text="Parent Contact").place(x=20,y=260)
entry8=Entry(window,textvariable=e8).place(x=210,y=260)
button1=Button(window,text="BACK",).place(x=20,y=300)
button2=Button(window,text="ADDNEW",command=register).place(x=100,y=300)

window.mainloop()
