# Task-1
# """
# h/w: Take three inputs, 
# 	check if their sum is greater than 100 or if one of them is divisible by 10.

# """

# n1 = int(input("enter first number : "))
# n2 = int(input("enter second number : "))
# n3 = int(input("enter third number : "))
# case1 = (n1+n2+n3) > 100
# case2 = (n1%10==0) or (n2%10==0) or (n3%10==0)
# print(case1 or case2)
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# Task-2

# """ 
# h/w: Take two inputs, check if both of the numbers 
#     are even and divided by 5, 
#     both are odd and divided by 5, 
#     or one of each divided by 5.
# """

# num1 = int(input("enter your first number : "))
# num2 = int(input("enter your second number : "))
# if (num1%2 == 0) and (num2%2 ==0) and ((num1%5 ==0) and (num2%5 ==0)):
#     print("Both numbers are even and divided by 5")
# elif (num1%2 != 0) and (num2%2 !=0) and ((num1%5 ==0) and (num2%5 ==0)):
#     print("Both numbers are odd and divided by 5")
# elif((num1%5 ==0) and (num2%5==0)):
#     print("one is even another is odd and Both number are divided by 5")
# elif((num1%5 ==0) or (num2%5==0)):
#     print("one of each number is divided by 5")
    
# ///////////////////////////////////////////////////////////////////////////////////////////

# Task-3

# """
# h/w: Take one input
# 	Power it with 5, subtract it with 0. Print the final result.
# """

# num1 = int(input("enter your number : "))
# num1 = (num1)**5
# num1 = num1 - 0
# print(num1)

# ////////////////////////////////////////////////////////////////////////////////////////

# # Task-4
# """
# h/w: print numbers from 10 to 1.
# """

# for m in range (10,0,-1):
#     print(m)

# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////

#Task-5

# """
# h/w: Create an empty list and store from 10 to 1 and print it.
# """
# list = []
# for m in range (10,0,-1):
#  list.append(m)
# print(list)

# /////////////////////////////////////////////////////////////////////////////////////////////////////////

# Task-6


# """ 
# h/w: Take two inputs from the user (both numbers),
#         print their sum + difference + product
# """
# num1 = int(input("enter first number : "))
# num2 = int(input("enter second number : "))
# result = (num1+num2) + (num1-num2) + (num1*num2)
# print(result)

# //////////////////////////////////////////////////////////////////////////////////////////////////////

# Task-7


# """
# h/w: print the id() of both variables before and after swapping.
# """

# n1 = int(input("enter your first number : "))
# n2 = int(input("enter your second number : "))
# print(f"before swap-- n1 = {n1}, n2 = {n2}")
# print(f"before swap id's of n1 = {id(n1)}, n2 = {id(n2)}")
# temp = n1
# n1 = n2
# n2 = temp
# print(f"after swap--n1 = {n1}, n2 = {n2}")
# print(f"after swap id's of n1 = {id(n1)}, n2 = {id(n2)}")

# //////////////////////////////////////////////////////////////////////////////////////////////////////////////

# Task - 8


# """
# h/w: Take a string input, print the second and second last character.

# """
# str = input("enter your string : ")
# print(str[1],str[-2])

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////

#Task-9
# """
# h/w: Take a multi-line string input
#         print the length of it after storing in variable using triple quotes.
# """
# n = input("Enter your string : ")

# print(len(n))

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////

# Task-10

# """
# h/w: Concatenate two strings separated by - and print their lengths.
# """

# a = "This-is-pYthon-class-daY-3"
# a = a.replace("-","")
# print(len(a))

# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# Task-11
# """
# h/w: Take a sentence from the user, 
# reverse the words and print along with - between each word.
# Example: Input: "Hello World" → Output: "World-Hello"
# """

# user = input().split()
# print("-".join(user[::-1]))

# //////////////////////////////////////////////////////////////////////////////////////////////////////////////


# #Task-12

# """
# h/w: Take a string input
# 	Replace all lowercase 'a' with 'A'
# """
# string = input()
# string = string.replace("a","A" )
# print(string)

# //////////////////////////////////////////////////////////////////////////////////////////////////////

# Task-13


# """
# h/w: Take a sentence, store alphabets and digits in separate lists.
# """

# listalpha = []
# listdigits = []

# user = input("enter your sentence : ")
# for sentence in range (0,len(user)) :
#     a = (user[sentence])
#     if a.isalpha():
#        listalpha.append(a)
#     elif a.isdigit():
#         listdigits.append(a)
# print(listalpha)
# print(listdigits)
      
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////

#Task-14

# """
# h/w: Take a string with leading and trailing spaces
#  	remove only trailing spaces, and print the cleaned string & it's length
# """
# user="  hi varma   "
# result = user.rstrip()
# print(result )
# print(f"length of cleaned string is : {len(result)}")

# ////////////////////////////////////////////////////////////////////////////////////////////////

#Task-15

# """
# h/w: Print all odd numbers from 1 to n using a for loop.
# """
# n = int(input("Enter your number : "))
# for i in range(1,n+1,2):
#     print(i)
    
# /////////////////////////////////////////////////////////////////////////////////////////////////////////    

#Task-16

# """
# h/w: Repeatedly asks for user input until they type "quit" or "QUIT" or "Quit" (use while loop). 

# """
# while True :
#   user = input("Enter your string : ")
#   if user == "quit":
#       break
#   elif user == "QUIT":
#       break
#   elif user =="Quit":
#       break

#///////////////////////////////////////////////////////////////////////////////////////////////

#Task-17
# """
# h/w: Repeatedly asks for user input until they type "quit". (use while loop). 
#     if they enter digit, store the numbers from 1 to n(user entered digit) in list and print it.
# """
# lst =[]
# while True :
#   user = input("Enter your input : ")
#   if user == "quit":
#       break
#   else:
#    if user.isalpha and user.isdigit() :
#       if user.isdigit:
#         for i in range (1,int(user)+1,1):
#             lst.append(i)
#         print(lst)
#         break

#////////////////////////////////////////////////////////////////////////////////////////////////////////

# Task-18
# num = int(input())
# table_cnt = 0
# for table in range(1, num+1):
#     if num % table == 0:
#       table_cnt += 1
#       print(table_cnt)

# if table_cnt == 2:
# 	print("Prime")
# else:
#     print("Not A Prime")
# # -----------------------
# num  = int(input())
# prime = []
# for i in range (1,num+1):
#   if num,isa:
      
        
# Input: Upper limit
n = int(input("Enter the value of n: "))

# Print prime numbers from 1 to n
print(f"Prime numbers from 1 to {n}:")
for num in range(1, n + 1):
    if (num):
        print(num, end=" ")