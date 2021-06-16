from tkinter import *

app=Tk()
app.geometry("550x500")

# Elerticity bill calculator
def calc():
	unit=int(input("Enter the unit: "))
	bill=0

	if (unit<=100):
		print("Below 100 unit,there is no charge")
	elif (unit>=0 and unit<=200):
		fixedprice=20
		bill=(100*0)+((unit-100)*1.5)+fixedprice
		print(bill)
	elif (unit>=0 and unit<=500):
		fixedprice=30
		bill=(100*0)+(100*2)+((unit-200)*3)+fixedprice
		print(bill)
	else:
		fixedprice=50
		bill=(100*0)+(100*3.5)+(300*4.6)+((unit-200)*6.6)+fixedprice
		print(bill)

label1=Label(app,text="Elerticity Bill Calculator")
label1.place(x=,y=)

app.mainloop()
