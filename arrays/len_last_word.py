class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        stack = []
        maxlen = 0

        for ch in s:
            if ch == " " and stack:
                maxlen = len(stack)
                stack = []
            if ch != " ":
                stack.append(ch)

        if stack:
            return len(stack)
        else:
            return maxlen




