"""
Given two strings that include only lowercase alpha characters, str_1 and str_2, write a function that returns a new sorted string that contains any character (only once) that appeared in str_1 or str_2.

Examples:

csLongestPossible("aabbbcccdef", "xxyyzzz") -> "abcdefxyz"
csLongestPossible("abc", "abc") -> "abc"
[execution time limit] 4 seconds (py3)

[input] string str_1

[input] string str_2

[output] string
"""

def csLongestPossible(str_1, str_2):
    # U - return a new sorted string with only one character in each string
    # create a new set.  Sets do not allow dups []
    new_set = set(str_1)
    
    for letters in str_2:
    # concatenate (put together) each character for only one appearance
        new_set.add(letters)
    # keyword sort(), then combine the sorted strings
  
    new_string = sorted(new_set)
    longest_string = ('').join(new_string)
    
    return longest_string

