#! python3

# Have the user enter a number 
# Determine if the number is an even number. 
# Hint: Use the modulus, which determines the remainder when two numbers are divided
# 1 mark

# Inputs:
# a number

# Outputs:
# "the number is even"
# "the number is odd"

x = int(input("Enter a number: "))
if (x % 2) == 1:
    print("The number is odd")
else:
    print("The number is even")