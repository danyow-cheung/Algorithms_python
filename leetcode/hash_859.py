class Solution(object):
    def buddyStrings(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        left = 0
        ans = {}
        while left<len(s):
            print(s[left],goal[left])
            if s[left] == goal[left]:
                left+=1
            else:
                diff = goal[left]
                print(s[left:])
                # exit(0)
                if diff in s[left:]:

                    ans[diff] = left
                    left+=1

        print(s,ans)


    def buddyStrings(self,s,goal):
        if len(s)!= len(goal):
            return False

        if s==goal:
            seen = set()
            for a in s:
                if a in seen:
                    return True
                seen.add(a)
            return False

        pairs = []
        for a,b in zip(s,goal):
            if a!= b:
                pairs.append((a,b))
            if len(pairs)>=3:
                return False
        return len(pairs)==2 and pairs[0]==pairs[1][::-1]


goal ="ba"

s = "aaaaaaabc"
goal = "aaaaaaacb"

obj = Solution().buddyStrings(s,goal)