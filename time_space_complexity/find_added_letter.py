"""
You are given two strings, str_1 and str_2, where str_2 is generated by randomly shuffling str_1 and then adding one letter at a random position.

Write a function that returns the letter that was added to str_2.

Examples:

csFindAddedLetter(str_1 = "bcde", str_2 = "bcdef") -> "f"
csFindAddedLetter(str_1 = "", str_2 = "z") -> "z"
csFindAddedLetter(str_1 = "b", str_2 = "bb") -> "b"
csFindAddedLetter(str_1 = "bf", str_2 = "bfb") -> "b"
Notes:

str_1 and str_2 both consist of only lowercase alpha characters.
[execution time limit] 4 seconds (py3)

[input] string str_1

[input] string str_2

[output] string
"""

def csFindAddedLetter(str_1, str_2):
    # set a new_str to be str1 + str2
    new_str1 = sorted(str_1)
    new_str2 = sorted(str_2)     # one longer 
    # add to sorted new string one, to match the length of string2
    new_str1.append(" ")  
    # compare string 1 to string 2 to find the added letter
    count = 0
    # for every letter in string2, compare to letter in string 1 at the same index
    for idx in new_str2:
        # if they don't match, return string2 for new char
        if idx != new_str1[count]:
           return idx
           # incremement to next letter
        count += 1
      