class Solution(object):
    def minimumDeviation(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = []
        print(nums)
        for i in nums:
            res.append(self.iseven(i))
        print(res)



    
    def iseven(self,num):
        if num%2==0:
            return num//2 
        else:
            return num*2 
    def minimumDeviation_leetcode(self,nums):
        '''
        完全没idea,用优先队列？
        https://leetcode.com/problems/minimize-deviation-in-array/solutions/3224219/python-simple-solution-youtube-link-attached/
        '''
        max_heap = []
        for num in nums:
            if num %2==0:
                num = -num 
            else:
                num = -num*2 
            heapq.heappush(max_heap,num)
        min_dev = float('inf')
        min_val = -max(max_heap)
        while len(nums)==len(max_heap):
            curr = -heapq.heappop(max_heap)
            min_dev = min(min_dev,curr-min_val)
            if curr%2==0:
                min_val = min(min_val,curr//2)
                heapq.heappush(max_heap,-curr//2)
            else:
                break
        return min_dev

            
nums = [1,2,3,4]
obj =Solution().minimumDeviation(nums)
