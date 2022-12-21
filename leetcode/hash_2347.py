class Solution(object):
    def bestHand(self, ranks, suits):
        """
        :type ranks: List[int]
        :type suits: List[str]
        :rtype: str
        """
        setS = set(suits)

        if len(setS)==1:
            return "Flush"
        hash_ = {}
        for i in ranks:
            if i not in hash_:
                hash_[i]=1
            else:
                hash_[i]+=1
        print('hash',hash_)
        for value in sorted(hash_.values(),reverse=True):
            if value>=3:
                return "Three of a Kind"
            elif value==2:
                return "Pair"
        return 'High Card'


'''task-1'''
ranks = [13,2,3,1,9]
suits = ["a","a","a","a","a"]
'''task-2'''
ranks = [4,4,2,4,4]
suits = ["d","a","a","b","c"]
'''wrong test-case'''
ranks = [13,12,3,4,7]
suits = ["a","d","c","b","c"]

ranks = [1,1,1,2,2]
suits = ["a","b","c","a","d"]

obj = Solution().bestHand(ranks,suits)