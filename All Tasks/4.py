# """  
# Create empty list 'names' and Get n inputs from the user & store it in 'names'
# After taking n inputs, 
# 	convert even indexed words into upper and odd indexed words to lower

# finally, form a sentence with all the modified words into one sentence separated by -
# print the list after modified
# print the combined sentence separated with -

# Sample Input1:
#   ["Alaric", "SteFan", "Damon", "ElEna"]
# Sample Output1:
#   ["ALARIC", "stefan", "DAMON", "elena"]
#   ALARIC-stefan-DAMON-elena

# Sample Input2:
#   ["Chris", "Evans", "Steeve", "CodeWala"]
# Sample Output2:
#   ["CHRIS", "evans", "STEEVE", "codewala"]
#   CHRIS-evans-STEEVE-codewala

# Sample Input3:
#   ["Caroline", "KlaUs"]
# Sample Output3:
#   ["CAROLINE", "klaus"]
#   CAROLINE-klaus

# CONSTRAINTS:
#   words can have upper/lower/digits in it 

# """


names = []
for ben in range(0,6):
    enter = input()
    names.append(enter)

for ben in range(0,6):
    if ben%2 == 0:
        names[ben] = names[ben].upper()
    else:
        names[ben] = names[ben].lower()
print(names)
print("-".join(names))