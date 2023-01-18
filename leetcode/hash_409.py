import collections
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        for i in collections.Counter(s).values():
            print(i)
            ans += i/2 * 2
            # ans是偶数但是element是奇数
            if ans %2==0 and i %2==1:
                ans += 1
        print(ans)
s = "abccccdd"
# s = 'a'
s = "aaaaaccc"
obj = Solution().longestPalindrome(s)