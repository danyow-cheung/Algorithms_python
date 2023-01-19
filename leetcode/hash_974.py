class Solution(object):
    def subarraysDivByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        暴力循環超時
        """
        ans = 0

        for i in range(len(nums)):
            for j in range(i+1,len(nums)+1):
                print(nums[i:j])
                if sum(nums[i:j])%k==0:
                    ans +=1
        print(ans )
        return  ans

    def subarraysDivByK_leetcode(self, nums, k):
        '''前綴和計數'''
        n = len(nums)
        prefixMod = 0
        result = 0
        modGroups = [0]*k
        modGroups[0]=1
        for i in nums:
            prefixMod = (prefixMod+i%k+k)%k
            result += modGroups[prefixMod]
            modGroups[prefixMod]+=1
        print(result)
        return result
    def subarraysDivByK_leetcode2(self, nums, k):
        '''哈希表+逐一統計'''
        record = {0:1}
        total = 0
        ans = 0
        for i in nums:
            total += i
            modules = total % k
            same = record.get(modules,0)
            ans += same
            record[modules] = same + 1
        return  ans

nums = [4,5,0,-2,-3,1]
k = 5
# nums = [5]
# k = 9
obj = Solution().subarraysDivByK_leetcode(nums,k)