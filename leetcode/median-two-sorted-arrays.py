import statistics

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        res = []
        i, j = 0,0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                res.append(nums1[i])
                i += 1
            else:
                res.append(nums2[j])
                j += 1
        
        while i < len(nums1):
            res.append(nums1[i])
            i += 1

        while j < len(nums2):
            res.append(nums2[j])
            j += 1

        return statistics.median(res)