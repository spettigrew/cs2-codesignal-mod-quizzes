"""
Given two strings, determine if they share a common substring. A substring may be as small as one character.

Example
s1 = 'and'
x2 = 'art

These share the common substring a.
s1 = 'be'
s2 = 'cat'



These do not share a substring.

Function Description

Complete the function twoStrings in the editor below.

twoStrings has the following parameter(s):

string s1: a string
string s2: another string
Returns

string: either YES or NO
Input Format

The first line contains a single integer p, the number of test cases.

The following p pairs of lines are as follows:

The first line contains string s1.
The second line contains string s2.
Constraints

s1 and s2 consist of characters in the range ascii[a-z].
1 <= p <= 10
1 <= |s1|, |s2| <= 10^5

Output Format

For each pair of strings, return YES or NO.

Sample Input

2
hello
world
hi
world
Sample Output

YES
NO
Explanation

We have p = 2 pairs to check:

1. s1 = 'hello', s2 = 'world'. The substrings "o" and "1" are common to both strings.
2. a = "hi", b = "world". s1 and s2 share no common substrings.
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the twoStrings function below.
def twoStrings(s1, s2):
    # time: O(n+m) where n = [s1] m = [s2]
    # time: O([s1] + [s2])
    # O(m)
    # add all the letters from s2 intoa hash table
    # create a set {"a", "b", "c", "d"} 
    set2 = set()

    for word1 in s2:
        set2.add(word1)

    #O(n)
    # loop through all the letters in s1
    for character in s1:
        #O(1)
        # we can take a single letter of s1, and check if it's contained in our hash table
        return "Yes"
    return "No"


# ---------- Other question in instruction ---------->
# what are the common substrings between s1 & s2
def commonSubstrings(s1, s2):
    # create a hashtable to find all substrings of s1
    subs1 = findSubstrings(s1)
    subs2 = findSubstrings(s2)
    common = set()

    for sub in subs1:
        if sub in subs2:
            common.add(sub )

    return common

def findSubstrings(s):
    subs = dict()
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            subs.add(s[i:j])

    return subs

print(commonSubstrings("abcd", "abcef"))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)

        fptr.write(result + '\n')

    fptr.close()
