"""
Given a string of words, return the length of the shortest word(s).

Notes:

The input string will never be empty and you do not need to validate for different data types.
[execution time limit] 4 seconds (py3)

[input] string input_str

[output] integer
"""

def csShortestWord(input_str):
    # # U - return len of shortest word
    # # set word to "infinate" for comparison
    min_length = float("inf")
    # # iterate through length of string to find the shorest word in the string
    for short in input_str.split():
        if len(short) < min_length:
            min_length = len(short)

    return min_length
