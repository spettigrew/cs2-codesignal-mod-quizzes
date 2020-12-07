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

    # def csLongestPossible(str_1, str_2):
        # theres a few ways to get this done
    #     # one of the simplest ways is to just build an array of unique characters
    #     # then sort it and return it
    #     unique_chars = []
    # ​
    #     for char in str_1:
    #         # check if the character has never been seen before
    #         if char not in unique_chars:
    #             # add to unique_chars
    #             unique_chars.append(char)
        
    #     # do the same loop for str_2
    #     for char in str_2:
    #         # check if the character has never been seen before
    #         if char not in unique_chars:
    #             # add to unique_chars
    #             unique_chars.append(char)
        
    #     # sort the array
    #     unique_chars.sort()
        
    #     # to turn the array to a string, use string.join()
    #     return ''.join(unique_chars)


