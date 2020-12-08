"""
Create a function that given an integer, returns an integer where every digit in the input integer is squared.

Examples:

csSquareAllDigits(9119) -> 811181 because 9^2 = 81, 1^2 = 1, 1^2 = 1, and 9^2 = 81
csSquareAllDigits(2483) -> 416649 because 2^2 = 4, 4^2 = 16, 8^2 = 64, and 3^2 = 9
[execution time limit] 4 seconds (py3)

[input] integer n

[output] integer

[Python 3] Syntax Tips
"""

def csSquareAllDigits(n):
   # initializea result string to hold our result 
    result = ""
    # iterate through the for loop, change n to a string str(n)
    for number in str(n):
    # change it back to an integer - return the integer value of the result
        # print (number)
        result += (str(int(number) ** 2))
    return (int(result))
        
 

