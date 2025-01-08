
'''
Example 1:

Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 2.
It does not matter what you leave beyond the returned k (hence they are underscores).
Example 2:

Input: nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5, nums = [0,1,4,0,3,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.
Note that the five elements can be returned in any order.
It does not matter what you leave beyond the returned k (hence they are underscores).
 
'''

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = sum([1 for x in nums if x!= val])

        # two pointer
        l = 0
        r = len(nums) - 1
        while l < r:
            while l < len(nums) and nums[l] != val:
                l += 1
            while nums[r] == val and r >= 0:
                r -= 1
            if l < r:
                nums[r], nums[l] = nums[l], nums[r]
                l += 1
                r -= 1

        print(nums, l, r)
        return count





