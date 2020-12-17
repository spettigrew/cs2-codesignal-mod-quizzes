"""
Given a string, your task is to replace each of its characters by the next one in the English alphabet; i.e. replace a with b, replace b with c, etc (z would be replaced by a).

Example

For inputString = "crazy", the output should be alphabeticShift(inputString) = "dsbaz".

Input/Output

[execution time limit] 4 seconds (py3)

[input] string inputString

A non-empty string consisting of lowercase English characters.

Guaranteed constraints:
1 ≤ inputString.length ≤ 1000.

[output] string

The resulting string after replacing each of its characters.

"""

def alphabeticShift(inputString):
    # replace char with char adjacent in the alphabet c->d, z->a, etc. 
    char = ""
    
    for letter in inputString:
        # set char to ascii value, then add 1: ord()
        new_letter = ord(letter) + 1
        # z == 122, if new letter is 122 + 1 assign new value
        if new_letter == 123:
            # new value of 'z' is now assigned to 'a' ascii value
            new_letter = 97
        # replace char with added string_value chr()
        char += chr(new_letter)
        # return new char
    return char
                    

