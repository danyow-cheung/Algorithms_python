class Solution(object):
    def smallestNumber(self, pattern):
        """
        :type pattern: str
        :rtype: str

        """
        ans = [i for i in range(1,len(pattern)+2)]
        print('before',ans)
        for i in range(len(pattern)-1):
            print(pattern[i])
            if pattern[i]=='D' and pattern[i+1]=='I':
                ans[i],ans[i+1] = ans[i+1],ans[i]
            elif pattern[i]=='D' and pattern[i+1]=='D':
                ans[i],ans[i+1] = ans[i+1],ans[i]
        print('after',ans)
    def smallestNumber_leetcode(self, pattern):
        res = []
        stack = []
        for i ,c in enumerate(pattern+'I',1):
            print(i,c,stack,res)
            stack.append(str(i))
            if c=='I':
                # 倒序輸出
                res += stack[::-1]
                # 重置為0
                stack = []
        print(res)
        return "".join(res)
        
        '''
        1 I [] []
        2 I [] ['1']
        3 I [] ['1', '2']
        4 D [] ['1', '2', '3']
        5 I ['4'] ['1', '2', '3']
        6 D [] ['1', '2', '3', '5', '4']
        7 D ['6'] ['1', '2', '3', '5', '4']
        8 D ['6', '7'] ['1', '2', '3', '5', '4']
        9 I ['6', '7', '8'] ['1', '2', '3', '5', '4']
        ['1', '2', '3', '5', '4', '9', '8', '7', '6']
        '''


pattern = "IIIDIDDD"
obj = Solution().smallestNumber_leetcode(pattern)