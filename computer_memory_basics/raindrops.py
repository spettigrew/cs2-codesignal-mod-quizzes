"""
Given a number, write a function that converts that number into a string that contains "raindrop sounds" corresponding to certain potential factors. A factor is a number that evenly divides into another number, leaving no remainder. The simplest way to test if one number is a factor of another is to use the modulo operator.

Here are the rules for csRaindrop. If the input number:

has 3 as a factor, add "Pling" to the result.
has 5 as a factor, add "Plang" to the result.
has 7 as a factor, add "Plong" to the result.
does not have any of 3, 5, or 7 as a factor, the result should be the digits of the input number.
Examples:

csRaindrops(28) -> "Plong"
28 has 7 as a factor, but not 3 or 5.
csRaindrops(30) -> "PlingPlang"
30 has both 3 and 5 as factors, but not 7.
csRaindrops(34) -> "34"
34 is not factored by 3, 5, or 7.
[execution time limit] 4 seconds (py3)

[input] integer number

[output] string
"""

def csRaindrops(number):
    # U - 105 is divisible by 3, 5 and 7. or 28% 7 = 0  is the remainder
    answer_string = ""
    # if number is divisible by 3
        # add Pling
    if number % 3 == 0:
        answer_string += "Pling"
    # if number is divisible by 5
        # add Plang
    if number % 5 == 0:
        answer_string += "Plang"
    # if number is divisible by 7
        # add Plong
    if number % 7 == 0:
        answer_string += "Plong"
    
    # if not divisible by any of those
        # return the number as a string
    if answer_string == "":
        # str converts number to a string
        answer_string = str(number)
    return answer_string