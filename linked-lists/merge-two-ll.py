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

# ----------- Alternate code from Artem - cs2 -----------------
    # l1 and l2 are pointers to the linked list, not the actual list
    # duplicate the linked lists before merging
    # LL's are just nodes holding a variable. Need to return the head of the LL.

    new_list_head = None
    new_list_tail = None

    # traverse these lists, until they are both None
    # each time we move either l1 or l2 forward:
    # we duplicate that node, and add to the end of new_list

    while l1 is not None or l2 is not None:
        # first: figure out which node we are adding
        new_node = None
        # compare values at l1 and l2
        if not l1:
            # if l1 does not exist, use l2 value
            new_node = ListNode(l2.value)
            l2 = l2.next
        elif not l2:
            new_node = ListNode(l1.value)
            l1 = l1.next
        elif l1.value <= l2.value:
            new_node = ListNode(l1.value)
            l1 = l1.next
        else:
            new_node = ListNode(l2.value)
            l2 = l2.next

        # Actually add the node to the end of the list
        # handle the case when the new_list is empty
        if new_list_head is None:
            new_list_head = new_node
        else:
            # add a new node to the existing linked list
            new_list_tail.next = new_node
            new_list_tail = new_node


    return new_list_head


# ------------- Alternative Code from CS part one-------- -->>>>>
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



