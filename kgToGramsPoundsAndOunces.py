from tkinter import *

window=Tk()
def conv():
    print(float(e_value.get())) #print on console
    grams=float(e_value.get())*1000
    pounds=float(e_value.get())*2.20462
    ounces=float(e_value.get())*35.274
    t1.insert(END,grams)
    t2.insert(END,pounds)
    t3.insert(END,ounces)
label_1=Label(window,text='Kg:',height=4,width=20)
label_1.grid(row=0,column=0)
e_value=DoubleVar()
entry=Entry(window,textvariable=e_value)
entry.grid(row=0,column=1)

button=Button(window,text="Convert",command=conv,padx=10)
button.grid(row=0,column=2,padx=40)
t1=Text(window,height=1,width=10)
t1.grid(row=1,column=0)
t2=Text(window,height=1,width=10)
t2.grid(row=1,column=1)
t3=Text(window,height=1,width=10)
t3.grid(row=1,column=2)

label_2=Label(window,text='Grams',height=1,width=5)
label_2.grid(row=2,column=0)
label_3=Label(window,text='Pounds',height=1,width=5)
label_3.grid(row=2,column=1)
label_4=Label(window,text='Ounces',height=1,width=5)
label_4.grid(row=2,column=2)
window.mainloop()