# no_of_subjects = int(input("Enter no of subjects of 100 Marks total : "))
# lab_subjects= int(input("Enter no of Lab_subjects : "))
# lab_subject = int(input("Enter no of 50 marks Subject : "))
# marks=[]
# Gpa= []
# credits=[]
# total=[]
# max_mark = 0
# max_credit = 0
# arrear = []
# def func(gpa):
#     for i in range(0,len(gpa)):
#         a=credits[i]*Gpa[i]
#         total.append(a)
         
# def marks_checker(mark,category):
#     if mark<50:
#         credits.append(0)
#         arrear.append(1) 
#     elif category=='S':
#         credits.append(3)
#     elif category=='L': 
#         credits.append(2)
#     elif category=='HL':
#         credits.append(1)
#     if mark<=100:
#         if mark>=90:
#             Gpa.append(10)
#         elif mark>=80:
#             Gpa.append(9)
#         elif mark>=70:
#             Gpa.append(8)
#         elif mark>=60:
#             Gpa.append(7)
#         elif mark>=50:
#             Gpa.append(6)
#         else:
#             Gpa.append(0)
#     # else:
#     #     print("Invalid Marks")
# try :
#     for i in range (0,no_of_subjects):
#         i=i+1
#         mark=int(input(f"Enter the marks of subject {i} : "))
#         marks.append(mark)
#         marks_checker(mark,'S')
#     for i in range(0,lab_subjects):
#         i=i+1
#         mark=int(input(f"Enter the marks of Lab {i} out of 100 : "))
#         marks.append(mark)
#         marks_checker(mark,'L')
#     for i in range(0,lab_subject):
#         i=i+1
#         mark=int(input(f"Enter the marks of Lab {i} out of 50 : "))
#         mark=mark*2
#         marks.append(mark)
#         marks_checker(mark,'HL')
#     func(Gpa)
#     print(marks)
# except :
#     pass
# for i in range(0,len(total)):
#     max_mark = max_mark+total[i]
#     max_credit = max_credit+credits[i]
# print(total)
# print("Gpa : ",round(max_mark/max_credit,3))
# print("Arrears : ",len(arrear))
from tkinter import * 
top = Tk()
Button(top,text="All subjects of 100 marks with labs",command=quit).pack()
Button(top,text="All subjects of 100 marks ",command=quit).pack()
top.mainloop()