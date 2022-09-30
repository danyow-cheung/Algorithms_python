'''問題描述

  两面族是岛屿上的一个新民族，他们的特点是说话时一句真话
一句假话，真假交替。即如果第一句说的是真话，则第二句必为假
话;如果第一句说的是假话，则第二句必然是真话。但第一句话到
底是真假却不得而知。
  现在谜语博士碰到了三个人，这三个人分别来自三个不同的民
族，诚实族、说谎族和两面族。谜语博士和这三个人分别进行了对
话。
  首先，谜语博士问左边的人:“中间的人是哪个族的?”左边
的人回答说:“是诚实族的。”
  谜语博士又问中间的人:“你是哪个族的?”中间的人回答
说:“两面族的。”
  最后，谜语博士问右边的人:“中间的人到底是哪个族的?”
右边的人回答说:“是说谎族的。”
  现在请编程求出这三个人各自来自哪个族。

'''


if __name__=="__main__":
    #分别使用变量L,M,R表示左边,中间,右边的人来自诚实族
    #分别使用变量LL,MM,RR表示左边,中间,右边的人来自两面族
    #0表示说谎，1表示诚实
    for L in range(2):   #穷举
        for M in range(2):
            for R in range(2):
                for LL in range(2):
                    for MM in range(2):
                        for RR in range(2):
                            if ((L and (not LL) and M and (not MM)) or ((not L) and (not M)) and (not M)):
                                if ((R and (not M) and (not MM) or (RR and (not R))) or ((not R) and (not RR) and (M or MM))):
                                    if ((L + LL != 2) and (M + MM != 2) and (R + RR != 2) and (L + M + R == 1) and (LL + MM + RR == 1)):
                                        # 使用三元表达式
                                        l = "两面族" if LL else ("诚实族" if L else "说谎族")
                                        m = "两面族" if MM else ("诚实族" if M else "说谎族")
                                        r = "两面族" if RR else ("诚实族" if R else "说谎族")
                                        print("左边的人来自" + l)
                                        print("中间的人来自" + m)
                                        print("右边的人来自" + r)
