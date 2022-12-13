class Solution(object):
    def digitCount(self, num):
        """
        :type num: str
        :rtype: bool
        """
        import collections
        count = collections.Counter(num)
        print(count,count[str(1)])
        ans = 0
        for i in range(len(num)):
            # index-i,value-num[i]
            # cur = count[str(i)]
            
            if int(num[i])== count[str(i)]:
                print('不相等吗')
                ans+=1 
                # return False
        # return True 
        print(ans,len(num))
        print(ans==len(num))

num ="1210"
obj = Solution().digitCount(num)