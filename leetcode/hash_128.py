class Solution(object):
    def longestConsecutive_leetcode(self, nums):
        '''
        https://leetcode.com/problems/longest-consecutive-sequence/solutions/2238932/c-python-simple-solution-w-explanation-o-n-o-n/
        '''
        max_len = 0 
        num_set = set(nums)
        for num in nums:
            if num-1 not in num_set:
                curr_num = num 
                curr_len = 1 
                while curr_num+1 in num_set:
                    curr_num +=1 
                    curr_len+=1 
                max_len = max(max_len,curr_len)
        return max_len
    

    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        最长连续序列
        """
        # value-count
        map ={}
        for i in nums:
            if i not in map:
                map[i]=1 
            else:
                map[i]+=1 
        print(map)
        flag =  0
        res = 0
        diff = 0 
        for i in sorted(map.keys()):
            if i-flag==diff:
                res+=1
                diff = i - flag 
            flag = i 

        print(res)

            

                

nums = [100,4,200,1,3,2]
obj = Solution().longestConsecutive(nums)