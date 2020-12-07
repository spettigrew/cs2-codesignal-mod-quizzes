"""Given a string, return a new string with all the vowels removed.

Examples:

csRemoveTheVowels("Lambda School is awesome!") -> "Lmbd Schl s wsm!"
Notes:

For this challenge, "y" is not considered a vowel.
[execution time limit] 4 seconds (py3)

[input] string input_str

[output] string
"""
def csRemoveTheVowels(input_str):
    # U -remove vowels in the string.
    # set vowels (upper and lower) to have removed
    vowels = "AaEeIiOoUu"
    # iterate through the string get all vowels
    for vowel in vowels:
        if vowel in input_str:
            # if there is a vowel,replace it with empty ''
            input_str = input_str.replace(vowel, '')
    # return input_str
    return input_str

# def csRemoveTheVowels(input_str):
#     # create a set of all vowels to use when we are checking if a character is a vowel
#     vowel_set = ('a', 'e','i', 'o', 'u')
    
#     # we will build a new string that has no vowels
#     result_str = ''
    
#     # loop over each character, and check if its a vowel
#     # if its a vowel, DO NOT add it to result_str, otherwise, add to result
#     for i in input_str:   
#         if i.lower() not in vowel_set:
#             result_str += i    
            
#     return result_str  