'''
Given a positive integer n, write a function that returns its binary equivalent as a string. The function should not use any in-built binary conversion function.

Examples

Example 1:

Input: 2
Output: "10"
Explanation: The binary equivalent of 2 is 10.
Example 2:

Input: 7
Output: "111"
Explanation: The binary equivalent of 7 is 111.

7 -> 111
8 -> 1000
 8 - 0* 2^0 + 0*2^1 + 0*2^2 +1*2^3

 8/8 == 1

'''
import math

class Solution:
    def dec2bin(self, val):
        i = 0
        while math.pow(2,i) <= val:
            i += 1
        # i is the first value where 2^i > val so we can go upto i-1
        print("i is :" , i)
        stack = []
        #8 -> 1
        for index in range(i-1,-1,-1):
            print("index ",index)
            cand = math.pow(2,index)
            if val > 0 and val >= cand:
                stack.append("1")
                val = val - cand
            else:
                stack.append("0")

        return int("".join(stack))

s = Solution()
result = s.dec2bin(5)
print(result)