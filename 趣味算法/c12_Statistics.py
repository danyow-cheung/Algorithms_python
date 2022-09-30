'''問題描述【統計學生成績】

有5个学生，每个学生有三门课程的成绩需要统计。
要求从键盘 输入学生的学号、姓名以及三门课程的成绩，
计算出平均成绩，
并 将原有的数据和计算出的平均成绩存放在磁盘文件stud中。
'''
if __name__ =="__main__":
    stu = [['','',0,0] for i in range(5)]
    # 輸入5個學生信息
    for i in range(5):
        print('\n请输入第%d个学生的信息:' % (i + 1)) 
        stu[i][0] = input('stuNo:')
        stu[i][1] = input('name:') 
        sum = 0
        # 求出平均成绩
        for j in range(3):
            stu[i][2] = int(input('score %d:' % (j + 1)))
            sum += stu[i][2]
            stu[i][3] = sum // 3.0
    print(stu)