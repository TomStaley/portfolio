'''

Pseudo Code

age = input "What is your age?"

if age is greater than 100
    output "Sorry, your dead."
elif age is 65 or older
    output "Enjoy your retirement!"
elif age is 40 or older
    output "Your over the hill."
elif age is under 13
    output "You qualify for the kiddie discount."
elif user is 21
    output "Congrats on your 21st!"
else
    output "Age is but a number."

'''

age = int(input("What is your age? "))

if age > 100:
    print("Sorry, your dead.")
elif age >= 65:
    print("Enjoy your retirement!")
elif age >= 40:
    print("Your over the hill.")
elif age < 13:
    print("You qualify for the kiddie discount.")
elif age == 21:
    print("Congrats on your 21st!")
else:
    print("Age is but a number.")
