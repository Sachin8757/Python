'''2. Write a program to find out whether a student has passed or failed if it requires a 
total of 40% and at least 33% in each subject to pass. Assume 3 subjects and 
take marks as an input from the user. '''

sub1=int(input("enter subject 1 marks:-"))
sub2=int(input("enter subject 2 marks:-"))
sub3=int(input("enter subject 3 marks:-"))

total=sub1+sub2+sub3
per=(total/300)*100

if(sub1>=33 and sub2>=33 and sub3>=33):
    print("you are pass")
else:
    print("you are fail")