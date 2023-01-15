class Solution(object):
    # def lst2num(self,list):


    def tictactoe(self, moves):
        """
        :type moves: List[List[int]]
        :rtype: str
        x為shu
        y為橫

        """
        # 初始化-1為未填入元素的格子
        table = [[-1]*3 for i in range(3)]
        res=  "Draw"
        for i in range(len(moves)):
            if i%2==0:
                # a move
                # print(moves[i],type(moves[i]))
                table[moves[i][0]][moves[i][1]] = "a"
            else:
                # b move

                table[moves[i][0]][moves[i][1]] = "b"
        print(table)

        # 橫著相等的情況
        for i in range(len(table)):
            if table[i][0]==table[i][1]==table[i][2]:
                print("橫相等")
                if table[i][0]=="a":
                    res ="A"
                elif table[i][0]=='b':
                    res ="B"
        # print(table)
        # 豎立的情況
        for i in range(len(table) - 2):
            for j in range(3):
                if table[i][j] == table[i+1][j]==table[i+2][j]:
                    if table[i][j]=='a':
                        res = "A"
                    elif table[i][j] == 'b':
                        res = "B"


        # 對角線情況
        for i in range(len(table) - 2):

            if table[i][0]==table[i+1][1]==table[i+2][2]:
                print(table[i][0],table[i+1][1],table[i+2][2])
                print('正對角線相同')
                if table[i][0] =="a":
                    res ="A"
                elif table[i][0] == 'b':
                    res = "B"

            elif table[i][-1] ==table[i+1][-2]==table[i+2][-3]:
                print(table[i][-1],table[i+1][-2],table[i+2][-3])
                print("反對角線相同")
                if table[i][-1] =="a":
                    res ="A"
                elif table[i][-1] == "b":
                    res = "B"
        print('table',table)

        for i in  range(len(table)):
            # print(table[i])
            # for j in table[i]:
            #     print(table[i],j)
            # print("pending情況",table[i].count(-1))
            if table[i].count(-1)==3 and res =="Draw":
                res = "Pending"
        print(res)
        return res


moves = [[0,0],[2,0],[1,1],[2,1],[2,2]]
moves = [[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]]
# moves = [[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]]
moves = [[0,2],[0,1],[2,1]]
moves = [[1,0],[2,0],[0,1]]
obj = Solution().tictactoe(moves)