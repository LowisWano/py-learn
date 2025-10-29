from functools import reduce

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        for i in range(len(nums)):
            prod = reduce(lambda x, y: x * y, nums[0:i]+nums[i+1:len(nums)])
            output.append(prod)
        return output