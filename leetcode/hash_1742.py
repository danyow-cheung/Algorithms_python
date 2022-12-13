class Solution(object):
    def countBalls(self, lowLimit, highLimit):
        """
        :type lowLimit: int
        :type highLimit: int
        :rtype: int
        """
        dict_ ={}
        for i in range(lowLimit,highLimit+1):
            cur = self.int2str(i)
            print(i,cur)
            if cur not in dict_:
                dict_[cur]=1
            elif dict_[cur]!=0:
                dict_[cur]+=1
        print(dict_)
        ans = max(dict_.values())
        print(ans)

        return ans 


    def int2str(self,num):
        num = str(num)
        ans = 0
        for i in num:
            ans+=int(i)
        # print(ans)
        return ans
lowLmit = 1
highLimit = 10
lowLmit = 5
highLimit = 15

obj = Solution().countBalls(lowLmit,highLimit)