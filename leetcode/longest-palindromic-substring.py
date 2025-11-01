class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""

        for i in range(0, len(s)):
            left = i-1
            right = i+1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            if len(s[left+1:right]) > len(res):
                res = s[left+1:right]

            left = i
            right = i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            if len(s[left+1:right]) > len(res):
                res = s[left+1:right]
        return res