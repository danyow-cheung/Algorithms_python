class Solution(object):
    def diStringMatch(self, s):
        """
        :type s: str
        :rtype: List[int]
        """

        res = [i for i in range(len(s)+1)]
        print(res)
        left = -1

        for i in range(len(s)):
            if s[i]=='D':
                res.insert(i,res[left])
                left-=1


        print(res[:len(s)+1])

s = 'IDID'
s ='III'
s ='DDI'
obj = Solution().diStringMatch(s)
