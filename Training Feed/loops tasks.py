# take 5 inputs from user
# after each input, print if input length is below or equal to 5, else print invalid
# """
for num in range(5):
    name = input(f"Enter Input-{num} :")
    if len(name) <= 5:
        print(f"Output: {name}")
    else:
        break