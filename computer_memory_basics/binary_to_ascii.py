"""
Given a binary string (ASCII encoded), write a function that returns the equivalent decoded text.

Every eight bits in the binary string represents one character on the ASCII table.

Examples:

csBinaryToASCII("011011000110000101101101011000100110010001100001") -> "lambda"
01101100 -> 108 -> "l"
01100001 -> 97 -> "a"
01101101 -> 109 -> "m"
01100010 -> 98 -> "b"
01100100 -> 100 -> "d"
01100001 -> 97 -> "a"
csBinaryToASCII("") -> ""
Notes:

The input string will always be a valid binary string.
Characters can be in the range from "00000000" to "11111111" (inclusive).
In the case of an empty input string, your function should return an empty string.
[execution time limit] 4 seconds (py3)

[input] string binary

[output] string
"""

def csBinaryToASCII(binary):
    # every 8 bits represents an ascii char - convert a binary to a string
    # break up string into bits of 8
    # Loop over the string and get substring size of 8
    # increment index by 8
    # per byte
        # convert to decimal
        # convert to char
    answer_string = ""
    i = 0
    #loop over binary string in parts of 8
    while i < len(binary):
        #create the current stubstring
        byte = binary[i : i + 8]
        # convert to decimal
        decimal = int(byte, 2)
        # convert to char
        char = chr(decimal)
        
        print(char)
        #print(byte)
        #print(int(byte, 2)) # Conver the binary to a decimal
        # add to answer to string
        answer_string += char
        i += 8
        #return the answer string
    return answer_string
            
    
    
    # # binary to decimal to ascii_char
    
    # # set an answer string to empty
    # ans_string = ""

    # # iterate through the binary string
    # # < 7 in binary string represents a char
    
    # # get ascii char
    
    # # return ans_string
    # return ans_string

    # take each bit and change it to a char        for loop len of binary divided by 8 to reach 8-bit
    # return "".join(chr(int(binary[i*8:i*8+8], 2)) for i in range(len(binary)//8))