class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        序列是默認遞增的
        """
     
        l = 0 
        r = len(numbers)-1 
        while l !=r:

            if numbers[r]+numbers[l]==target:
                return [l+1,r+1]
            if numbers[r]+numbers[l]>target:
                r-=1 
            else:
                l+=1
                
        
numbers = [2,7,11,15]
target = 9
obj = Solution().twoSum(numbers,target)
