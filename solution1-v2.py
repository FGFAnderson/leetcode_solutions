class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        numIndex = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if target - nums[i] in numIndex: 
                return numIndex[complement], i
            
            numIndex[nums[i]] = i

            