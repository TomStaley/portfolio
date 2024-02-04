'''
THIS PROGRAM CONTAINS MANY ERRORS

The purpose of this program is to analyse a sentence for capitalisation errors
'''

letter2 = " "
err_num = 0


err_str = str(input("Please enter a sentence to be analysed: "))
For letter in err_str:#syntax error, for shouldn't be capitalised
    if letter = letter.upper(): #syntax error, = should be ==
        letter2 == letter #logical error, this should be at the end of the if statement, not here.
        if letter2 == " ":
            print(str(Letter) + " is correct!")#runtime error, letter shouldn't be capitalised
            print("Previous letter: " + letter2)
        elif letter == " ":
            print("letter is a space!")
        else:
            print(str(letter) + " is incorrect")
            print("Previous letter: " + letter2)
            err_num += 1


print(f"This sentence contains {err_num} errors!")




'''
REAL CODE


err_str = str(input("Please enter a sentence to be analysed: "))
for letter in err_str:
    if letter == letter.upper():
        if letter2 == " ":
            print(str(letter) + " is correct!")
            print("Previous letter: " + letter2)
        elif letter == " ":
            print("letter is a space!")
        else:
            print(str(letter) + " is incorrect")
            print("Previous letter: " + letter2)
            err_num += 1
    letter2 = letter

print(f"This sentence contains {err_num} errors!")
'''
