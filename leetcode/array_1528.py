class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        res = []
        word_=[]

        for i in s:
            word_.append(i)

        for i in range(len(indices)):
            print(indices[i],s[i])
            res.insert(indices[i],word_[i])
            print(res)
        print("".join(res))

s = 'codeleet'
indices = [4,5,6,7,0,2,1,3]

obj = Solution().restoreString(s,indices)