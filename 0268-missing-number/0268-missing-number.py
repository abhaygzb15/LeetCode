class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int"""
       
        n = len(nums)
        L = set(nums)
        for i in range(n + 1):
            if i not in L:
                return i
