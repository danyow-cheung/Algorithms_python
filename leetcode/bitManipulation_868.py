class Solution(object):
    def binaryGap(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = bin(n)[2:]
        ans_lst= list(ans)
        print(ans_lst)

        if ans_lst.count("1")<2:
            return 0

        cur = []
        for i in range(len(ans_lst)):
            if ans_lst[i]=="1":
                cur.append(i)
        print(cur)
        return cur[-1]-cur[0]-1
    def binaryGap_leetcode(self,n):
        A = [i for i in xrange(32) if (n >> i) & 1]
        if len(A) < 2: return 0
        return max(A[i + 1] - A[i] for i in xrange(len(A) - 1))

n = 22
obj = Solution().binaryGap(n)
