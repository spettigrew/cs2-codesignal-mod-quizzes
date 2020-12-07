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

    # def csAnythingButFive(start, end):
    #     # this is fairly tricky. We basically want to scan all numbers from start to end, and check that they do not have the digit 5
    #     # the easiest thing to do here, is to generate a range of numbers, convert them to strings, and check if the string contains the character "5"
        
    #     # generate the range (remember the question says end is inclusive, so use end + 1 !)
    #     num_range = range(start, end + 1)
        
    #     # now lets just count all numbers that do not have the character 5 in it
    #     # we cant easily check for digits using integers, but strings are easy! lets convert the numbers to strings
    #     number_count = 0
    #     for num in num_range:
    #         # convert the number to a string, and check if it has the character 5
    #         num_str = str(num)
    #         if '5' not in num_str:
    #             number_count += 1
        
    #     return number_count


