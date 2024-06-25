'''5. Write a program which finds out whether a given name is present in a list or not.'''


list=['sachin','manish','sushil']

name=input("enter a name :-")
if name in list:
    print(name,"is in the list")
else:
    print(name,"is not in the list")