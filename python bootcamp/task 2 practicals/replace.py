'''

Pseudo Code

define the given sentance as a variable

use .replace() to replace all ! to " " in the variable
output the variable

use .upper() to make the variable uppercase
output the variable

output the variable in reverse

'''

sentance = "The!quick!brown!fox!jumps!over!the!lazy!dog."

sentance = sentance.replace("!"," ")
print(sentance)

sentance = sentance.upper()
print(sentance)

#using [::-1] reverses the variable
print(sentance[::-1])
