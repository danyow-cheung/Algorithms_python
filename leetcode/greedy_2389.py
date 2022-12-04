class Solution(object):
    def answerQueries(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[int]
        :rtype: List[int]
        answer[i]是nums中元素之和小于等于queries[i]的子序列的最大长度
        """
        answer = []

        nums.sort()

        for i in queries:
            count = 0
            for j in nums:
                if i>= j:
                    i-=j
                    count+=1
                else:
                    break
            answer.append(count)

        print(answer)
        return answer
    def answerQueries_tle(self,queries,nums):
        '''超时间'''
        answer = [0] * len(queries)
        nums.sort()
        for i in range(len(queries)):
            for j in range(len(nums)):
                if sum(nums[:j + 1]) <= queries[i]:
                    answer[i] = j + 1
        return answer

nums = [4,5,2,1]
queries = [3,10,21]
nums =[2,3,4,5]
queries=[1]
obj = Solution().answerQueries(nums,queries)