class Solution(object):
    def letterCombinations_leetcode(self, digits):
        def backtracking(digit,index,ans):
            if index==len(digit):
                res.append(ans)
                return 
            # 单层递归逻辑
            letters = map[digits[index]]
            for letter in letters:
                backtracking(digit,index+1,ans+letter)
        res = []
        map = {"2":"abc", '3':"def", '4':"ghi", '5':"jkl", '6':"mno", '7':"pqrs", '8':"tuv", '9':"wxyz"}
        if not digits:
            return []
        backtracking(digits,0,'')
        return res 
    
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        ans = []

        num2alph = {
            2:'abc',
            3:'def',
            4:'ghi',
            5:'jkl',
            6:'mno',
            7:'pqrs',
            8:'tuv',
            9:'wxyz'
        }
        for i in digits:
            ans.append(num2alph[int(i)])
        print(ans)
        numLen = len(ans)
        for i in ans:
            for j in i:
                print(i,j)



digits = "23"
obj = Solution().letterCombinations(digits)
