class Solution(object):
    '''
    in case not working 
    class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.res = False
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.helper(board, i, j, word)
                if self.res:
                    return self.res
        return self.res

    def helper(self, board, i, j, word):
        if self.res:
            return
        if len(word) == 0:
            self.res = True
            return
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[0]:
            return
        tmp = board[i][j]
        board[i][j] = "#"
        for (r, c) in [(i-1,j), (i+1,j), (i,j-1), (i,j+1)]:
            self.helper(board, r, c, word[1:])
            
        board[i][j] = tmp
    '''
    def exist_leetcode(self, board, word):
        '''
        https://leetcode.com/problems/word-search/solutions/2683259/simple-beginner-friendly-approach-dfs-o-mn-3-l-o-l/
        '''
        # 變量存儲標籤
        self.res = False
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.helper(i,j,word)
                if self.res:
                    return True
        return False 
    
    def helper(self,i,j,word):
        if self.res:
            return
        # 如果已經遍歷完所有的元素，設置self.res為真
        if len(word)==0:
            self.res =True
            return
        # 邊界情況，並且不等於 
        if i<0 or i>=len(board) or j <0 or j>=len(board[0]) or board[i][j]!=word[0]:
            return

        temp = board[i][j]
        board[i][j]='#'
        for (r,c) in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
            self.helper(r,c,word[1:])
        board[i][j]=temp 

    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        m  = len(board)
        n  = len(board[0])
        
        def dfs(x,y,z):
            print(board[x][y],word_list[z],x,y)

            # 如果該位置是輸入的str，在這個位置上繼續找下一個字幕
            '''報錯
            ~~TypeError: list indices must be integers or slices, not str
            if board[x][y]==word_list[z]:
            Line 10 in dfs (Solution.py)
                dfs(x-1,y,word_list[z+1])
            Line 12 in dfs (Solution.py)
                dfs(i,j,z)
            Line 34 in exist (Solution.py)
                ret = Solution().exist(param_1, param_2)
            Line 59 in _driver (Solution.py)
                _driver()
            Line 70 in <module> (Solution.py)~~
            '''
            if board[x][y]==word_list[z]:
                if m>x>0 and n>y>0: 
                    '''IndexError: list index out of range
                    print(board[x][y],word_list[z],x,y)
                    Line 12 in dfs (Solution.py)
                        dfs(x+1,y,z+1)
                    Line 31 in dfs (Solution.py)
                        dfs(x+1,y,z+1)
                    Line 31 in dfs (Solution.py)
                        dfs(i,j,z)
                    Line 52 in exist (Solution.py)
                        ret = Solution().exist(param_1, param_2)
                    Line 87 in _driver (Solution.py)
                        _driver()
                    Line 97 in <module> (Solution.py)
                    '''
                    dfs(x-1,y,z+1)
                    dfs(x+1,y,z+1)
                    dfs(x,y-1,z+1)
                    dfs(x,y+1,z+1)
                    return True
            # 邊界情況和不等於word_list[z]的情況
            if x<=0 or x>=n or y<0  or y>=n or board[i][j]!=word_list[z]:
                return False
        
        word_list = [i for i in word]        
        print(word_list)
        # dfs(0,0,word_list[0])
        # 先找到word_list[0]第一個在不在board裡面再去迭代
        for i in range(m):
            for j in range(n):
                if board[i][j]==word_list[0]:
                    # dfs(i,j,word_list[0])
                    for z in range(len(word_list)-1):
                        # print(z,word_list[z],z+1,word_list[z+1])

                        dfs(i,j,z)
                        # print(word_list[z],type(z))
                        # print(board[i][j],type(i),type(j))









board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"
obj = Solution().exist(board,word)