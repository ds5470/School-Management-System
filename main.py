import os
from tkinter import*
root=Tk()
root.geometry('1200x200')
l=Label(root,text="COGNITIVE SCHOOL MANAGEMENT SYSTEM",font=("ALGERIAN", 25))
l.grid(row=0,column=1)

def addition():
    os.system('addition.py')

def modification():
    os.system('modification.py')
def deletion():
    os.system('deletion.py')
def report():
    os.system('report.py')
    
b1=Button(root,text="ADDING NEW STUDENT DETAIL",bg="black",
          fg="cyan",font=("times new roman", 18),command=addition)
b1.grid(row=1,column=0)
b2=Button(root,text="MODIFYING ANY RECORD",bg="black",
          fg="cyan",font=("times new roman", 18),command=modification)
b2.grid(row=1,column=1)
b3=Button(root,text="DELETING ANY RECORD",bg="black",
          fg="cyan",font=("times new roman", 18),command=deletion)
b3.grid(row=2,column=0)
b4=Button(root,text="REPORT",bg="black",
          fg="cyan",font=("times new roman", 18),command=report)
b4.grid(row=2,column=1)
#root.mainloop()

