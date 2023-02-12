class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n==1:
            return str(n)
        res = ""
        while n>0:
            res += self.helper_2(self.helper(str(n)))
            print(res)
            n-=1 
        # print(res[n:])
        return (self.helper_2(self.helper(str(n))))
            
    def helper(self,string):
        # string = '223314444411'
        res = []
        import collections
        print(collections.Counter(string))
        for idx,value in collections.Counter(string).items():
            res.append([int(idx),value])
        print(res)
        return res 
        
    def helper_2(self,array):
        print(array,type(array))
        print("".join(str(i[1])+str(i[0]) for i in array))
        return ("".join(str(i[1])+str(i[0]) for i in array))
        
    def countAndSay_leetcode(self, n):
        '''https://leetcode.com/problems/count-and-say/solutions/2716350/recursive-solution-python/'''
        ans = self.say(n)
        return ans 

    def say(self,remain):
        if remain==1:
            return "1"

        res = self.say(remain-1)
        ans =""
        count = 0
        temp = res[0]

        for char in res:
            if char!=temp:
                ans += str(count)+temp 
                count = 0
                temp = char 
            count +=1 
        ans += str(count)+temp
        return ans 
        


n = 1
n= 4 

obj = Solution().countAndSay(n)
# obj = Solution().helper_2(n)
