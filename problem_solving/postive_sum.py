"""
Given an array of integers, return the sum of all the positive integers in the array.

Examples:

csSumOfPositive([1, 2, 3, -4, 5]) -> 1 + 2 + 3 + 5 = 11
csSumOfPositive([-3, -2, -1, 0, 1]) -> 1
csSumOfPositive([-3, -2]) -> 0
Notes:

If the input_arr does not contain any positive integers, the default sum should be 0.
[execution time limit] 4 seconds (py3)

[input] array.integer input_arr

[output] integer
"""

def csSumOfPositive(input_arr):
    # U - return all postive numbers

    # set numbers to 0
    numbers = 0
    # make sure sum does not include negative numbers. nums > 0
    return sum(numbers for numbers in input_arr if numbers > 0)
