class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        maxlen = 0

        for n in numset:
            if n-1 not in numset:
                count = 0
                m = n
                while True:
                    count += 1
                    m = m+1
                    if m not in numset:
                        break
                maxlen = max(maxlen, count)

        return maxlen

            
