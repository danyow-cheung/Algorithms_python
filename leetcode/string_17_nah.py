class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        map_dict = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        res= []
        if len(digits)==0:return res 

            
        single_num = self.get_single_num(digits)
        
        
        for i in single_num:
            if i!= 0:
                res.append(map_dict.get(i))
        
        print(res)

        


    '''从字符串中得到每一位的数字'''
    def get_single_num(self,digits):

        n = len(digits)
        digits = int(digits)
        if  n<=4:
            g_w = digits%10
            s_w = digits//10 % 10
            b_w = digits//100 %10
            q_w = digits//1000
        # print(q_w,b_w,s_w,g_w)
        
        return [q_w,b_w,s_w,g_w]

    def str_method(self,digits):

        for i in digits:
            print(i)

    def letterCombinations_v2(self, digits):
        digits_lst =[]
        map_dict = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}


        def backtrack(i,curStr):
            pass 
            

    
digits = "23" 
# digits=""
#obj = Solution().letterCombinations(digits)
obj = Solution().letterCombinations_v2(digits)