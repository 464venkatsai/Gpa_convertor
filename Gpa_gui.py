try :
    from tkinter import * 
    top = Tk()
    subjects_=StringVar()
    labs_=StringVar()
    hlabs_=StringVar()
    check=IntVar()
    names=[]
    marks=[]
    fr=Frame(top)
    fr.grid()
    Gpa= []
    credits=[]
    total=[]
    max_mark = 0
    max_credit = 0
    arrear = []
    catagory = []
    def hallo():
        for i in names:
            marks.append(int(i.get()))
                
    def clear_frame():
        for widgets in fr.winfo_children():
                widgets.destroy()
            
    def func(gpa):
        for i in range(0,len(gpa)):
            a=credits[i]*Gpa[i]
            total.append(a)
            
    def marks_checker(mark,category):
        if mark<50:
            if catagory=='HL':
                if mark<25:
                    credits.append(0)
                    arrear.append(1)   
                else:
                    credits.append(1)  
            else:
                credits.append(0)
                arrear.append(1)     
        elif category=='S':
            credits.append(3)
        elif category=='L': 
            credits.append(2)

        if mark<=100:
            if mark>=90:
                Gpa.append(10)
            elif mark>=80:
                Gpa.append(9)
            elif mark>=70:
                Gpa.append(8)
            elif mark>=60:
                Gpa.append(7)
            elif mark>=50:
                Gpa.append(6)
            else:
                Gpa.append(0)

    def ok():
        hallo()
        max_mark=0
        max_credit=0
        i=0
        for k in range(0,len(marks)):
            marks_checker(marks[i],catagory[i])
            i=i+1
        func(Gpa)
        for i in range(0,len(total)):
            max_mark = max_mark+total[i]
            max_credit = max_credit+credits[i]
            max_gpa=round(max_mark/max_credit,2)
            max_arrear = len(arrear)
        clear_frame()
        print("Marks : ",marks)
        print(credits)
        l1=Label(fr,text="Report Generated",font="Bold 15")
        l1.grid(rowspan=1,columnspan=5,padx=50,pady=15)
        l1=Label(fr,text="GPA :   ",font="Bold 15")
        l1.grid(row=1,column=1,padx=50,pady=15)
        l1=Label(fr,text=f"{max_gpa}",font="Bold 15")
        l1.grid(row=1,column=2,padx=50,pady=15)
        l1=Label(fr,text="Arrears : ",font="Bold 15")
        l1.grid(row=2,column=1,padx=50,pady=15)
        l1=Label(fr,text=f"{max_arrear}",font="Bold 15")
        l1.grid(row=2,column=2,padx=50,pady=15)
        Button(fr,text="Finish",command=quit,width=15).grid(rowspan=2,columnspan=3,padx=15,pady=15)

    def submit():   
        clear_frame()
        subjects=int(subjects_.get())
        labs=int(labs_.get())
        hlabs=int(hlabs_.get())
        print(hlabs_)
        lab_no=1
        for i in range(0,subjects):
            name=StringVar()
            i=i+1
            j=0
            l3=Label(fr,text=f"Subject {i} : ",font="lucida 14")
            l3.grid(row=i,column=j,padx=15,pady=15)
            e3=Entry(fr,textvariable=name,font="lucida 19")
            e3.insert(END,"80")
            e3.grid(row=i,column=j+1,padx=15,pady=15)
            names.append(e3)
            catagory.append('S')
            
        length = subjects+labs
        for i in range(subjects,length):
            i=i+1
            name=StringVar()
            j=0
            l3=Label(fr,text=f"Lab {lab_no} of 100 Marks: ",font="lucida 14")
            l3.grid(row=i,column=j,padx=15,pady=15)
            e3=Entry(fr,textvariable=name,font="lucida 19")
            e3.insert(END,"80")
            e3.grid(row=i,column=j+1,padx=15,pady=15)
            names.append(e3)
            lab_no=lab_no+1 
            catagory.append('L')
        new_length=length+hlabs
        for i in range(length,new_length):
            i=i+1
            name=StringVar()
            j=0
            l3=Label(fr,text=f"Lab {lab_no} of 50 Marks: ",font="lucida 14")
            l3.grid(row=i,column=j,padx=15,pady=15)
            e3=Entry(fr,textvariable=name,font="lucida 19")
            e3.insert(0,"20")
            e3.grid(row=i,column=j+1,padx=15,pady=15)
            names.append(e3)
            lab_no=lab_no+1 
            catagory.append('HL')
        b3=Button(fr,text="Done",command=ok,font="lucida 14",width=35,height=1,borderwidth=5)
        b3.grid(rowspan=subjects,columnspan=2,padx=15,pady=15)
        print(catagory)
        
    def Marks100():
        clear_frame()
        l1=Label(fr,text="No of Subjects     : ",font="lucida 14")
        l1.grid(row=1,column=1,padx=15,pady=15)
        l2=Label(fr,text="No of Lab Subjects : ",font="lucida 14")
        l2.grid(row=2,column=1,padx=15,pady=15)
        l2=Label(fr,text="No of Lab Subjects of  50 : ",font="lucida 14")
        l2.grid(row=3,column=1,padx=15,pady=15)
        e1=Entry(fr,textvariable=subjects_,font="lucida 19",)
        e1.insert(END,"4")
        e1.grid(row=1,column=2,pady=10)
        e2=Entry(fr,textvariable=labs_,font="lucida 19")
        e2.insert(END,"4")
        e2.grid(row=2,column=2,pady=10)
        e3=Entry(fr,textvariable=hlabs_,font="lucida 19")
        e3.insert(END,"1")
        e3.grid(row=3,column=2,padx=25,pady=15)
        b1=Button(fr,text="submit",command=submit,font="lucida 14",width=35,height=1,borderwidth=5)
        b1.grid(rowspan=4,columnspan=3,padx=15,pady=15)
    Marks100()
    top.mainloop()

except:
    pass
