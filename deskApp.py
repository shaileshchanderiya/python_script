
from tkinter import *
#import sqlitedb
from sqlitedb import  Database

database=Database("Book-Database.db")

def get_selected(event):
    try:
        global selected_tuple
        index=l1.curselection()[0]
        selected_tuple=l1.get(index)
        e1.delete(0,END)
        e1.insert(END,selected_tuple[1])
        e2.delete(0,END)
        e2.insert(END,selected_tuple[2])
        e3.delete(0,END)
        e3.insert(END,selected_tuple[3])
        e4.delete(0,END)
        e4.insert(END,selected_tuple[4])
    except IndexError:
        pass
def update_command():
    database.update(selected_tuple[0],e1_val.get(),e2_val.get(),e3_val.get(),e4_val.get())
    

def view_command():
    l1.delete(0, END)
    for row in database.view():     
        l1.insert(END,row)

    
def search_entry():
    l1.delete(0, END)
    for row in database.Search(e1_val.get(),e2_val.get(),e3_val.get(),e4_val.get()):
        l1.insert(END,row)

def add_command():
    database.insert(e1_val.get(),e2_val.get(),e3_val.get(),e4_val.get())
    l1.delete(0, END) 
    l1.insert(END, (e1_val.get(),e2_val.get(),e3_val.get(),e4_val.get()))     

def delete_command():
    database.delete(selected_tuple[0])

window=Tk()
window.wm_title("BookStore")
e1_val=StringVar()
e1=Label(window,text="Title")
e1.grid(row=0,column=0)
e1=Entry(window,textvariable=e1_val)
e1.grid(row=0,column=1)

e2_val=StringVar()
e2=Label(window,text="Author")
e2.grid(row=0,column=2)
e2=Entry(window,textvariable=e2_val)
e2.grid(row=0,column=3)

e3_val=StringVar()
e3=Label(window,text="Year")
e3.grid(row=1,column=0)
e3=Entry(window,textvariable=e3_val)
e3.grid(row=1,column=1)

e4_val=StringVar()
e4=Label(window,text="ISBN")
e4.grid(row=1,column=2)
e4=Entry(window,textvariable=e4_val)
e4.grid(row=1,column=3)

b1=Button(window,text='View All', width=12, command=view_command)
b1.grid(row=2,column=3)
b2=Button(window,text='Add Entry' , width=12 ,command=add_command)
b2.grid(row=3,column=3)
b3=Button(window,text='Update selected', width=12, command=update_command)
b3.grid(row=4,column=3)
b4=Button(window,text='Delete selected', width=12, command=delete_command)
b4.grid(row=5,column=3)
b5=Button(window,text='Search Entry', width=12, command=search_entry)
b5.grid(row=6,column=3)
b6=Button(window,text='Close', width=12, command=window.destroy)
b6.grid(row=7,column=3)

l1=Listbox(window, height=6, width=35)
l1.grid(row=2,column=0, rowspan=6, columnspan=2)

s1=Scrollbar(window)
s1.grid(row=2,column=2,rowspan=6)

l1.configure(yscrollcommand=s1.set)
s1.configure(command=l1.yview)

l1.bind('<<ListboxSelect>>',get_selected)

window.mainloop()