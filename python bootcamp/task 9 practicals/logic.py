'''
This program displays a logical error

The correct outcome should be:
1. print each number in the list
2. after each number is printed, remove the number from the list
3. after all numbers are printed, print the empty list
4. the printed numbers should be in sequence, and the list should be empty
'''

numbers = [1,2,3,4,5]
for num in numbers:
    print(num)
    numbers.remove(num)
print(numbers)
