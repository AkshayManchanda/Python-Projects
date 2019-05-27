from tkinter import *
from math import sqrt

root=Tk()
root.title('Calculator')
e=''
equa=StringVar()
e1=Entry(root,bd=10,textvariable=equa,font=25,justify=RIGHT)
e1.grid(columnspan=3,padx=30,pady=20)

def buttonPress(num):
    global e
    e=e+str(num)
    equa.set(e)

def fButtonPress(num):
    global e
    if num=='AC':
        e=''
        equa.set(e)
    elif num=='C':
        e=e[:-1]
        equa.set(e)
    elif num=='=':
        e=eval(e)
        equa.set(e)
        e=''
    elif num=='@':
        e=eval('sqrt(float(e))')
        equa.set(e)
        e=''
    elif num=='^':
        e=eval('float(e)*float(e)')
        equa.set(e)
        e=''
        
frame=Frame(root)
frame.grid(row=1,column=0)
button1=Button(frame,text='7',height=2,width=5,bd=4,command = lambda:buttonPress(7))
button2=Button(frame,text='8',height=2,width=5,bd=4,command = lambda:buttonPress(8)) 
button3=Button(frame,text='9',height=2,width=5,bd=4,command = lambda:buttonPress(9) )
button4=Button(frame,text='/',height=2,width=5,bd=4,fg='green',command= lambda:buttonPress('/'))
button5=Button(frame,text='AC',height=2,width=5,bd=4,fg='red',command= lambda:fButtonPress('AC'))
button6=Button(frame,text='C',height=2,width=5,bd=4,fg='red',command= lambda:fButtonPress('C'))
button1.grid(row=1,column=0)
button2.grid(row=1,column=1)
button3.grid(row=1,column=2)
button4.grid(row=1,column=3)
button5.grid(row=1,column=4)
button6.grid(row=1,column=5)

button7=Button(frame,text='4',height=2,width=5,bd=4,command= lambda:buttonPress(4))
button8=Button(frame,text='5',height=2,width=5,bd=4,command= lambda:buttonPress(5))
button9=Button(frame,text='6',height=2,width=5,bd=4,command= lambda:buttonPress(6))
button10=Button(frame,text='*',height=2,width=5,bd=4,fg='green',command= lambda:buttonPress('*'))
button11=Button(frame,text='(',height=2,width=5,bd=4,fg='blue',command= lambda:buttonPress('('))
button12=Button(frame,text=')',height=2,width=5,bd=4,fg='blue',command= lambda:buttonPress(')'))
button7.grid(row=2,column=0)
button8.grid(row=2,column=1)
button9.grid(row=2,column=2)
button10.grid(row=2,column=3)
button11.grid(row=2,column=4)
button12.grid(row=2,column=5)

button13=Button(frame,text='1',height=2,width=5,bd=4,command= lambda:buttonPress(1))
button14=Button(frame,text='2',height=2,width=5,bd=4,command= lambda:buttonPress(2))
button15=Button(frame,text='3',height=2,width=5,bd=4,command= lambda:buttonPress(3))
button16=Button(frame,text='-',height=2,width=5,bd=4,fg='green',command= lambda:buttonPress('-'))
button17=Button(frame,text='sqrt( )',height=2,width=5,bd=4,fg='blue',command= lambda:fButtonPress('@'))
button18=Button(frame,text='x^2',height=2,width=5,bd=4,fg='blue',command= lambda:fButtonPress('^'))
button13.grid(row=3,column=0)
button14.grid(row=3,column=1)
button15.grid(row=3,column=2)
button16.grid(row=3,column=3)
button17.grid(row=3,column=4)
button18.grid(row=3,column=5)

button19=Button(frame,text='0',height=2,width=5,bd=4,command= lambda:buttonPress(0))
button20=Button(frame,text='.',height=2,width=5,bd=4,command= lambda:buttonPress('.'))
button21=Button(frame,text='%',height=2,width=5,bd=4,fg='green',command= lambda:buttonPress('%'))
button22=Button(frame,text='+',height=2,width=5,bd=4,fg='green',command= lambda:buttonPress('+'))
button23=Button(frame,text='=',height=2,width=12,bd=4,fg='blue',command= lambda:fButtonPress('='))
button19.grid(row=4,column=0)
button20.grid(row=4,column=1)
button21.grid(row=4,column=2)
button22.grid(row=4,column=3)
button23.grid(row=4,column=4,columnspan=2)

root.mainloop()