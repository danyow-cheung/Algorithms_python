import collections


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        count = collections.Counter(s)
        print(count)
        for i in count.values():
            print(i)
            ans += i/2*2
            if ans%2==0 and i%2==1:
                ans+=1
        return ans



s = "abccccdd"
s = 'ccc'
obj = Solution().longestPalindrome(s)