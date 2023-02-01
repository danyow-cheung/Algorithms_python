class Solution(object):
    def letterCasePermutation(self, s):
        """
        :type s: str
        :rtype: List[str]
        from leetcode:https://leetcode.com/problems/letter-case-permutation/solutions/379928/python-clear-solution/
        """
        res = []
        def backtrack(sub="",i=0):
            if len(sub)==len(s):
                res.append(sub)
            else:
                if s[i].isalpha():
                    backtrack(sub+s[i].swapcase(),i+1)
                backtrack(sub+s[i],i+1)
        backtrack()
        return res 
        

        


s = "a1b2"
# s = '3z4'
obj = Solution().letterCasePermutation(s)