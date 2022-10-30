from collections import Counter
import numpy as np 

class Solution(object):
    def mostFrequentEven(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        count = Counter(nums)
        print(count)

        # 计数器中最大次数
        max_freq = max(count.values())
        # if max_freq==1 :return -1 
        
        # 最大值
        res = np.inf
        for key,_ in count.items():
            if key %2==0 and count.get(key)==max_freq:
                
                res = min(res,key)

            if key %2 == 0 and count.get(key)==1:
                res = -1 
                return -1 
            
        print(res)
        return res
    def mostFrequentEven_leetcode(self,nums):
        # 保留偶数
        nums = [n for n in nums if n %2 ==0]
        nums.sort()
        
        count = Counter(nums)
        print(len(nums))
        print(count)
        res = 0 
        if len(nums)>0:
            
            res = count.get(max(count.values()))
            print(res)
            
        elif len(nums)==1:
            res = nums[0]
        else:
            res = -1 
    

nums = [0,1,2,2,4,4,1]
# nums = [4,4,4,9,2,4]
# nums = [29,47,21,41,13,37,25,7] # output:-1
# nums = [10000]# output:10000
nums = [0,0,0,0]

obj = Solution().mostFrequentEven_leetcode(nums)
