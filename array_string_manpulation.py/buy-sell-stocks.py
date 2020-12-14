"""
You are given the prices of a stock, in the form of an array of integers, prices. Let's say that prices[i] is the price of the stock on the ith day (0-based index). Assuming that you are allowed to buy and sell the stock only once, your task is to find the maximum possible profit (the difference between the buy and sell prices).

Note: You can assume there are no fees associated with buying or selling the stock.

Example

For prices = [6, 3, 1, 2, 5, 4], the output should be buyAndSellStock(prices) = 4.

It would be most profitable to buy the stock on day 2 and sell it on day 4. Thus, the maximum profit is prices[4] - prices[2] = 5 - 1 = 4.

For prices = [8, 5, 3, 1], the output should be buyAndSellStock(prices) = 0.

Since the value of the stock drops each day, there's no way to make a profit from selling it. Hence, the maximum profit is 0.

For prices = [3, 100, 1, 97], the output should be buyAndSellStock(prices) = 97.

It would be most profitable to buy the stock on day 0 and sell it on day 1. Thus, the maximum profit is prices[1] - prices[0] = 100 - 3 = 97.

Input/Output

[execution time limit] 4 seconds (py3)

[input] array.integer prices

Guaranteed constraints:
1 ≤ prices.length ≤ 105,
1 ≤ prices[i] ≤ 106.

[output] integer

The maximum possible profit.
"""

# if you need the index, do a range loop. If you need the value, do a for/in loop. If you need both, do an enumerate (returns index, and value)


def buyAndSellStock(prices):        #O(log^n)
    # take the indices of buy/sell and subtract to get highest profit
    # iterate and compare numbers - all the other numbers
    # check to see if array is > 
    if prices == sorted(prices, reverse=True) or len(prices) < 2:
        return 0
        
    # initialize a variable to hold the highest profit
    highest_profit = prices[1] - prices[0]
    # initialze to hold the smallest number
    smallest_num = prices[0]
    
    # range loop to start at first index
    for i in range(1, len(prices)):
        # check is selected number - smallest is larger than the highest profit
        profit = prices[i] - smallest_num
        # going to check the highest profit
        if profit > highest_profit:
            highest_profit = profit
            # only going to update the smallest num occasionaly, check it once
        if prices[i] < smallest_num:
            smallest_num = prices[i]
    return highest_profit


    # --------- Did NOT pass hidden test ---------------->>>>>>>> O(n^2)
    # # take the indices of buy/sell and subtract to get the highest profit
    # # iterate and compare numbers - all the other numbers
    
    # max_profit = 0
    
    # # iterate a nested loop - to check buy/sell days
    # # first loop to get buy day
    # for buy_day, buy_price in enumerate(prices):
    #     # print(buy_day, buy_price)
    #     for sell_day, sell_price in enumerate(prices[buy_day + 1:]):
    #         # print(f"Sell days {prices[buy_day + 1:]}")
    #         # initialize a profit
    #         profit = 0
    #         #if buy_day != sell_day:
    #         # sell price - the buy price = days profit
    #         profit = sell_price - buy_price
    #         #print(profit)
    #         # check if profit is greater than the max profit
    #         if profit > max_profit:
    #             # print(f"Buy-price {buy_price}, Sell-price {sell_price}")
    #             # print(f"Profit {profit}, max_profit {max_profit}")
    #             # max profit equals profit
    #             max_profit = profit
    # return max_profit
        
