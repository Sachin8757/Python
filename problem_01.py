#1. Write a program to find the greatest of four numbers entered by the user.
num1=int(input("enter value of 1:-"))
num2=int(input("enter value of 2:-"))
num3=int(input("enter value of 3:-"))
num4=int(input("enter value of 4:-"))

if(num1>num2 and num1>num3 and num1>num4):
    print("num1 is greatest")
elif(num2>num1 and num2>num3 and num2>num4):
    print("num2 is greatest")

elif(num3>num2 and num3>num1 and num3>num4):
    print("num3 is greatest")

elif(num4>num2 and num4>num3 and num4>num1):
    print("num4 is greatest")
    