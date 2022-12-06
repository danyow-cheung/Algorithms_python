class Solution(object):
    def minimumMoves(self, s):
        """
        :type s: str
        :rtype: int
        https://leetcode.com/problems/minimum-moves-to-convert-string/

        """
        if not 'X' in s:
            return 0

        ans = []
        left =0

        while left<len(s):
            if s[left]!="X":
                ans.append(left)
            left += 1

        # return len(ans)+1
        print(ans)


s = "XXX"
# s = 'XX0X'
# s = "OXOX"
obj = Solution().minimumMoves(s)