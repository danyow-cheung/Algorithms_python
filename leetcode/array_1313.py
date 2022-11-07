class Solution(object):
    def decompressRLElist(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        考虑每对相邻的两个元素 [freq, val] = [nums[2*i], nums[2*i+1]]（其中i >= 0），
        每一对都表示解压后子列表中有 freq个值为val的元素，
        你需要从左到右连接所有子列表以生成解压后的列表。
        """
        res= []
        for i in range(0,len(nums),2):
            print(nums[i])
            for freq in range(nums[i]):
                res.append(nums[i+1])
        print(res)

nums = [1,2,3,4]
nums =[1,1,2,3]
obj = Solution().decompressRLElist(nums)