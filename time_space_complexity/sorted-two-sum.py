"""
Given a sorted array (in ascending order) of integers and a target, write a function that finds the two integers that add up to the target.

Examples:

csSortedTwoSum([3,8,12,16], 11) -> [0,1]
csSortedTwoSum([3,4,5], 8) -> [0,2]
csSortedTwoSum([0,1], 1) -> [0,1]
Notes:

Each input will have exactly one solution.
You may not use the same element twice.
[execution time limit] 4 seconds (py3)

[input] array.integer numbers

[input] integer target

[output] array.integer
"""

def csSortedTwoSum(numbers, target):
    # set an empty dict to num
    num_dict = {}
    
    # two for loops
    for i in range(len(numbers)):
        num_dict[numbers[i]] = i
        
    for i in range (len(numbers)):
        current_num = numbers[i]
        # check to see if comliment is in dict.
        compliment = target - current_num
    # check for duplicate elements
        if compliment in num_dict and i != num_dict[compliment]:
            return [i, num_dict[compliment]]

    # complement is the number that will add to the num to equal the target. Or target - cur_num = complement.