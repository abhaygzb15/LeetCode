class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        L = []
        for i in range(len(nums)):
            if nums[i] == target:
                L.append(i)
        if len(L) == 0:
            return [-1, -1]
        else:
            return [L[0], L[-1]]
