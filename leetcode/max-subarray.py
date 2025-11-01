class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        globmax, currmax = nums[0], nums[0]
        for i in range(1, len(nums)):
            currmax = max(nums[i], currmax + nums[i])
            if currmax > globmax:
                globmax = currmax
        return globmax