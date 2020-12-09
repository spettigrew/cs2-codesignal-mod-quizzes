"""
Create a function that returns True if the given string has any of the following:

Only letters and no numbers.
Only numbers and no letters.
If a string has both numbers and letters or contains characters that don't fit into any category, return False.

Examples:

csAlphanumericRestriction("Bold") ➞ True
csAlphanumericRestriction("123454321") ➞ True
csAlphanumericRestriction("H3LL0") ➞ False
Notes:

Any string that contains spaces or is empty should return False.
[execution time limit] 4 seconds (py3)

[input] string input_str

[output] boolean
"""

def csAlphanumericRestriction(input_str):
    
    if input_str.isalpha():
            return True
    if input_str.isnumeric():
        return True
    else: 
        return False


    # has_letters = False
    # has_numbers = False

    # # for char in input_str:
    # #     if int(char):
    # #         has_numbers = True
    # #     else:
    # #         has_letters = True

    # # loop over every character and check
    # for char in input_str:
    #     # is this a number or not?
    #     try:
    #         int(char)
    #         has_numbers = True
    #     except:
    #         # be sure this is a letter and not some symbol
    #         if not ('a' <= c <= 'z' or 'A' <= c <= 'Z'):
    #             return False
    #         has_letters = True


    # if has_letters:
    #     if not has_numbers:
    #         return True

    # if has_numbers:
    #     if not has_letters:
    #         return True

    # return False