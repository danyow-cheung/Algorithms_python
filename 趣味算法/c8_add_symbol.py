'''問題描述【在指定位置插入字符】
请编写程序，实现以下功能:在字符串中的所有数字字符前加 一个“$”符号。
例如，输入A1B23CD45，输出A$1B$2$3CD$4$5。
'''

def insert_str(s):
    a = [0]*len(s)
    # 遍歷字符串
    for i in range(len(s)):
        a[i]=s[i]
    # 遍歷數組元素
    for i in a:
        # 用isdigit()函數判斷是否為數字
        flag = i.isdigit()
        if flag == True:
            i = "$"+i 
        print(i,end="")


if __name__=="__main__":
    s = "A1B23CD45"
    print("final")
    insert_str(s)