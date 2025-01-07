from typing import List

'''
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

 

Example 1:

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.


nums1 m+n n 0's 
nums2 n 

m is 0 , n is not 

 1 4 5 0 0 
 
 2 3 
 
 step 1 
 
  1 4 0 0 5
  2 3 
  
   step 2
   
  1 0 0 4 5 
  2 3 
  
   step 3 
  1 0 3 4 5 
  
   step 4 
  1 2 3 4 5
  
 1 2 3 4 5 
'''


class Solution:

    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        last = m + n - 1

        # Merge in reverse order
        while m > 0 and n > 0:
            if nums1[m - 1] > nums2[n - 1]:
                nums1[last] = nums1[m - 1]
                m -= 1
            else:
                nums1[last] = nums2[n - 1]
                n -= 1
            last -= 1

        # Fill nums1 with leftover nums2 elements
        while n > 0:
            nums1[last] = nums2[n - 1]
            n -= 1
            last -= 1
        print(nums1)

s = Solution()
nums1 = [1,0]
m = 1
nums2 = [2]
n = 1
s.merge(nums1,m,nums2,n)



