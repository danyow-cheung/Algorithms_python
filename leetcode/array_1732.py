class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        res = [0]
        for i in range(len(gain)):

            # print(i)
            res.append(res[i]+gain[i])
        print(res)
        print(max(res))
gain = [-5,1,5,0,-7]
obj = Solution().largestAltitude(gain)