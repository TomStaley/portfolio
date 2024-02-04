'''

Psuedo Code

answer = 0
sum = 0
loop_no = 0


While answer does not equal -1:
    answer = input("Please input a number (-1 to stop): ")
    loop_no add 1
    sum add answer

find the average by dividing the sum by the loop_no
print(f"The average of all the numbers given is {average}")

'''

answer = 0
total = 0 #can't use sum because thats a function
loop_no = 0

#pseudo code won't work because the while loop will finish the iteration before breaking,
#so I've used an if statment instead
while True:
    answer = int(input("Please input a number (-1 to stop): "))
    if answer == -1:
        #stops the while loop
        break
    loop_no += 1
    total += answer
    print(total)
    print(loop_no)

average = total / loop_no
print(f"The average of all the numbers given is {average}!")
