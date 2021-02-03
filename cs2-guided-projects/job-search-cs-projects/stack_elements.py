"""
Write a function sortStack that receives a stack of integers and returns another stack containing those same integers in sorted order. You may use at most one additional stack to hold items, but you may not copy the elements into any other data structure.
"""

class Stack:
    def __init__(self):
        self.storage = []

# put element on top of the stack
    def push(self, item):
        self.storage.append(item)

# take element off of the top of the stack
    def pop(self): 
        return self.storage.pop()

# just look at (peek) at the element on top of the stack
    def peek(self):
        return self.storage[::-1]

# no elements left in the stack
    def isEmpty(self):
        return self.storage.length == 0

    def print_contents(self):
        for elem in self.storage:
            print(elem)

def sort_stack(input_stack: Stack): # O(n^2)
    # iterate through the stack until stack is empty
    output_stack = Stack()

    while not input_stack.is_empty():
        # take out first element from our input stack
        temp_ele = input_stack.pop()
        # compare with the output stack
        #if empty OR if temp element is smaller than the top element of the output stack
        while not output_stack.is_empty() and temp_ele > output_stack.peek():
            input_stack.push(output_stack.pop())

        output_stack.push(temp_ele)
            # put temp element into the output stack
            # take out temp element into the output stack
        # the temp element is larger than the top:
            # keep putting the top of the output stack onto the input stack
            # until temp element is smaller than the top
    return output_stack

s = Stack()
s.push(4)
s.push(10)
s.push(8)
s.push(5)
s.push(1)
s.push(6)

sorted_stack = sort_stack(s)

sorted_stack.print_contents()  # should print 1, 4, 5, 6, 8, 10