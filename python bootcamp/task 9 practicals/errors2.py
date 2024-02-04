# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

animal = "Lion"#runtime error, Lion is written as a variable instead of a string
animal_type = "cub"
number_of_teeth = 16

#2 logical errors, needs an f at beginning of string to format correctly, and animal teeth/type variables are swapped
full_spec = f"This is a {animal}. It is a {animal_type} and it has {number_of_teeth} teeth"

print(full_spec)#sytax error, no brackets
