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

 # --------------- Notes from after hours --------------------------------
    # create a dict where the keys are letters and the value are number of times they appear in input
    # go through each letter
        # if not in dict, add letter as a key and make value =1
        # else: add +1 to the value in the dict 
        # Makes this runtime O(n)


    # print(list(input_str))
    # print(list(enumerate(input_str)))

    # for i, char in enumerate(input_str):    #runtime is O(n^2)
    #     # # check if char is unique       input string will not equal an empty string
    #     # if char not in input_str[i+1: ] and input_str[i+1] != "":
    #     #check if char is unique
    #     if input_str.count(char) == 1:
    #         return i
    #       # the length of the loop is length string = O(n)  Count is O(n)
    # return -1

        





    # # U - return the index of the first non-repeating char. If none, return -1
    # # set unique character to 0
    # uni_char = 0
    
    # # iterate through the string to find first unique char
    # # for char in input_str:
        
    
    # # If none, return -1
    # if uni_char == 0:
    #     return -1   # only 2/5 tests passing

