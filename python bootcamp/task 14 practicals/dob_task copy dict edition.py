'''

This file reads data from the provided txt file (DOB.txt) and outputs it in a different format.
In the file, the data is stored as [name] [birthdate] on each line.
The file only needs to be read, so the standard 'r' read mode is ideal.

The new format is:
Name:
[print all names]
[/n]
Birthdate:
[print all birthdates]


Please note: I was unsure how this task wanted me to construct the file structure, so
this program assumes that DOB.txt is in the same directory as the program.
If DOB.txt is in the same file as in the dropbox, the file should be opened from:
"./10-018 IO Operations - Input/Task file/DOB.txt"

'''

#program stores the data in this dictionary
dobData = {"name": "dob"}

#opens the file as file, standard reading mode, encoded with utf-8
with open('DOB.txt', 'r', encoding='utf-8') as file:
    for line in file:
        lineList = line.split(" ")
        tempName = f"{lineList[0]} {lineList[1]}"
        tempBd = f"{lineList[2]} {lineList[3]} {lineList[4]}"
        dobData[tempName] = tempBd

print(dobData)
names = dobData.keys()
birthdates = dobData.values()

print(
    f'''
Name:
{names}

Birthdate:
{birthdates}
'''
)