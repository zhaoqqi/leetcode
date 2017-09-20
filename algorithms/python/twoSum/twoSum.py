class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        i = 1
        for num in nums:
            if (target-num) in nums[i:]:
                if num == (target-num):
                    index2 = nums[i:].index(target-num)+i
                else:
                    index2 = nums.index(target-num)
                return [nums.index(num), index2]
            i = i + 1