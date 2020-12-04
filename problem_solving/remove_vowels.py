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