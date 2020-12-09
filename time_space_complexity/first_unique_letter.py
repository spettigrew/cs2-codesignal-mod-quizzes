"""
Given a string, write a function that returns the index of the first unique (non-repeating) character. If there isn't a unique (non-repeating) character, return -1.

Examples:

csFirstUniqueChar(input_str = "lambdaschool") -> 2
csFirstUniqueChar(input_str = "ilovelambdaschool") -> 0
csFirstUniqueChar(input_str = "vvv") -> -1
Notes:

input_str will only contain lowercase alpha characters.
[execution time limit] 4 seconds (py3)

[input] string input_str

[output] integer

"""

def csFirstUniqueChar(input_str):
    #     U - return the index of the first non-repeating char. If none, return -1   
    # iterate through the string to find first unique char
        
    for i in range(len(input_str)):
        if input_str.count(input_str[i]) == 1:
            return i
    
    return -1
        





    # # U - return the index of the first non-repeating char. If none, return -1
    # # set unique character to 0
    # uni_char = 0
    
    # # iterate through the string to find first unique char
    # # for char in input_str:
        
    
    # # If none, return -1
    # if uni_char == 0:
    #     return -1   # only 2/5 tests passing

