import collections


class Solution(object):
    def greatestLetter(self, s):
        """
        :type s: str
        :rtype: str
        """
        n_num = len(set(s))
        print(n_num)
        s = s.lower()

        # s.upper()
        count = collections.Counter(s)
        print(count)
        # print('sum_count= ',sum(count))
        ans = []

        for key,value in count.items():
            if value>=2:
                ans.append(key)
        print(ans)

        if len(ans)!=0:
            res = max(ord(i) for i in ans)
            return chr(res).upper()

        return ""
    def greatestLetter_leetcode(self,s):
        see = set()
        res =""
        for c in s:
            see.add(c)
            if c.upper() in see and c.lower() in see:
                res = max(res,c.upper())
        print(see)
        return res

s = "lEeTcOdE"
s = "arRAzFif"
obj = Solution().greatestLetter_leetcode(s)
