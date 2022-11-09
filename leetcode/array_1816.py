class Solution(object):
    def truncateSentence(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        s_lst = s.split()
        print(s_lst)
        print(" ".join(s_lst[:k]))
s = "Hello how are you Contestant"
s = "What is the solution to this problem"
k = 4
obj = Solution().truncateSentence(s,k)