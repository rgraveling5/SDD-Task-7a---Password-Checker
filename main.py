"""
Program Title

A Programmer
01/01/1970

A brief description of what the program does
"""
#open the input_data file
file = open('input_data.txt','r')

entered = input("Please enter password: ")

actual = file.read()

correct = False

counter = 0 

if entered == actual:
  correct = True
else:
  correct = False

while correct == False and counter <6:
  print("Incorrect")
  counter = counter + 1
  entered = input("Please enter password: ")
  if entered == actual:
    correct = True
  else:
    correct = False



if correct == True:
  print("Congratulations. You may enter")
elif correct == False:
  print("Too many attempts. Go away")





