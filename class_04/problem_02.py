# 2. Write a program to accept marks of 6 students and display them in a sorted 
# manner.
mar=[]
marks1=int(input("enter marks of student:- "))
mar.append(marks1)
marks2=int(input("enter marks of student:- "))
mar.append(marks2)
marks3=int(input("enter marks of student:- "))
mar.append(marks3)
marks4=int(input("enter marks of student:- "))
mar.append(marks4)
marks5=int(input("enter marks of student:- "))
mar.append(marks5)
marks6=int(input("enter marks of student:- "))
mar.append(marks6)
mar.sort()
print(f"sort list is{mar}")