# https://leetcode.com/problems/reverse-string/
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # 파이썬 내장 함수 이용
        s.reverse()

        # 투포인터 이용한 방식
        # for i in range(len(s)//2):
        #     s[i], s[-(i+1)] = s[-(i+1)], s[i]
