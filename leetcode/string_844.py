class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        def stack(s):
            ans = []
            for i in range(len(s)):
                if s[i]=='#':
                    if len(ans)==0:
                        continue
                    ans.pop()
                if s[i]!='#':
                    ans.append(s[i])
            return ans 
        ans_s = stack(s)
        ans_t = stack(t)
        print(ans_s==ans_t)
        return ans_s==ans_t
        


s = "ab#c"
t = "ad#c"

# s = "ab##"
# t = "c#d#"

s ="a##c"
t ="#a#c"

# s = 'y#fo##f'
# t ="y#f#o##f"

obj = Solution().backspaceCompare(s,t)
