import collections


class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        res = 0


        counts = collections.Counter(stones)
        for key,value in counts.items():
            if key in jewels:
                print(key,value)
                res += value
        print(res)

jewels = "aA"
stones = "aAAbbbb"
obj = Solution().numJewelsInStones(jewels,stones)