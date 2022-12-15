class Solution(object):
    def countGoodSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        items = []
        left = 0
        # while left<=
        for i in range(len(s)):
            if len(s[i:i+3])==3:
                items.append(s[i:i+3])
        print(items)
        ans = 0
        for i in items:
            # print(len(set(i)),len(i))
            if len(i) == len(set(i)):
                # print(len(i),set(i),i)
                ans+=1
        print(ans)

s = 'xyzzaz'
# s = "aababcabc"
obj = Solution().countGoodSubstrings(s)