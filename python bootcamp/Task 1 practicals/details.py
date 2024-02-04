'''
PSEUDO CODE

input name (string)
input age (integer)
input house number (string)
input street name (string)

output all of this information in a single sentence, use formatting

'''
user_name = input("What is your name? ")
age = int(input("What is your age? "))
house_no = input("What is your house number? ")
street_name = input("What is your street name? ")

print(f"Your name is {user_name}, your age is {age}, your address is {house_no} {street_name}.")
