from tkinter import *
from tkinter import messagebox
import mysql.connector
import tkinter.font as font

mycon=mysql.connector.connect(host="localhost",user="root",password="",database="stdform")
cur=mycon.cursor()

window = Tk()
window.geometry("800x550")
window.configure(bg="#49A")
myFont=font.Font(family="Helvetica",weight="bold")


def register():
    dbid=""
    id=e1.get()
    select="select StudentID from detail where StudentID='%s'"%(id)
    cur.execute(select)
    result=cur.fetchall()
    for i in result:
        dbid=i[0]
    if(int(id)==dbid):
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
            e1.delete("0",END)
            e2.delete("0",END)
            e3.delete("0",END)
            e4.delete("0",END)
            e5.delete("0",END)
            e6.delete("0",END)
            e7.delete("0",END)
            e8.delete("0",END)
        else:
            messagebox.askokcancel("Information","Some feilds left blank")

def show_rec():
    dbid=""
    id=e1.get()
    select="select StudentID from detail where StudentID='%s'"%(id)
    cur.execute(select)
    result=cur.fetchall()
    for i in result:
        dbid=i[0]
        print(dbid)
    select1="SELECT StudentID,StudentName,HomeAddress,ContactNumber,SubjectTakencode,SubjectTaken,ParentName,ParentContact FROM detail WHERE StudentID='%s'"%(id)
    cur.execute(select1)
    result1=cur.fetchall()
    StudentName=""
    HomeAddress=""
    ContactNumber=""
    SubjectTakencode=""
    SubjectTaken=""
    ParentName=""
    ParentContact=""
    if(int(id)==dbid):
        for i in result1:
            StudentName=i[1]
            HomeAddress=i[2]
            ContactNumber=i[3]
            SubjectTakencode=i[4]
            SubjectTaken=i[5]
            ParentName=i[6]
            ParentContact=i[7]
        e2.insert(0, StudentName)
        e3.insert(0,HomeAddress)
        e4.insert(0,ContactNumber)
        e5.insert(0,SubjectTakencode)
        e6.insert(0,SubjectTaken)
        e7.insert(0,ParentName)
        e8.insert(0,ParentContact)
    
def update_rec():
        id=e1.get()
        StudentName=e2.get()
        HomeAddress=e3.get()
        ContactNumber=e4.get()
        SubjectTakencode=e5.get()
        SubjectTaken=e6.get()
        ParentName=e7.get()
        ParentContact=e8.get()
        update="update detail set StudentName='%s',HomeAddress='%s',ContactNumber='%s',SubjectTakencode='%s',SubjectTaken='%s',ParentName='%s',ParentContact='%s' where StudentID='%s'"%(StudentName,HomeAddress,ContactNumber,SubjectTakencode,SubjectTaken,ParentName,ParentContact,id)
        cur.execute(update)
        mycon.commit()
        messagebox.askokcancel("Update","Record succesfully updated")

def clear_rec():
        e1.delete("0",END)
        e2.delete("0",END)
        e3.delete("0",END)
        e4.delete("0",END)
        e5.delete("0",END)
        e6.delete("0",END)
        e7.delete("0",END)
        e8.delete("0",END)

def Delete_rec():
    StudentID=e1.get()
    delete="delete from detail where StudentID='%s'"%(StudentID)
    cur.execute(delete)
    mycon.commit()
    messagebox.showinfo("Information","Record deleted")
    e1.delete("0",END)
    e2.delete("0",END)
    e3.delete("0",END)
    e4.delete("0",END)
    e5.delete("0",END)
    e6.delete("0",END)
    e7.delete("0",END)
    e8.delete("0",END)


label1 = Label(window,text="NEW STUDENT REGISTRATION",bg="#49A")
label1["font"]=myFont
label1.place(x=310,y=30)
label2=Label(window,text="Student ID",bg="#49A").place(x=20,y=70)
e1=Entry(window)
e1.place(x=210,y=70)
label3=Label(window,text="Student Name",bg="#49A").place(x=20,y=110)
e2=Entry(window)
e2.place(x=210,y=110)
label4=Label(window,text="Home Address",bg="#49A").place(x=20,y=140)
e3=Entry(window)
e3.place(x=210,y=140)
label5=Label(window,text="Contact Number",bg="#49A").place(x=20,y=170)
e4=Entry(window)
e4.place(x=210,y=170)
label6=Label(window,text="Subject Taken(Code)",bg="#49A").place(x=20,y=200)
e5=Entry(window)
e5.place(x=210,y=200)
label7=Label(window,text="Subject Taken(Name)",bg="#49A").place(x=20,y=240)
e6=Entry(window)
e6.place(x=210,y=240)
label8=Label(window,text="Parent Name",bg="#49A").place(x=20,y=270)
e7=Entry(window)
e7.place(x=210,y=270)
label9=Label(window,text="Parent Contact",bg="#49A").place(x=20,y=300)
e8=Entry(window)
e8.place(x=210,y=300)

button1=Button(window,text="ADD",command=register,height=1,width=7)
button1.place(x=380,y=70)
label10=Label(window,text="( Click ADD button to confirm your REGISTRATION. )",bg="#49A").place(x=440,y=70)
button2=Button(window,text="SHOW",command=show_rec,height=1,width=7).place(x=380,y=120)
label11=Label(window,text="( Enter your registred StudentID-\n- then click SHOW button to view your information. )",bg="#49A").place(x=440,y=110)
button3=Button(window,text="UPDATE",command=update_rec,height=1,width=7).place(x=380,y=180)
label12=Label(window,text="( Modify some information-\n-then click UPDATE button to update your information. )",bg="#49A").place(x=440,y=170)
button4=Button(window,text="CLEAR",command=clear_rec,height=1,width=7).place(x=380,y=240)
label13=Label(window,text="( Click CLEAR button to clear your information .)\n Note: It dose not delete your information.",bg="#49A").place(x=440,y=240)
button5=Button(window,text="DELETE",command=Delete_rec,height=1,width=7).place(x=380,y=310)
label14=Label(window,text="( Click DELETE button to delete your information.)",bg="#49A").place(x=440,y=310)

label15=Label(window,text="Instruction:")
label15["font"]=myFont
label16=Label(window,text="1. Please fill all the above information. If you miss some information. REGISTRATION must bring error. ",bg="#49A").place(x=50,y=380)
label17=Label(window,text="2. IF you are already registred person, enter your StudentID then click SHOW button to view your information.",bg="#49A").place(x=50,y=400)
label18=Label(window,text="3. Incase you gived some wrong information don't panic, view your information then modify it after click UPDATE button\n your information will be updated. ",bg="#49A").place(x=50,y=420)
label15.place(x=30,y=350)
window.mainloop()
