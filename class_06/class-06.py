#conditonal statment
age=int(input("enter you age:-"))
if(age>=18):
    print("you are above the age of consent")
elif(age<0):
    print("you are enter negative age")
elif(age==0):
    print("this age not exist")
else:
    print("you are below the age of consent")