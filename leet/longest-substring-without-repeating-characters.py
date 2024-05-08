# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if 1 == len(s):
            return 1
        i, j = 0, 1
        ans = 0
        while i < j and j <= len(s):
            tmp = len(set(s[i:j]))
            if len(s[i:j]) == tmp:
                j += 1
                if tmp > ans:
                    ans = tmp
            else:
                i += 1

        return ans
