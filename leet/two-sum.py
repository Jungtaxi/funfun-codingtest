# https://leetcode.com/problems/two-sum/description/
from itertools import combinations


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nCr = combinations(range(len(nums)), 2)
        for i in nCr:
            if nums[i[0]] + nums[i[1]] == target:
                return list(i)
