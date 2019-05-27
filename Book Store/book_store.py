#DATABASE
 
import sqlite3 as sq

conn=sq.connect("database.db")
cursor=conn.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS books(number INTEGER PRIMARY KEY, title text, author text, year text, isbn INTEGER);""")
def addEntry():
    a=str(e1_value.get())
    b=str(e2_value.get())
    c=str(e3_value.get())
    d=int(e4_value.get())
    tuple1 = (a,b,c,d)
    cursor.execute("INSERT INTO books VALUES(NULL,?,?,?,?)",tuple1)
    conn.commit()
 
def updateSelected():
    a=str(e1_value.get())
    b=str(e2_value.get())
    c=str(e3_value.get())
    d=int(e4_value.get())
    tuple2 = (a,b,c,d,v)
    cursor.execute("UPDATE books SET title=? , author=?, year=?, isbn=? WHERE number=?",tuple2)
    conn.commit()
    
def deleteSelected():
    cursor.execute("DELETE FROM books WHERE number=?",(v,))
    conn.commit()
    
def searchEntry():
    a=str(e1_value.get())
    b=str(e2_value.get())
    c=str(e3_value.get())
    d=int(e4_value.get())
    tuple4 = (a,b,c,d)
    cursor.execute("SELECT * FROM books WHERE title=? OR author=? OR year=? OR isbn=?",tuple4)
    z = cursor.fetchall()
    list.delete(0,'end')
    for i in z:
        list.insert(END,i)
    
def viewAll():
    cursor.execute("SELECT * FROM books")
    z = cursor.fetchall()
    list.delete(0,'end')
    for i in z:
        list.insert(END,i)
        print(i)
        
 



# GUI


from tkinter import *
root=Tk()
root.title("Book Store")

v=0

root.configure(background='#76D7C4')
def listBoxValue(event):
    global v
    value=list.get(ACTIVE)
    v=value[0]
    e1_value.set(value[1])
    e2_value.set(value[2])
    e3_value.set(value[3])
    e4_value.set(value[4])

topFrame = Frame(root)
topFrame.configure(background='#76D7C4')
label1 = Label(topFrame,text='Title:',padx=20,pady=10,background='#76D7C4').grid(row=0,column=0,sticky=E)
e1_value = StringVar()
e1 = Entry(topFrame,textvariable=e1_value).grid(row=0,column=1)
label2 = Label(topFrame,text="Author:",padx=20,pady=10,background='#76D7C4').grid(row=0,column=2,sticky=E)
e2_value = StringVar()
e2 = Entry(topFrame,textvariable=e2_value).grid(row=0,column=3)
label3 = Label(topFrame,text='Year:',padx=20,pady=10,background='#76D7C4').grid(row=1,column=0,sticky=E)
e3_value = StringVar()
e3 = Entry(topFrame,textvariable=e3_value).grid(row=1,column=1)
label4 = Label(topFrame,text="ISBN:",padx=20,pady=10,background='#76D7C4').grid(row=1,column=2,sticky=E)
e4_value = IntVar()
e4 = Entry(topFrame,textvariable=e4_value).grid(row=1,column=3)
topFrame.pack(padx=20)


    
leftFrame = Frame(root)
leftFrame.configure(background='#76D7C4')
list = Listbox(leftFrame,height=10,width=40,bg='#F4F6F6')
list.bind('<<ListboxSelect>>',listBoxValue)
list.pack(side=LEFT,padx=10)
leftFrame.pack(side=LEFT,padx=30,pady=40)
scrollbar = Scrollbar(leftFrame)
scrollbar.pack(side=RIGHT,fill=Y)
scrollbar.config(command=list.yview)
list.config(yscrollcommand = scrollbar.set)


rightFrame = Frame(root)
rightFrame.configure(background='#76D7C4')
b1 = Button(rightFrame,text="View All",height=1,bd=4,width=15,bg='#AEB6BF',command=viewAll)
b1.grid(row=0,column=0,pady=3)
b2 = Button(rightFrame,text="Search Entry",height=1,bd=4,width=15,bg='#AEB6BF',command=searchEntry)
b2.grid(row=1,column=0,pady=3)
b3 = Button(rightFrame,text="Add Entry",height=1,bd=4,width=15,bg='#AEB6BF',command=addEntry)
b3.grid(row=2,column=0,pady=3)
b4 = Button(rightFrame,text="Update Selected",height=1,bd=4,width=15,bg='#AEB6BF',command=updateSelected)
b4.grid(row=3,column=0,pady=3)
b5 = Button(rightFrame,text="Delete Selected",height=1,bd=4,width=15,bg='#AEB6BF',command=deleteSelected)
b5.grid(row=4,column=0,pady=3)
rightFrame.pack(side=RIGHT,padx=10,pady=5)
root.mainloop()

