"""
Note: Your solution should have O(n) time complexity, where n is the number of elements in l, since this is what you will be asked to accomplish in an interview.

You have a singly linked list l, which is sorted in strictly increasing order, and an integer value. Add value to the list l, preserving its original sorting.

Note: in examples below and tests preview linked lists are presented as arrays just for simplicity of visualization: in real data you will be given a head node l of the linked list

Example

For l = [1, 3, 4, 6] and value = 5, the output should be
insertValueIntoSortedLinkedList(l, value) = [1, 3, 4, 5, 6];
For l = [1, 3, 4, 6] and value = 10, the output should be
insertValueIntoSortedLinkedList(l, value) = [1, 3, 4, 6, 10];
For l = [1, 3, 4, 6] and value = 0, the output should be
insertValueIntoSortedLinkedList(l, value) = [0, 1, 3, 4, 6].
Input/Output

[execution time limit] 4 seconds (py3)

[input] linkedlist.integer l

A singly linked list of integers sorted in strictly increasing order. Thus, all integers in the list are pairwise distinct.

Guaranteed constraints:
0 ≤ list size ≤ 104,
-109 ≤ element value ≤ 109.

[input] integer value

A single integer value to be inserted into l. It is guaranteed that there is not an element equal to value in l before the insertion is performed.

Guaranteed constraints:
-109 ≤ value ≤ 109.

[output] linkedlist.integer

Return l after inserting value into it, with the original sorting preserved.
"""

# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def insertValueIntoSortedLinkedList(l, value):
    # print(type(l))
    # 'l' is a list node and at our head. Insert new value into the list.
    # Iterate (while loop) to the spot in the list where we want to insert the new value
    # We're at the right spot when the next node is greater than the current value (and the previous is less than)
    # Insert the new value
    # create the new node 
    new_node  = ListNode(value)
    if l is None:
        return ListNode(value)
    
    prev_node = None
    next_node = l

    while next_node is not None and value > next_node.value:
        prev_node = next_node
        next_node = next_node.next      # points to next node in the linked list

    # set the new node.next to the next node
    new_node.next = next_node
    # set previous node.next to new node
    if prev_node is not None:
        prev_node.next = new_node
    else:                           # we're trying to insert at the beginning at the list. Our last edge case (gotcha)
        l = new_node        
    return l

# -------------- Alternative code -----------------------

    # # create a new node with the value
    # node = ListNode(value)
    # # if there is no list return the new node
    # if l == None:
    #     return node
    # else:
    #     # else if the list.value (first item in the list) > the new value
    #     if l.value > value:
    #         # set new values as the first item in the list
    #         node.next = l
    #         return node
    #     else:
    #         # else create a temp value for the current list item and the previous set to None
    #         temp, prev = l, None
    #         # while the there is a next item and current item value is less
    #         # than the value iterate
    #         while temp.next and temp.value <= value:
    #             # set previous to temp and temp to next
    #             prev = temp
    #             temp = temp.next
    #         # check if temp.next is None (last item) and still not larger than the value
    #         if temp.next == None and temp.value <= value:
    #             # if so add the value as the last item in the list since it is the largest
    #             temp.next = node
    #         else:
    #             # else if the next item is larger than the value set the next item as the next item of the new value
    #             node.next = prev.next
    #             # and set the previous item to point to the new value next
    #             prev.next = node
    #         # return the list
    #         return l
