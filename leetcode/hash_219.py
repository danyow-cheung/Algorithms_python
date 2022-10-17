class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        # 保證是不重複的
        # key:數字，val:數組裡面的下標
        hashmap = dict()
        for i in range(len(nums)):
            if nums[i] in hashmap and abs(i - hashmap[nums[i]])<=k:
                return True 
            else:
                # 存儲下標
                hashmap[nums[i]] =i
        
        return False 



nums = [1,2,3,1]
k = 3 
obj = Solution().containsNearbyDuplicate(nums,k)
        