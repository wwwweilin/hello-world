# test of while statement
number = 23
runing = True
while runing:
   guess = int(input('Enter an integer: '))

   if guess == number:
      print("Congratulations, you guessed it.")
      runing =  False
   elif guess < number:
      print("No,it is a little higher than that")
   else:
      print("No,it is a little lower than that")
else:
    print("Over")
print("DONE")