'''6. Write a program to calculate the grade of a student from his marks from the 
following scheme:
90 – 100 => Ex
80 – 90 => A
70 – 80 => B
60 – 70 =>C
50 – 60 => D
<50 => F'''

marks=int(input("enter marks:-"))
if(marks>=90 and marks<=100):
    print("Ex")
elif(marks>=80 and marks<=89):
    print("A")

elif(marks>=70 and marks<=79):
    print("B")
    
elif(marks>=60 and marks<=69):
    print("C")
    
elif(marks>=50 and marks<=59):
    print("D")
else:
    print("f")


