'''

Psuedo Code

import math to allow the use of math.pow()

take user input as a string variable (call it user_in), and use the given prompt

apply user_in through .lower()
if (user_in != bond) or (user_in != investment):
    output error message

elif user == bond:
    ask for user inputs for current house value, interest rate, months left to repay
    divide the interest rate by 100, then divide that by 12 for the month_rate

    put the variables into this formula
    repayment = ((month_rate*value)/(1 - (1 + month_rate)**(-months)))
    output the repayment

elif user == investment:
    ask for user inputs for money, interest rate, years, and type of interest

    if type == simple:
        put the given variables in the following formula
        amount = money * (1 + (rate/100) * years)
    elif type == compound:
        put the variables in the following formula
        amount = money * math.pow((1+(rate/100)),years)
        math.pow(x,y) is the same as saying "x to the power of y"
    else:
        output error
    output amount

REMEMBER:
1. make sure all integers are casted
2. string inputs should be .lower() ed
3. test that the calculations are correct (they are, although I'm not sure about the bonds)

'''

import math

user_in = input('''
                investment  - to calculate the amount of interest you'll earn on your investment
                bond        - to calculate the amount you'll have to repay on a home loan

                Please enter either 'investment' or 'bond' from the menu above to proceed:

''')

user_in = user_in.lower()

if user_in not in ("bond", "investment"):
    print("That is not a valid option!")

elif user_in == "bond":
    #user inputs
    value = float(input("What is your current house value? "))
    rate = int(input("What is your yearly interest rate? "))
    months = int(input("How many months do you plan to take to repay the bond? "))

    #work out monthly rate
    month_rate = (rate / 100) / 12

    repayment = ((month_rate*value)/(1 - (1 + month_rate)**(-months)))
    print(f"You will have to pay £{repayment:.2f} every month.")

elif user_in == "investment":
    #user inputs
    money = float(input("How much money are you depositing? "))
    rate = int(input("what is your interest rate? "))
    years = int(input("How many years are you planning on investing? "))
    interest = input("Do you want calculations for 'compound' or 'simple' interest? ")

    #this is to make sure it isn't case sensitive
    intererst = interest.lower()

    #the next if elif executes the respective calculations
    if interest == "simple":
        amount = money * (1 + (rate/100) * years)
        print(f"Your amount after {years} years is £{amount:.2f}")

    elif interest == "compound":
        rate = rate / 100
        amount = money * math.pow((1 + rate), years)
        print(f"Your amount after {years} years is {amount:.2f}")

    else:
        print("That is not a valid input!")
