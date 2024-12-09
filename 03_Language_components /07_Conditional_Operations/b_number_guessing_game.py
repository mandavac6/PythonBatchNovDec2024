LUCKY_NUMBER = 35

number_guessed = int(input("Enter a number between 0 to 100 inclusive:"))
if number_guessed == LUCKY_NUMBER:
    print("YOU GOT IT !!!")
elif number_guessed > LUCKY_NUMBER:  
    print("Number is lower than you guessed")
elif number_guessed < LUCKY_NUMBER: 
    print("Number is higher than you guessed")