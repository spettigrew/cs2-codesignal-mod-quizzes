"""
Note: Your solution should have O(l1.length + l2.length) time complexity, since this is what you will be asked to accomplish in an interview.

Given two singly linked lists sorted in non-decreasing order, your task is to merge them. In other words, return a singly linked list, also sorted in non-decreasing order, that contains the elements from both original lists.

Example

For l1 = [1, 2, 3] and l2 = [4, 5, 6], the output should be
mergeTwoLinkedLists(l1, l2) = [1, 2, 3, 4, 5, 6];
For l1 = [1, 1, 2, 4] and l2 = [0, 3, 5], the output should be
mergeTwoLinkedLists(l1, l2) = [0, 1, 1, 2, 3, 4, 5].
Input/Output

[execution time limit] 4 seconds (py3)

[input] linkedlist.integer l1

A singly linked list of integers.

Guaranteed constraints:
0 ≤ list size ≤ 104,
-109 ≤ element value ≤ 109.

[input] linkedlist.integer l2

A singly linked list of integers.

Guaranteed constraints:
0 ≤ list size ≤ 104,
-109 ≤ element value ≤ 109.

[output] linkedlist.integer

A list that contains elements from both l1 and l2, sorted in non-decreasing order.

"""

# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def mergeTwoLinkedLists(l1, l2):
    # create empty node to hold the new merged list
    merged_node = ListNode(0)
    # end will hold the end node
    end = merged_node
    while True:
        # if either list becomes empty join lists
        if l1 is None:
            end.next = l2
            break
        if l2 is None:
            end.next = l1
            break
        # merge the smaller list to the end of the larger and create a head from the merged list
        if l1.value <= l2.value:
            end.next = l1
            l1 = l1.next
        else:
            end.next = l2
            l2 = l2.next
        # iterate the end node
        end = end.next
    return merged_node.next


# ------------- Alternative Code ----------------->>>>>
# iterate through the linked list
    # make an output list and add to that
    # if l1 is None and l2 is None:
    #     return None
    
    # if l2 is None:
    #     return l1
        
    # if l1 is None:
    #     return l2
        
    # out = None          # output head. Head of the new list.
    # cur_l1 = l1         # current position in l1 to loop through existing l1 # Same for l2
    # cur_l2 = l2
              
    # if cur_l1.value <= cur_l2.value:
    #     out = ListNode(cur_l1.value)
    #     cur_l1  = cur_l1.next
    # else:
    #     out = ListNode(cur_l2.value)
    #     cur_l2 = cur_l2.next
        
    # tail = out  # tail of the merged list and use that to add new items to the list
       
    # while cur_l1 or cur_l2:
    #     if cur_l1 is None:
    #         new_node = ListNode(cur_l2.value)
    #         tail.next = new_node
    #         tail = tail.next
    #         cur_l2 = cur_l2.next
    #         continue
    #     if cur_l2 is None:
    #         new_node = ListNode(cur_l1.value)
    #         tail.next = new_node
    #         tail = tail.next
    #         cur_l1 = cur_l1.next
    #         continue
            
    #     if cur_l1.value <= cur_l2.value:
    #         new_node = ListNode(cur_l1.value)
    #         tail.next = new_node
    #         tail = tail.next
    #         cur_l1 = cur_l1.next
    #     else:
    #         new_node = ListNode(cur_l2.value)
    #         tail.next = new_node
    #         tail = tail.next
    #         cur_l2 = cur_l2.next
    # return out



