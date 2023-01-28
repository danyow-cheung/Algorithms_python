class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        time_count = []
        digit_count = []
        i = 0
        left = 0 
        right = 0 
        while i <len(s):
            # print(i)
            # if s[i].isnumeric():
            #     time_count.append(int(s[i]))

            if s[i]=='[':
                left = i +1
                print("元素需要乘的次数",s[i-1],type(s[i-1]))
            elif s[i]==']':
                right = i -1
                
                digit_count.append(int(s[left-2])*s[left:right+1])
            i+=1

        print(digit_count)
        
        # print(time_count,digit_count)
        # res = ""
        # for i in range(len(time_count)):
        #     res += time_count[i]*digit_count[i]
        # print("res:",res)
        # return res 

    def decodeString_leetcode(self, s):
        '''https://leetcode.com/problems/decode-string/solutions/87662/python-solution-using-stack/'''
        stack = []
        curNum = 0 
        curString = ""
        for c in s:
            if c=='[':
                stack.append(curString)
                stack.append(curNum)
                curString = ""
                curNum = 0 
            elif c==']':
                num = stack.pop()
                prevString = stack.pop()
                curString = prevString+num*curString
            elif c.isdigit():
                curNum = curNum*10+int(c)
            else:
                curString += c 
        return curString


s = "3[a]2[bc]"
s = "3[a2[c]]"
obj = Solution().decodeString_leetcode(s)
