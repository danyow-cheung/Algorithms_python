class Solution(object):
    def mostFrequent(self, nums, key):
        """
        :type nums: List[int]
        :type key: int
        :rtype: int
        """
        hash_ = {}

        for i in range(len(nums)-1):
            if nums[i]==key:
                if nums[i+1] not in hash_:
                    hash_[nums[i+1]]=1
                else:
                    hash_[nums[i+1]]+=1
        print(hash_)
        for i in sorted(hash_.values(),reverse=True):
            print(self.getKey(hash_,i))
            return self.getKey(hash_,i)


    def getKey(self,hash_,target):
        for key,value in hash_.items():
            if value == target:
                return key



nums = [1,100,200,1,100]
key = 1
nums = [2,2,2,2,3]
key = 2

obj = Solution().mostFrequent(nums,key)