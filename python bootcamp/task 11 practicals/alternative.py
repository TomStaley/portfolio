'''

This code will:
1. take an input from the user and save it as a string
2. the user will then choose to either:
    a) have each character in the string alternate between upper and lower cases
    b) have each word in the string alternate between upper and lower cases

ISSUES:
1. pyright is bring up an error on userList.append():
    "Type of "append" is partially unknown"
    I don't know what this means but it doesn't seem to cause any errors or further problems
'''

#user inputs
userStr = str(input("Please input a sentence: "))
userChoice = input("Please input either 'character' (capitalise every other letter) or 'word' (capitalise every other word): ")
userChoice = userChoice.lower()

#utillity variables
newStr = ""
capBool = False


#"character": cycles through each letter, and checjs capBool.
#if capBool is true, make the letter lower.
#if capBool is false, make the letter upper.
#it adds each letter to newStr.
if userChoice == "character":
    print("User chose 'character'")
    for letter in userStr:
        if capBool is False:
            newStr += letter.upper()
            capBool = True
        elif capBool is True:
            newStr += letter.lower()
            capBool = False


#"word": splits the sentence, then cycles through each word.
#does the same as "character", but appends to userList instead of newStr.
#uses .join on userList to reconstruct the sentence, then sets as newStr.
elif userChoice == "word":
    print("User chose 'word'")
    userList = []
    userStr = userStr.split(" ")
    for word in userStr:
        if capBool is True:
            userList.append(str(word.upper()))
            capBool = False
        elif capBool is False:
            userList.append(str(word.lower()))
            capBool = True
    newStr = " ".join(userList)


#error handling
else:
    print("That is not a valid input!")

print()
print(f"Your new string is: '{newStr}'")
