class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        TMD想不明白了
        """
        m = len(board[0])

        # 打横
        # for i in range(len(board)):
        #     for j in range(0,len(board[i]),3):
        #         print('row=',board[i][j:j+3])

        for i in range(0,len(board),3):
            for j in range(0,len(board[i]),3):

                print('row=',board[i:i+3][j:j+3])
                # 
                print(board[i][j:j+3])
    
    
    
    def isValidSudoku_leetcode(self, board):
        '''https://leetcode.com/problems/valid-sudoku/solutions/2572765/python-explained-steps-clean-code-best-method/'''
        rows = [set() for x in range(9)]
        cols = [set() for x in range(9)]
        squares = [[set() for x in range(3)] for y in range(3)]
    
        for x in range(9):
            for y in range(9):
                cell_value = board[x][y]
                # 为空跳过
                if cell_value =='.':
                    continue
                if cell_value in rows[x] or cell_value in cols[y] or cell_value in squares[x//3][y//3]:
                    return False
                rows[x].add(cell_value)
                cols[y].add(cell_value)
                squares[x//3][y//3].add(cell_value)
        return True



        
board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

# obj = Solution().isValidSudoku(board)
obj = Solution().isValidSudoku_leetcode(board)
