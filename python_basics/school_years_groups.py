"""
Imagine a school that children attend for years. In each year, there are a certain number of groups started, marked with the letters. So if years = 7 and groups = 4For the first year, the groups are 1a, 1b, 1c, 1d, and for the last year, the groups are 7a, 7b, 7c, 7d.

Write a function that returns the groups in the school by year (as a string), separated with a comma and space in the form of "1a, 1b, 1c, 1d, 2a, 2b (....) 6d, 7a, 7b, 7c, 7d".

Examples:

csSchoolYearsAndGroups(years = 7, groups = 4) ➞ "1a, 1b, 1c, 1d, 2a, 2b, 2c, 2d, 3a, 3b, 3c, 3d, 4a, 4b, 4c, 4d, 5a, 5b, 5c, 5d, 6a, 6b, 6c, 6d, 7a, 7b, 7c, 7d"
Notes:

1 <= years <= 10
1 <= groups <=26
[execution time limit] 4 seconds (py3)

[input] integer years

[input] integer groups

[output] string
"""

def csSchoolYearsAndGroups(years, groups):

    a = "a"
    string = ""
    for i in range(years):
      for g in range(groups):
          string += str(i +1) + a + ", "
          a = chr(ord(a) + 1)
      a = "a"
    string.strip()
    return string[:-2]

#     # start with years and loop from 1 to 7 years
#     year_groups = 0
#     #create a list of all chars from a to g (z)
#     # characters = list(string.ascii_lowercase)
#     characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

#     # start with years, then go to groups.
#     for year in range(1, years + 1):
#         for group in range(0, groups):
#             year_group_str = str(year) + characters[group_number]
#             if year == years and group_number == groups -1:
#                 year_groups += year_group_str
#             else:
#                 year_groups += year_group_str + ','

#     # year_groups = year_groups.strip(', ')
#     return year_groups

# # for y in range(1, years + 1):
# #         for g in range(groups):
# #             if result != "":
# #                 result += ", "

# # Another option to strip at the end with slices:
# # result = result[:-2]
