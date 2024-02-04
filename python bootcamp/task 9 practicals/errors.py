# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

print("Welcome to the error program")#syntax error, needed ()
print("\n")#two syntax errors, unnexpected indent, no brackets

# Variables declaring the user's age, casting the str to an int, and printing the result
age_Str = "24" #one syntax error, unexpected indent; and two runtime errors, wrong use of ==, needs to be a whole number to cast to int
age = int(age_Str)#one syntax error, unexpected indent; and one runtime error, can't cast a string to an integer (solved on previous line)
print("I'm " + str(age) + " years old.")#one sytax error, unexpected indent; one runtime error, forgot to cast age to string

# Variables declaring additional years and printing the total years of age
years_from_now = 3.5#sytax error, unexpected indent; runtime error, string should be a float for future calculation; logical error, should be 3.5 (see end of code)
total_years = age + years_from_now#sytax error, unexpected indent


#syntax error, no brackets; logical error, the second string should be a variable;
#two runtime errors, they used the wrong variable name and need to cast it to a string;
print("The total number of years: " + str(total_years))

# Variable to calculate the total amount of months from the total amount of years and printing the result
total_months = total_years * 12#runtime error, wrong variable
print ("In 3 years and 6 months, I'll be " + str(total_months) + " months old") #syntax error, no brackets; runtime error, cast total_months to string

#LOGICAL ERROR
#the outcome was 324, when it should be 330
#this is because they only put 3 for the additional years, when it should've been 3.5

#HINT, 330 months is the correct answer

