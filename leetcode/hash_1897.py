import collections


class Solution(object):
    def makeEqual(self, words):
        """
        :type words: List[str]
        :rtype: bool
        """

        hash_ = {}
        for i in words:
            for j in i:
                if j not in hash_:
                    hash_[j]=1
                else:
                    hash_[j]+=1
        n = len(words)
        
        for i in hash_:
            if hash_[i]%n!=0:
                return False
        return True
        
        
        
        
        
        
        
        
        
        
        
        

       
       
       
       



words = ["abc","aabc","bc"]
# words = ['ab','a']
words = ['a','b']
# words = ["abc","cba"]
obj = Solution().makeEqual(words)