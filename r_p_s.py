from tkinter import *
import random

main = Tk()
main.geometry("800x450")

yscore=[]
Cscore=[]

def rock():
	label4.configure(text="Your Selected:Rock")
	option=["Rock","Paper","Scissor"]
	cc=random.choice(option)
	label6.configure(text="Computer Selected:"+cc)
	if(cc=="Rock"):
		yscore.append(0)
		Cscore.append(0)
	elif(cc=="Paper"):
		yscore.append(0)
		Cscore.append(1)
	else:
		yscore.append(1)
		Cscore.append(0)
	label5.configure(text="Your Score:"+str(sum(yscore)))
	label7.configure(text="Computer Score:"+str(sum(Cscore)))

def paper():
	label4.configure(text="Your Selected:Paper")
	option=["Rock","Paper","Scissor"]
	cc=random.choice(option)
	label6.configure(text="Computer Selected:"+cc)
	if(cc=="Paper"):
		yscore.append(0)
		Cscore.append(0)
	elif(cc=="Scissor"):
		yscore.append(0)
		Cscore.append(1)
	else:
		yscore.append(1)
		Cscore.append(0)
	label5.configure(text="Your Score:"+str(sum(yscore)))
	label7.configure(text="Computer Score:"+str(sum(Cscore)))

def scissor():
	label4.configure(text="Your Selected:Scissor")
	option=["Rock","Paper","Scissor"]
	cc=random.choice(option)
	label6.configure(text="Computer Selected:"+cc)
	if(cc=="Scissor"):
		yscore.append(0)
		Cscore.append(0)
	elif(cc=="Rock"):
		yscore.append(0)
		Cscore.append(1)
	else:
		yscore.append(1)
		Cscore.append(0)
	label5.configure(text="Your Score:"+str(sum(yscore)))
	label7.configure(text="Computer Score:"+str(sum(Cscore)))

label1=Label(text="Rock Paper Scissor",fg="blue",font=("arial",30))
label1.place(x=240,y=20)
label8=Label(text="Let's Start The Game...",fg="green",font=("arial",14,"bold"))
label8.place(x=300,y=80)
label2=Label(text="Your option",fg="gray",font=("arial",15))
label2.place(x=80,y=100)
label3=Label(text="Score",fg="gray",font=("arial",15))
label3.place(x=100,y=230)

button1=Button(text="Rock",height=2,width=15,bg="pink",font=("arial",10,"bold"),command=rock)
button1.place(x=200,y=150)
button2=Button(text="Paper",height=2,width=15,bg="skyblue",font=("arial",10,"bold"),command=paper)
button2.place(x=400,y=150)
button3=Button(text="Scissor",height=2,width=15,bg="gray",font=("arial",10,"bold"),command=scissor)
button3.place(x=600,y=150)

label4=Label(text="Your Selected:---",font=("arial",13))
label4.place(x=200,y=260)
label5=Label(text="Your Score:-",font=("arial",13))
label5.place(x=410,y=260)
label6=Label(text="Computer Selected:---",font=("arial",13))
label6.place(x=180,y=320)
label7=Label(text="Computer Score:-",font=("arial",13))
label7.place(x=410,y=320)

main.mainloop()