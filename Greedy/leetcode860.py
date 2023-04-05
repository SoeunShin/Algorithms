# LeetCode 860. Lemonade Change

"""
At a lemonade stand, each lemonade costs $5. Customers are standing in a queue
to buy from you and order one at a time (in the order specified by bills).
Each customer will only buy one lemonade and pay with either a $5, $10, or $20 bill.
You must provide the correct change to each customer so that the net transaction is that the customer pays $5.

Note that you do not have any change in hand at first.

Given an integer array bills where bills[i] is the bill the ith customer pays,
return true if you can provide every customer with the correct change, or false otherwise.

Input: bills = [5,5,5,10,20]
Output: true

Input: bills = [5,5,10,10,20]
Output: false
"""

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        ch5 = ch10 = 0

        for i in bills:
            if i == 5:
                ch5 += 1
            elif i == 10:
                if ch5 == 0:
                    return False   
                ch10 += 1
                ch5 -= 1             
            else: # i == 20
                if ch5 > 0 and ch10 > 0:
                    ch5 -= 1
                    ch10 -= 1
                elif ch5 >= 3:
                    ch5 -= 3
                else:
                    return False
        return True
