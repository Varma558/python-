# """ 
# TASK: Get the username from the user and generate the userid
# For Memory Issues, Limit the userid to length 10 with following conditions
#   - if the length of userid is less than 10, then cover it with 0 at prefix
#   - if length of userid exceeds 10, then remove the extra characters

# For the security reasons, we had to mask the user id with following:
#   replace the last two characters with 'X'
# Print the userid along with masked userid

# Sample Input1:
#   nick
# Sample Output1:
#   000000nick ---- 000000niXX

# Sample Input2:
#   codewala
# Sample Output2:
#   00codewala ---- 00codewaXX

# Sample Input3:
#   SteeveRogers
# Sample Output3:
#   SteeveRoge ---- SteeveRoXX

# """




username = input("Enter your username : ")
length = len(username)
n = 10-length
a = ((n)*"0")
b = username
first = (a+b)
c = (f"----{(a+b)[0:8]}")
mask = ("XX")
second = (c+mask)
print(f"your userid : {first+second}")

email = input()
n=email.replace("@gmail.com", " ")
print(n)
m = n.lower()
print(m)