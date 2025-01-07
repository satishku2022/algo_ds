'''
Given a string, write a function that uses a stack to reverse the string. The function should return the reversed string.

Examples

Example 1:

Input: "Hello, World!"
Output: "!dlroW ,olleH"
'''


class Solution:
    def reverseString(self, s):
        stack = []
        for ch in s:
            stack.append(ch)
        return "".join(stack[::-1])

input = "Hello, World!"
sol = Solution()
print(sol.reverseString(input))
