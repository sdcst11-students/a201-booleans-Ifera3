#! python3

# Have the user enter a number 
# Determine if the number is an integer
# 1 mark

# Inputs:
# a number

# Outputs:
# "the number is an integer"
# "the number is not an integer"
import math


x = float(input("enter a number: "))
if (x % 2) == 0:
    print("the number is an integer")
elif (x % 2) == 1:
    print("the number is an integer")
else:
    print("The number is not a integer")