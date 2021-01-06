"""
Given a string sequence consisting of the characters '(', ')', '[', ']', '{', and '}'. Your task is to determine whether or not the sequence is a valid bracket sequence.

The Valid bracket sequence is defined in the following way:

An empty bracket sequence is a valid bracket sequence.
If S is a valid bracket sequence then (S), [S] and {S} are also valid.
If A and B are valid bracket sequences then AB is also valid.
Example

For sequence = "()", the output should be validBracketSequence(sequence) = true;
For sequence = "()[]{}", the output should be validBracketSequence(sequence) = true;
For sequence = "(]", the output should be validBracketSequence(sequence) = false;
For sequence = "([)]", the output should be validBracketSequence(sequence) = false;
For sequence = "{[]}", the output should be validBracketSequence(sequence) = true.
Input/Output

[execution time limit] 4 seconds (py3)

[input] string sequence

A bracket sequence, consisting of the characters (, ), [, ], {, and }.

Guaranteed constraints:
0 ≤ sequence.length ≤ 106.

[output] boolean

true if sequence is a valid bracket sequence and false otherwise.
"""

def validBracketSequence(sequence):
    # initiate an empty array check
    check = []
    # if the sequence brackets are blank, return True
    if sequence == "":
        return True
    # if the 0 indice is a closing bracket, return False
    if sequence[0] == ")" or sequence[0] == "}" or sequence[0] == "]":
       return False
    
    # iterate through the pairs of brackets in sequence
    for parens in sequence:
        # if the brackets are blank, continue
        if parens == " ":
            continue
        # if there are opening brackets, add a closing bracket
        if parens == "(" or parens == "{" or parens == "[":
            check.append(parens)
        # check if the opening bracket is the last item in the array and the opening closing are sequential
        elif parens == ")" and check[-1] == "(" or parens == "}" and check[-1] == "{" or parens == "]" and check[-1] == "[":
            # if the length of the check equals 0, return false
            if len(check) == 0:
                return False
            # or pop off the last item
            else:
                check.pop()
        # if item still exists, return False
        else:
            return False
    
    if check:
        return False
    return True
        

