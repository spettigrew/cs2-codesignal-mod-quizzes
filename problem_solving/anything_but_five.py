"""
Given a start integer and an ending integer (both inclusive), write a function that returns the count (not the sum) of all integers in the range (except integers that contain the digit 5).

Examples:

csAnythingButFive(1, 5) -> 1, 2, 3, 4, -> 4 (there are 4 integers in the range that do not contain the digit 5)
csAnythingButFive(1, 9) -> 1, 2, 3, 4, 6, 7, 8, 9 -> 8
csAnythingButFive(4, 17) -> 4,6,7,8,9,10,11,12,13,14,16,17 -> 12
Notes:

The output can contain the digit 5.
The start number will always be less than the end number (both numbers can also be negative).
[execution time limit] 4 seconds (py3)

[input] integer start

[input] integer end

[output] integer
"""

def csAnythingButFive(start, end):
    # U - count every integer execpt 5

    # set up a new count to start 1 to count integers. inclusive
    count = 1
    # iterate through the array to go through the integers ex. 1-9
    for idx in range(start, end):
        # if 5 is in the string, do not count it
        if "5" not in str(idx):
            # add one number to the string before/after.
            count += 1
    #return count
    return count

