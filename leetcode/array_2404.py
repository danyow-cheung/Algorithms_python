import collections


class Solution(object):
    def mostFrequentEven(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = {}
        for i in nums:
            if i%2==0 and i not in res:
                res[i]=1 
            elif i%2==0 and i in res:
                res[i]+=1
                
        print(res)

        if len(res)==0 :
            return -1 
        else:
            for i in res:
                if i ==0:return res[0]
                if i==max(res.values()):
                    min = i    
                    print(min)             
                    return min

    
    

nums = [0,1,2,2,4,4,1]
# nums = [4,4,4,9,2,4]
nums = [29,47,21,41,13,37,25,7]
nums = [0,0,0,0]

obj = Solution().mostFrequentEven(nums)
