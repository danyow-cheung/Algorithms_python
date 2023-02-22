class Solution(object):
    def myAtoi_leetcode(self,s):
        sign = 1 
        result = 0 
        index = 0 
        n = len(s)
        INT_MAX = pow(2,31)-1 
        INT_MIN = -pow(2,31)

        # Discard all spaces from the beginning of the input string.
        while index < n and s[index] == ' ':
            index += 1
        
        # sign = +1, if it's positive number, otherwise sign = -1. 
        if index < n and s[index] == '+':
            sign = 1
            index += 1
        elif index < n and s[index] == '-':
            sign = -1
            index += 1
        
        # Traverse next digits of input and stop if it is not a digit. 
        # End of string is also non-digit character.
        while index < n and s[index].isdigit():
            digit = int(s[index])
            
            # Check overflow and underflow conditions. 
            if ((result > INT_MAX // 10) or (result == INT_MAX // 10 and digit > INT_MAX % 10)):
                # If integer overflowed return 2^31-1, otherwise if underflowed return -2^31.    
                return INT_MAX if sign == 1 else INT_MIN
            
            # Append current digit to the result.
            result = 10 * result + digit
            index += 1
        
        # We have formed a valid number without any overflow/underflow.
        # Return it after multiplying it with its sign.
        return sign * result


    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        应该可以实现但是leetcode无法通过
        """
        res = []
        # print(s)

        # s = s.split()
        # print(s)
        negative = False
        for i in s:
            if i.isdigit(): # 这个情况下如果前面有空格也有正负号数字会无法检测
                res.append(i)
            elif i=='-':
                negative=True
            else:
                pass 

        if negative:
            # print("-"+"".join(res))
            ans = int("".join(res))
            # print(-ans,type(ans))
            return -ans 

        else:
            # print("".join(res))
            ans = int("".join(res))
            # print(ans,type(ans))
            return ans 



s = "   -42"
# s = "4193 with words"
s = "words and 987"
obj = Solution().myAtoi(s)