class Solution(object):
    def minDeletionSize(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        ans = 0

        for i in strs:
            if len(i)==1:
                continue
            # 排序輸出
            for j in range(len(i)-1):
                print( ord(i[j]),type(j),type(i[j]))
                if abs(ord(i[j]) - ord(i[j+1]))!=1:
                    ans += 1

        print(ans,strs[ans])
        return ans

    def  minDeletionSize_leetcode(self,strs):
        # for column in zip(*strs):
        #     print(column,type(column))
        #     print(sum(list(column)),sorted(column))
        return sum(list(column) != sorted(column) for column in zip(*strs))



strs = ["cba","daf","ghi"]
strs = ['a','b']
strs = ['zyx','wvu','tsr']
obj = Solution().minDeletionSize_leetcode(strs)