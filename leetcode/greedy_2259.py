class Solution(object):
    def removeDigit(self, number, digit):
        """
        :type number: str
        :type digit: str
        :rtype: str
        """
        ans = []
        for i in range(len(number)):
            if digit == number[i]:
                # 省略中间相同的进行拼接
                ans.append([number[0:i],number[i+1:len(number)]])
        print(ans)

        max_val = 0

        for i in ans:
            cur =""
            for j in i :
                if j != "":
                    cur+= j
                    # print(cur)
                    max_val = max(int(cur),max_val)

        print(max_val)
        # print(sum(ans))

number = '123'
digit = "3"

# number= '1231'
# digit = '1'

# number= '551'
# digit = '5'
obj = Solution().removeDigit(number,digit)