import collections


class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count=  collections.Counter(nums)
        print(count)


        ans = []
        # 按照key的顺序进行排序
        for key in sorted(count.keys()):
            print(key,count[key])
            if count[key] and count[key+1]!=0:
                ans.append(count[key+1]+count[key])
        print(ans)
        if len(ans)!=0:

            return max(ans)
        return  0

nums = [1,3,2,2,5,2,3,7]
# nums = [1,2,3,4]
# nums = [1,3,5,7,9,11,13,15,17]
# nums = [1,1,1,1,1,1,1,1,0]
obj = Solution().findLHS(nums)