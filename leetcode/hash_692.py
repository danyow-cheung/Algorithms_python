class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        import collections
        count = collections.Counter(words)
        print(count)
        ans = []
        for i,j in sorted(count.items(),key=lambda p:(-p[1],p[0])):
            
            print(i,j)
            k-=1 
            ans.append(i)
            if k==0:
                break
        print(ans)

        return ans 

            
words = ["i","love","leetcode","i","love","coding"]
k = 2
words = ["the","day","is","sunny","the","the","the","sunny","is","is"]
k = 4

obj = Solution().topKFrequent(words,k)
