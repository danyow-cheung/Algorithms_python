class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        hash = {
            1:'I',
            5:'V',
            10:'X',
            50:'L',
            100:'C',
            500:'D',
            1000:'M'
        }
        res = []
        print(num)
        
        while num>0:
            num = num//10    
            
            if hash[num]:
                res.append(hash[num])
            print(num)
        print("".join(res))

num = 30
obj = Solution().intToRoman(num)