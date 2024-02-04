'''

This program registers users for an exam venue
It outputs the registered data to a file called "reg_form.txt"

The way it does this, as defined by the brief, is:
1. it asks how many students the user wants to register
2. run a for loop that runs for the number provided, ask the user for a student id every loop
3. Write each id to the text file
4. also make sure to include a dotted line after every id, so that the students can sign in

'''

#we'll add each new student to this list
studentList =["LIST OF STUDENTS"]

loopNo = int(input("How many students are you registering? "))

#the range is defined by the previous input
#ask the user for an id, then append the line, every loop
for x in range(0, loopNo):
    studentId = str(input("Please input a student ID: "))
    studentList.append(studentId + " ...........................")

#we just need the standard "w" writing, because the register is rewritten every day.
#can't write a list (and it'd be ugly), so use join to make a string. also use \n to format right
with open('reg_form.txt', 'w', encoding='utf-8') as file:
    file.write("\n".join(studentList))
