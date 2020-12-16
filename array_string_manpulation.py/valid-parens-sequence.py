"""
You are given a parentheses sequence, check if it's regular.

Example

For s = "()()(())", the output should be
validParenthesesSequence(s) = true;
For s = "()()())", the output should be
validParenthesesSequence(s) = false.
Input/Output

[execution time limit] 4 seconds (py3)

[input] string s

A string, consisting only of '(' and ')'.

Guaranteed constraints:
0 ≤ s.length ≤ 105.

[output] boolean

true is the sequence is regular and false otherwise.    
"""

def validParenthesesSequence(s):    # all tests pass
    #check for parens sequences
    check = []
    if s == "":
        return True
    if s[0] == ')':
        return False
    for paren in s:
        if paren == '(':
            check.append(paren)
        else:
            if len(check) == 0:
                return False
            else:
                check.pop()
    if check != []:
        return False
    return True
            
 # --------- Passing all but one test 273/300 ------------->>>>>

# iterate through string to check for open/close parens
    # storing parens
    # parens_dict = {"(":0, ")":0}
    # # for each paren in s and placing in data structure
    # if s == "":
    #     return True
    # if s[0] == ")":
    #     return False
    # if s[len(s) -1] == "(":
    #     return False 
    # for paren in s:
    #     if paren == "(":
    #         parens_dict[")"] += 1
    #     elif paren == ")":
    #         parens_dict[")"] -= 1
    # if parens_dict[")"] < 0:
    #     return False
    # return True