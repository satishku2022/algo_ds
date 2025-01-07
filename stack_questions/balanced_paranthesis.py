'''

Given a string s containing (, ), [, ], {, and } characters. Determine if a given string of parentheses is balanced.

A string of parentheses is considered balanced if every opening parenthesis has a corresponding closing parenthesis in the correct order.

Example 1:

Input: String s = "{[()]}";
Expected Output: true

Example 2:

Input: string s = "{[}]";
Expected Output: false

Example 3:

Input: String s = "(]";
Expected Output: false
'''


class Solution:
    def isValid(self, s):
        stack = []
        bracket_map = { ")":"(", "}":"{","]":"["}

        # iter over string ch by ch
        for ch in s:

            if ch not in bracket_map.keys():
                stack.append(ch)
                continue
            if not stack:
                return False
            if stack and stack[-1]!=bracket_map[ch]:
                return False
            if stack and stack[-1]==bracket_map[ch]:
                stack.pop()
        return len(stack)==0



s = "{[()]]}"
sol = Solution()
result = sol.isValid(s)
print(f"result {result}")