class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        ans = [None]*len(indices)
        print(ans)
        for i in range(len(s)):
            ans[indices[i]]= s[i]

        print("".join(ans))

s = 'codeleet'
indices = [4,5,6,7,0,2,1,3]

obj = Solution().restoreString(s,indices)