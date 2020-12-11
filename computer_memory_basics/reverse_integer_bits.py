"""
Given an integer, write a function that reverses the bits (in binary) and returns the integer result.

Examples:

csReverseIntegerBits(417) -> 267
417 in binary is 110100001. Reversing the binary is 100001011, which is 267 in decimal.
csReverseIntegerBits(267) -> 417
csReverseIntegerBits(0) -> 0
Notes:

The input integer will not be negative.
[execution time limit] 4 seconds (py3)

[input] integer n

[output] integer
"""

def csReverseIntegerBits(n):
    # turn number to binary
    binary_num = bin(n)
    print(binary_num[2:])
    # reverse that binary string 
    # turn the reverse string back to an int
    reversed_num = binary_num[2:][::-1] 
    # creates new list. :: separators to different numbers. -1 back to front. first colon is the beginning. second         # colon is where we want to stop(end)
    #print(reversed_num)
    # return the int
    return int(reversed_num, 2)


    #  # reverse bits - into binary and return that integer result
    
    # # convert the decimal to binary and replace binary with empty string
    # binary = bin(n).replace("0b", "")
    # # make a variable and take the binary and reverse it
    # reverseBinary = binary[::-1]
    
    # # binary is base two. Return the integer from the reversed binary
    # return int (reverseBinary, 2)


    
    # # set result to 0
    # result = 0

    # # iterate throught the integer to get the binary OR (.pop() and add to the new list, then .append())
    # for bits in n(len(n)):
    #     # convert number to binary
    #     .split(" ")
    #     #reverse the binary
    #     .reverse()
    #     #join the reversed binary list - convert back to a string
    #     .join()
    #     # assign binary to decimal and convert 
    #     binary_num = decimal
        
    #     # get the decimal from reversed binary
    #     decimal += 1
        
    # #return result
    # return result