class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        return self.helper(s,wordDict,{})
    def helper(self,s,wordDict,memo):
        if s in memo:
            return memo[s]
        if not s:
            return []

        res = []
        for word in wordDict:
            if not s.startswith(word):
                continue 
            if len(word)==len(s):
                res.append(word)
            else:
                resultofTheRest = self.helper(s[len(word):],wordDict,memo)
                for item in resultofTheRest:
                    item = word+" "+item 
                    res.append(item)
        memo[s]=res 
        return res 


s = "catsandog"
wordDict = ["cats","dog","sand","and","cat"]
obj = Solution().wordBreak(s,wordDict)