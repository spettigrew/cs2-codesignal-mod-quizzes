"""
For a given positive integer n determine if it can be represented as a sum of two Fibonacci numbers (possibly equal).

Example

For n = 1, the output should be
fibonacciSimpleSum2(n) = true.

Explanation: 1 = 0 + 1 = F0 + F1.

For n = 11, the output should be
fibonacciSimpleSum2(n) = true.

Explanation: 11 = 3 + 8 = F4 + F6.

For n = 60, the output should be
fibonacciSimpleSum2(n) = true.

Explanation: 60 = 5 + 55 = F5 + F10.

For n = 66, the output should be
fibonacciSimpleSum2(n) = false.

Input/Output

[execution time limit] 4 seconds (py3)

[input] integer n

Guaranteed constraints:
1 ≤ n ≤ 2 · 109.

[output] boolean

true if n can be represented as Fi + Fj, false otherwise.
"""

def fibonacciSimpleSum2(n):

    #UPER - find 2 fib numbers that are equal (sum) to a num in the fib sequence
        # f(i) = f(i-1) + f(i-2)
        # base cases
            # i = 0, f(0) = 0, f(1) = 1
        # Plan - index placement does not matter, just need 2 numbers to equal the sum
            # target - num = complement. IF it complement number exists
            # if we have two numbers, return true
            # if complement number does not exist, continue
    fibs = [0, 1]
    # iniiate a set - like a dict where we just have keys
    fibs_set = {0, 1}
    i = 2
    # generate the list of the fib sequence
    # while True loop, go through, if not break out of the loop
    while True:
        # assign a new num to fib index -1 + fib index-2
        new_fib_num = fibs[i-1] + fibs[i-2]
        # if the new num is greater than n (or target)
        if new_fib_num > n:
            # exit the loop
            break
        # add the new num to the fib sequence
        fibs.append(new_fib_num)
        # loop over the set and add
        fibs_set.add(new_fib_num)
        # index plus one
        i +=1

    # look at each number, 
    # get it's compliment
    # check if compliment exisits or not
    for fib_num in fibs:
        compliment = n - fib_num
        # check if this compliment exists in the fibs array
        if compliment in fibs:
            return True

    return False
    
    # if 0 < n <  5:
    #     return True
    
    # # get the fib sequence up to (n)
    # # initialize the array with the first two digits of 0 & 1
    # sequence = [0, 1]
    # # iterate up to (n) starting at two
    # for i in range(2, n):
    #     # initialize to hold our variables
    #     fib = 0 
    #     # add i-2 in the sequence and i-1 in the sequence
    #     if (i -1) + (i -2) == fib:
    #     # if n >= fib, keep going
    #         if n >= fib:
    #             # append(fib) to the sequence
    #             sequence.append(fib)    
    #         # otherwise if fib is >= to n
    #         else:
    #             if fib >= n:
    #             # break
    #                 break
    #             print(sequence)
                
    #         # check if any of the 2 numbers in the array add up to n
    #         if fib + n == i:
    #             return True
    #     return False
                
       


    # if n <= 0:
    #     return 0
    # elif n == 1:
    #     return 1
    # else:
    #     return fibonacciSimpleSum2(n-1) + fibonacciSimpleSum2(n-2)
