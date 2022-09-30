'''問題描述【刪除*符號】
现在有一串字符需要输入，规定输入的字符串中只包含字母和 “*”符号。
请编写程序，实现除了字符串前后的“*”之外，将串 中其他的“*”全部删除。

例如，假设输入的字符串为:****A*BC*DEF*G********，
删除 串中的“*”后，字符串变为:****ABCDEFG********。
'''
'''算法分析
我们使用最简单的方法来实现，定义一个fun()函数，
在函数中 遍历这个字符串，将字符串拆分开，并将每个字符分别存入数组， 
然后遍历这个数组，判断每个数组字符元素是否是“*”，如果是就 替换为空，然后返回字符串结果。
'''

def fun(s):
    a =[0]*len(s)
    # 將字符串拆分存入數組
    for i in range(len(s)):
        a[i]=s[i]
    print("结果:", end="")
    for j in a:
        if j=='*':
            j=""
        print(j,end="")

'''其他方法【正則表達式】
'''
import re 
def fun_re(s):
    result_str = re.sub(r'([a-zA-Z]+)(.+)([a-zA-Z]+)', lambda match:"".join([m.replace("*","")for m in match.groups()]),s)
    print(result_str)
if __name__ == "__main__":
    s = "***A*BC*DEF*G********"
    print("输入的字符串为:", s)
    fun_re(s)

