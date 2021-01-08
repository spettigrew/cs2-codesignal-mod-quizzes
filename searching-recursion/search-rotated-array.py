"""
Given an integer array nums sorted in ascending order, and an integer target.

Suppose that nums is rotated at some pivot unknown to you beforehand (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You should search for target in nums and if found return its index, otherwise return -1.

Example 1:
Input: nums = [6,7,0,1,2,3,4,5], target = 0
Output: 2

Example 2:
Input: nums = [6,7,0,1,2,3,4,5], target = 3
Output: 5

Example 3:
Input: nums = [1], target = 0
Output: -1

Note:

1 <= nums.length < 100
1 <= nums[i] <= 100
All values of nums are unique.
[execution time limit] 4 seconds (py3)

[input] array.integer nums

[input] integer target

[output] integer
"""

def csSearchRotatedSortedArray(nums, target):
    # initiate a start and ending index
    start_idx = 0
    end_idx = len(nums) - 1
    # set up a while loop to find the target
    while not end_idx < start_idx:
        # the middle index = min + max divided by 2
        mid_idx = (end_idx + start_idx) // 2
        # if mid index equal target, return mid index
        if nums[mid_idx] == target:
            # we found it! Return the middle index
            return mid_idx
        # if the number at the start of the index is less than the middle
        elif nums[start_idx] <= nums[mid_idx]:
            # target must be less than the number between the start and at the middle index 
            if nums[start_idx] <= target < nums[mid_idx]:
                # move end index to the middle
                end_idx = mid_idx
            else:
                # move the start of the index to the middle plus one
                start_idx = mid_idx + 1
        else:
            # if the end of the index is less than the target and the middle index
            if nums[end_idx - 1] >= target > nums[mid_idx]:
                # set the start to middle plus one
                start_idx = mid_idx + 1
            else:
                # move end index to the middle
                end_idx = mid_idx
        # if target is not there, return minus one (edge case)
    return -1

# ------------------- Linear Approach ------------------
    # start_idx = 0
    # for i in range(len(nums)):
    #     if nums[i] == target:
    #         return i
    # return -1

# --------- Leetcode solution -------------------------
# class Solution(object):
#     def pivotIndex(self, nums):
#         S = sum(nums)
#         leftsum = 0
#         for i, x in enumerate(nums):
#             if leftsum == (S - leftsum - x):
#                 return i
#             leftsum += x
#         return -1