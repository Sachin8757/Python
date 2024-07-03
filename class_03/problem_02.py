# 2. Write a program to fill in a letter template given below with name and date.
# letter = ''' 
# Dear <|Name|>,
# You are selected!
# <|Date|>

name=input("enter your name:")
date=input("enter data:-")
print(f'''Dear {name}
      You are selected !
      {date}''')