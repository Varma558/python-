

""" 
create a function which takes two positional arguments i.e., start and end
print the list which has the even numbers between start to end (inclusive)

- start and end should be the user inputs
HINT:- You can create user inputs outside the function and pass them while calling

Sample Input:
  4
  20
Sample Output:
  [4, 6, 8, 10, 12, 14, 16, 18, 20]
"""

def digits(start, end):
    list = []
    for num in range(start, end+1):
        if num % 2 == 0:
        	list.append(num)
    print(list)
start = int(input("Enter Start: "))
end = int(input("Enter End: "))
digits(start, end)