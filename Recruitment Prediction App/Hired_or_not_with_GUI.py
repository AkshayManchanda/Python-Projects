from tkinter import *
import pandas as pd
import numpy as np
import seaborn as sb
from sklearn.linear_model import LinearRegression
from sklearn.cross_validation import train_test_split
from sklearn import metrics
from sklearn.linear_model import LogisticRegression
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
from sklearn import svm, datasets
from statistics import *

def to_binary(pred):
    return int(pred > 0.5)

def HoN(val):
        if(val == 0):
            return 'Not Hired'
        else:
            return 'Hired'

def trainLinearReg(X,y):
    model = LinearRegression()
    model.fit(X,y)
    return model

def trainLogisticReg(X,y):
    model = LogisticRegression()
    model.fit(X,y)
    return model

def trainDecisionTree(X,y):
    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(X,y)
    return clf 
    
def trainRandomForest(X,y):
    clf = RandomForestClassifier(n_estimators = 10)            
    clf = clf.fit(X,y)
    return clf

def trainSVM(X,y):
    C=2.0
    svc = svm.SVC(kernel='linear', C=C).fit(X, y)
    return svc

def click_chk():
    myvals=[[e2_value.get(),e3_value.get(),e4_value.get(),e5_value.get(),e6_value.get()]]
    print(myvals)
    res = []
    res.append(to_binary(modelln.predict(myvals)))
    res.append(modellg.predict(myvals)[0])
    res.append(modeldt.predict(myvals)[0])
    res.append(modelrf.predict(myvals)[0])
    res.append(modelsvm.predict(myvals)[0])
    v1.set(str(HoN(res[0])))
    v2.set(str(HoN(res[1])))
    v3.set(str(HoN(res[2])))
    v4.set(str(HoN(res[3])))
    v5.set(str(HoN(res[4])))    
#     m=mode(res)
#     myvals=myvals[0]
#     myvals.insert(0,e1_value.get())
#     myvals.append(m)
#     print(myvals)
#     df.append(myvals)
#     df.to_csv("Predata.csv")
    
    
df = pd.read_csv("PrepData.csv")
features = list(df.columns[2:7])
y = df['Hired']
X = df[features]

modelln = trainLinearReg(X,y)
modellg = trainLogisticReg(X,y)
modeldt = trainDecisionTree(X,y)
modelrf = trainRandomForest(X,y)
modelsvm = trainSVM(X,y)

root=Tk()
root.config(bg='#34495E')
e1_value = StringVar()
e2_value = DoubleVar()
e3_value = DoubleVar()
e4_value = IntVar()
e5_value = DoubleVar()
e6_value = DoubleVar()
topFrame = Frame(root,bg='black')
logo = PhotoImage(file="logo.png")
w1 = Label(topFrame,image=logo,height=100,width=200).grid(row=1,column=6,columnspan=2,padx=50)  
w2 = Label(topFrame,justify=LEFT,padx=10,text="Tech Company Pvt Ltd.",font=('times', 50, 'bold'),fg='#148F77').grid(row=1,column=1,padx=50,columnspan=2)
topFrame.pack()
middleFrame=Frame(root)

label1 = Label(middleFrame,text='Name : ',font=25,padx=10,pady=10)
label1.grid(row=1,column=1,padx=90,pady=10,sticky='W')
entry1 = Entry(middleFrame,font=35,textvariable=e1_value)
entry1.grid(row=1,column=2,padx=90,pady=10)

label2 = Label(middleFrame,text='Percentage : ',font=25,padx=10,pady=10)
label2.grid(row=2,column=1,padx=90,pady=10,sticky='W')
entry2 = Entry(middleFrame,font=35,textvariable=e2_value)
entry2.grid(row=2,column=2,padx=90,pady=10)

label3 = Label(middleFrame,text='Backlog : ',font=25,padx=10,pady=10)
label3.grid(row=3,column=1,padx=90,pady=10,sticky='W')
entry3 = Entry(middleFrame,font=35,textvariable=e3_value)
entry3.grid(row=3,column=2,padx=90,pady=10)

label4 = Label(middleFrame,text='Internship : ',font=25,padx=10,pady=10)
label4.grid(row=4,column=1,padx=90,pady=10,sticky='W')
entry4 = Entry(middleFrame,font=35,textvariable=e4_value)
entry4.grid(row=4,column=2,padx=90,pady=10)

label5 = Label(middleFrame,text='First Round : ',font=25,padx=10,pady=10)
label5.grid(row=5,column=1,padx=90,pady=10,sticky='W')
entry5 = Entry(middleFrame,font=35,textvariable=e5_value)
entry5.grid(row=5,column=2,padx=90,pady=10)

label6 = Label(middleFrame,text='Communication Skills : ',font=25,padx=10,pady=10)
label6.grid(row=6,column=1,padx=90,pady=10,sticky='W')
entry6 = Entry(middleFrame,font=35,textvariable=e6_value)
entry6.grid(row=6,column=2,padx=90,pady=10)

rightFrame = Frame(root,bg="Black")
button1 = Button(rightFrame,text="CHECK", fg='white',bg="#2E86C1",bd=4,font=80,padx=20,pady=5,command=click_chk)
button1.grid(row=1,column=10)
rightFrame.pack(side=RIGHT,padx=90)

middleFrame.pack(pady=20,padx=20)
bottomFrame = Frame(root)
bottomFrame.config(bg='#34495E')
label_res = Label(bottomFrame,text='Result:',font=55,padx=20,pady=10,bg='#34495E',fg='WHITE')
label_res.grid(row=0,column=0)

v1=v2=v3=v4=v5=StringVar()

rlabel1 = Label(bottomFrame,text='Linear Regression: ',font=25,padx=10,pady=10,bg='#34495E',fg='WHITE')
rlabel1.grid(row=1,column=2)
rlabel2 = Label(bottomFrame,text='Logistic Regression: ',font=25,padx=10,pady=10,bg='#34495E',fg='WHITE')
rlabel2.grid(row=2,column=2)
rlabel3 = Label(bottomFrame,text='Decision Tree: ',font=25,padx=10,pady=10,bg='#34495E',fg='WHITE')
rlabel3.grid(row=3,column=2)
rlabel4 = Label(bottomFrame,text='\tRandom Forest: ',font=25,padx=10,pady=10,bg='#34495E',fg='WHITE')
rlabel4.grid(row=1,column=5)
rlabel5 = Label(bottomFrame,text='SVM: ',font=25,padx=10,pady=10,bg='#34495E',fg='WHITE')
rlabel5.grid(row=2,column=5)
    
rlabelv1 = Label(bottomFrame,textvariable=v1,font=25,padx=10,pady=10,bg='#34495E',fg='WHITE')
rlabelv1.grid(row=1,column=3)
rlabelv2 = Label(bottomFrame,textvariable=v2,font=25,padx=10,pady=10,bg='#34495E',fg='WHITE')
rlabelv2.grid(row=2,column=3)
rlabelv3 = Label(bottomFrame,textvariable=v3,font=25,padx=10,pady=10,bg='#34495E',fg='WHITE')
rlabelv3.grid(row=3,column=3)
rlabelv4 = Label(bottomFrame,textvariable=v4,font=25,padx=10,pady=10,bg='#34495E',fg='WHITE')
rlabelv4.grid(row=1,column=6)
rlabelv5 = Label(bottomFrame,textvariable=v5,font=25,padx=10,pady=10,bg='#34495E',fg='WHITE')
rlabelv5.grid(row=2,column=6)
    
bottomFrame.pack(pady=10)




root.mainloop()
#---------------------------------------------------------------------------------------------------------
