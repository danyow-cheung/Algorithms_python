'''問題描述【委派任務】
某项任务需要在A、B、C、D、E、F这6个人中挑选人来完成，但 挑选人受限于以下条件:
1)A和B两个人至少去一人。 
2)A和D不能同时去。 
3)A、E和F三人中要挑选两个人去。 
4)B和C同时去或者都不去。 
5)C和D两人中只能去一个。 
6)如果D不去，那么E也不去。 

试编程求出应该让哪几个人去完成这项任务。
'''

if __name__ =="__main__":
    # a,b,c,d,e,f可能取值（0，1）
    #窮舉所有情況
    for A in range(2):
        for B in range(2):
            for C in range(2):
                for D in range(2):
                    for E in range(2):
                        for F in range(2):
                            if (A+B >= 1) and (A+D != 2) and (A+E+F == 2) and ((B+C == 0) or (B+C == 2)) and (C+D == 1)and ((D+E == 0) or D == 1):
                                #三元表达式
                                
                                a = '' if A == 1 else "未" 
                                print("A" + a + "被选择去完成任务")
                                
                                b = '' if B == 1 else "未" 
                                print("B" + b + "被选择去完成任务")

                                c = '' if C == 1 else "未" 
                                print("C" + c + "被选择去完成任务")
                                
                                d = '' if D == 1 else "未" 
                                print("D" + c + "被选择去完成任务")
                                
                                e = '' if E == 1 else "未" 
                                print("E" + c + "被选择去完成任务")
                                
                                f = '' if F == 1 else "未" 
                                print("F" + c + "被选择去完成任务")
                                