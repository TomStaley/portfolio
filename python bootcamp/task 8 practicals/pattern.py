'''

Psuedo code

the goal is to create an output that looks like this:

*
**
***
****
*****
****
***
**
*

using a single for loop and if-else statement
using a list like ["*","**", etc] would make this easy, but that isn't what they want me to do

the plan is:
use a for loop with a range(1,10)
in the loop is an if-else
if x is <= 5 then add to a counter
else subtract from the counter
(still in the for loop, after the ifelse) print("*" * counter)

'''

counter = 0

for i in range(1,10):
    if i <= 5:
        counter += 1
    else:
        counter -= 1
    print("*"*counter)
