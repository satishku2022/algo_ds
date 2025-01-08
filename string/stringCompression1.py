from typing import List

class Solution:


    '''

        2 ptr
        l - 0
        r ----------
    '''



    def compress(self, chars: List[str]) -> int:
        read, write, length = 0, 0, len(chars)
        '''
            read tracks of iterating
            write traks writing 
            
        '''
        print(chars)

        while read < length:
            read_next = read + 1
            while read_next < length and chars[read_next] == chars[read]:
                read_next += 1
            # read next -> 2
            print(chars[read],read_next, read)
            chars[write]=chars[read]
            write+=1
            val = read_next-read
            if val > 1:
                chlist = list(str(val))
                for ch in chlist:
                    chars[write]=ch
                    write+=1

            read = read_next

        return len(chars[:write])



    def compressBasic2(self, chars: List[str]) -> int:
        curr_ch = None
        count = 0
        stack = []
        for ch in chars:
            if ch != curr_ch:
                if curr_ch is not None:
                    stack.append(curr_ch)
                    if count > 1:
                        chlist = list(str(count))
                        for ch_ in chlist:
                            stack.append(ch_)
                count = 1
                curr_ch = ch
            else:

                count += 1
        stack.append(curr_ch)
        if count > 1:
            chlist = list(str(count))
            for ch_ in chlist:
                stack.append(ch_)
        chars = stack
        print(chars)
        return len("".join(chars))



    def compressBasic(self, chars: List[str]) -> int:
        curr_ch = None
        count = 0
        stack = []
        for ch in chars:
            if ch != curr_ch:
                if curr_ch is not None:
                    stack.append(curr_ch)
                    if count > 1:
                        stack.append(str(count))
                count = 1
                curr_ch = ch
            else:

                count += 1
        stack.append(curr_ch)
        if count > 1:
            stack.append(str(count))
        print(stack)
        return len("".join(stack))


sol  = Solution()
input =   ["a","a","b","b","b","c","c","c"]
print(sol.compress(input))

'''
443. String Compression
Attempted
Medium

Topics

Companies

Hint
Given an array of characters chars, compress it using the following algorithm:

Begin with an empty string s. For each group of consecutive repeating characters in chars:

If the group's length is 1, append the character to s.
Otherwise, append the character followed by the group's length.
The compressed string s should not be returned separately, but instead, be stored in the input character array chars. Note that group lengths that are 10 or longer will be split into multiple characters in chars.

After you are done modifying the input array, return the new length of the array.

You must write an algorithm that uses only constant extra space.



Example 1:

Input: chars = ["a","a","b","b","c","c","c"]
Output: Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
Explanation: The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".
Example 2:

Input: chars = ["a"]
Output: Return 1, and the first character of the input array should be: ["a"]
Explanation: The only group is "a", which remains uncompressed since it's a single character.
Example 3:

Input: chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
Output: Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].
Explanation: The groups are "a" and "bbbbbbbbbbbb". This compresses to "ab12".

'''