class Solution(object):
    def titleToNumber_leetcode(self, columnTitle):
        # https://leetcode.com/problems/excel-sheet-column-number/solutions/1790567/python3-clean-solution-explained/
        ans = 0 
        pos = 0
        for letter in reversed(columnTitle):
            print(letter)
            digit = ord(letter) - 64 
            ans += digit *26**pos 
            pos+=1 
        return ans 
        

    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        res = 0
        n = len(columnTitle)
        if n>1:
            res  +=25
            n-=1 
        print(res)
        # 轉換為小寫
        columnTitle=columnTitle.lower()
        for i in columnTitle:
            res +=ord(i)-ord('a') +1

        # res +=ord(columnTitle)-ord('a') +1
        print(res)
        return res 


columnTitle = "A"

columnTitle = "AB"
columnTitle = "ZY"

obj = Solution().titleToNumber_leetcode(columnTitle)