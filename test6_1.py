# test of if statement
number = 23
guess = int(input('Enter an integer: '))

if guess == number:
    print("Congratulations, you guessed it.")  # new block strats here
    print("(but you do not win any prizes)")  # nwe block ends here
elif guess < number:
    print("No,it is a little higher than that")
else:
    print("No,it is a little lower than that")
print("DONE")
