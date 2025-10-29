from functools import reduce

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        for i in range(len(nums)):
            prod = reduce(lambda x, y: x * y, nums[0:i]+nums[i+1:len(nums)])
            output.append(prod)
        return output

      
# more efficient solution

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        accumprod = 1
        for i in range(len(nums)):
            prefix.append(accumprod)
            accumprod *= nums[i]
            

        suffix = []
        accumprod = 1
        for i in range(len(nums)-1, -1, -1):
            suffix.insert(0, accumprod)
            accumprod *= nums[i]
        
        output = []
        for i in range(len(nums)):
            output.append(prefix[i] * suffix[i])

        return output

