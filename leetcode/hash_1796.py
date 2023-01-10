class Solution(object):
    def secondHighest(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = set()
        for i in s:
            # print(i,type(i))
            if i.isdigit():
                ans.add(int(i))
        # print(ans)
        if len(ans)>1:
            print(sorted(ans)[-2])
            return sorted(ans)[-2]
        return -1

s = "dfa12321afd"
obj = Solution().secondHighest(s)