import collections


class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        count = collections.Counter(text)
        ans = min(count['b'],count['a'],count['l']//2,count['o']//2,count['n'])
        print(ans)
        return ans

text = "nlaebolko"
text = "loonbalxballpoon"
obj = Solution().maxNumberOfBalloons(text)