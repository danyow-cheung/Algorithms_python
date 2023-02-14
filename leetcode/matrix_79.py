class Solution(object):
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
            if board[x][y]==word_list[z]:
                if n>x>0 and n>y>0: 
                    dfs(x-1,y,word_list[z+1])
                    dfs(x+1,y,word_list[z+1])
                    dfs(x,y-1,word_list[z+1])
                    dfs(x,y+1,word_list[z+1])
                    return True
            # 邊界情況和不等於word_list[z]的情況
            if x<0 or x>=n or y<0  or y>=n or board[i][j]!=word_list[z]:
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






board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"
obj = Solution().exist(board,word)