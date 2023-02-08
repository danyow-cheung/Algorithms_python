class Solution(object):
    def generateParenthesis_brute_force(self, n):
        """
        :type n: int
        :rtype: List[str]
        https://leetcode.com/problems/generate-parentheses/solutions/127698/generate-parentheses/
        """

        def generate(A = []):
            if len(A) == 2*n:
                if valid(A):
                    ans.append("".join(A))
            else:
                A.append('(')
                generate(A)
                A.pop()
                A.append(')')
                generate(A)
                A.pop()

        def valid(A):
            bal = 0
            for c in A:
                if c == '(': bal += 1
                else: bal -= 1
                if bal < 0: return False
            return bal == 0

        ans = []
        generate()
        print(ans)

        return ans

    def generateParenthesis_back_tracking(self, n):
        '''
        還是不懂可惡
        https://leetcode.com/problems/generate-parentheses/solutions/2542620/python-java-w-explanation-faster-than-96-w-proof-easy-to-understand/
        '''
        ans = []
        def dfs(left,right,s):
            if len(s)==2*n:
                ans.append(s)
                return 
            if left<n:
                dfs(left+1,right,s+"(")
            if right<left:
                dfs(left,right+1,s+')')
        dfs(0,0,'')
        return ans 

n = 3
obj = Solution().generateParenthesis_brute_force(n)