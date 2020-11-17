#1. Two Sum

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        passed = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in passed.keys():
                return [i, passed[diff]]
            passed[nums[i]] = i
