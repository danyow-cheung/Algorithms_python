class Solution(object):
    def countPoints(self, rings):
        """
        :type rings: str
        :rtype: int
        """
        d=  {}
        res = 0
        for i in range(10):
            d[i] = [0,0,0]
        print(d)
        for i in range(0,len(rings),2):
            j = int(rings[i+1])
            if rings[i] =='R':
                d[j][0]+=1
            elif rings[i]=='G':
                d[j][1]+=1
            else:
                d[j][2]+=1
        print(d)

        for v in d.values():
            print(v)
            if min(v)>0:
                res+=1
        print(res)
rings = "B0B6G0R6R0R6G9"
obj = Solution().countPoints(rings)